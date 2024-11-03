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
    with open("doge_brute_force_log.txt", "a") as log_file:
        while True:
            chave_privada = HDKey(network=doge_network).private_hex  # Gera uma chave privada aleatória para Dogecoin
            endereco = HDKey(chave_privada, network=doge_network).address()  # Gera o endereço correspondente
            
            log_file.write(f"Tentando chave {contador}: {chave_privada} -> {endereco}\n")
            log_file.flush()  # Grava imediatamente no arquivo
            print(f"Tentando chave {contador}: {chave_privada} -> {endereco}")
            contador += 1

            if endereco == carteira:
                print(f"Chave encontrada! {chave_privada}")
                log_file.write(f"Chave encontrada! {chave_privada}\n")
                break

if __name__ == "__main__":
    print("Iniciando projeto Caça Tesouro DOGE")
    
    # Carteira alvo de Dogecoin com saldo conhecido
    carteira_tesouro = "DPwQPzebSMcN4kzkcdEvqE8rE2r8SfJ8pC"
    
    # Consultar o saldo da carteira
    saldo = consultar_saldo(carteira_tesouro)
    
    if saldo is not None:
        print(f"Saldo da carteira {carteira_tesouro}: {saldo} DOGE")
    
    # Tentar encontrar a chave privada
    tentar_encontrar_chave(carteira_tesouro)
    print("Finalizando processo.")

