from datetime import datetime

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

def make_layout()->Layout:
    layout=Layout(name="screen")
    
    layout.split(
        Layout(name="head",size=3),
        Layout(name="body",ratio=7),
        Layout(name="foot",size=6)
    )
    
    layout["body"].split_row(
        Layout(name="display",ratio=7),
        Layout(name="panel",ratio=2)
    )
    
    layout["foot"].split_row(
        Layout(name="input",ratio=7),
        Layout(name="clock",ratio=2)
    )
    
    return layout

class clock:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True,padding=1)
        grid.add_column(justify="center")
        grid.add_row(
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white")

layout=make_layout()
layout["clock"].update(clock())

with Live(layout, refresh_per_second=20, screen=True):
    while True:
        sleep(0.1)