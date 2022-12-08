import replicate
import os


# Função pra criação de uma predição e salva-lá em static
def create_prediction(prompt_input,prompt_encoded):
    try:
        model = replicate.models.get("stability-ai/stable-diffusion")
        output_url = model.predict(prompt=prompt_input)[0]
        os.system("wget -cO - {} > {}/{}.png".format(output_url,"static",prompt_encoded))

    except:
        print("Algum erro ocorreu ao fazer a predição!")


  