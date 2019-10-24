#!/usr/bin/env python
from subprocess import run, PIPE


proc = run("hostname")
print(proc)
print()

# proc = run("netstat -an", shell=True)


proc = run("netstat -an", shell=True, stdout=PIPE)
output = proc.stdout.decode()  # get output as str (not bytes)
lines = output.splitlines()  # split output into array of lines

for line in lines:
    if "ESTABLISHED" in line:
        print(line)

p = run("hostname", stdout=PIPE)
hostname = p.stdout.decode().rstrip()
print("Host name is", hostname)

