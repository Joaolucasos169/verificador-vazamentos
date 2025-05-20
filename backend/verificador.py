import hashlib
import requests

def verificar_senha(senha):
    sha1_hash = hashlib.sha1(senha.encode('utf-8')).hexdigest().upper()
    prefixo = sha1_hash[:5]
    sufixo = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefixo}"
    headers = {"User-Agent": "VerificadorVazamentos"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            linhas = response.text.splitlines()
            for linha in linhas:
                hash_sufixo, count = linha.split(':')
                if hash_sufixo.strip().upper() == sufixo:
                    return f"🔴 SENHA VAZADA! Encontrada {count.strip()} vezes."
            return "🟢 Senha segura! Nenhum vazamento conhecido."
        else:
            return f"Erro na API: {response.status_code}"
    except Exception as e:
        return f"Erro ao verificar senha: {e}"
        
def verificar_email(email):
    url = f"https://leakcheck.io/api/public?check={email}"
    headers = {"User-Agent": "VerificadorVazamentos - Estudo"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            dados = response.json()
            if dados.get("found") is True:
                fontes = "\n".join(f"{fonte}" for fonte in dados.get("sources", []))
                return f"\n🔴 O e-mail '{email}' foi encontrado em vazamentos!\n{fontes}:"
            else:
                return f"\n✅ O e-mail '{email}' NÃO foi encontrado em vazamentos conhecidos."
        else:
            return f"\nErro ao acessar a API. Código: {response.status_code}"
    except Exception as e:
       return f"\nErro ao verificar e-mail: {e}"
        
        
def salvar_resultado(texto):
        try:
            with open("resultado.txt", "a", encoding="utf8") as f:
                f.write(texto + "\n")
            return True
        except Exception as e:
            return False