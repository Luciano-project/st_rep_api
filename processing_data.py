import base64
import os

# Decodificar nome em base64
def decode_name(name):
    decoded = base64.b64decode(name).decode("ascii")
    return decoded

# Codificar nome em base64
def encode_name(prompt_input="lalaa",random_number=1,data_hora=12):
    name_image = base64.b64encode(bytes(f'{prompt_input}|{random_number}|{data_hora}',"ascii"))
    new_name = str(name_image).split("'")[1]
    return new_name

# Retorno de todos arquivos existentes na pasta static
def get_files_list():
    files = [arq for arq in os.listdir("static")]
    names = {name_encoded : name_encoded for name_encoded in files}
    return names


if __name__== "__main__":
    print(get_files_list())