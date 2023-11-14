import os
import requests

import tools.messages as msg
import tools.commands as ccmd

from configs import Config as cfg


class ImageBuilder:
    """A Docker image builder."""

    _endpoint = "https://api.paranoidandroid.co/updates/{}"

    def __init__(self, device: str, branch: str, clean: bool) -> None:
        self._device = device
        self._branch = branch
        self._clean = clean
        self._endpoint = self._endpoint.format(self._device)
        # extend image name with a tag
        self._name_image = f"{cfg.NAME_IMAGE}:{device}-{branch}"

    def _check_arguments(self) -> None:
        """Validate the provided device and branch arguments.
        
        Device name check is a simple request done to AOSPA API.
        If the device name is invalid, the request will result in error.

        Branch name check is acquiring the data from the device check and looking
        looking for the "version" attribute across all available builds.
        If branch name is invalid, the "version": "<branch>" search will result in error.
        """
        # device check
        data = {}
        try:
            data = requests.get(self._endpoint).json()["updates"]
        except Exception:
            msg.error(
                'Could not validate "{}" device, please check the provided value and the connection.'\
                .format(self._device)
            )
        # branch check
        check = 0
        for build_info in data:
            if build_info["version"] == self._branch.capitalize():
                check = 1
                break
        if check != 1:
            msg.error(
                'Could not detect specified "{}" branch for the "{}" device'\
                .format(self._branch, self._device)
            )

    def _clean_cache(self) -> None:
        """Clean local Docker cache if specified."""
        if self._clean:
            msg.note("Cleaning local Docker cache..")
            ccmd.launch(f"docker rmi {self._name_image} -f")
            msg.done("Done!")

    def build(self) -> None:
        """Run the image build."""
        self._check_arguments()
        self._clean_cache()
        os.chdir(cfg.DIR_ROOT)
        build_args = (
            f"DEVICE={self._device}",
            f"BRANCH={self._branch}"
        )
        ccmd.launch(
            'docker build . -t {} {}'\
            .format(
                self._name_image,
                " ".join([f"--build-arg {arg}" for arg in build_args])
            )
        )
