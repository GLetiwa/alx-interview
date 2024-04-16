#!/usr/bin/python3
""" python function """


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened.
    """
    if not boxes:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()
    visited.add(0)  # Start with the first box unlocked

    # Initialize a queue to perform BFS
    queue = [0]

    # Perform BFS
    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]  # Keys in the current box

        # Check each key in the current box
        for key in keys:
            # If the key can unlock a new box and it hasn't been visited yet
            if key < len(boxes) and key not in visited:
                visited.add(key)
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)


# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # False
