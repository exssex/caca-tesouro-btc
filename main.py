# Arquivo inicial do projeto Caça Tesouro DOGE
print("Iniciando projeto Caça Tesouro DOGE")
import requests
from bitcoinlib.keys import HDKey
from bitcoinlib.networks import Network

# Definir o network para Dogecoin
doge_network = Network('dogecoin')

# Função para consultar o saldo de uma carteira na blockchain de Dogecoin
def consultar_saldo(carteira):
    print("Consultando saldo...")
    url = f"https://dogechain.info/api/v1/address/balance/{carteira}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        saldo = float(data['balance'])  # O saldo já vem em DOGE
        return saldo
    else:
        print(f"Erro ao consultar a carteira {carteira}")
        return None

# Função para tentar encontrar a chave privada
def tentar_encontrar_chave(carteira):
    print("Iniciando brute force de chaves privadas para Dogecoin...")
    contador = 0
    while True:
        chave_privada = HDKey(network=doge_network).private_hex  # Gera uma chave privada aleatória para Dogecoin
        endereco = HDKey(chave_privada, network=doge_network).address()  # Gera o endereço correspondente
        
        print(f"Tentando chave {contador}: {chave_privada} -> {endereco}")
        contador += 1

        if endereco == carteira:
            print(f"Chave encontrada! {chave_privada}")
            break

if __name__ == "__main__":
    print("Iniciando projeto Caça Tesouro DOGE")
    
    # Exemplo de carteira a ser verificada
    carteira_tesouro = "D6dPhoV3f1hR2L4q6yXb69aZs5FTpCtQEG"  # Substitua pelo endereço alvo

    # Consultar o saldo da carteira
    saldo = consultar_saldo(carteira_tesouro)
    
    if saldo is not None:
        print(f"Saldo da carteira {carteira_tesouro}: {saldo} DOGE")
    
    # Tentar encontrar a chave privada
    tentar_encontrar_chave(carteira_tesouro)
    print("Finalizando processo.")

