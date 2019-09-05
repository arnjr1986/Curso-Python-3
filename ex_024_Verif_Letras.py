#Ler nome de uma cidade e dizer se começa com nome SANTO

cidade = str(input('Digite o nome de uma cidade: ')).strip()

print(cidade[:5].upper() == 'Santo')
