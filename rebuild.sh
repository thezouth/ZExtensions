python setup.py sdist
pip uninstall --no-cache-dir -y zextensions 
pip install --no-cache-dir -U dist/zextensions-0.0.7.tar.gz
jupyter nbextension uninstall airflow_scheduler
jupyter nbextension uninstall airflow_scheduler --py
jupyter nbextension uninstall airflow_scheduler --py --user
jupyter nbextension install airflow_scheduler --py --user
jupyter nbextension enable airflow_scheduler --py --user
jupyter serverextension enable airflow_scheduler --py --user
