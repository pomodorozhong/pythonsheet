import pandas as pd
import numpy as np


def match(search_keys: 'series', search_range: 'series'):
    result = []

    for key in search_keys:
        if (search_range == key).any():
            index = int((search_range == key).argmax())
        else:
            index = "!NO_MATCH!"

        result.append(index)

    return result


def index(references: 'series', rows_to_extract: 'series'):
    result = []

    for row in rows_to_extract:
        if row == "!NO_MATCH!":
            result.append("NO_MATCH")
        else:
            result.append(references[row])

    return result
