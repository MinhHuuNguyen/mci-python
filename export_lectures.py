
import os
import argparse


def export(python_path, html_path, lesson):
    lectures = sorted(os.listdir(python_path))

    for lecture in lectures:
        if not lecture.endswith('.ipynb'):
            continue
        
        if lesson != -1 and not lecture.startswith(f'{lesson}'):
            continue

        nb_path = os.path.join(python_path, lecture)
        os.system(f'jupyter nbconvert --to html_embed {nb_path}')

        html_name = lecture.split('.')[0]
        from_path = os.path.join(python_path, f'{html_name}.html')
        to_path = os.path.join(html_path, f'{html_name}.html')
        os.system(f'mv {from_path} {to_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start inference')
    parser.add_argument(
        '--lesson', type=int, default=-1, help='Lesson number')
    args = parser.parse_args()

    PYTHON_PATH = 'python/'
    HTML_PATH = 'html/'

    export(PYTHON_PATH, HTML_PATH, args.lesson)
