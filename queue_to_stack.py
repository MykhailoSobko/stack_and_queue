"""Queue to stack converter."""

from linkedstack import LinkedStack


def queue_to_stack(queue):
    """Return a stack that contains items from the queue."""
    stack = LinkedStack()
    item_list = []

    for item in queue:
        item_list.insert(0, item)

    for item in item_list:
        stack.push(item)

    return stack
