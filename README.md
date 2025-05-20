# 🔐 Verificador de Vazamentos de Dados

Este é um projeto em Python que permite verificar se **senhas** ou **e-mails** foram expostos em vazamentos de dados públicos. Utiliza a API pública do [Have I Been Pwned](https://haveibeenpwned.com/) para senhas e simulação (ou LeakCheck.io) para e-mails.

## 🧠 Funcionalidades

- Verificação de senhas contra vazamentos conhecidos
- Verificação de e-mails (simulada ou via API pública gratuita)
- Opção de salvar os resultados em um arquivo `.txt`
- Interface de linha de comando (CLI) simples

---
## 🔧 Tecnologias usadas
- Python 3.x
- hashlib (padrão do Python)
- requests (requisições HTTP)
---

## 📌 APIs utilizadas
- Pwned Passwords – para verificar senhas.
- LeakCheck.io – para verificar e-mails (ou lógica simulada).
---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/Joaolucasos169/verificador-vazamentos.git
cd verificador-vazamentos
```

### 2. Instale as dependências

```bash
pip install requests
```

### 3. Execute o projeto

```bash
python verificador.py
```


