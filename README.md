# aospa-vanilla-builder — an easy wrapper for Dockerized GMS-less AOSPA builds

aospa-vanilla-builder is a simple Dockerized wrapper for building "vanilla" AOSPA (aka without Google Mobile Services).

All of the steps are done according to official AOSPA instruction manual with a few additions to make the entire build process automated.

## Usage

The usage of this wrapper consists of two parts:

- preparing the environment (aka building the Docker image);
- launching the ROM build.

Both steps are handled automatically within the wrapper.

```help
$ python3 wrapper --help
usage: wrapper [-h] [--clean CLEAN] device branch

positional arguments:
  device         select a device codename
  branch         select AOSPA branch

options:
  -h, --help     show this help message and exit
  --clean CLEAN  select to clean up Docker cache before the build
```

As an example, to launch a build for OnePlus 5T device with Topaz branch, use:

```sh
python3 wrapper oneplus5t topaz
```
