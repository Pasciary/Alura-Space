# AluraSpace

AluraSpace é uma aplicação web desenvolvida em Django para gerenciamento e exibição de uma galeria de imagens astronômicas. O projeto foi criado com o objetivo de praticar conceitos de backend, frontend e integração com o painel administrativo do Django.

## 🚀 Funcionalidades

- Cadastro, edição e exclusão de fotografias via painel administrativo
- Organização das imagens por categorias
- Visualização de galeria com imagens populares, mais curtidas e mais vistas
- Layout responsivo e moderno
- Estrutura de templates reutilizáveis
- Separação clara entre arquivos estáticos (CSS, imagens, ícones) e templates

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Django
- HTML5 & CSS3
- Templates Django
- WSL (Windows Subsystem for Linux) para ambiente de desenvolvimento

## 📁 Estrutura do Projeto

```
AluraSpace/
├── galeria/                # App principal da galeria
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── setup/                  # Configurações do projeto Django
│   ├── settings.py
│   └── ...
├── static/                 # Arquivos estáticos (CSS, imagens, ícones)
├── templates/              # Templates HTML
│   └── galeria/
│       ├── base.html
│       ├── index.html
│       └── ...
├── manage.py
└── requirements.txt
```

## ⚙️ Como rodar o projeto

1. **Clone o repositório:**
   ```sh
   git clone git@github.com:Pasciary/Alura-Space.git
   cd Alura-Space
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Aplique as migrações:**
   ```sh
   python manage.py migrate
   ```

5. **Crie um superusuário para acessar o admin:**
   ```sh
   python manage.py createsuperuser
   ```

6. **Rode o servidor de desenvolvimento:**
   ```sh
   python manage.py runserver
   ```

7. **Acesse a aplicação:**
   - Frontend: [http://localhost:8000/](http://localhost:8000/)
   - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## 👨‍💻 Contribuição

Sinta-se à vontade para abrir issues, enviar pull requests ou sugerir melhorias!