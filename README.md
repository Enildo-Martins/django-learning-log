# 🐍 Projeto Django de Aprendizado

Este é um projeto Learning Log completo desenvolvido com Django. O objetivo da aplicação é permitir que usuários cadastrados criem e gerenciem seus próprios tópicos de estudo e adicionem anotações de aprendizado a cada um deles. O projeto está versionado com Git, utiliza um banco de dados local e está pronto para ser executado em outras máquinas com facilidade.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- Django 5.2.4
- django-bootstrap3: Para estilização rápida e responsiva dos templates.
- SQLite: Banco de dados padrão do Django para desenvolvimento.
- Git: Para versionamento de codigo.
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