from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import requests
from rich.console import Console

console = Console()

def passive_scan(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        raise_on_status=False
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('https://', adapter)

    try:
        response = session.get(url, timeout=30)

        if response.status_code != 200 or not response.text.strip().startswith(("{", "[")):
            return []

        data = response.json()
        results = set()
        for entry in data:
            for name in entry['name_value'].split("\n"):
                if domain in name:
                    results.add(name.strip())
        return sorted(results)
    except Exception:
        return []

def brute_force_scan(domain, wordlist_path):
    try:
        with open(wordlist_path, "r") as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        console.print(f"[red]Wordlist not found: {wordlist_path}[/red]")
        return []

    found = []
    for sub in subdomains:
        full_url = f"http://{sub.strip()}.{domain}"
        try:
            response = requests.get(full_url, timeout=3)
            if response.status_code < 400:
                console.print(f"[green][FOUND][/green] {full_url}")
                found.append(full_url)
        except:
            continue
    return found
