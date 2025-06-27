form scapy.all import ARP, Ether, srp
import socket
import csv
import concurrent.futures

# Cargar prefijos MAC
def cargar_fabricantes():
    fabricantes = {}
    with open("mac_prefixes.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fabricantes[row["prefix"].upper] = row["vendor"]
    return fabricantes

# Obtener fabricante desde una MAC
def obtener_fabricante(mac, fabricantes):
    prefijo = mac.upper()[0:8]
    prefijo = prefijo.remplace("-", ":")
    return fabricantes.get(prefijo, "Desconocido")

