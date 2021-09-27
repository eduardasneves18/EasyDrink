## EasyDrink E-Comerce de bebidas

## Este sistema está em desenvolvimento

### Tabela de conteúdos
- Título
- Status
- Conteúdo
- Descrição
- Layout
- Deploy 
- Pré-Requisitos
- Dependências e Libs Instaladas
- Como rodas a aplicação teste na WEB
- Como rodar a aplicação no seu PC
- Databases
- Solução de problemas
- Contribuintes
- Tarefas em aberto
- Licenças

## Descrição
Com intuito de epreender, nós, a DreamTech, decidimos criar a nossa própria ferramenta de trabalho, na qual unia o objetivo individual de cada um e o objetivo do Entra21. A partir disso, desenvolvemos um e-commerce(comércio eletrônico) voltado para a distribuição de bebidas local e nacional. Visando alcançar aqueles que apreciam o lazer acompanhado de uma boa bebida, decidimos simplificar esse processo de descoberta de novos sabores e a sua aquisição. A EasyDrink busca apresentar ao consumidor o que há de melhor no mercado de bebidas, tornando a vida ainda mais alegre.

## Layout
- home - quem somos
- login - cadastro -

## Pré-Requisitos
- Python 3.8
- Djago (versao??)
- Mysql (versao??)
- Heroku para usar como banco de dados

### Ferramentas utilizadas desenvolvimento
- Trello para organização tarefas
- VSCode para edição e testes de códigos
- Nosso repositorio GIT fica na GITHUB.com e está aberto ao publico. 

## Dependências e Libs Instaladas
- pip freeze > requirements.txt e incluir o resultado de requirements.txt aqui. 

## Como rodar a aplicação na WEB



## Como rodar os testes e desenvolvimento da app

- incluir o roteiro de criação de:
    - python -m venv venv
    - activate (descrver comandso para o activate)
    - faça um clone do codigo disponivel em https://github.com/xxxxxx.git
    - modifique o arquiv local_settins.py de acordo com a sua configuração do banco de dados.    


## Database
- Estamos utilizando o banco de dados na nuvem (mysql) em HOST, DATABASE..

- Para seus testes vc pode utilizar o SqLite modificando o arquivo local_setting.py conforme acima. 

## Solução de problemas

- Em caso de qualquer problema entre em contato com um dos nossos contribuintes, através dos seguintes emails-contatos:

    - amandarafaela1415@gmail.com  (47) 99999.9999
    - 
    - 
    - 

## Ferramentas e tecnologias
No desenvolvimento do EasyDrink usamos como ferramenta de gestão de tarefas o Trello, onde empregamos pequenas atividades e fomos criando um fluxo de trabalho produtivo e organizado. Com reuniões diárias de acompanhamento, relatávamos no que estávamos trabalhando e as dificuldades, dessa forma nos ajudávamos internamente e procurávamos formas de solucionar os problemas. Como repositório usamos o GitLab(gitlab.com), onde podemos trabalhar simuntaneamente.


## Instalações
- Primeiramente é necessário fazer a intalação do Python (versão utilizada: 3.9.16).

- Em seguida instalação do django através do comando "pip install django" (versão utilizada: 3.2.6).

- Agora tem que fazer o clone do projeto no GitLab.No GitLab acessar o projeto "e-commerce", clicar em "clone" e copiar o caminho HTTPS, como mostrado na seguinte imagem: https://gitlab.com/e-commerce53/e-commerce/-/wikis/uploads/8b9533053f58d26f5318c34e75535678/image.png
No seu terminal local você vai fazer o comando git "GIT CLONE" e adicionar o caminho HTTPS copiado anteriormente. No repositório escolhido, caso seja uma pasta nova é necessário fazer um 'GIT INIT' antes de realizar o "GIT CLONE". Exeplo: https://gitlab.com/e-commerce53/e-commerce/-/wikis/uploads/c5efff7b688f685aa20a2ceeca2a5cec/image.png

- Depois de clonar o repositório por padrão o git vai estar na BRANCH "MAIN". Imagem: https://gitlab.com/e-commerce53/e-commerce/-/wikis/uploads/c29297ab08d0f964067c7ef87fb07261/image.png

- Agora é recomendável ativar o ambiente virtual através do comando: Scripts\activate.ps1

- Agora que seu ambiente virtual já está ativado, você deve fazer o download de todas a bibliotecas co projeto através do comando "pip install requirements.txt".

- Após o termino da instalação deve-se executar o comando "python mange.py mekemigratios" para satualizar o banco de dados e os modelos.

- Em seguida "python mange.py migrate" para aplicar os comandos realizados. 

- Depois de de concluir deve-se executar "python mange.py runserver"


## Suporte
Em nosso site temos a página de ajuda na qual se pode tirar dúvidas com base em perguntas frequentes ou se necessário fazer entrar em contato, basta enviar um e-mail para a empresa. Todos os meios de comunicação estão dispoíveis na nossa página de contato. 



## Contribuintes
A DreamTech foi criada e é composta por cinco colaboradores, que viram no projeto do Entra21 uma oportunidade para empreender utilizando os conhecimentos adquiridos durante esses seis meses de curso. Com base nisso pensamos em como iriamos dividir a nossa equipe para que funcionasse da melhor forma, realçando e se baseando nas qualidades e facilidades de cada um. Nossa equipe se resume em:


- Eduarda Silva Neves: desenvolvedora lider, responsável por parte da codificação backend, revisão de códigos, organização das tarefas da equipe e documentação do projeto EasyDrink;

- Luigi Cleffi: desenvolvedor, responsável pelo design do nosso site, parte da segurança de dados e codificação frontend do projeto EasyDrink;

- Dara Francini Pinheiro: desenvolvedora, responsável por parte da codificação frontend, testes e documentação do projeto EasyDrink;

- Matheus Medeiros Oselame: desenvolvedor backend, responsável pela administração do banco de dados;

- Amanda Rafaela Eduardo: desenvolvedor backend, responsável pela administração do conteúdo e produtos do projeto EasyDrink.


## Licença

Este software esta licenciado sob o modelo: ..xlxlxlxlxlxlxlx 
leia na integra o acordo de licenca no link --:: github... licençc-file

## TO DO (Pendencias)
- Finalizar as funcionalidades do Pix

Descrição dos Arquivos e Diretorios deste projeto.
├── easydrink = contém a pasta do backend e do frontend do projeto
│   ├── carts = tem os códigos do carrinho
│   │   └── migrations = envia as informações do carrinho para o banco de dados
│   ├── easydrink = 
│   ├── pages = 
│   ├── products = 
│   │   └── migrations = envia as funções dos products para o banco de dados
│   ├── search = possui os códigos da barra de pesquisa
│   │   └── migrations = envia as informações de busca para o banco de dados
│   ├── static = 
│   │   ├── css = 
│   │   ├── images = 
│   │   ├── js = 
│   │   └── templates = possui os templates de cada página do projeto
│   │       ├── base = possui os arquivos base para fazer os outros templates
│   │       ├── cart = possui o template do carrinho
│   │       ├── categories = possui os templates das páginas com as categorias das bebidas
│   │       ├── products = possui os templates da página dos produtos
│   │       └── user = possui os templates da página de cadastro do usuário
│   └── users
│       └── migrations = envia as informações do usuário para o banco de dados



O que? vc chegou até aqui?? usuarios nunca leem arquivos README... hahahah..
