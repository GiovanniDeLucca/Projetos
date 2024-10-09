#!/usr/bin/env python3
import requests
import argparse
import re
from rich.console import Console

console = Console()

def fuzz(url, wordlist):  

    with open(wordlist, 'r') as file:
        dir = [line.strip() for line in file]

    for line in dir:
        url_completa = f'{url}/{line}'

        try:
            response = requests.get(url_completa)
            if response.status_code == 200:
                console.print(f'[green][+][/green] {url_completa} - {response.status_code}')
            elif response.status_code == 404:
                console.print(f'[red][!][/red] {url_completa} - {response.status_code}')
            elif response.status_code == 302:
                console.print(f'[yellow][~][/yellow] {url_completa} - {response.status_code}')
            else: 
                console.print(f'[purple][*][/purple] {url_completa} - {response.status_code}')    

        except requests.RequestException as e:
            print(f' Erro, por favor tente novamente: {e}')

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description="WebFuzzer")
    parser.add_argument('-u', '--url', help='Alvo desejado', required=True)
    parser.add_argument('-w', '--wordlist', help='Local da Wordlist', required=True)

    args = parser.parse_args()

    if not re.match(r'^https?://', args.url):
        args.url = f'https://{args.url}'
        
    try:
        fuzz(args.url, args.wordlist)     
    except EOFError:
        exit(1)
    except KeyboardInterrupt:
        exit(1)
