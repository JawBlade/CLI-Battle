"""

Use Bar to renderer a sort-of circle.

"""
import math

from rich.align   import Align
from rich.bar     import Bar
from rich.columns import Columns
from rich         import print
from rich.console import Group
from rich.panel   import Panel
from rich.live    import Live
from rich.layout  import Layout

SIZE = 40

#change the end value to creat the health bar move.
bar = Bar(100, width=50, begin=0, color='red', end=100)

HealthBar = Columns(
    ['❤️  ', bar],
    align='center',
    title='HP'
)

#creates a decent looking Health bar
#live will be used to make the health bar and stuff move visually
#with Live(Panel.fit(Align.center(bar), padding=0)) as live:
#    live.start()


layout = Layout()

layout.split_column(
    Layout(
        Panel(Align.center("[bold white]CLI Battle[/]", vertical='middle')),
        name="header",
        ratio=1  # tiny top panel
    ),
    Layout(name="bottom", ratio=2)  # bottom takes most space
)

layout["bottom"].split_row(
    Layout(Panel.fit((Align.center(HealthBar, vertical='middle', height=10)), title="Player", style="blue")),
    Layout(Panel.fit((Align.center(HealthBar, vertical='middle', height=10)), title="Enemy", style="red"))
)



print(layout)