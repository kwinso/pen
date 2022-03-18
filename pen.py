#!/bin/env python

import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="subp")
    p = subparsers.add_parser(
        "export",
        help="Exports a given value addres to shell variable accessible from every terminal.",
        aliases=["e"],
        usage="%(prog)s <value>"
    ).add_argument("value", help="A value to export.")

    subparsers.add_parser(
        "show",
        aliases=["s"],
        help="Shows an exported $PEN var. (Use -c to copy)",
    ).add_argument(
        "-c",
        nargs="?",
        help="Show and copy to clipboard",
        type=bool,
        default=False,
    )

    return parser.parse_args()


def main():
    args = parse_args()
    pen_file = os.getenv("HOME") + "/.pen"

    if hasattr(args, "value") and args.vaue is not None:
        with open(pen_file, "w") as f:
            f.write(args.value)

    elif args.subp == "show":
        try:
            with open(pen_file, "r") as f:
                value = f.read()
                if value:
                    print(value)
                    if hasattr(args, "c"):
                        os.system(
                            f"echo -n {value} | xclip -selection clipboard")
                        print("Copied to clipboard.")
                else:
                    print("No value is exported.")
        except Exception as e:
            print(
                f"Unable to open {pen_file} file.\nMaybe it's not created yet. Create it with 'pen export <value>' command.")


if __name__ == "__main__":
    main()
