import requests
import pandas as pd
import time

# essa aplicação é um scrap do site apto.vc
# consulte a documentação para o scrap de outros sites

BUILD_ID = "KD41YWHMuzlPQhhefsn7D"

HEADERS = {
    "x-nextjs-data": "1",
    "User-Agent": "Mozilla/5.0"
}

# monta uma URL para consultar a API interna da apto utilizando o ID do nextjs
def montar_url(path):
    if "?" in path:
        base, query = path.split("?", 1)
        return f"https://apto.vc/_next/data/{BUILD_ID}{base}.json?{query}"
    else:
        return f"https://apto.vc/_next/data/{BUILD_ID}{path}.json"

# faz a consulta a API com o url.
# caso código de status seja 200, retorna um json com informações
def buscar_pagina(path):
    url = montar_url(path)

    try:
        res = requests.get(url, headers=HEADERS, timeout=5)

        print("URL:", url)
        print("STATUS:", res.status_code)

        res.raise_for_status()  # erro se não for 200

        return res.json()

    except requests.exceptions.Timeout:
        print("Timeout")
    
    except requests.exceptions.ConnectionError:
        print("Não foir possível conectar com a API")

    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e}")

    except ValueError:
        print("Dados para requisição inválidos!")

    return None

# extrai dados especificos do json
def extrair_cards(data):
    try:
        return data["pageProps"]["realties"]["data"]
    except:
        return []

# monta o formato do card com apenas informações necessárias para a pesquisa
def montar_card(card):
    return {
        "nome": card.get("name"),
        "endereco": card.get("address"),
        "bairro": card.get("neighborhoods", [{}])[0].get("name"),
        "preco": card.get("price"),
        "area": card.get("area"),
        "quartos": card.get("bedrooms"),
        "banheiros": card.get("bathrooms"),
        "vagas": card.get("parking"),
        "status": card.get("status", {}).get("name"),
        "link": card.get("permalink")
    }

# realiza o scrap efetivamente e organiza os dados.
def main():
    base_path = "/br/rj/rio-de-janeiro"
    todos = []
    page = 1

    while True:
        if page == 1:
            path = base_path
        else:
            path = f"{base_path}?page={page}"

        print(f"\nPágina {page}")
        print("PATH:", path)

        data = buscar_pagina(path)
        cards = extrair_cards(data)

        if not cards:
            print("Página não contém dados. Encerrando aplicação...")
            break

        print(f"{len(cards)} imóveis")

        for c in cards:
            todos.append(montar_card(c))

        page += 1
        time.sleep(1)

    df = pd.DataFrame(todos)

    if df.empty:
        print("DataFrame vazio")
    else:
        df.to_csv("apartamentos_rio.csv", index=False, sep=";", encoding="utf-8-sig")
        print("Scrap concluído e salvo!")


if __name__ == "__main__":
    main()