# Input: Name of the Brazilian city based on state(federation)
# Output: Total and percentage of correct answers

print("Brazilian Federations Game")
print("Type q to exit")

count_passed = 0
count_failed = 0

federations = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracajú",
    "Tocantins": "Palmas"
}

for k,v in federations.items():
    input_user = input(f"What is the capital from {k}?\n")
    if input_user == 'q':
        break
    if input_user.upper() == v.upper():
        count_passed += 1
    else:
        count_failed += 1

print(f"Total passed: {count_passed}")
print(f"Percentage passed: {(count_passed * 100)/27:.2f}")



