Comandos para configuração do projeto roteamentornp localmente:

Instalar a bibliotecas necessárias:

        pip3 install Django

        sudo apt install libpq-dev python3-dev

        pip3 install psycopg2



Deve ser configurado no settings.py o caminho usuário e senha do bando de dados:


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.path.join('roteamento'),
            'USER': 'root',
            'PASSWORD':'123456',
            'HOST':'127.0.0.1',
            'PORT':''
        }
    }

Posteriormente rode os seguintes comando na ordem:

    python3 manage.py migrate

    python3 manage.py makemigrations rotas

    python3 manage.py migrate

    


Criar um usuário e uma senha para a parte de administração

    python3 manage.py createsuperuser --username=joe --email=joe@example.com



Para iniciara aplicação é necessário rodar o comando

        python3 manage.py runserver



Acessar o endereço http://localhost:8000/rotas/ para acesso o template básico das rotas


Configurando a rota de administração

        ./manage.py shell
        from django.contrib.sites.models import Site
        site = Site()
        site.domain = 'localhost'
        site.name = 'localhost'
        site.save()


Acessar o ebndereço http://localhost:8000/admin/ para acessar o template de administração

