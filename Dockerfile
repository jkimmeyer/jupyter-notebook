FROM jupyter/base-notebook

# Install required packages on top of base Jupyter image
RUN pip install --no-cache \
   scipy \
   numpy \
   pandas \
   scikit-learn \
   matplotlib \
   tensorflow

ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

WORKDIR ${HOME}
USER ${USER}

# Copy all files (current directory onwards) into the image
COPY ./index.ipynb /home/${NB_USER}/work
