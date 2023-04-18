# input: 'This is a pen. This is an apple. Applepen.'
# output:('p',6)
from typing import Tuple

import operator


def max_char(text: str) -> Tuple[str, int]:
    text = text.lower()
    result = {}
    for val in text:
        if result.get(val):
            result[val] += 1
        else:
            result[val] = 1

    max_val = max(result, key=result.get)
    return max_val, result[max_val]


if __name__ == "__main__":
    input = "This is a pen. This is an apple. Applepen."
    print(max_char(input))
