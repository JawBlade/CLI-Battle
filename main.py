from rich.align   import Align
from rich.bar     import Bar
from character    import characters
from rich.columns import Columns
from rich         import print
from rich.prompt  import Prompt
from rich.panel   import Panel
import random
from rich.layout  import Layout

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
    equal=True,
    padding=(0,15)
)

Player = Columns(
    [HealthBar, moves],
    column_first=True,
    align='center',
    padding=(3,0)
)

Enemy = Columns(
    [HealthBar, moves],
    column_first=True,
    align='center',
    padding=(3,0)
)

layout = Layout()

layout.split_column(
    Layout(
        Panel(Align.center("[bold white]CLI Battle[/]", vertical='middle')),
        name="title",
        ratio=1
    ),
    Layout(name="bottom", ratio=2),
    Layout(name="choice", ratio=1)
)

def main():
    player = characters('player', color='blue')
    enemy = characters('Enemy', color='red')       

    player_layout = Layout(Panel(Align.center(Player, vertical='top'), title= player.name, style= player.color))
    enemy_layout = Layout(Panel(Align.center(Enemy, vertical='top'), title= enemy.name, style= enemy.color))
    choice_layout = Layout(Panel(Align.center("Choose an action (press Enter)", vertical='middle'), title= "Options", style= 'green'))
    
    layout["bottom"].split_row(
        player_layout,
        enemy_layout
    )

    layout['choice'].split_row(choice_layout)

    print(layout)

    turn = 0 
    while True:
        if turn % 2 == 0:
            layout['choice'].update(Panel(Align.center("Your turn! Choose an action:", vertical='middle'), title= "Options", style= 'green'))
        else:
            layout['choice'].update(Panel(Align.center("Enemy's turn! Press Enter to continue.", vertical='middle'), title= "Options", style= 'red'))
            

        choice = input('')
        print(layout)


if __name__ == '__main__':
    main()