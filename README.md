# Scraper Apto.vc

Esta aplicação realiza scraping de condomínios do site [Apto.vc](https://apto.vc/). A aplicação coleta todos os condomínios na pagina via request e armazena em um arquivo Excel formatado.

---

## Tecnologias usadas
* Python
* Pandas
* Requests

---

## Dados obtidos na extração
* Nome
* Endereço
* Bairro
* Preço mínimo por apartamento
* Área mínima por apartamento
* Mínimo de quartos por apartamento
* Mínimo de banheiros por apartamento
* Vagas por morador
* Status
* Link para mais informações

## Como executar o projeto
### 1- Clone este repositório para o seu computador.
No seu terminal, execute:
```
git clone https://github.com/nanic1/aptovc-scrap
cd aptovc-scrap
```

### 2- Defina a cidade que deseja filtar
Com o código aberto, na função main, mude o **base_path** para o UF e cidade que deseja filtrar. **NÃO** use acentos no caminho.

Ex:
* Filtro Rio de Janeiro
```
base_path = "/br/rj/rio-de-janeiro"
```

* Filtro São Paulo
```
base_path = "/br/sp/sao-paulo"
```

O apto.vc não fornece cobertura para todos os estados e cidades. Consultar o [apto.vc](https://apto.vc/) para mais informações.

### 3-Execute a aplicação
No terminal, execute:

```
python app.py
```

Se tudo correr bem, a aplicação vai exibir no terminal algo parecido com:

```
Página 1
PATH: /br/{UF}/{cidade}
URL: https://apto.vc/_next/data/KD41YWHMuzlPQhhefsn7D/br/{UF}/{cidade}.json
STATUS: 200
12 imóveis
```

Significa que o app está verificando todos os imóveis de cada página. Assim que ele chegar a última página, vai exibir isso no terminal:

```
Página X
PATH: /br/rj/rio-de-janeiro?page=X
URL: https://apto.vc/_next/data/KD41YWHMuzlPQhhefsn7D/br/rj/rio-de-janeiro.json?page=X
STATUS: 404
Erro HTTP: 404 Client Error: Not Found for url: https://apto.vc/_next/data/KD41YWHMuzlPQhhefsn7D/br/rj/rio-de-janeiro.json?page=X
Página não contém dados. Encerrando aplicação...
Scrap concluído e salvo!
```

Significa que a aplicação percorreu por todo arquivo json, portanto, finaliza a aplicação e salva os dados obtidos formatados em um arquivo CSV chamado **apartamentos_scrap.csv** 
Nesse arquivo você consegue visualizar a base com todos os condôminios da cidade filtrada.

## Autor
