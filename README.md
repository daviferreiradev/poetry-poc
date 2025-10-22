# Poetry POC - Demonstração Prática

Demonstração completa do Poetry: gerenciamento de dependências, ambientes virtuais e build de pacotes Python.

## Pré-requisitos

### Instalar o Poetry

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

-   **Reinicie o computador** após a instalação

## Estrutura do Projeto

| Arquivo/Pasta    | Função                                                   |
| ---------------- | -------------------------------------------------------- |
| `main.py`        | Código principal da aplicação                            |
| `pyproject.toml` | Configuração do projeto e dependências                   |
| `poetry.lock`    | Versões exatas das dependências (gerado automaticamente) |
| `dist/`          | Artefatos de build (.whl e .tar.gz)                      |

## Passo a Passo da Demonstração

### 1. Verificar Poetry Instalado

```powershell
poetry --version
```

**O que faz:** Confirma se o Poetry está instalado e funcionando.

### 2. Criar Projeto do Zero

```powershell
poetry init
```

**O que faz:** Cria o `pyproject.toml` através de perguntas interativas.

### 3. Adicionar Dependências

```powershell
poetry add requests
```

**O que faz:**

-   Instala a biblioteca `requests`
-   Cria ambiente virtual automaticamente
-   Atualiza `pyproject.toml` com a dependência
-   Gera `poetry.lock` com versões exatas

### 4. Testar Execução

```powershell
poetry run python main.py
```

**O que faz:** Executa o script dentro do ambiente virtual do Poetry.
**Resultado esperado:** Demonstração completa com APIs de CEP e cotação

### 5. Configurar Build (Manual)

Adicione ao final do `pyproject.toml`:

```toml
[tool.poetry]
packages = [
    { include = "*.py" }
]
```

**Por que necessário:** Poetry precisa saber quais arquivos incluir no pacote quando o código está na raiz.

### 6. Fazer Build

```powershell
poetry build
```

**O que faz:** Gera pacotes para distribuição (wheel e sdist).

## Comandos Úteis para Trabalho em Equipe

### Instalar dependências de um projeto existente:

```powershell
poetry install
```

**Quando usar:** Após clonar um repositório com `pyproject.toml` e `poetry.lock`

### Verificar o que está instalado:

```powershell
poetry show
```

### Ver localização do ambiente virtual:

```powershell
poetry env info
```

### Exportar para requirements.txt (para compatibilidade):

```powershell
# Instalar o plugin de export
poetry self add poetry-plugin-export

# Exportar dependências para requirements.txt
poetry export -f requirements.txt --output requirements.txt
```

**Quando usar:** Para compatibilidade com projetos que ainda usam pip/requirements.txt

## Gerenciamento Automático de Ambiente Virtual

O Poetry **cria automaticamente** um ambiente virtual isolado para cada projeto:

### Ver onde estão as bibliotecas:

```powershell
poetry env info
```

**Saída exemplo:**

```
Path: C:\Users\SeuUsuario\AppData\Local\pypoetry\Cache\virtualenvs\poetry-poc-ABC123-py3.13
```

### Estrutura do ambiente virtual:

-   **Bibliotecas:** `...\virtualenvs\poetry-poc-ABC123-py3.13\Lib\site-packages\`
-   **Python:** `...\virtualenvs\poetry-poc-ABC123-py3.13\Scripts\python.exe`
-   **Isolamento:** Cada projeto tem suas próprias bibliotecas

### Vantagens do ambiente automático:

-   ✅ **Zero configuração:** Não precisa criar/ativar venv manualmente
-   ✅ **Isolamento total:** Cada projeto independente
-   ✅ **Limpeza:** Não polui o Python global

## Extensibilidade e Plugins

O Poetry permite personalização através de plugins e scripts:

### Plugin de Export (Compatibilidade)

```powershell
# Instalar plugin
poetry self add poetry-plugin-export

# Gerar requirements.txt
poetry export -f requirements.txt --output requirements.txt
```

**Por que usar:** Compatibilidade com ferramentas que ainda dependem de `requirements.txt`

## Principais Vantagens do Poetry

1. **Gerenciamento Unificado**: Um único arquivo (`pyproject.toml`) para dependências, metadados e configurações
2. **Reprodutibilidade**: `poetry.lock` garante que todos usem exatamente as mesmas versões
3. **Ambientes Automáticos**: Cria e gerencia ambientes virtuais sem comandos extras

## Principais Desvantagens do Poetry

1. **Curva de Aprendizado**: Desenvolvedores precisam aprender novos comandos (`poetry add` vs `pip install`)
2. **Configuração Manual**: Projetos com estrutura não padrão requerem configuração extra (como visto no passo 5)

## Explicação dos Arquivos Gerados

### `pyproject.toml`

-   **Metadados**: nome, versão, autor do projeto
-   **Dependências**: bibliotecas necessárias com versões
-   **Build**: configuração para geração de pacotes

### `poetry.lock`

-   **Versões exatas**: todas as dependências com versões específicas
-   **Reprodutibilidade**: garante mesmo ambiente em qualquer máquina
-   **Dependências transitivas**: inclui dependências das dependências
-   **IMPORTANTE**: Sempre commitar no Git (NÃO vai no .gitignore)

### `dist/poetry_poc-0.1.0-py3-none-any.whl`

-   **Wheel**: pacote compilado para instalação rápida
-   **Conteúdo**: código + metadados prontos para distribuição

### `dist/poetry_poc-0.1.0.tar.gz`

-   **Source Distribution**: código fonte compactado
-   **Uso**: para quando wheel não está disponível
