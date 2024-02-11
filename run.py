from app import *
from app.routes import app_flask


# Função pra criação de uma predição e salva-lá em static


if __name__ == '__main__':
    app_flask.run(port=5000, debug=True)

    """try:
        model = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={"prompt": prompt_input}
            )
        output_url = model.predict(prompt=prompt_input)[0]
        os.system("wget -cO - {} > {}/{}.png".format(output_url,"static"))
        return 

    except Exception as e:
        print('Erro ao criar a previsão: ',e)
        return "Erro ao criar a previsão: ",e
"""