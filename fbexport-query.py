from subprocess import run
from argparse import ArgumentParser
from os import environ
from configparser import ConfigParser
import shutil

FBEXPORT_KEY = "FBEXPORT"
CONFIG_FNAME = "CONFIG.ini"

FBCOMMAND = [
    "-Sc",
    "-J",
    "Y-M-D",
    "-H",
    "",
    "-U",
    "sysdba",
    "-P",
    "masterkey",
]


class FbexportError(Exception):
    pass


def find_fbexport() -> str:
    try:
        fbexport = environ[FBEXPORT_KEY]
    except KeyError:
        config = ConfigParser()
        config.read(CONFIG_FNAME)
        try:
            fbexport = config["DEFAULT"][FBEXPORT_KEY]
        except KeyError:
            fbexport = shutil.which("fbexport")
    if fbexport is None:
        raise FbexportError("fbexport not found.")
    return fbexport


def run_query(db: str, query: str, out: str):
    fbexport = find_fbexport()
    command = [fbexport]
    for token in FBCOMMAND:
        command.append(token)
    command.append("-D")
    command.append(db)
    command.append("-Q")
    command.append(query)
    command.append("-F")
    command.append(out)
    run(command)


def main():
    parser = ArgumentParser("fbexport-query.py")
    parser.add_argument("db", help="Database location.")
    parser.add_argument("sql", help="File with SQL query to execute.")
    parser.add_argument(
        "--out", help="Output location. Use '-' for stdout (default).", default="-"
    )
    args = parser.parse_args()
    with open(args.sql) as f:
        query = f.read()
        run_query(args.db, query, args.out)


if __name__ == "__main__":
    main()
