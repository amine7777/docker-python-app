FROM centos:7

RUN yum install -y python-devel

RUN yum install -y centos-release-scl
RUN yum install -y devtoolset-7-gcc-*
RUN echo "source scl_source enable devtoolset-7" >> /etc/bashrc
RUN source /etc/bashrc

RUN yum -y update && yum clean all

RUN mkdir -p /go && chmod -R 777 /go && \
    yum install -y centos-release-scl && \
    yum -y install git go-toolset-7-golang && yum clean all

ENV GOPATH=/go \
    BASH_ENV=/opt/rh/go-toolset-7/enable \
    ENV=/opt/rh/go-toolset-7/enable \
    PROMPT_COMMAND=". /opt/rh/go-toolset-7/enable"

WORKDIR /go


RUN mkdir -p /app
WORKDIR /app
COPY . /app
ENTRYPOINT python app.py
