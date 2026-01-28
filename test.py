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

moves = Columns(
    ['1) Attack', '2) Defend', '3)Heal'],
    align = 'center',
    title = 'Options',
    equal=True
)

Player = Columns(
    [HealthBar, moves],
    column_first=True,
    align='center'
)

Enemy = Columns(
    [HealthBar, moves],
    column_first=True,
    align='center'
)

#creates a decent looking Health bar
#live will be used to make the health bar and stuff move visually
#with Live(Panel.fit(Align.center(bar), padding=0)) as live:
#    live.start()


layout = Layout()

layout.split_column(
    Layout(
        Panel(Align.center("[bold white]CLI Battle[/]", vertical='middle')),
        name="title",
        ratio=1
    ),
    Layout(name="bottom", ratio=2)
)

enemy_healthBar = Layout(Panel(Align.center(HealthBar, vertical='top'), title="Enemy", style="red"))

Player = Layout(Panel(Align.center(Player, vertical='top'), title="Player", style="blue"))
Enemy = Layout(Panel(Align.center(Enemy, vertical='top'), title="Enemy", style="red"))

layout["bottom"].split_row(
    Player,
    Enemy
)



print(layout)