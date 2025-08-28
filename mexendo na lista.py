# Parte 01

# Lista inicial 
nomes = ['Joaquim', 'Maria', 'Ana']
print('Lista inicial: ', nomes)

# Adicionando elementos
nomes.append('Carlos')
print('Após append: ', nomes)

nomes.insert(1, 'Fernanda') # Insire 'Fernanda' na posição 1
print('Após insert: ', nomes)

# Modificando elementos
nomes[2] = 'Paulo' # Modifica o elemento no índice 2
print('Após modificação: ', nomes)

# Parte 02

# Removendo elementos
del nomes[3] #Remove o elemento no índice 3
print('Após del: ', nomes)

nomes.remove('Maria') # Remove a primeira ocorrêncian de 'Maria'
print('Após remove: ', nomes)

removido = nomes.pop(2) # Remova e retorna o elemento no índice 2
print(f'Após pop (removido (removido)):, nomes')

nomes.clear() # Esvazia a lista 
print('Após clear:', nomes)