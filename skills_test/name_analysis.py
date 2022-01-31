
import os
import re
from functools import partial
from multiprocessing import Pool

import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt


def read_data(data_file, root_path):
    '''
    Read data from file name and root path
    Return None if it's not txt-comma-delimited file
    '''
    if data_file.endswith('txt'):
        path = os.path.join(root_path, data_file)
        df = pd.read_csv(path, sep=',', header=None)
        df.columns = ['name', 'sex', 'occurrences']

        year = int(re.search(r'\d+', data_file).group())
        df['year'] = [year] * len(df)
        return df
    return


def plot_hist(x_list, y_list, color, suptitle, out_name):
    plt.bar(x_list, y_list, color=color)
    plt.suptitle(suptitle)
    plt.savefig(out_name, dpi=1000)
    plt.clf()


def plot_hist_by_year_and_sex(df):
    '''
    Plot hist of number of babies each year and sex (male and female)
    '''
    print('Plotting histogram by year and sex...')
    # Group dataframe by sex and year,
    # aggregate by sum on occurrences and reset index
    df_grouped = df.groupby(['sex','year']).agg({'occurrences': 'sum'}).reset_index()

    for gender in ['M', 'F']:
        df_grouped_gender = df_grouped[df_grouped.sex == gender].sort_values(by=['year'])

        count_list = df_grouped_gender.occurrences.to_list()
        year_list = df_grouped_gender.year.to_list()

        plot_name = 'male' if gender == 'M' else 'female'
        suptitle = f'Number of babies each year ({plot_name})'
        out_name = f'baby_each_year_{plot_name}.jpg'
        plot_hist(year_list, count_list, 'orange', suptitle, out_name)


def get_top_k_df(_year, _sex, df, top_k):
    '''
    Get top k most popular names each year
    '''
    df_year_sex = df[(df.year == _year) & (df.sex == _sex)]
    df_sorted = df_year_sex.sort_values(by=['occurrences'], ascending=False)
    df_top_k = df_sorted.head(top_k)
    return df_top_k


def get_most_popular_names(df, unique_year_list, top_k=1000):
    '''
    Get top k most popular names each year (male and female)
    '''

    print('Getting most popular names...')
    all_df_list = []
    for sex in ['M', 'F']:
        with Pool(4) as pool:
            df_list = list(tqdm(pool.imap(partial(get_top_k_df, df=df, _sex=sex, top_k=top_k),
                                          unique_year_list),
                                total=len(unique_year_list)))
            all_df_list.extend(df_list)

    return pd.concat(all_df_list, ignore_index=True)


def get_number_babies_by_names(df, names, unique_year_list):
    '''
    Get number of babies each year by name
    '''
    for name in names:
        df_name = df[df.name == name]
        df_grouped = df_name.groupby(by='year').agg({'occurrences': 'sum'}).reset_index()
        df_sorted = df_grouped.sort_values(by=['year'])
        count_list = df_sorted.occurrences.to_list()

        if len(count_list) != len(unique_year_list):
            tmp_year_list = df_sorted.year.to_list()
            for year in unique_year_list:
                if year not in tmp_year_list:
                    tmp_df = {
                        'year': year,
                        'occurrences': 0
                    }
                    df_sorted = df_sorted.append(tmp_df, ignore_index=True)

            new_df_sorted = df_sorted.sort_values(by=['year'])
            count_list = new_df_sorted.occurrences.to_list()

        # print(len(unique_year_list), len(count_list))
        plot_hist(unique_year_list, count_list, 'orange', name, f'{name}.jpg')


def analyze_name_diversity(df_full, df_popular):
    '''
    Analyze name diversity according to year and sex
    '''
    def count_name_by_year(tmp_df, sex):
        tmp_sex_df = tmp_df[tmp_df.sex == sex]
        tmp_sex_count_df = tmp_sex_df.groupby(by='year').agg({'occurrences': 'sum'})
        return tmp_sex_count_df.reset_index()
    
    def count_percent(inputt):
        return inputt[0] / inputt[1] * 100


    for gender in ['M', 'F']:
        df_popular_count = count_name_by_year(df_popular, gender)
        df_full_count = count_name_by_year(df_full, gender)

        df_merged = pd.merge(df_popular_count, df_full_count, how='inner', on='year')
        df_merged['percent'] = df_merged[['occurrences_x', 'occurrences_y']].apply(count_percent, axis=1)
        df_merged = df_merged.sort_values(by='year')

        plot_name = 'male' if gender == 'M' else 'female'
        plot_hist(df_merged.year.to_list(),
                  df_merged.percent.to_list(),
                  'orange',
                  f'Percent of number of top 1000 names ({plot_name})',
                  f'percent_1k_names_{plot_name}.jpg')


def analyze_name_male_female(df, test_name):
    '''
    Analyze name transition between male and female
    '''

    def divide(occ):
        return occ[0] / (occ[0] + occ[1])

    df_name = df[df.name == test_name]

    df_name_male = df_name[df_name.sex == 'M'].drop(columns=['name', 'sex'])
    df_name_female = df_name[df_name.sex == 'F'].drop(columns=['name', 'sex'])

    df_name_merged = pd.merge(df_name_male, df_name_female, how='outer', on='year').sort_values('year')
    year_list = df_name_merged.year.to_list()
    df_name_merged = df_name_merged.fillna(0)

    df_name_merged['male_percent'] = df_name_merged[['occurrences_x', 'occurrences_y']].apply(divide, axis=1)
    df_name_merged['female_percent'] = df_name_merged[['occurrences_y', 'occurrences_x']].apply(divide, axis=1)

    male_percent_list = df_name_merged.male_percent.to_list()
    female_percent_list = df_name_merged.female_percent.to_list()
    _range = range(len(year_list))

    plt.bar(_range, male_percent_list, color='orange', edgecolor='white', width=1)
    plt.bar(_range, female_percent_list, bottom=male_percent_list, color='blue', edgecolor='white',  width=1)
    plt.xticks(_range, year_list, rotation=90, fontsize='xx-small')
    plt.xlabel(f'{test_name}')
    plt.savefig(f'name_{test_name}_transition.jpg', dpi=1000)
    plt.clf()


if __name__ == '__main__':
    data_folder_path = 'Names'
    data_files = os.listdir(data_folder_path)

    print('Reading data...')
    with Pool(4) as pool:
        df_list = list(tqdm(pool.imap(partial(read_data, root_path=data_folder_path),
                                      data_files),
                            total=len(data_files)))

    df_list = [df for df in df_list if df is not None]
    df_full = pd.concat(df_list, ignore_index=True)

    # Plot hist of number of babies each year and sex (male and female)
    plot_hist_by_year_and_sex(df_full)

    # Get top k most popular names each year (male and female)
    unique_year_list = list(df_full.year.sort_values().unique())
    most_popular_names_df = get_most_popular_names(df_full, unique_year_list, top_k=1000)
    most_popular_names_df.to_csv('most_popular_names_df.csv', index=False)

    # Plot hist of number of babies each year whose name
    # Philip, Harry, Elizabeth, Marilyn
    names = ['Philip', 'Harry', 'Elizabeth', 'Marilyn']
    get_number_babies_by_names(df_full, names, unique_year_list)

    # most_popular_names_df = pd.read_csv('most_popular_names_df.csv')
    # Plot hist of percent of 1000 most popular names
    analyze_name_diversity(df_full, most_popular_names_df)

    # Analyze name transition between male and female
    test_name = 'Leslie'
    analyze_name_male_female(df_full, test_name)
