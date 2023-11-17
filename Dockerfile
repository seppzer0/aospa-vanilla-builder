FROM ubuntu:22.04

# define build arguments
ARG DEVICE
ARG BRANCH
ARG WORKSPACE=build

# overwrite build arguments with environment variables, to embed the values into the image
ENV DEVICE ${DEVICE}
ENV BRANCH ${BRANCH}

# define workdir
WORKDIR /aospa

# make DEVICE and BRANCH mandatory for specification
RUN test -n "${DEVICE}" || (echo "[ ! ] DEVICE is not set; please use '--build-arg <device>' for the 'docker build' command" && false)
RUN test -n "${BRANCH}" || (echo "[ ! ] BRANCH is not set; please use '--build-arg <branch>' for the 'docker build' command" && false)

# install basic packages
RUN apt-get update && \
    apt-get install -y \
        git-core \
        gnupg \
        flex \
        bison \
        build-essential \
        zip \
        curl \
        zlib1g-dev \
        libc6-dev-i386 \
        libncurses5 \
        x11proto-core-dev \
        libx11-dev \
        lib32z1-dev \
        libgl1-mesa-dev \
        libxml2-utils \
        xsltproc \
        unzip \
        python3 \
        python-is-python3 \
        fontconfig && \
    apt-get autoremove -y

# installing repo
ADD https://storage.googleapis.com/git-repo-downloads/repo /usr/local/bin/
RUN chmod 755 /usr/local/bin/*

# initializing repo + downloading the source tree
RUN repo init -u https://github.com/AOSPA/manifest -b ${BRANCH} && \
    repo sync --no-clone-bundle --current-branch --no-tags -j$(nproc --all) && \
    repopick -t ${BRANCH}-vanilla

# build
CMD [ "./rom-build.sh",  "${DEVICE}" ]
