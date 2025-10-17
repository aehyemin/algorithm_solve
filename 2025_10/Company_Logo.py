#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    s_c = Counter(s)
    
    sc_sort = sorted(s_c.items(), key=lambda x:(-x[1], x[0]))[:3]

    for ap, score in sc_sort:
        print(ap, score)
