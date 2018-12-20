from .positionals import Direction


class Node:
    """
    Tree Node class for action tree search
    """
    def __init__(self):
        actions = Direction.get_all_cardinals() + [Direction.Still]
        children = []

    def expand(self):
        return