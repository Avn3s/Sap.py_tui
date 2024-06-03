from datetime import datetime
from os import listdir
from keyboard import is_pressed,read_key

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.live import Live
from time import sleep

console = Console()

cmd=""
chunk_size = 7
result_dict = {i//chunk_size + 1: listdir("songs")[i:i+chunk_size] for i in range(0, len(listdir("songs")), chunk_size)}
page_no=1


def make_layout() -> Layout:
    global chunk_size
    layout = Layout(name="screen")

    layout.split(
        Layout(name="head", size=3),
        Layout(name="body", size=chunk_size+2),
        Layout(name="foot", size=6),
    )

    layout["body"].split_row(
        Layout(name="display", ratio=7),
        Layout(name="panel", ratio=2)
    )

    layout["foot"].split_row(
        Layout(name="input", ratio=7), 
        Layout(name="clock", ratio=2)
    )

    return layout


class clock:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True, padding=1)
        grid.add_column(justify="center")
        grid.add_row(
            datetime.now().ctime().split()[3],
        )
        return Panel(grid, style="violet")


class head:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_row(
            "Sap.py",
        )
        return Panel(grid, style="blue")


class display:
    def __rich__(self) -> Panel:
        global chunk_size, result_dict, page_no
        table = Table.grid(expand=True)
        table.add_column(justify="left")
        for index, song in enumerate(result_dict[page_no], 1):
            table.add_row(f"{index}. {song[:-4:]}")
        return Panel(table, style="blue")
'''
class input:
    def __rich__(self)->Panel:
        global cmd
        key=''
        if read_key()=='backspace':
            key+="\b"
        elif read_key()=='enter':
            cmd=key
            key=""
        elif read_key()=='space':
            key+=' '
        elif read_key()=='capslock':
            pass
        table=Table.grid(expand=True)
        table.add_column(justify="left")
        table.add_row(f"> {key}")
        return Panel(table)
'''
layout = make_layout()
layout["clock"].update(clock())
layout["head"].update(head())
layout["display"].update(display())
#layout["input"].update(input())

with Live(layout, refresh_per_second=5, screen=True) as live:
    while True:
        if is_pressed('q'):
            exit()
        else:
            live.update(layout)