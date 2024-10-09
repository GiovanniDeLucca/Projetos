### Summary

O WebFuzzer é uma ferramenta  para realizar fuzzing em sites, funcionando tanto em Linux quanto em Windows.

Utilize o parâmetro **-u** para especificar a URL desejada e o parâmetro **-w** para definir a wordlist a ser utilizada.

### Instalation

- `git clone https://github.com/GiovanniDeLucca/Projetos`
- `chmod +x fuzz.py`
  
### Usage
```bash
--help
usage: fuzz.py [-h] -u URL -w WORDLIST

WebFuzzer

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Alvo desejado
  -w WORDLIST, --wordlist WORDLIST
                        Local da Wordlist
``` 

