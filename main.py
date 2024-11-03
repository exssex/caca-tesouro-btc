# Arquivo inicial do projeto Caça Tesouro BTC
print("Iniciando projeto Caça Tesouro BTC")
import requests
import time
import os
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
                print("Tempo limite de 1 hora atingido. Reiniciando...")
                log_file.write("Tempo limite de 1 hora atingido. Reiniciando...\n")
                log_file.flush()
                break  # Sai do loop para reiniciar o script

            # Gera uma chave privada aleatória e o endereço correspondente
            chave_privada = HDKey().private_hex
            endereco = HDKey(chave_privada).address()
            log_entry = f"Tentando chave: {chave_privada} -> {endereco}\n"
            
            # Imprime e grava no log
            print(log_entry.strip())
            log_file.write(log_entry)
            log_file.flush()  # Força a escrita no log para evitar problemas de buffer

            # Verifica se encontrou a chave correta
            if endereco == carteira:
                sucesso_msg = f"Chave encontrada! {chave_privada}"
                print(sucesso_msg)
                log_file.write(sucesso_msg + "\n")
                log_file.flush()
                break

# Função principal que reinicia automaticamente se o script parar
def main():
    while True:
        try:
            print("Iniciando nova tentativa...")
            carteira_tesouro = "1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9"
            
            # Consultar o saldo da carteira
            saldo = consultar_saldo(carteira_tesouro)
            
            if saldo is not None:
                print(f"Saldo da carteira {carteira_tesouro}: {saldo} BTC")
            
            # Tentar encontrar a chave privada
            tentar_encontrar_chave(carteira_tesouro)
            
            print("Reiniciando o processo...")
            
        except Exception as e:
            print(f"Erro detectado: {e}. Reiniciando o processo...")
            time.sleep(5)  # Aguarda 5 segundos antes de reiniciar

if __name__ == "__main__":
    main()
