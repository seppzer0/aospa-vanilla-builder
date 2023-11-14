import io
import os
import sys


def note(text: str) -> None:
    """A "note" wrapper.

    :param text: Text to wrap.
    """
    print(f"[ * ] {text}")


def error(text: str, dont_exit: bool = False) -> None:
    """An "error" wrapper.

    :param text: Text to wrap.
    """
    print(f"[ ! ] {text}", file=sys.stderr)
    if not dont_exit:
        sys.exit(1)


def cancel(text: str) -> None:
    """A "cancel" wrapper.

    :param text: Text to wrap.
    """
    print(f"[ ~ ] {text}")
    sys.exit(0)


def done(text: str) -> None:
    """A "done" wrapper.

    :param text: Text to wrap.
    """
    print(f"[ + ] {text}")


def outputstream() -> None:
    """Stream output messages."""
    stream = os.getenv("OSTREAM", "screen")
    if stream != "screen":
        sys.stdout = open(stream, "a")
    else:
        sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), write_through=True)
