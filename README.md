## backend-django

Você pode tentar acessar nossa solução em http://www.hackathon-klabin.com:3000
Atualmente ela está hospedada na AWS. Por questões de orçamento, a instância na nuvem pode apresentar instabilidades. Ao final desse documento encontra-se instruções para instalção e execução dele localmente. Caso o link http://www.hackathon-klabin.com:3000 fique muito tempo fora do ar, sintam-se livres para nos contatar, somos do Grupo 5.

## Installation
É possível rodar tudo localmente, mas pode ser necessário atualizar o valor da variável "apiBaseURL" no código da interface e podem ocorrer problemas ao tentar atualizar a WordCloud na interface. A maneira mais fácil de testar a solução continua sendo utilizar a interface remota em http://www.hackathon-klabin.com:3000 
# Instruçoes
- Clone esse repositório
- Será utilizado python3 e pip para instalar as dependencias
- Instale as bibliotecas necessárias utilizando `pip install -r requirements.txt`
- Descompacte o arquivo "sentimentAnalysis.rar" (você pode usar `unrar x sentimentAnalysis.rar` caso esteja em uma máquina linux)
- rode python3:
```
$ python3
> import nltk
> nltk.download('punkt')
> nltk.download('stopwords')
```
- Para rodar a "aspect-based sentiment analysis" precisará instalar: `python3 -m spacy download en_core_web_sm`

Rode o servidor django com `python3 manage.py runserver 0:3001`
ou utilizando `nohup python3 manage.py runserver 0.0.0.0:3001 > app.log &`

# Interface
- Clone o repositório da interface que está em https://github.com/CarinaAlvarez/HackathonKlabin
- Execute `npm install`
- Execute `npm start`
- A interface deve abrir automaticamente, caso isso não aconteça, acesse localhost:3000
