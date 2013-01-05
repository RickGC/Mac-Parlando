#!/usr/bin/env python

#  Mac Parlando
#
#  Copyright (C) 2013 Ricardo Gallegos *RickGC*
#
#  Mac Parlando is free software; you can redistribute it and/or modify it under
#  the terms of the GNU General Public License version 2, as published by the
#  Free Software Foundation
#
#  Mac Parlando is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
#  details (http://www.gnu.org/licenses/gpl.txt).
#
#  You should have received a copy of the GNU General Public License
#  along with sapyto-Public_Edition; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

# Escrito por RickGC
# Modulo para hacer que el sistema OSX hable
# con distintas voces segun lo que tu escribas

import subprocess
import sys
import time
from time import sleep

Autor = "RickGC"
email = "RickGC0@gmail.com"
version = "1.0"

print chr(27)+"[1;32m"+"[*] "+chr(27)+"[0m" "Mac Parlando"
print chr(27)+"[1;32m"+"[*] "+chr(27)+"[0m" "Escrito por %s" % (Autor)
print chr(27)+"[1;32m"+"[*] "+chr(27)+"[0m" "Version %s" % (version)

def salir():
    print chr(27)+"[1;31m"+"[!] "+chr(27)+"[0m" "Saliendo"
    print chr(27)+"[1;32m"+"[*] "+chr(27)+"[0m" "Tenga un buen dia =)"
    print chr(27)+"[1;32m"+"[*] "+chr(27)+"[0m" "Atte: RickGC"
    sleep(1)
    sys.exit()

def intentar_denuevo():
    print "\n"+chr(27)+"[1;31m"+"[!] "+chr(27)+"[0m" "=( Error numero invalido"
    print chr(27)+"[1;31m"+"[!] "+chr(27)+"[0m" "Porfavor intente de nuevo"
    sleep(2)

def menu():
    menu_voces = raw_input("\n[>] Menu de Voces para desplegar su mensaje\n\n[>] 1.  Kathy.\n[>] 2.  Vicki.\n[>] 3.  Victoria.\n[>] 4.  Alex.\n[>] 5.  Bruce.\n[>] 6.  Fred.\n[>] 7.  Cantado Grave.\n[>] 8.  Cantado Agudo.\n[>] 9.  Robot.\n[>] 00. Salir.\n\n" +chr(27)+"[1;94m"+"[-] "+chr(27)+"[0m" "Elija el numero de voz que guste usar: ")
    if len(menu_voces) > 3:
       intentar_denuevo()
       menu()
    elif menu_voces == "1":
                     Voz = "Kathy"
    elif menu_voces == "2":
                     Voz = "Vicki"
    elif menu_voces == "3":
                     Voz = "Victoria"
    elif menu_voces == "4":
                     Voz = "Alex"
    elif menu_voces == "5":
                     Voz = "Bruce"
    elif menu_voces == "6":
                     Voz = "Fred"
    elif menu_voces == "7":
                     Voz = "Bad"
    elif menu_voces == "8":
                     Voz = "Good"
    elif menu_voces == "9":
                     Voz = "Zarvox"
    elif menu_voces == "00":
                      salir()
    else:
         intentar_denuevo()
         menu()

    Texto = raw_input(chr(27)+"[1;94m"+"[-] "+chr(27)+"[0m" "Escriba su texto para ser hablado por su Mac aqui: ")
    print chr(27)+"[1;32m"+"[*] "+chr(27)+"[0m" "Su Mac esta Parlando..."
    subprocess.Popen("say -v %s %s" % (Voz,Texto), shell=True).wait()
    menu()
menu()