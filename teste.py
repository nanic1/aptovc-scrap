import requests
import pandas as pd
import time
import re

base_url = "https://www.chavesnamao.com.br/api/realestate/listing/items/"
todos_dados = []
page = 0  # começando pela página 0

# simulando navegador
headers = {
    "User-Agent": "Mozilla/5.0"
}

while True:
    params = {
        "level1": "apartamentos-a-venda",
        "level2": "rj-rio-de-janeiro",
        "pg": page,
        "quebra": "[95502]",
        "server": 0,
        "viewport": "desktop"
    }

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Erro na página {page}: {response.status_code}")
        break

    try:
        info = response.json()
    except requests.JSONDecodeError:
        print(f"Não foi possível decodificar JSON na página {page}")
        break

    anuncios = info.get("items", [])
    # remove anuncio
    anuncios = [a for a in anuncios if "id" in a]

    if not anuncios:
        print(f"Fim dos anúncios na página {page}")
        break

    for data in anuncios:
        # Extrair nome do condomínio
        publisher_name = data.get("publisher", {}).get("name")
        descricao = data.get("descriptionRaw", "")
        match = re.search(r"[Cc]ondom[ií]nio\s+([^\-•,\.]+)", descricao)
        condominio = match.group(1).strip() if match else publisher_name

        endereco_info = data.get("publisher", {}).get("address", {})
        rua = endereco_info.get("street", {}).get("name", "")
        bairro = endereco_info.get("neighborhood", {}).get("name", "")
        cidade = endereco_info.get("city", {}).get("name", "")
        estado = endereco_info.get("state", {}).get("acronym", "")
        endereco = f"{rua}, {bairro}, {cidade}, {estado}"

        status = data.get("newEnterprise", {}).get("enterpriseStatus", {}).get("name")
        preco = data.get("prices", {}).get("main")
        metro_quadrado = data.get("area", {}).get("useful")

        todos_dados.append({
            "condominio": condominio,
            "endereco": endereco,
            "status": status,
            "preco": preco,
            "m2": metro_quadrado
        })

    print(f"Página {page} processada")
    page += 1

    time.sleep(1)  # pausa de 1 segundo entre requisições

print(f"Total de imóveis coletados: {len(todos_dados)}")

# Salva em Excel
df = pd.DataFrame(todos_dados)
df.to_excel("base_chavesnamao.xlsx", index=False, engine='openpyxl')
print("Dados salvos em 'base_chavesnamao.xlsx'")