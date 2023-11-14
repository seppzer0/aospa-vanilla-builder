# aospa-vanilla-builder — an easy wrapper for GMS-less AOSPA builds

aospa-vanilla-builder is a simple Dockerized wrapper for building "vanilla" AOSPA (aka without Google Mobile Services).

All of the steps are done according to official AOSPA instruction manual with a few additions to make the entire build process automated.

## Usage

The usage of this wrapper consists of two parts:

### 1. Preparing the environment

To prepare the containerized build environment, use:

```sh
docker build . -t aospa-vanilla-builder
```

This action will prepare a Docker image that has all the settings, tools and sources required for the AOSPA build.

### 2. Launching the ROM build

To launch the ROM build using the prepared Docker image, use:

```sh
docker run --rm -it aospa-vanilla-builder
```
