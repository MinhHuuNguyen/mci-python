# MCI PYTHON LEVEL 1
## Run this command to export lectures, practices and solutions
``` bash
python export_lectures.py --lesson 0
```

## Run these commands to set up data folder tree
### Step 1: Download the `daily historical sales data`
by running this command <br>
```
gdrive download 1R83MNlUShY55i3CzlXpMAMcxnEg4Hruw
```
or download from this [link](https://drive.google.com/file/d/1R83MNlUShY55i3CzlXpMAMcxnEg4Hruw/view?usp=sharing)
### Step 2: Download the `credit scoring data`
by running this command <br>
```
gdrive download 1Am5zRIh0Yg2JMWJ4ADhZqGZWss08WOdr
```
or download from this [link](https://drive.google.com/file/d/1Am5zRIh0Yg2JMWJ4ADhZqGZWss08WOdr/view?usp=sharing)
### Step 2: Create folder, move file and unzip
``` bash
mkdir data
mv predict_future_sales.zip data
mv credit_scoring.zip data
unzip data/predict_future_sales.zip -d data
unzip data/credit_scoring.zip -d data
rm -rf data/__MACOSX
```

# MCI PYTHON INSTRUCTOR SKILLS TEST
## Requirements
The test requirements are available [here](https://github.com/MinhHuuNguyen/mci-python-level-1/blob/skill_test/skills_test/requirements.pdf).
## Run these commands to set up data folder tree
### Step 1: Download the `US baby name data` by running this command <br>
```
gdrive download 1AlgPZuIKSf8iU6bI4TqO3-MwjNBKMmTv
```
or download from this [link](https://drive.google.com/file/d/1AlgPZuIKSf8iU6bI4TqO3-MwjNBKMmTv/view?usp=sharing)
### Step 2: Create folder, move file and unzip
``` bash
mv Names.zip skills_test
unzip skills_test/Names.zip -d skills_test
rm -rf skills_test/Names/__MACOSX
```
