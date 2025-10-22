import requests
from datetime import datetime


def obter_cep(cep):
    """Busca informações de um CEP usando a API ViaCEP"""
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"erro": f"Erro na requisição: {e}"}


def obter_cotacao_dolar():
    """Busca cotação atual do dólar usando API pública"""
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["rates"]["BRL"]
    except requests.RequestException as e:
        return f"Erro ao obter cotação: {e}"


def main():
    print("=" * 50)
    print("🐍 POETRY POC - Demonstração Completa")
    print("=" * 50)

    # Teste 1: Verificar conectividade
    print("\n1. Testando conectividade...")
    try:
        response = requests.get("https://httpbin.org/status/200", timeout=5)
        print(f"✅ Conectividade OK (Status: {response.status_code})")
    except requests.RequestException:
        print("❌ Problema de conectividade")
        return

    # Teste 2: Buscar informações de CEP
    print("\n2. Buscando informações do CEP 01310-100 (Paulista, SP)...")
    cep_info = obter_cep("01310100")
    if "erro" not in cep_info:
        print(f"📍 Endereço: {cep_info.get('logradouro', 'N/A')}")
        print(f"🏘️  Bairro: {cep_info.get('bairro', 'N/A')}")
        print(
            f"🏙️  Cidade: {cep_info.get('localidade', 'N/A')}/{cep_info.get('uf', 'N/A')}")
    else:
        print(f"❌ {cep_info['erro']}")

    # Teste 3: Cotação do dólar
    print("\n3. Obtendo cotação atual do dólar...")
    cotacao = obter_cotacao_dolar()
    if isinstance(cotacao, float):
        print(f"💰 1 USD = R$ {cotacao:.2f}")
        print(f"💵 R$ 100,00 = USD {100/cotacao:.2f}")
    else:
        print(f"❌ {cotacao}")

    # Teste 4: Informações do sistema
    print("\n4. Informações da execução:")
    print(f"⏰ Executado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"📦 Usando requests versão: {requests.__version__}")

    print("\n" + "=" * 50)
    print("🎉 Poetry POC executada com sucesso!")
    print("🔧 Dependências gerenciadas pelo Poetry")
    print("🏗️  Ambiente virtual isolado")
    print("=" * 50)


if __name__ == "__main__":
    main()
