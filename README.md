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
Para uma melhor visualização das soluções propostas, criamos uma interface que serve como protótipo de como seria o acesso aos dados referentes à gamificação da Luna. Seria acessível para todos os funcionários, com a exceção da seção 'Status da Klabin' que seria reservada para o RH com o resultado dos feedbacks recebidos. Nesta interface, seriam apresentados o total de pontos do funcionário e o total de pontos de seu departamento. Também haveria uma seção 'Placar de Pontos', onde seria possível observar sua posição no placar individual e a posição de seu departamento no placar de departamentos, assim como qual seria os prêmios da rodada, incentivando uma competição amigável para interagirem mais com a Luna. Na seção 'Histórico de Pontos', o funcionário poderia observar sua evolução na obtenção de pontos ao longo de 3 meses, assim como a evolução de seu departamento, de forma a criar o entusiasmo de querer se superar sempre. 

![todas as opções da interface](/images/interface-all-cards.png)

A interface apresentada, neste caso, seria a de um funcionário do RH, já que apresenta, também, a seção "Status da Klabin", a qual ilustra a situação geral do conjunto de feedbacks por meio de uma WordCloud, um gráfico da relação entre os feedbacks positivos e negativos, um gráfico da evolução percentual de feedbacks positivos ao longo de 3 meses e uma subseção de "Redflags". A WordCloud representa as palavras usadas com maior frequência nos feedbacks. A subseção de "Redflags" apresenta os feedbacks que apresentaram termos impróprios, que estão divididos em termos machistas, racistas, lgbtq+fóbicos e outros. Este informe sobre termos impróprios permite ao RH identificar e, portanto, melhorar problemas no ambiente de trabalho, de forma a se obter um ambiente de trabalho harmônico e agradável para todos.

![conversar com a luna](/images/interface-chat-with-luna.png)

Outra ferramenta presenta nesta interface seria o chat com a Luna. Como não tínhamos acesso ao código utilizado para as interação com a Luna, criamos um chat que possibilita uma interação simples, mas com perguntas da Luna que visam obter respostas equivalentes a feedbacks e, consequentemente, material para uma subsequente análise de sentimentos. Logo após a interação com a Luna, o funcionário poderá verificar, ao recarregar a página, que seus pontos aumentaram. Uma outra proposta extra seria a de permitir que a Luna possa receber arquivos pelo chat, de forma a facilitar, por exemplo, o envio de atestados médicos pelos funcionários.

![enviar arquivo](/images/interface-sending-file.png)


# Instalação
É possível rodar tudo localmente, mas pode ser necessário atualizar o valor da variável "apiBaseURL" no código da interface. A maneira mais fácil de testar a solução continua sendo utilizar a interface remota em http://www.hackathon-klabin.com:3000 
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

#### Atenção, ambas as pastas (backend e interface) devem estar localizadas na mesma pasta raiz. 
-Também pode ser necessário executar `npm run-scripts build` na pasta da interface
