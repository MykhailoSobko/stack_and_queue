"""
Stack to queue converter.
"""

from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """Return a queue that contains items from the stack."""
    queue = LinkedQueue()
    item_list = []

    for item in stack:
        item_list.insert(0, item)

    for item in item_list:
        queue.add(item)

    return queue
