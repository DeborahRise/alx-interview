#!/usr/bin/python3
"""
n number of locked boxes
Each box numbered sequentially from 0 - (n - 1)
Each box may contain keys to the other boxes.
or every box must be directly accessible from an unlocked box
There can be boxes without keys, but can they be opened?
Write a method that can determine if all boxes can be opened
    Requirements to open a box:
    boxes = [[], [], []]
    if box[1] contains key 5.
    then box[1] contains a key that can open box 5.
    box[0] is always open = True.

    if ALL BOXES can be opened, return True
    else return False.

    e.g: box[3] = [2, 12, 9]

    meaning, box at index 3 contains keys that can open box at index 2, 12,
More:
box[0] is always open
the keys in box[0] determines the box to open next.
isVisited = False
for box in boxes:
    for b in box:
    if b < len(boxes):
        boxes[b] = isOpen
"""


def canUnlockAll(boxes):
    unlocked = set([0])
    keys = [0]
    len_box = len(boxes)
    counter = 0

    if len_box == 1:
        return True

    while counter < len(keys):
        index = keys[counter]
        for key in boxes[index]:
            if key not in unlocked and key < len_box:
                unlocked.add(key)
                keys.append(key)
        counter += 1
    return len(unlocked) == len_box
