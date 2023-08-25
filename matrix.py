from names import get_full_name as genname
from random import choice, randrange, sample
from time import sleep
import json
import os
from utils import read, configurator

SIZES = ["Big", "Small", "Medium"]
FOODS = ["Burger", "Sadwich", "Lasagna", "Pizza", "Spaghetti", "Donut", "Burrito"]

COLORS = {
    "red": "#f44336", 
    "green": "#4caf50", 
    "blue": "#008cba",
    "gray": "#555555",
    "black": "#000000"
    }


def f_walk():
    n = randrange(1, 25)
    return "walked", f"{str(n)} metres", "green"


def f_eat():
    size = choice(SIZES)
    food = choice(FOODS)
    return "ate", f"a {str(size)} {str(food)}", "blue"


def f_sleep():
    n = randrange(1, 10)
    return "slept", f"{str(n)} hours", "gray"


def f_nothing():
    n = randrange(1, 25)
    return "nothing", f"{str(n)} minutes", "black"


options = [
    f_walk,
    f_eat,
    f_sleep,
    f_nothing,
]


class Human:
    def __init__(self, name: str = None):
        self.name = genname() if name == None else name

    def log(self, event: str, details: str, color: str):
        """Log

        Keyword arguments:
        event: A string
        Return: Dict containing name & event"""
        result = {"name": self.name, "event": event, "details": details, "color": COLORS[color]}
        print(f'"{result["name"]}"    \t{result["event"]}\t({result["details"]})')
        return result

    def do(self, action):
        """Do action

        Keyword arguments:
        action: A function that returns a event
        Return: Dict containing name & event"""
        ev, de, co = action()
        return self.log(ev, de, co)

    def dump(self):
        """Dump

        Return: Name of Human"""
        return self.name


class Simulation:
    def __init__(self, humans: list):
        """Simulation

        Keyword arguments:
        humans: A list of Humans"""
        self.humans = humans

    def _tick(self, file):
        """Internal: Run a Tick

        Return: List of dicts with name & event as args"""
        history = []
        for human in self.humans:
            opt = choice(options)
            history.append(human.do(opt))
        with open(file, "a") as f:
            f.write(json.dumps(history) + "\n")

    def run(self, file: str, iters: int = 5):
        """Run the simulation

        Keyword arguments:
        file: Simulation File name
        iters: Iterations
        Return: List of Humans"""

        newfile = os.path.exists(file)
        if not newfile:
            configurator(file, [human.dump() for human in self.humans])
        for iter in range(iters):
            json.dumps(self._tick(file)) + "\n"


def genhumans(file: str, n: int):
    """Generate humans from Simulation file.
    if there is no file: generate n humans.

    Keyword arguments:
    file: Simulation File name
    n: if file not exist, generate n humans
    Return: List of Humans
    """
    newfile = os.path.exists(file)
    humans = []
    if newfile:
        humans = [Human(name) for name in read(file)["humans"]]
    else:
        humans = [Human() for i in range(n)]
    return humans


def make_sim(file: str, iters: int = 5, n: int = 10):
    h = Human()
    s = Simulation(genhumans(file, n))
    s.run(file, iters)


if __name__ == "__main__":
    make_sim("main.sim", 10)
