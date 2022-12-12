# Stable Diffusion - API Replicate

<h2>Introdução e Funcionamento</h2>
Para o correto funcionamento dessa aplicação será necessário estar com o ambiente virtual devidamente criado e ativado, instalar pacotes contidos em "requirements.txt" e exportar o token api do replicate. Para todos esses casos teráo tópicos relcionados e explicando.

Primeiramente siga os tópicos antes de prosseguir aqui. Esta aplicação foi desenvolvida em python com flask e suas dependências. O core da aplicação é o <b>app.py</b>, onde será recebido e fará a delegação do tratamento das requisições.<br>

<h5>app.py</h5>
Este arquivo possui as configurações para rodar a API, e que além de delegar as funções, recebe uma string no formato <i>base64</i> como requisição, esta será decodificada para e disso extraído o prompt para ser gerado a predição.
<br><br>

<h5>processing_data.py</h5>
Neste estão todas as funções relacionada a decodificação no formato base64, responsável pela extração do prompt.
<br><br>

<h5>prediction.py</h5>
Depois de ter o prompt extraído existem 2 situações possíveis, caso exista: será retornado a imagem <i>.png</i> para aquele prompt; caso não exista: será criado uma imagem e retornada ao usuário.


<h3>Ambiente virtual</h3>
Para criação do ambiente virtual basta rodar o arquivo <b>config.py</b>, Ele fará automaticamente a criação do ambiente.<br>
Logo após é necessário ativar o ambiente virtual no path:<br>
  *   <b>venv/bin/activate*</b> -- Importante verificar como iniciar de acordo com o sistema operacional. Recomendo ativá-lo antes de prosseguir.--
<br>
<br>
<h3>Instalação de pacotes</h3>
Para instalar as dependências necessárias ao projeto basta rodar o arquivo <b>install_requirements.py</b>
<br>
<br>
<h3>Chave Replicate</h3>
Para que seja possível fazer a predição é necessário exportar a chave Replicate da API. Com o ambiente virtual ativo, faça:<br>
* <b>export REPLICATE_API_TOKEN=[seu token]</b>


