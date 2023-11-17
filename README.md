# aospa-vanilla-builder

An easy wrapper for Dockerized GMS-less AOSPA builds.

## Contents

- [aospa-vanilla-builder](#aospa-vanilla-builder)
  - [Contents](#contents)
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [Credits](#credits)

## Description

This project is a simple Dockerized wrapper for building "vanilla" AOSPA (aka without Google Mobile Services).

All of the steps are done according to official AOSPA instruction manual with a few additions to make the entire build process automated.

aospa-vanilla-builder can be used for any device and branch supported by AOSPA, as long as there is an existing official build present on the [project's page](https://paranoidandroid.co).

## Prerequisites

To use this wrapper, the following is required to be installed:

- Docker (either Docker Desktop or Docker CLI, depending on your OS);
- Python 3.x + PIP (3.10+ is stronly recommended).

Also, if you are considering running this locally, please make sure you have sufficient RAM and ROM resources available on your machine (32+ Gb and 512+ Gb accordingly).

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

## Credits

- [AOSPA/manifest](https://github.com/AOSPA/manifest): AOSPA's official guide on building the ROM image.
