"""

Use Bar to renderer a sort-of circle.

"""
import math

from rich.align import Align
from rich.bar import Bar
from rich import print
from rich.panel import Panel

SIZE = 40


bar = Bar(100, width=50, begin=0, color='red', end=100)
#creates a decent looking Health bar
print(Panel.fit(Align.center(bar), padding=0))