FROM jupyter/datascience-notebook
RUN pip install --quiet --no-cache-dir 'celery' && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
