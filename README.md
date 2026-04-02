# Scrap Condomínios

Esta aplicação realiza scraping de condomínios do site [Apto.vc](https://apto.vc/). A aplicação coleta todos os condomínios na pagina via request e armazena em um arquivo Excel formatado.

---

## Tecnologias necessárias
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

---

## Como executar o projeto
### 1- Clone este repositório para o seu computador
No terminal do seu computador, execute:

```
git clone https://github.com/nanic1/condominio-scrap
cd condominio-scrap
```

É necessário ter o Git instalado para fazer a clonagem deste repositório.

### 2- Instale as dependências necessárias
Dentro do projeto, execute no terminal:

```
pip install pandas
```

É necessário ter o Python instalado para executar o projeto e instalar as dependências.

### 3- Defina a cidade que deseja filtar
Com o código aberto, na função main, mude o **url** para o UF e cidade que deseja filtrar. **NÃO** use acentos no caminho.

Ex:
* Filtro Rio de Janeiro
```
url = "https://apto.vc/_next/data/c4CV659C9opeV5h-S4PrC/br/rj/rio-de-janeiro.json?"
```

* Filtro São Paulo
```
url = "https://apto.vc/_next/data/c4CV659C9opeV5h-S4PrC/br/sp/sao-paulo.json?"
```

O apto.vc não fornece cobertura para todos os estados e cidades. Consultar o [apto.vc](https://apto.vc/) para mais informações.

### 4- Execute a aplicação
No terminal, execute:

```
python app.py
```

Se tudo correr bem, a aplicação vai exibir no terminal algo parecido com:

```
Página: 1
STATUS: 200
12 imóveis encontrados na página 1
```

Significa que o app está verificando todos os imóveis de cada página. Assim que ele chegar a última página, vai exibir isso no terminal:

```
Página: 27
STATUS: 404
Erro: 404 Client Error: Not Found for url: https://apto.vc/_next/data/c4CV659C9opeV5h-S4PrC/br/rj/rio-de-janeiro.json??page=27
Erro ao buscar a página. Encerrando...
Scrap realizado com sucesso!
```

Significa que a aplicação não achou dados nenhum na página, portanto, finaliza a aplicação e salva os dados obtidos formatados em um arquivo CSV chamado **base_apto.xlsx** 
Nesse arquivo você consegue visualizar a base com todos os condomínios da cidade filtrada.

## Autor
Pedro Kurtz
