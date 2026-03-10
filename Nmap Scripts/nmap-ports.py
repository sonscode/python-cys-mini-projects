import os

site = input("Enter website to scan: ")

os.system("nmap -F "+site)


