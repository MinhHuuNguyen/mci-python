
# To run this function, we have to install gdrive and put it in the home directory
function process_data {
  [ ! -d $1 ] && mkdir $1

  # Download data
  for data_id in $2
  do
    ~/gdrive download $data_id
  done

  # Move and unzip data
  for data_name in $3
  do
    mv $data_name $1
    unzip "$1/$data_name" -d $1
  done

  # Remove redundant files
  [ -d "$1/__MACOSX" ] && rm -rf "$1/__MACOSX"
}

# Download data for deep learning course
# If this code does not work, you can download the datasets from these links below
# 1. covid19_tweets_dataset.zip: https://drive.google.com/file/d/1PJBmSE54fhe1_WDU_kTB3tIf7GDEPHIW/view?usp=sharing
# 2. dog_cat_dataset.zip: https://drive.google.com/file/d/1PBirGT9ytlTJsnNnAGlT0xEpAzLX3N7K/view?usp=sharing
# 3. house_prices_dataset.zip: https://drive.google.com/file/d/1PNMkytuhg8ZSvQFdInzFPRIW9PF8EXL5/view?usp=sharing
# 4. speech_emotion_dataset.zip: https://drive.google.com/file/d/1PLbB47FucyIwE9n8LjNrypqlerhEo7jZ/view?usp=sharing
process_data \
    "deep_learning/data" \
    "1PJBmSE54fhe1_WDU_kTB3tIf7GDEPHIW 1PBirGT9ytlTJsnNnAGlT0xEpAzLX3N7K 1PNMkytuhg8ZSvQFdInzFPRIW9PF8EXL5 1PLbB47FucyIwE9n8LjNrypqlerhEo7jZ" \
    "covid19_tweets_dataset.zip dog_cat_dataset.zip house_prices_dataset.zip speech_emotion_dataset.zip"

# Download data for python level 1 course
# If this code does not work, you can download the datasets from these links below
# 1. predict_future_sales.zip: https://drive.google.com/file/d/1R83MNlUShY55i3CzlXpMAMcxnEg4Hruw/view?usp=sharing
# 2. credit_scoring.zip: https://drive.google.com/file/d/1Am5zRIh0Yg2JMWJ4ADhZqGZWss08WOdr/view?usp=sharing
process_data \
    "python_lv1/data" \
    "1R83MNlUShY55i3CzlXpMAMcxnEg4Hruw 1Am5zRIh0Yg2JMWJ4ADhZqGZWss08WOdr" \
    "predict_future_sales.zip credit_scoring.zip"

# Download data for skills test
# If this code does not work, you can download the dataset from these link below
# 1. Names.zip: https://drive.google.com/file/d/1AlgPZuIKSf8iU6bI4TqO3-MwjNBKMmTv/view?usp=sharing
process_data \
    "skills_test" \
    "1AlgPZuIKSf8iU6bI4TqO3-MwjNBKMmTv" \
    "Names.zip"