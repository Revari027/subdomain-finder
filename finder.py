import pyfiglet
import requests
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box
from rich.progress import Progress

from utils import passive_scan, brute_force_scan

console = Console()


def show_banner():
    banner = pyfiglet.figlet_format("Subdomain Finder", font="slant")
    console.print(f"[bold cyan]{banner}[/bold cyan]")

    console.print(
        Panel(
            "[bold white]Created by[/bold white] [bold cyan]caramell_revv[/bold cyan]\n"
            "[bold green][bold white]From:[/bold white] Universitas Negeri Jakarta[/bold green]\n"
            "[dim]Follow for more tools & ideas![/dim]",
            title="[bold green]Author[/bold green]",
            border_style="cyan",
            box=box.ROUNDED
        )
    )


def run_passive_scan(domain):
    console.print(f"\n[bold blue]Scanning {domain} using passive mode...[/bold blue]\n")
    subdomains = []
    raw_results = passive_scan(domain)
    total = len(raw_results)
    for i, sub in enumerate(raw_results, start=1):
        clickable_url = f"http://{sub}"
        console.print(f"[green][{i}/{total}] {clickable_url}[/green]")
        subdomains.append(clickable_url)
    return subdomains


def run_brute_force_scan(domain, wordlist_path):
    try:
        with open(wordlist_path, "r") as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        console.print(f"[red]Wordlist not found: {wordlist_path}[/red]")
        return []

    found = []
    console.print(f"\n[bold blue]Brute-forcing subdomains for {domain}...[/bold blue]\n")
    with Progress() as progress:
        task = progress.add_task(f"[cyan]Scanning {domain}[/cyan]", total=len(subdomains))
        for sub in subdomains:
            full_url = f"http://{sub.strip()}.{domain}"
            try:
                response = requests.get(full_url, timeout=3)
                if response.status_code < 400:
                    console.print(f"[green][FOUND][/green] {full_url}")
                    found.append(full_url)
            except:
                pass
            progress.update(task, advance=1)
    return found


def run_program():
    while True:
        show_banner()

        domain = Prompt.ask("[bold yellow]Enter target domain (e.g., example.com)[/bold yellow]")
        mode = Prompt.ask(
            "[bold green]Select scan mode[/bold green]",
            choices=["passive", "brute"],
            default="passive"
        )

        if mode == "passive":
            subdomains = run_passive_scan(domain)
        else:
            wordlist = Prompt.ask(
                "[bold yellow]Enter path to wordlist[/bold yellow]",
                default="wordlists/subdomains.txt"
            )
            subdomains = run_brute_force_scan(domain, wordlist)

        if subdomains:
            console.print(f"\n[bold green]Found {len(subdomains)} subdomain(s):[/bold green]")
            for sub in subdomains:
                console.print(f" - [cyan]{sub}[/cyan]")
        else:
            console.print("[bold red]No subdomains found.[/bold red]")

        save = Prompt.ask("\n[bold yellow]Do you want to save the result to a file?[/bold yellow]", choices=["y", "n"], default="n")
        if save == "y":
            filename = f"result_{domain}.txt"
            with open(filename, "w") as f:
                for sub in subdomains:
                    f.write(sub + "\n")
            console.print(f"[green]Result saved to {filename}[/green]")

        again = Prompt.ask("\n[bold yellow]Do you want to scan another domain?[/bold yellow]", choices=["y", "n"], default="n")
        if again.lower() != "y":
            console.print("\n[bold green]Thanks for using Subdomain Finder. Goodbye![/bold green]\n")
            break


if __name__ == "__main__":
    try:
        run_program()
    except KeyboardInterrupt:
        console.print("\n[bold red]Scan interrupted by user (Ctrl+C). Exiting...[/bold red]")
