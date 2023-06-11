import json


def read(file: str):
    out = {}
    with open(file, "r") as f:
        k = f.read().splitlines()
        out["header"] = k[0]
        out["humans"] = k[1].split(":")
        out["iters"] = {}
        for i in range(2, len(k)):
            iter = json.loads(k[i])
            out["iters"][i - 2] = iter
    return out


def reads(s: str):
    out = {}
    k = s.splitlines()
    out["header"] = k[0]
    out["humans"] = k[1].split(":")
    out["iters"] = {}
    for i in range(2, len(k)):
        iter = json.loads(k[i])
        out["iters"][i] = iter
    return out


def configurator(file: str, humans: list):
    with open(file, "w") as f:
        res = ":".join(humans)
        f.write("-AxelMatrix Simulation File-\n" + res + "\n")


def configurators(humans: list):
    res = ":".join(humans)
    return "-AxelMatrix Simulation File-\n" + res + "\n"


def add_human(file: str, human: str):
    res = read(file)
    humans: list = res["humans"]
    humans.append(human)
    with open(file, "w") as f:
        res = ":".join(humans)
        f.write("-AxelMatrix Simulation File-\n" + res + "\n")
