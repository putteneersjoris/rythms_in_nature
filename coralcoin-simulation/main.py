from treelib import Tree
from numpy.random import choice, normal

AVAILABLE_NODES = ["0"]
tree = Tree()
tree.create_node(
    identifier="0",
    data={
        "buffer": 0,
        "available": True,
        "transaction_count": 0,
    },
)

class Agent:
    def __init__(self, magnitude):
        self.magnitude = magnitude
        self.node = "0"

    def find_nearest_node(self):
        if not AVAILABLE_NODES:
            tree.save2file("tree.txt")
            tree.show()
            print("GAME OVER")
            exit()
        elif self.node in AVAILABLE_NODES:
            pass
        else:
            self.node = choice(AVAILABLE_NODES)

    def water_transfer(self):
        tree.get_node(self.node).data["buffer"] += normal(
            loc=self.magnitude,
            scale=abs(self.magnitude) / 10
        )

    def grow_coral(self):
        tree.get_node(self.node).data["transaction_count"] += 1
        if tree.get_node(self.node).data["transaction_count"] > 9:
            delta = abs(tree.get_node(self.node).data["buffer"] - 0)
            # kill
            if delta > 4:
                AVAILABLE_NODES.remove(self.node)
            # grow
            elif delta > 2:
                AVAILABLE_NODES.remove(self.node)
                AVAILABLE_NODES.append(self.node + "0")
                tree.create_node(
                    identifier=self.node + "0",
                    data={
                        "buffer": 0,
                        "available": True,
                        "transaction_count": 0
                    },
                    parent=tree.get_node(self.node),

                )
            # branch
            else:
                AVAILABLE_NODES.remove(self.node)
                AVAILABLE_NODES.append(self.node + "0")
                AVAILABLE_NODES.append(self.node + "1")
                tree.create_node(
                    identifier=self.node + "0",
                    data={
                        "buffer": 0,
                        "available": True,
                        "transaction_count": 0
                    },
                    parent=tree.get_node(self.node),
                )
                tree.create_node(
                    identifier=self.node + "1",
                    data={
                        "buffer": 0,
                        "available": True,
                        "transaction_count": 0
                    },
                    parent=tree.get_node(self.node),
                )

    def commit_transaction(self):
        self.find_nearest_node()
        self.water_transfer()
        self.grow_coral()

agents = [
    Agent(magnitude=1),  # rain
    Agent(magnitude=1),  # rain
    Agent(magnitude=1),  # rain
    Agent(magnitude=1),  # rain
    Agent(magnitude=1),  # snow
    Agent(magnitude=-1),  # heatwave
    Agent(magnitude=-1),  # heatwave
    Agent(magnitude=-0.7),  # person
    Agent(magnitude=-0.7),  # person
    Agent(magnitude=-0.7),  # person
    Agent(magnitude=-0.7),  # person
    Agent(magnitude=-0.7),  # person
    Agent(magnitude=-0.7),  # person
    Agent(magnitude=-0.7),  # person
    Agent(magnitude=-0.7),  # person
    Agent(magnitude=-0.7),  # person
    Agent(magnitude=-0.7),  # person
]

while True:
    for agent in agents:
        agent.commit_transaction()
