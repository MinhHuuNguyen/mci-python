conda install -c anaconda jupyter -y
conda install -c conda-forge tqdm -y
conda install -c anaconda numpy -y
conda install -c anaconda pandas -y
conda install -c anaconda openpyxl -y
conda install -c conda-forge matplotlib -y
conda install -c anaconda seaborn -y
conda install -c anaconda scikit-learn -y
conda install -c conda-forge tensorflow -y
conda install -c conda-forge keras -y
conda install -c conda-forge jupyter_nbextensions_configurator -y
conda install -c conda-forge jupyter_contrib_nbextensions -y
conda install -c conda-forge autopep8 -y
conda install -c conda-forge librosa -y
conda install -c anaconda nltk -y
python -c "import nltk; nltk.download('stopwords')"

# This line will fix the warning:
# `nbextension 'execute_time/ExecuteTime' has duplicate listings in both`
# It will remove the jupyter_contrib_nbextensions install from the user directory
# More details can be found
# https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator/issues/25
jupyter contrib nbextensions uninstall --user
