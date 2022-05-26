
courses_list=("python_lv1" "python_lv2" "deep_learning")
for data_name in ${courses_list[@]}
do
python export_lectures.py --input "$data_name/lectures" --output "$data_name/html_files"
done
