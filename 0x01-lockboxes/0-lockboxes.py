#!/usr/bin/python3
"""
n number of locked boxes
Each box numbered sequentially from 0 - (n - 1)
Each box may contain keys to the other boxes
Write a method that can determine if all boxes can be opened
    Requirements to open a box:
    boxes = [[], [], []]
    if box[1] contains key 5.
    then box[1] contains a key that can open box 5.
    box[0] is always open = True.

    if ALL BOXES can be opened, return True
    else return False.

    e.g: box[3] = [2, 12, 9]

    meaning, box at index 3 contains keys that can open box at index 2, 12, 9
"""

def canUnlockAll(boxes):
    number_of_boxes = len(boxes)
    box_keys = set()
    for box in boxes:
        for b in box:
            box_keys.add(b)
    for n in range(1, number_of_boxes):
        if n not in box_keys:
            return False
    return True
