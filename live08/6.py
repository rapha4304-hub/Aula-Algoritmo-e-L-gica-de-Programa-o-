clientes = [
    {
        "id": 23,
        "nome": "Raphael",
        "Valor": 589.80
    },
    {
        "id": 45,
        "nome": "Luana",
        "Valor": 1200.00
    },
    {
        "id": 12,
        "nome": "André",
        "Valor": 250.00
    }
]

for cliente in clientes:
    if cliente["Valor"] > 589.80:
        cliente["Valor"] -= 50
        print(
            f"Cliente {cliente['nome']},  Valor: {cliente['Valor']}")
    else:
        print(
            f"Cliente {cliente['nome']},  Valor: {cliente['Valor']}")
