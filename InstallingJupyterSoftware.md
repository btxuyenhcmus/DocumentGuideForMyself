# Getting started with JupyterLab
## Installation
JupyterLab can be installed using *conda* or *pip3*.
### conda
If you use *conda*, you can install it with:
```
conda install -c conda-forge jupyterlab
```
### pip3
If you use *pip3*, you can install it with:
```
pip3 install jupyterlab
```
If installing using *pip3 install --user*, you must add the user-level *bin* directory to your *PATH* environment variable in order to lauch *jupyter lab*.
# Getting stated with the classic Jupyter Notebook
## Prerequisite: Python
While Jupyter runs code in many programming languages, Python is a requirement (Python 3.3 or greater, or Python 2.7) for installing the JupyterLab or the classic Jupyter Notebook.
## Installing Jupyter Notebook using Conda
### conda
We recommend installing Python and Jupyter using the conda package manager. The miniconda distribution includes a minimal Python and conda installation.
Then you can install the notebook with:
```
conda install -c conda-forge notebook
```
### pip3
If you use *pip3*, you can install it with:
```
pip3 install notebook
```
Congratulations, you have installed Jupyter Notebook! To run the notebook, run the following command at the Terminal (Mac/Linux) or Command Prompt (Windows):
```
jupyter notebook
```
# Getting started with Voilà
## Installation
Voilà can be installed using *conda* or *pip3*.
### conda
If you use *conda*, you can install it with:
```
conda install -c conda-forge voila
```
### pip3
If you use *pip3*, you can install it with:
```
pip install voila
```

# Installed jupyter extensions
```
pip3 install jupyter_contrib_nbextensions
pip3 install jupyter_nbextensions_configurator
jupyter contrib nbextension install --user
jupyter nbextensions_configurator enable --user
```
