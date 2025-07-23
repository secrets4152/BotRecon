import subprocess
import os
import re

#Input domain
domain = input("Enter the target name: ")

#Run Subfinder to find subdomains
subfinder_cmd = f"subfinder -d {domain} -o subdomains.txt"
subprocess.run(subfinder_cmd, shell=True)

#Run DNSX to find the IP of the subdomains
dnsx_cmd = f"dnsx -silent -a -resp -l subdomains.txt -o subdomains2.txt"
subprocess.run(dnsx_cmd, shell=True)

with open('subdomains2.txt', 'r') as arquivo:
    conteudo = arquivo.read()

#Use regular expression to find subdomains within square brackets
padrao = r'[(.*?)]'
resultados = re.findall(padrao, conteudo)

with open('resultados_regex.txt', 'w') as arquivo_resultados:
    for resultado in resultados:
        arquivo_resultados.write(resultado + '\n')

#Run Naabu to validate ports
naabu_cmd = f"naabu -l resultados_regex.txt -verify -o subdomains3.txt"
subprocess.run(naabu_cmd, shell=True)

#Run HTTPX to check 200 status codes and capture screenshots
httpx_cmd = f"/root/go/bin/httpx -l subdomains3.txt -o results.txt -status-code -screenshot"
subprocess.run(httpx_cmd, shell=True)

#Read and print the results content
with open('results.txt', 'r') as arquivo_resultados:
    conteudo_resultados = arquivo_resultados.read()

print(conteudo_resultados)
