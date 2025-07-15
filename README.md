# 🐍 Projeto Django de Aprendizado

Este é um projeto desenvolvido com Django para fins de estudo e prática. Ele inclui um banco de dados local, está versionado com Git e pronto para ser executado em outras máquinas com facilidade.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- Django 5.2.4
- SQLite (banco de dados padrão do Django)
- Git para versionamento
- Ambiente virtual (`venv`)

---

## 🚀 Como rodar este projeto em outra máquina

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Crie o ambiente
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate

# Instalar as dependencias
pip install -r requirements.txt

# Aplique as migrações do banco de dados
python manage.py migrate

# Execute o servidor local
python manage.py runserver

```

## 📝 Observações

O banco de dados (db.sqlite3) não é versionado no Git. Ele será recriado com as migrações.

Lembre-se de ativar o ambiente virtual sempre que for rodar o projeto.

O arquivo requirements.txt garante que todas as dependências sejam instaladas corretamente.

