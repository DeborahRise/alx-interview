def canUnlockAll(boxes):
    opened_box = set()
    is_visited = set()
    if len(boxes) == 1:
            return True
    return isOpen(boxes, is_visited=(), opened_box=(boxes[0]))

def isOpen(boxes, index=0, is_visited=(), opened_box=()):
    number_of_boxes = len(boxes)
    if boxes[index] & boxes != opened_box:
        for b in boxes[index]:
            if boxes[index] not in is_visited | boxes[b] not in opened_box:
                is_visited.add(boxes[index])
                if b < number_of_boxes:
                    opened_box.add(boxes[b])
                if boxes == opened_box:
                    return True
                isOpen(boxes, b, is_visited, opened_box)
            for n in boxes[b]:
                if boxes[b] in is_visited & boxes[n] in opened_box:
                    continue
                else:
                    isOpen(boxes, n, is_visited, opened_box)
            if boxes == opened_box:
                    return True
            return False
            
    if boxes[index] | boxes == opened_box:
            return True
    return False
    




    # for box in boxes:
    #     for b in box:
    #         is_visited.add(box)
    #         if b < number_of_boxes:
    #             opened_box.add(boxes[b])
    #             for item in boxes[b]:
    #                 is_visited.add(boxes[b])
    #                 if item < number_of_boxes:
    #                     opened_box.add(boxes[item])
    # for n in range(1, number_of_boxes):
    #     if n not in opened_box:
    #         return False
    # return True