from rich.console import Console
from rich.table import Table

console = Console()

while True:
    word = input("Word: ")
    if word == "":
        break

    # Créer une table pour formater la sortie
    table = Table(show_header=False, box=None)
    table.add_row(f"[bold white]{word}[/bold white]", "*")

    console.print(table)
