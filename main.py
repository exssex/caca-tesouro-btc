# Arquivo inicial do projeto Caça Tesouro BTC
print("Iniciando projeto Caça Tesouro BTC")
import requests
import time
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
    start_time = time.time()
    duration_limit = 3600  # Limite de tempo em segundos (1 hora)

    # Abre o arquivo de log em modo append
    with open("chave_brute_force.log", "a") as log_file:
        while True:
            # Verifica se o tempo limite foi atingido
            elapsed_time = time.time() - start_time
            if elapsed_time > duration_limit:
                print("Tempo limite de 1 hora atingido. Encerrando...")
                log_file.write("Tempo limite de 1 hora atingido. Encerrando...\n")
                break

            # Gera uma chave privada aleatória e o endereço correspondente
            chave_privada = HDKey().private_hex
            endereco = HDKey(chave_privada).address()
            log_entry = f"Tentando chave: {chave_privada} -> {endereco}\n"
            
            # Imprime e grava no log
            print(log_entry.strip())
            log_file.write(log_entry)

            # Verifica se encontrou a chave correta
            if endereco == carteira:
                sucesso_msg = f"Chave encontrada! {chave_privada}"
                print(sucesso_msg)
                log_file.write(sucesso_msg + "\n")
                break

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


