from app import *

app_flask = Flask(__name__)

@app_flask.route('/prediction', methods=['POST'])  # Método HTTP que será usado na requisi
def prediction():
    if request.form["generate"] and request.form["prompt"]:
        prompt_input = processing_prediction(request.form["prompt"])
        return redirect('/')
    else:
        return redirect(url_for('/'))
    
@app_flask.route('/', methods=['GET'])
def files():
    context = {}
    for i in os.listdir('app/static'):
        context[i] = f'app/static/{i}'
    return render_template('index.html', context=context)


def processing_prediction(prompt_input):
    prompt_input = request.form["prompt"]
    try:
        prediction = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={"prompt": prompt_input}
            )
        url = prediction[0]
        prompt_input = str(prompt_input).replace(" ","_")
        require_img = requests.get(url)
        with open(f'app/static/{ prompt_input }.png', 'wb') as img:
            img.write(require_img.content)
        return prompt_input
    
    except Exception as e:
        print('Erro ao criar a previsão: ',e)
        return "Erro ao criar a previsão: ",e