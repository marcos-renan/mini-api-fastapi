from fastapi import FastAPI

app = FastAPI()

#mock de dados usando dicionario
vendas = {
  1: {"item": "lapis", "preco_unitario": 3, "quantidade": 5},
  2: {"item": "caneta", "preco_unitario": 4, "quantidade": 10},
  3: {"item": "borracha", "preco_unitario": 2, "quantidade": 15},
  4: {"item": "caderno", "preco_unitario": 10, "quantidade": 20},
  5: {"item": "apontador", "preco_unitario": 1, "quantidade": 25},
}

#definindo rota inicial
@app.get('/')
def home():
  return {'Vendas': len(vendas)}

#rota para ver vendas especificas
@app.get('/vendas/{id_venda}')
def pegar_venda(id_venda: int):
  if id_venda in vendas:
    return vendas[id_venda]
  else:
    return {'Erro': 'ID da venda não existe'}