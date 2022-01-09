#!/usr/bin/env python3
import os
import string
import binascii
import codecs
import errno
import struct
import argparse
import shutil
import subprocess

from binascii import unhexlify


def ensure_dir(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Helper - Specify input file analysis and output folder to save corpus for strings in the overall project ---------------------------------------------------------------------------  Example usage : python3 thisfile.py outdir str.txt"
        )
    )

    # parser.add_argument("tokenpath",
    # help="Destination directory for tokens")
    parser.add_argument("cur", help="Current Path")
    parser.add_argument("db", help="CodeQL database Path")
    parser.add_argument("tokenpath", help="Destination directory for tokens")

    return parser.parse_args()


def static_analysis(file, file2, cur, db):
    with open(cur + "/" + file, "w") as f:
        print(cur + "/" + file)
        stream = os.popen("codeql query run " + cur + "/" + file2 + " -d " + db)
        output = stream.read()
        f.write(output)
        f.close()


def copy_tokens(cur, tokenpath):
    subprocess.call(
        ["mv " + cur + "/" + "arrlits/*" + " " + cur + "/" + tokenpath + "/."],
        shell=True,
    )
    
    subprocess.call(
        ["mv " + cur + "/" + "globals/*" + " " + cur + "/" + tokenpath + "/."],
        shell=True,
    )
    subprocess.call(
        ["mv " + cur + "/" + "locals/*" + " " + cur + "/" + tokenpath + "/."],
        shell=True,
    )
    subprocess.call(
        ["mv " + cur + "/" + "magics/*" + " " + cur + "/" + tokenpath + "/."], shell=True
    )
    subprocess.call(
        ["mv " + cur + "/" + "memcmp-vals/*" + " " + cur + "/" + tokenpath + "/."],
        shell=True,
    )
    subprocess.call(
        ["rm -rf strcmp-strs memcmp-strs strncmp-strs lits strtool-strs"], shell=True
    )
    subprocess.call(["rm *.out"], shell=True)
    subprocess.call(["find " + tokenpath + " -size 0 -delete"], shell=True)


def codeql_analysis(cur, db):
    print("codeql analysis func")
    static_analysis("arrlits.out", "array-literals.ql", cur, db)
    static_analysis("magics.out", "magic-values.ql", cur, db)
    static_analysis("memcmpvals.out", "memcmpvals.ql", cur, db)
    static_analysis("regex.out", "regex-values.ql", cur, db)
    static_analysis("strcmpvals.out", "strcmpvals.ql", cur, db)
    static_analysis("globals.out", "Global-values.ql", cur, db)
    static_analysis("strstr.out", "strstrvals.ql", cur, db)
    static_analysis("locals.out", "local-variables.ql", cur, db)
    
    
    start_fd(0, cur)


def start_fd
(tokenpath, cur):
    print("At start func")
    command = ["python3", cur + "/array-literals.py", cur + "/arrlits/.", cur + "/arrlits.out"]
    worker1 = subprocess.Popen(command)
    print(worker1.communicate())

    command1 = [
        "python3",
        cur + "/Global-values.py",
        cur + "/globals/",
        cur + "/globals.out",
    ]
    worker2 = subprocess.Popen(command1)
    print(worker2.communicate())

    command2 = [
        "python3",
        cur + "/local-variables.py",
        cur + "/locals/",
        cur + "/locals.out",
    ]
    worker3 = subprocess.Popen(command2)
    print(worker3.communicate())

    command5 = [
        "python3",
        cur + "/magic-values.py",
        cur + "/magics/",
        cur + "/magics.out",
    ]
    worker6 = subprocess.Popen(command5)
    print(worker6.communicate())

    command8 = [
        "python3",
        cur + "/memcmpvals.py",
        cur + "/memcmpvals/",
        cur + "/memcmpvals.out",
    ]
    worker9 = subprocess.Popen(command8)
    print(worker9.communicate())

    command9 = [
        "python3",
        cur + "/regex-values.py",
        cur + "/regexvals/",
        cur + "/regex.out",
    ]
    worker7 = subprocess.Popen(command9)
    print(worker7.communicate())

    command10 = [
        "python3",
        cur + "/strcmpvals.py",
        cur + "/strcmpvals/",
        cur + "/strcmpvals.out",
    ]
    worker8 = subprocess.Popen(command8)
    print(worker8.communicate())

    command11 = [
        "python3",
        cur + "/strstrvals.py",
        cur + "/strstrvals/",
        cur + "/strstr.out",
    ]
    worker10 = subprocess.Popen(command11)
    print(worker10.communicate())
    


def main():
    args = parse_args()
    ensure_dir(args.tokenpath)
    codeql_analysis(args.cur, args.db)
    copy_tokens(args.cur, args.tokenpath)
  


if __name__ == "__main__":
    main()
