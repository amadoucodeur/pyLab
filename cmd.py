import os
import sys
import subprocess

li = []
path = os.path.expanduser("~/.zsh_history")
with open(path,"r") as f:
    history = f.read().split("\n")

li = [i.partition(";")[-1] for i in history if i.partition(";")[-1] != '']
li.reverse()

commande = li[int(sys.argv[1])]

if "cmd" not in commande:
    subprocess.run(commande, shell=True)
