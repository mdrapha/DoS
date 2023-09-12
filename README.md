# DoS

Este repositório contém um código Python para simular um ataque DoS (Denial of Service) a um IP especificado.

### Descrição

O script utiliza a biblioteca `socket` para criar conexões SYN a um IP e porta especificados. Com o uso de múltiplas threads, o código pode gerar uma grande quantidade de solicitações simultâneas, buscando sobrecarregar o servidor alvo.

### Como usar

1. Garanta que o Python 3.x esteja instalado em sua máquina.
2. Execute o script usando a seguinte sintaxe:

```
python dosattack.py <ip> <port> <threads>
```

Onde:
- `<ip>` é o endereço IP do servidor alvo.
- `<port>` é a porta de destino no servidor.
- `<threads>` é o número de threads que serão usadas para executar o ataque.

Por exemplo:

```
python dosattack.py 192.168.1.1 80 100
```
