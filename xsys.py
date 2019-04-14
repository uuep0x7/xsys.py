# -*- coding: utf-8 -*-

import os, string, sys


#===========================================
# Váriavies com as Cores
#===========================================
NONE="\033[0m" # Eliminar as Cores, deixar padrão)
NN="\033[0m" # Eliminar as Cores, deixar padrão)
 
## Cores de Fonte
K="\033[0;30m" # Black (Preto)
R="\033[0;31m" # Red (Vermelho)
G="\033[0;32m" # Green (Verde)
Y="\033[0;33m" # Yellow (Amarelo)
B="\033[0;34m" # Blue (Azul)
M="\033[0;35m" # Magenta (Vermelho Claro)
C="\033[0;36m" # Cyan (Ciano - Azul Claro)
W="\033[0;37m" # White (Branco)
 
## Efeito Negrito (bold) e cores
BK="\033[1;30m" # Bold+Black (Negrito+Preto)
BR="\033[1;31m" # Bold+Red (Negrito+Vermelho)
BG="\033[1;32m" # Bold+Green (Negrito+Verde)
BY="\033[1;33m" # Bold+Yellow (Negrito+Amarelo)
BB="\033[1;34m" # Bold+Blue (Negrito+Azul)
BM="\033[1;35m" # Bold+Magenta (Negrito+Vermelho Claro)
BC="\033[1;36m" # Bold+Cyan (Negrito+Ciano - Azul Claro)
BW="\033[1;37m" # Bold+White (Negrito+Branco)
 
## Cores de fundo (backgroud)
BGK="\[\033[40m\]" # Black (Preto)
BGR="\[\033[41m\]" # Red (Vermelho)
BGG="\[\033[42m\]" # Green (Verde)
BGY="\[\033[43m\]" # Yellow (Amarelo)
BGB="\[\033[44m\]" # Blue (Azul)
BGM="\[\033[45m\]" # Magenta (Vermelho Claro)
BGC="\[\033[46m\]" # Cyan (Ciano - Azul Claro)
BGW="\[\033[47m\]" # White (Branco)

## Cores Piscante
PCK="\033[5;30m" #Piscante+Black (Preto)
PCR="\033[5;31m" #Piscante+Red (Vermelho)
PCG="\033[5;32m" #Piscante+Green (Verde)
PCY="\033[5;33m" #Piscante+Yellow (Amarelo)
PCB="\033[5;34m" #Piscante+Blue (Azul)
PCM="\033[5;35m" #Piscante+Magenta (Vermelho Claro)
PCC="\033[5;36m" #Piscante+Cyan (Ciano - Azul Claro)
PCW="\033[5;37m" #Piscante+White (Branco)

##### Variaveis & Limpar tela
y = os.name
os.system('cls' if os.name == 'nt' else 'clear')

##### Identificação do sitema operacional
if y == "nt": 
	print("======================================")
	print("["+BR+"+"+NN+"] Sistema Windows NT \n["+BB+"+"+NN+"] Bem vindo ao xSys")
	print("======================================")
	while True:
		cmmd = raw_input("\n["+BB+"+"+NN+"] xSys > ")
		os.system(cmmd)
else:
	print("======================================")
	print("["+BR+"+"+NN+"] Bem vindo ao xSys")
	print("======================================")
	while True:
		cmmd = raw_input("\n["+PCG+"+"+NN+"] xSys > ")
		os.system(cmmd)
	