 FROM jupyter/base-notebook

# Install required packages on top of base Jupyter image
COPY ./requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install --no-cache -r requirements.txt

ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

WORKDIR ${HOME}
USER ${USER}

# Copy all files (current directory onwards) into the image
COPY . /home/${NB_USER}/work
# Add EXPOSE to document the intended port of our jupyter web server
# and make automation of starting containers and using the given port easier
EXPOSE 8888
