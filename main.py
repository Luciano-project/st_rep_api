import os

#Aplicar o token Replicate no ambiente virtual
# && echo "Token aplicado ao ambiente virtual!"')

# Carregará as configurações para a aplicação
try:
    # Verificará se há o diretório media (onde ficarão os arquivos gerados por predições), caso não haja será criado o mesmo
    os.system(f'if [ ! -d static ]; then mkdir media && echo "Diretório {"static/"} criado com sucesso!"; fi')
    # Seleciona o path para salvar os arquivos
    save_path='static'
    token_replicate = input('Insira seu API token Replicate: ')
    os.system(f'export REPLICATE_API_TOKEN={token_replicate}; echo "Chave exportada com sucesso"')
    os.system('python3 app.py')
except:
    print("Erro ao tentar criar diretório.")
