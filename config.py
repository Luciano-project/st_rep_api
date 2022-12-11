import os


# Arquivo de configuração inicial da aplicação.

list_dir = os.listdir()
# Carregará as configurações para a aplicação
try:
    # Verificará se há o diretório static (onde ficarão os arquivos gerados por predições), caso não haja será criado o mesmo
    os.system(f'if [ ! -d static ]; then mkdir static && echo "Diretório {"static/"} criado com sucesso!"; fi')
    # Seleciona o path para salvar os arquivos
    save_path='static'

    if "venv" not in list_dir:
        print("Criando ambiente virtual...")
        os.system("python3 -m venv venv")
        print("Ambiente virtual criado com sucesso!")
except:
    print("Erro ao tentar criar diretório.")
