# Drink Water Tracker :sweat_drops:

Este projeto é um aplicativo que ajuda os usuários a monitorar e registrar seu consumo diário de água, garantindo que alcancem suas metas diárias de hidratação com base no seu peso corporal.

Estrutura do Projeto
---
O projeto é dividido em duas partes principais:

back-end: Implementado usando Django REST Framework, responsável por gerenciar a API e o banco de dados.
front-end: Implementado usando Vue.js com Vue Router e Vuex, responsável pela interface do usuário.

Funcionalidades
---
Cadastro de Usuário: Os usuários podem se cadastrar fornecendo seu nome e peso. O sistema calculará automaticamente a meta diária de consumo de água com base no peso (35ml por kg).
Registro de Consumo: Os usuários podem registrar a quantidade de água que beberam ao longo do dia e verificar se atingiram a meta diária.
Histórico: Exibe o histórico de consumo de água dos usuários ao longo do tempo, permitindo acompanhar o progresso.

Requisitos
---
back-end:

Python 3.10+
Django 5.1
Django REST Framework

front-end:

Node.js 16+
Vue.js 3
Vue Router
Vuex
Bootstrap

Instalação
---
### Clonando o Repositório
```
git clone https://github.com/seu-usuario/drink_water_tracker.git
cd drink_water_tracker
```
### Configuração do Back-end
Vá para a pasta do back-end:
```
cd back-end
```
Crie e ative um ambiente virtual:
```
python -m venv venv
# Python 3.10 ou superior
source venv/bin/activate
# No Windows: venv\Scripts\activate
```
Instale as dependências:
```
pip install -r requirements.txt
```
Configure o banco de dados:
```
python manage.py makemigrations
python manage.py migrate
```
Execute o servidor de desenvolvimento:
```
python manage.py runserver
```

### Configuração do Front-end
Vá para a pasta do front-end:
```
cd ../front/drink_water_tracker
```
Instale as dependências:
```
npm install
```

Execute o servidor de desenvolvimento:
```
npm run dev
```
Acesso à Aplicação
---
O back-end estará disponível em http://127.0.0.1:8000/.

O front-end estará disponível em http://localhost:5174/.

Uso
---
Login e Cadastro: Acesse a tela inicial para cadastrar um novo usuário com nome e peso.

Registro de Consumo: Após o login, registre seu consumo de água ao longo do dia.

Ver Histórico: Navegue até a seção de histórico para ver o registro de consumo diário.

Contribuições
Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:

Faça um fork do repositório.
---
Crie uma branch para a sua feature (git checkout -b feature/nome-da-feature).
Commit suas mudanças (git commit -m 'Adicionei nova feature').
Faça um push para a branch (git push origin feature/nome-da-feature).
Abra um Pull Request.
