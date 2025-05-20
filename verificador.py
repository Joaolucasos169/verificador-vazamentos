import hashlib
import requests

def menu():
    print("\nVerificador de Vazamentos de Dados")
    print("1. Verificar senha")
    print("2. Verificar email")
    print("3. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção:")

        if escolha == "1":
            senha = input("Digite a senha para verificar: ")
            verificar_senha(senha)

        elif escolha == "2":
            email = input("Digite o email para verificar: ")
            verificar_email(email)

        elif escolha == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

def verificar_senha(senha):
    sha1_hash = hashlib.sha1(senha.encode('utf-8')).hexdigest().upper()

    prefixo = sha1_hash[:5]
    sufixo = sha1_hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefixo}"

    headers = {
        "User-Agent": "VerificadorVazamentos - Estudo"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            hashes = response.text.splitlines()
            
            for linha in hashes:
                hash_sufixo, count = linha.split(':')
                
                if sufixo == hash_sufixo:
                   resultado = f"Senha vazada! A senha foi encontrada {count} vezes."
                   print(resultado)
                   salvar_resultado(resultado)
                   return
                
            resultado = "Senha não vazada!"
            print(resultado)
            salvar_resultado(resultado)
        else:
            print(f"Erro ao acessar a API. Status code: {response.status_code}")
    except Exception as e:
        print(f"Erro ao verificar senha: {e}")
        
def verificar_email(email):
    url = f"https://leakcheck.io/api/public?check={email}"

    headers = {
        "User-Agent": "VerificadorVazamentos - Estudo"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            resultado = response.json()
            if resultado.get("found") is True:
                resultado = f"\n🔴 O e-mail '{email}' foi encontrado em vazamentos:"
                for item in resultado.get("sources", []):
                    resultado += f"• {item}\n"
            else:
                resultado = f"\n✅ O e-mail '{email}' NÃO foi encontrado em vazamentos conhecidos."
                print(resultado)
                salvar_resultado(resultado)
        else:
            print(f"\nErro ao acessar a API. Código: {response.status_code}")
    except Exception as e:
        print(f"\nErro ao verificar e-mail: {e}")
        
        
def salvar_resultado(texto):
    escolha = input("Deseja salvar seu resulto em um arquivo .txt? (s/n): ").strip().lower()
    if escolha == "s":
        try:
            with open("resultado.txt", "a", encoding="utf8") as arquivo:
                arquivo.write(texto + "\n")
            print("✅ Resultados slavos em 'resultado.txt'.\n")
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")
    else:
        print("Resultado não salvo.\n")

main()