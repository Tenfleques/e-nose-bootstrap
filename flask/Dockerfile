FROM debian:latest

#  $ docker build . -t continuumio/anaconda:latest -t continuumio/anaconda:5.3.0 -t continuumio/anaconda2:latest -t continuumio/anaconda2:5.3.0
#  $ docker run --rm -it continuumio/anaconda2:latest /bin/bash
#  $ docker push continuumio/anaconda:latest
#  $ docker push continuumio/anaconda:5.3.0
#  $ docker push continuumio/anaconda2:latest
#  $ docker push continuumio/anaconda2:5.3.0

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda2-5.3.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN conda install -c anaconda flask
RUN conda install jupyter -y --quiet 
RUN mkdir /opt/notebooks

#RUN /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root

ADD ./app /app
WORKDIR /app

EXPOSE 8888
EXPOSE 5000

CMD [ "python", "app.py" ]