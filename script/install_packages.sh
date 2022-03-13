conda create -n mci_env python=3.8 -y
conda activate mci_env
conda install -c anaconda jupyter -y
conda install -c conda-forge tqdm -y
conda install -c anaconda numpy -y
conda install -c anaconda pandas -y
conda install -c conda-forge matplotlib -y
conda install -c anaconda seaborn -y
conda install -c anaconda scikit-learn -y
conda install -c conda-forge tensorflow -y
conda install -c conda-forge keras -y
conda install -c conda-forge jupyter_nbextensions_configurator -y
conda install -c conda-forge jupyter_contrib_nbextensions -y
conda install -c conda-forge autopep8 -y
conda install -c anaconda nltk -y
python "import nltk; nltk.download('stopwords')"
