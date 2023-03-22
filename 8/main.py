def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def part1(p):
    visible = 0

    # Edges
    visible += len(p) * 2 + (len(p[0]) - 2) * 2

    for row_index, row_item in enumerate(p):
        if row_index == 0 or row_index == len(p) - 1:
            continue
        for col_index, col_item in enumerate(row_item):
            if col_index == 0 or col_index == len(row_item) - 1:
                continue

            current_tree = col_item
            top_trees = [i[col_index] for i in p[:row_index]]
            bottom_trees = [i[col_index] for i in p[row_index+1:]]

            visible_from_left = all(current_tree > i
                                    for i in row_item[:col_index])
            visible_from_right = all(current_tree > i
                                     for i in row_item[col_index+1:])
            visible_from_top = all(current_tree > i for i in top_trees)
            visible_from_bottom = all(current_tree > i for i in bottom_trees)

            visible += any([visible_from_top, visible_from_right,
                           visible_from_left, visible_from_bottom])

    return visible


def calc_vision_score(current_tree, tree_list):
    index = 0
    score = 0
    while index != len(tree_list):
        score += 1
        if tree_list[index] >= current_tree:
            return score
        index += 1

    return score


def part2(p):
    score = 0

    for row_index, row_item in enumerate(p):
        if row_index == 0 or row_index == len(p) - 1:
            continue
        for col_index, col_item in enumerate(row_item):
            if col_index == 0 or col_index == len(row_item) - 1:
                continue

            current_tree = col_item
            top_trees = [i[col_index] for i in p[:row_index][::-1]]
            bottom_trees = [i[col_index] for i in p[row_index+1:]]

            score_from_left = calc_vision_score(
                current_tree, row_item[:col_index][::-1])
            score_from_right = calc_vision_score(
                current_tree, row_item[col_index+1:])
            score_from_top = calc_vision_score(current_tree, top_trees)
            score_from_bottom = calc_vision_score(current_tree, bottom_trees)

            temp_score = score_from_top * score_from_right * \
                score_from_left * score_from_bottom
            score = temp_score if temp_score > score else score

    return score


if __name__ == "__main__":
    main()
