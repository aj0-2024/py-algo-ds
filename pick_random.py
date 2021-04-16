import random
import click


@click.group()
def cli():
    """Pick random topics for daily review"""


@cli.command()
def algorithm():
    """Pick a random algorithm set for review"""
    topic = random.choice([
        "Primitive Types", "Array", "String", "Linked List",
        "Stack and Queues", "Binary Trees", "Binary Search Tree", "Heaps",
        "Search", "Sorting", "Recursion", "Dynamic Programming",
        "Divide & conquer", "Greedy Algorithms", "Geometry", "Math",
        "Sliding window", "Trie", "Backtracking", "Hash Tables", "Graph",
        "Path finding"
    ])
    print("Topic for today is -->", topic)


@cli.command()
def system_design():
    """Pick a random topic for review"""
    topic = random.choice([
        "Data models", "Storage & Retrieval", "Encoding & Evolution",
        "Replication", "Partitioning", "Transactions",
        "Trouble with distributed systems", "Consensus algorithms",
        "Stream systems", "Future of design systems"
    ])
    print("Topic for today is -->", topic)


if __name__ == "__main__":
    cli()
