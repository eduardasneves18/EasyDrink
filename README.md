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
- 
## EasyDrink | E-Comerce de bebidas

;;

## Este sistema está em desenvolvimento


## Conteúdo


## Descrição
Com intuito de empreender, nós, a DreamTech, decidimos criar a nossa própria ferramenta de trabalho, na qual unia o objetivo individual de cada um e o objetivo do Entra21. A partir disso, desenvolvemos um e-commerce(comércio eletrônico) voltado para a distribuição de bebidas local e nacional. Visando alcançar aqueles que apreciam o lazer acompanhado de uma boa bebida, decidimos simplificar esse processo de descoberta de novos sabores e a sua aquisição. A EasyDrink busca apresentar ao consumidor o que há de melhor no mercado de bebidas, tornando a vida ainda mais alegre.

## Layout
- Home
- Página do usuário 
- Login
- Carrinho
- Finalização do pedido
- Produtos
- Produto e suas especificações



## Deploy 


## Pré-Requisitos 
- Python 3.9.4
- Django 3.2.7
- Mysql 4.1.6 
- VSCode para edição dos códigos
- Trello para a organização
- Discord para as reunões



## Ferramentas e tecnologias
No desenvolvimento do EasyDrink usamos como ferramenta de gestão de tarefas o Trello, onde empregamos pequenas atividades e fomos criando um fluxo de trabalho produtivo e organizado. Com reuniões diárias de acompanhamento, relatávamos no que estávamos trabalhando e as dificuldades, dessa forma nos ajudávamos internamente e procurávamos formas de solucionar os problemas. Como repositório usamos o GitLab(gitlab.com), onde podemos trabalhar simuntaneamente.

## Dependências e Libs Instaladas
- appdirs==1.4.4
- appnope==0.1.2
- asgiref==3.2.10
- autopep8==1.5.4
- backcall==0.2.0
- certifi==2020.6.20
- cffi==1.14.3
- chardet==3.0.4
- charset-normalizer==2.0.4
- colorama==0.4.4
- coreapi==2.3.3
- coreschema==0.0.4
- cryptography==3.1.1
- decorator==5.0.9
- defusedxml==0.7.0rc1
- Deprecated==1.2.12
- distlib==0.3.2
- Django==3.1.1
- django-autoslug==1.9.8
- django-braces==1.14.0
- django-cors-headers==3.5.0
- django-environ==0.4.5
- django-oauth-toolkit==1.3.2
- django-rest-framework-social-oauth2==1.1.0
- djangorestframework==3.11.1
- drf-social-oauth2==1.0.8
- filelock==3.0.12
- idna==2.10
- ipython==7.26.0
- ipython-genutils==0.2.0
- itypes==1.2.0
- jedi==0.18.0
- Jinja2==2.11.2
- jwcrypto==1.0
- MarkupSafe==1.1.1
- matplotlib-inline==0.1.2
- numpy==1.20.3
- oauthlib==3.1.0
- parso==0.8.2
- pexpect==4.8.0
- pickleshare==0.7.5
- Pillow==8.3.1
- prompt-toolkit==3.0.19
- ptyprocess==0.7.0
- pycodestyle==2.6.0
- pycparser==2.20
- Pygments==2.10.0
- PyJWT==1.7.1
- python-social-auth==0.2.21
- python3-openid==3.2.0
- pytz==2020.1
- requests==2.24.0
- requests-oauthlib==1.3.0
- six==1.15.0
- social-auth-app-django==4.0.0
- social-auth-core==3.3.3
- sqlparse==0.3.1
- toml==0.10.1
- traitlets==5.0.5
- typing-extensions==3.10.0.0
- Unidecode==1.2.0
- uritemplate==3.0.1
- urllib3==1.25.10
- virtualenv==20.4.7
- wcwidth==0.2.5
- wrapt==1.12.1

## Como rodas a aplicação teste na WEB
http://projeto-teste-212.heroku.com
Faça seu cadastro
Apos se logar voce pode navegar nas categorias de produtos.
Selecione os produtos....

## Como rodar a aplicação no seu PC
- Primeiramente é necessário fazer a intalação do Python (versão utilizada: 3.9.16).
- Em seguida instalação do django através do comando "pip install django" (versão utilizada: 3.2.6).
- No seu terminal local você vai criar seu ambiente virtual e ativa-lo através dos seguintes comandos na ordem descrita:
  -> python -m venv (nome do seu ambiente virtual)
  -> cd (nome do ambiente virtual)
  -> Scripts/activate
  
- Agora é a hora de fazer o clone do projeto no GitHub (https://github.com/eduardasneves18/EasyDrink). Apos acessar o link anterior do nosso repositório, clicar em "clone" e copiar o caminho HTTPS, como mostrado na seguinte imagem:  <img src="https://user-images.githubusercontent.com/86806534/135764669-e47f0b95-8e4e-402f-a044-284609ce7de9.PNG" width="5%"></img>   
                                                                                                             
-  No repositório escolhido, caso seja uma pasta nova é necessário fazer um 'GIT INIT' antes de realizar o "GIT CLONE".                                                                      
- Ainda no seu terminal local: fazer o comando git "GIT CLONE" e adicionar o caminho HTTPS copiado anteriormente.

- Depois de clonar o repositório por padrão o git vai estar na BRANCH "MAIN". 
                                  
- Agora que seu ambiente virtual já está ativado, você deve fazer o download de todas a bibliotecas co projeto através do comando "pip install requirements.txt".
                                                                                                                                           
- Após o termino da instalação deve-se executar o comando "python mange.py mekemigratios" para atualizar o banco de dados e os modelos.

- Em seguida "python mange.py migrate" para aplicar os comandos realizados. 

- Depois de de concluir deve-se executar "python mange.py runserver"

- Com o servidor rodando, pode acessar o nosso projeto pelo seguinte link: http://127.0.0.1:8000/


## Databases
Inicialmente utilizamos o gerenciador de banco de dados SqLite.
Na versão de apresentação utilizamos o GDB Mysql Server na Gogole Cloud fornecido pelo instrutor Adriano Machado, que é o responsável pelo projeto.
Endereços de conexão: Server.IP DatabaseName: DbE21G1

## Solução de problemas
Caso você tenha alguma dúvida ou encontrou algum problema em nossa aplicação, fique a vontade para entrar em contato com nossos colaboradores atráves dos seguintes contatos:

        - amandarafaela1415@gmail.com / (47) 9 8418 9821
        - eduardasneves18@gmail.com / (47) 9 9620 4693
        - matheusmedeiros2003@gmail.com / (47) 9 9606 5225
        - luigicleiffi674@gmail.com / (47) 9 9699 0424
        - darafrancinipinheiro@gmail.com / (47) 9 9656 3080

## Contribuintes
A DreamTech foi criada e é composta por cinco colaboradores, que viram no projeto do Entra21 uma oportunidade para empreender utilizando os conhecimentos adquiridos durante esses seis meses de curso. Com base nisso pensamos em como iriamos dividir a nossa equipe para que funcionasse da melhor forma, realçando e se baseando nas qualidades e facilidades de cada um. Nossa equipe se resume em:

- Eduarda Silva Neves: desenvolvedora lider, responsável por parte da codificação backend, revisão de códigos e organização das tarefas da equipe DreamTech;

- Luigi Cleffi: desenvolvedor, responsável pelo design do nosso site, parte da segurança de dados e codificação frontend do projeto EasyDrink;

- Dara Francini Pinheiro: desenvolvedora, responsável por parte da codificação frontende e testes do projeto EasyDrink;

- Matheus Medeiros Oselame: desenvolvedor backend, responsável pela administração do banco de dados;

- Amanda Rafaela Eduardo: responsável pela documentação e administração do conteúdo/produtos do projeto EasyDrink.


## Licença
Nós estamos utilizando a licença: GNU General Public License v3.0
Caso queira consultar acesse: https://github.com/Machado-tec/readme/blob/main/LICENSE
 


## TO DO

- Desenvolver a área administrativa do site 
        ° Dashboard do administrador
        ° Painel de metas
        ° Administração das finanças
        ° Controle de estoque para os fornecedores
        ° Página de administração do perfil do usuário
        ° Controle dos carrinhos não finalizados
- Pagamento e carteira   
- Finalizar transações dentro do site
- Filtros pela avaliação do usuário
- Página de rastreamento de produtos
- Destaques
- Opção de logout
- Tratar quantidade de itens no carrinho conforme o estoque
- linkar os detalhes do produto com a view 
- Dar funcionalidade aos ícones dos produtos
- Tela dos vinhos favoritos
- Filtros para pesquisa
- Imagens dos produtos na home
- Avaliação dos produtos


teste

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


pages
│   │   admin.py
│   │   apps.py
│   │   forms.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───static
│   │   ├───css
│   │   │       style_base.css
│   │   │       style_cart.css
│   │   │       style_login.css
│   │   │       style_navbar.css
│   │   │       style_slider.css
│   │   │
│   │   ├───images
│   │   │   │   android-icon-144x144.png
│   │   │   │   android-icon-192x192.png
│   │   │   │   android-icon-36x36.png
│   │   │   │   android-icon-48x48.png
│   │   │   │   android-icon-72x72.png
│   │   │   │
│   │   │   └───user
│   │   │           default.jpg
│   │   │
│   │   └───js
│   │           script_cart.js
│   │           script_nav.js
│   │           script_slider.js
│   │
│   └───__pycache__
│           forms.cpython-39.pyc
│           models.cpython-39.pyc
│           urls.cpython-39.pyc
│           views.cpython-39.pyc
│           __init__.cpython-39.pyc
│
├───payments
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │
│   └───__pycache__
│           models.cpython-39.pyc
│           __init__.cpython-39.pyc
│
├───products
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   serializers.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   0001_initial.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           0001_initial.cpython-39.pyc
│   │           __init__.cpython-39.pyc
│   │
│   └───__pycache__
│           models.cpython-39.pyc
│           serializers.cpython-39.pyc
│           urls.cpython-39.pyc
│           views.cpython-39.pyc
│           __init__.cpython-39.pyc
│
├───search
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   └───__pycache__
│           models.cpython-39.pyc
│           urls.cpython-39.pyc
│           views.cpython-39.pyc
│           __init__.cpython-39.pyc
│
├───services
│   │   auth_service.py
│   │   cart_service.py
│   │   products_service.py
│   │
│   └───__pycache__
│           auth_service.cpython-39.pyc
│           cart_service.cpython-39.pyc
│           products_service.cpython-39.pyc
│
├───static
│   └───images
│       └───media
│               heineken.jfif
│               Itaipava-Pilsen_350ml-_19---SUADA.jpg
│               skolbeats.png
│               skol_beats.jfif
│
├───staticfiles
│   ├───admin
│   │   ├───css
│   │   │   │   autocomplete.css
│   │   │   │   base.css
│   │   │   │   changelists.css
│   │   │   │   dashboard.css
│   │   │   │   fonts.css
│   │   │   │   forms.css
│   │   │   │   login.css
│   │   │   │   nav_sidebar.css
│   │   │   │   responsive.css
│   │   │   │   responsive_rtl.css
│   │   │   │   rtl.css
│   │   │   │   widgets.css
│   │   │   │
│   │   │   └───vendor
│   │   │       └───select2
│   │   │               LICENSE-SELECT2.md
│   │   │               select2.css
│   │   │               select2.min.css
│   │   │
│   │   ├───fonts
│   │   │       LICENSE.txt
│   │   │       README.txt
│   │   │       Roboto-Bold-webfont.woff
│   │   │       Roboto-Light-webfont.woff
│   │   │       Roboto-Regular-webfont.woff
│   │   │
│   │   ├───img
│   │   │   │   calendar-icons.svg
│   │   │   │   icon-addlink.svg
│   │   │   │   icon-alert.svg
│   │   │   │   icon-calendar.svg
│   │   │   │   icon-changelink.svg
│   │   │   │   
│   │   │   └───gis
│   │   │           move_vertex_off.svg
│   │   │           move_vertex_on.svg
│   │   │
│   │   └───js
│   │       │   actions.js
│   │       │   actions.min.js
│   │       │   autocomplete.js
│   │       │   calendar.js
│   │       │   cancel.js
│   │       │   change_form.js
│   │       │
│   │       ├───admin
│   │       │       DateTimeShortcuts.js
│   │       │       RelatedObjectLookups.js
│   │       │
│   │       └───vendor
│   │           ├───jquery
│   │           │       jquery.js
│   │           │       jquery.min.js
│   │           │       LICENSE.txt
│   │           │
│   │           ├───select2
│   │           │   │   LICENSE.md
│   │           │   │   select2.full.js
│   │           │   │   select2.full.min.js
│   │           │   │
│   │           │   └───i18n
│   │           │           af.js
│   │           │           ar.js
│   │           │           az.js
│   │           │           bg.js
│   │           │           bn.js
│   │           │
│   │           └───xregexp
│   │                   LICENSE.txt
│   │                   xregexp.js
│   │                   xregexp.min.js
│   │
│   ├───css
│   │       style_cart.css
│   │       style_login.css
│   │       style_navbar.css
│   │       style_slider.css
│   │
│   ├───drf-yasg
│   │   │   immutable.min.js
│   │   │   insQ.min.js
│   │   │   redoc-init.js
│   │   │   style.css
│   │   │   swagger-ui-init.js
│   │   │   url-polyfill.min.js
│   │   │   
│   │   ├───redoc
│   │   │       redoc-logo.png
│   │   │       redoc.min.js
│   │   │
│   │   ├───redoc-old
│   │   │       redoc.min.js
│   │   │
│   │   └───swagger-ui-dist
│   │           absolute-path.js
│   │           favicon-32x32.png
│   │           index.js
│   │           oauth2-redirect.html
│   │           swagger-ui-bundle.js
│   │           swagger-ui-es-bundle-core.js
│   │           swagger-ui-es-bundle.js
│   │           swagger-ui-standalone-preset.js
│   │           swagger-ui.css
│   │
│   ├───images
│   │   │   android-icon-144x144.png
│   │   │   android-icon-192x192.png
│   │   │   android-icon-36x36.png
│   │   │   android-icon-48x48.png
│   │   │   android-icon-72x72.png
│   │   │   
│   │   └───user
│   │           default.jpg
│   │
│   ├───js
│   │       script_cart.js
│   │       script_nav.js
│   │       script_slider.js
│   │
│   └───rest_framework
│       ├───css
│       │       bootstrap-theme.min.css
│       │       bootstrap-tweaks.css
│       │       bootstrap.min.css
│       │       default.css
│       │       font-awesome-4.0.3.css
│       │       prettify.css
│       │
│       ├───docs
│       │   ├───css
│       │   │       base.css
│       │   │       highlight.css
│       │   │       jquery.json-view.min.css
│       │   │
│       │   ├───img
│       │   │       favicon.ico
│       │   │       grid.png
│       │   │
│       │   └───js
│       │           api.js
│       │           highlight.pack.js
│       │           jquery.json-view.min.js
│       │
│       ├───fonts
│       │       fontawesome-webfont.eot
│       │       fontawesome-webfont.svg
│       │       fontawesome-webfont.ttf
│       │       fontawesome-webfont.woff
│       │       glyphicons-halflings-regular.eot
│       │       glyphicons-halflings-regular.svg
│       │       glyphicons-halflings-regular.ttf
│       │       glyphicons-halflings-regular.woff
│       │       glyphicons-halflings-regular.woff2
│       │
│       ├───img
│       │       glyphicons-halflings-white.png
│       │       glyphicons-halflings.png
│       │       grid.png
│       │
│       └───js
│               ajax-form.js
│               bootstrap.min.js
│               coreapi-0.1.1.js
│               csrf.js
│               default.js
│               jquery-3.4.1.min.js
│               prettify-min.js
│
├───templates
│   │   about.html
│   │   contacts.html
│   │   home.html
│   │   orders.html
│   │   pagination.html
│   │   slider.html
│   │   wishes_list.html
│   │
│   ├───base
│   │       aside.html
│   │       base.html
│   │       footer.html
│   │       logo_image.html
│   │       nav.html
│   │
│   ├───cart
│   │       cart_detail.html
│   │
│   ├───categories
│   │       category_list.html
│   │
│   ├───products
│   │       products_bestsellers.html
│   │       products_list.html
│   │       product_detail.html
│   │
│   ├───search
│   │       result_query.html
│   │       search_form.html
│   │
│   └───user
│           login.html
│           logout.html
│           register.html
│           reset_password.html
│           reset_password_confirmed.html
│           verify_confirmed_email.html
│           verify_email.html
│
├───users
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   renderers.py
│   │   serializers.py
│   │   tests.py
│   │   urls.py
│   │   utils.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   0001_initial.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           0001_initial.cpython-39.pyc
│   │           __init__.cpython-39.pyc
│   │
│   └───__pycache__
│           models.cpython-39.pyc
│           renderers.cpython-39.pyc
│           serializers.cpython-39.pyc
│           urls.cpython-39.pyc
│           utils.cpython-39.pyc
│           views.cpython-39.pyc
│           __init__.cpython-39.pyc
│
└───__pycache__
        utils.cpython-39.pyc

Muito obrigada por ter lido a nossa documentação. Caso queira conversar com a nossa equipe ou tirar alguma dúvida entre em contato conosco atráves dos nossos e-mails de contato.

