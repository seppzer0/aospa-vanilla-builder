import os
import shutil

import tools.commands as ccmd

from configs import Config as cfg


class RomBuilder:
    """AOSPA ROM builder."""

    def __init__(self, device: str, branch: str) -> None:
        self._device = device
        self._branch = branch
        # extend image name with a tag
        self._name_image = f"{cfg.NAME_IMAGE}:{device}-{branch}"

    def _setup_volumes(self) -> None:
        """Mount directories for file sharing between host and container."""
        # create a clean directory for artifacts
        shutil.rmtree(cfg.DIR_ARTIFACTS, ignore_errors=True)
        os.mkdir(cfg.DIR_ARTIFACTS)

    def build(self) -> None:
        """Create a Docker container and run the build."""
        self._setup_volumes()
        cmd = "docker run --rm -it -v {}:/artifacts --name {} {}"\
              .format(
                cfg.DIR_ARTIFACTS,
                cfg.NAME_CONTAINER,
                cfg.NAME_IMAGE
              )
        ccmd.launch(cmd)
