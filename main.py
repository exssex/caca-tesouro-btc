# Arquivo inicial do projeto Caça Tesouro BTC
print("Iniciando projeto Caça Tesouro BTC")
import requests
from bitcoinlib.keys import HDKey

# Função para consultar o saldo de uma carteira na blockchain
def consultar_saldo(carteira):
    print("Consultando saldo...")
    url = f"https://blockchain.info/q/addressbalance/{carteira}?confirmations=6"
    response = requests.get(url)
    
    if response.status_code == 200:
        saldo = int(response.text) / 100000000  # Converter para BTC
        return saldo
    else:
        print(f"Erro ao consultar a carteira {carteira}")
        return None

# Função para tentar encontrar a chave privada
def tentar_encontrar_chave(carteira):
    print("Iniciando brute force de chaves privadas...")
    i = 0  # Contador de tentativas
    while True:  # Loop infinito até encontrar a chave
        chave_privada = HDKey().private_hex  # Gera uma chave privada aleatória
        endereco = HDKey(chave_privada).address()  # Gera o endereço correspondente
        print(f"Tentando chave {i}: {chave_privada} -> {endereco}")
        
        if endereco == carteira:
            print(f"Chave encontrada! {chave_privada}")
            break
        
        i += 1  # Incrementa o contador de tentativas

if __name__ == "__main__":
    print("Iniciando projeto Caça Tesouro BTC")
    
    # Endereço da carteira a ser verificada
    carteira_tesouro = "1CaBVPrwUxbQYYswu32w7Mj4HR4maNoJSX"
    
    # Consultar o saldo da carteira
    saldo = consultar_saldo(carteira_tesouro)
    
    if saldo is not None:
        print(f"Saldo da carteira {carteira_tesouro}: {saldo} BTC")
    
    # Tentar encontrar a chave privada
    tentar_encontrar_chave(carteira_tesouro)
    print("Finalizando processo.")
