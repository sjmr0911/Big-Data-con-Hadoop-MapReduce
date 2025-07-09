#!/usr/bin/env python3
import sys
import re

#Lee Linea por Linea desde la entrada estandar
for line in sys.stdin:
    #Convierte a minusculas y separa por palabras usando regex
    words = re.findall(r"\b\w+\b", line.lower())
    for word in words:
	#Emite palabra con contador 1
        print(f"{word}\t1")
