import sys
import argparse

from models.image_builder import ImageBuilder


def parse_args() -> argparse.Namespace:
    """Parse aerguments."""
    args = None if sys.argv[1:] else ["-h"]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "device",
        help="select a device codename"
    )
    parser.add_argument(
        "branch",
        help="select AOSPA branch"
    )
    parser.add_argument(
        "--clean",
        help="select to clean up Docker cache before the build"
    )
    return parser.parse_args(args)


def main(args: argparse.Namespace) -> None:
    # build the Docker image
    image_builder = ImageBuilder(
        device=args.device,
        branch=args.branch,
        clean=args.clean
    )
    image_builder.build()
    # build the ROM image


if __name__ == "__main__":
    main(parse_args())