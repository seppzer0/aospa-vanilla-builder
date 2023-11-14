import subprocess
from typing import Union

import tools.messages as msg


def launch(cmd: str, get_output: bool = False) -> Union[str, None]:
    """
    A custom subprocess wrapper to launch commands.

    :param cmd: A command to launch.
    :param loglvl: Log level.
    :param get_output: A switch to get the piped output of the command.
    """
    # determine stdout and check some of the cases
    cstdout = subprocess.PIPE if get_output is True else None
    # avoid using shell
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=cstdout, stderr=subprocess.STDOUT)
        # return only output if required
        if get_output is True:
            return result.stdout.decode('utf-8').splitlines()[0]
    except Exception:
        msg.error(f"Error executing command: {cmd}")
