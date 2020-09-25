# backend-django

Esse é o repositório que contém o código server-side de nossa aplicação. Ele funciona em conjunto com a interface, que encontra-se em https://github.com/CarinaAlvarez/HackathonKlabin

O backend possui diferentes endpoints, são eles:
![Exemplo](/images/employee-endpoint.png)
* employee/
  * utilizado para cadastrar um novo funcionário ou obter informações a respeito de um funcionário da Klabin
* topscores/
  * endpoint responsável por retornar, já ordenados, os funcionários que possuem maior pontuação
* feedback/
  * utilizado para ler ou criar um feedback
  * este endpoint também é responsável por executar as analises (tanto a sentiment analysis, quanto a aspect-based, e também a procura por red-flags) antes de salvar o feedback em nosso database
* wordcloud/
  * responsável por gerar uma wordcloud atualizada e salvá-la
* redflags/
  * endpoint que irá retornar uma lista com os feedbacks que necessitam de uma atenção especial - de acordo com as configurações de quais palavras levantariam esse alerta


Você pode tentar acessar nossa solução em http://www.hackathon-klabin.com:3000
Atualmente ela está hospedada na AWS. Por questões de orçamento, a instância na nuvem pode apresentar instabilidades. Ao final desse documento encontra-se instruções para instalção e execução dele localmente. Caso o link http://www.hackathon-klabin.com:3000 fique muito tempo fora do ar, sintam-se livres para nos contatar, somos do Grupo 5.

# Aplicação
![interface](/images/interface-main-page.png)
![conversar com a luna](/images/interface-chat-with-luna.png)
![enviar arquivo](/images/interface-sending-file.png)
![todas as opções da interface](/images/interface-all-cards.png)

# Instalação
É possível rodar tudo localmente, mas pode ser necessário atualizar o valor da variável "apiBaseURL" no código da interface e podem ocorrer problemas ao tentar atualizar a WordCloud na interface. A maneira mais fácil de testar a solução continua sendo utilizar a interface remota em http://www.hackathon-klabin.com:3000 
## Instruções
- Clone esse repositório
- Será utilizado python3 e pip para instalar as dependencias
- Instale as bibliotecas necessárias utilizando `pip install -r requirements.txt`
- Descompacte o arquivo "sentimentAnalysis.rar" (você pode usar `unrar x sentimentAnalysis.rar` caso esteja em uma máquina linux)
- rode python3:
```cmd
$ python3
> import nltk
> nltk.download('punkt')
> nltk.download('stopwords')
```
- Para rodar a "aspect-based sentiment analysis" precisará instalar: `python3 -m spacy download en_core_web_sm`

Rode o servidor django com `python3 manage.py runserver 0:3001`
ou utilizando `nohup python3 manage.py runserver 0.0.0.0:3001 > app.log &`

## Interface
- Clone o repositório da interface que está em https://github.com/CarinaAlvarez/HackathonKlabin
- Execute `npm install`
- Execute `npm start`
- A interface deve abrir automaticamente, caso isso não aconteça, acesse localhost:3000
