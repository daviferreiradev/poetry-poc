# 🚀 Exemplo prático: Usando o Poetry

Este projeto mostra como usar o Poetry para instalar bibliotecas, rodar scripts, criar pacotes e usar plugins no Python.

## 📦 Estrutura dos arquivos

| Arquivo/Pasta      | Função                                                       |
| ------------------ | ------------------------------------------------------------ |
| `pyproject.toml`   | ⚙️ Configuração do projeto, dependências e ponto de entrada  |
| `poetry_poc/`      | 📁 Pacote principal do projeto                               |
| └─ `__init__.py`   | 🏷️ Identifica a pasta como pacote Python                     |
| └─ `__main__.py`   | 🏃 Código principal: faz requisição HTTP e imprime resultado |
| `dist/`            | 📦 Artefatos gerados pelo build (`.whl` e `.tar.gz`)         |
| `requirements.txt` | 📄 Lista de dependências exportada pelo plugin (opcional)    |
| `README.md`        | 📚 Este guia rápido                                          |

## 1️⃣ Instalar o Poetry

Instala o gerenciador de dependências Poetry no seu computador.

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Depois feche e abra o terminal de novo para garantir que o comando `poetry` funcione.
Para conferir se instalou:

```powershell
poetry --version
```

Esse comando mostra a versão instalada do Poetry.

## 2️⃣ Adicionar uma biblioteca

Instala a biblioteca `requests` só para este projeto, sem afetar outros projetos Python.

```powershell
poetry add requests
```

O Poetry baixa e instala a biblioteca, além de atualizar o arquivo de dependências do projeto.

## 3️⃣ Rodar o script usando o Poetry

O código principal está em `poetry_poc/__main__.py` e usa a biblioteca `requests`:

```python
import requests
print("Poetry está funcionando!", requests.get("https://google.com", timeout=5).status_code)
```

Para rodar o projeto dentro do ambiente virtual do Poetry:

```powershell
poetry run poetry-poc
```

Esse comando executa o ponto de entrada do projeto, usando todas as dependências instaladas pelo Poetry, sem precisar ativar o ambiente virtual manualmente.

## 4️⃣ Gerar o pacote do projeto

Cria os arquivos de distribuição para instalar o projeto em outros ambientes.

```powershell
poetry build
```

Esse comando gera a pasta `dist/` com dois arquivos:

-   `.whl` (pacote Wheel, usado para instalação rápida)
-   `.tar.gz` (pacote fonte)
    Esses arquivos podem ser enviados para outros desenvolvedores ou publicados em repositórios.

## 5️⃣ (Opcional) Exportar um requirements.txt

Gera um arquivo `requirements.txt` com todas as dependências do projeto, útil para quem prefere instalar com pip.

```powershell
poetry self add poetry-plugin-export
poetry export -f requirements.txt --output requirements.txt
```

Assim, você pode compartilhar as dependências do projeto com quem não usa Poetry.

---

✅ Resumo: O Poetry facilita instalar bibliotecas, rodar scripts, empacotar projetos e ainda pode ser estendido com plugins. Cada comando acima tem uma função específica para deixar o trabalho com Python mais organizado e prático.
