from flask import Flask,request,redirect,url_for
from flask_restful import Resource, Api
from processing_data import decode_name,get_files_list
from prediction import create_prediction

app = Flask(__name__)
api = Api(app)

# Objeto para encaminhar informções aos endpoints 
class ReturnApp(Resource):
    def get(self, name):
        # Recebe um dicionario com os arquivos da pasta static
        list_files = get_files_list()

        # Acrescenta a string base64 a extenção do arquivo
        name_plus_extension = name+'.png'

        # Nome base64 para ser descriptografado
        decoded=decode_name(name)

        # Verificação, caso não exista cria a predição aguardando o tempo para que a mesma seja entregue
        if name_plus_extension not in list_files:
            create_prediction(decoded.split("|")[0],name)
            #time.sleep(10)
        return redirect(url_for('static', filename=name_plus_extension))
        
api.add_resource(ReturnApp, '/<string:name>')

if __name__ == '__main__':
    app.run()
    