from typing import List


def compress_indexes_into_ranges(indexes: List[int]):
    # compress indexes into ranges
    ranges = []
    start = indexes[0]
    end = indexes[0]
    for index in indexes[1:]:
        if index == end + 1:
            end = index
        else:
            ranges.append((start, end))
            start = index
            end = index

    ranges.append((start, end))
    return ranges
