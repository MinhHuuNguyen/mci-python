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
or download from this [link](https://drive.google.com/open?id=1R83MNlUShY55i3CzlXpMAMcxnEg4Hruw&authuser=20152464%40student.hust.edu.vn&usp=drive_fs)
### Step 2: Create folder, move file and unzip
``` bash
mkdir data
mv predict_future_sales.zip data
unzip data/predict_future_sales.zip -d data
rm -rf data/__MACOSX
```