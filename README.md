# Django Templates - Integração HTML + Django

Projeto demonstrando a integração entre templates HTML e o sistema de templates do Django.

## 📁 Estrutura do Projeto

```
mysite/
├── blog/                # App do blog
│   ├── models.py       # Model Post
│   ├── admin.py        # Configuração do admin
│   ├── urls.py         # URLs do blog
│   └── migrations/     # Migrações do banco
├── config/             # Configurações do Django
│   ├── settings.py     # Settings com TEMPLATES configurado
│   ├── urls.py         # URLs principais
│   └── wsgi.py        # WSGI application
├── templates/          # Templates HTML
│   ├── base.html      # Template base com herança
│   ├── index.html     # Página inicial (extends base.html)
│   ├── post_detail.html
│   └── sidebar.html
├── views/             # Views customizadas
│   └── post_view.py   # Views do blog
├── manage.py          # Script de gerenciamento Django
└── requirements.txt   # Dependências
```

## 🎯 Funcionalidades Django Templates Demonstradas

### 1. **Herança de Templates** (`{% extends %}`)
- base.html define a estrutura HTML básica
- index.html herda de base.html usando `{% extends 'base.html' %}`

### 2. **Blocos de Conteúdo** (`{% block %}`)
- `{% block title %}` para títulos personalizados
- `{% block content %}` para conteúdo principal
- `{% block extra_scripts %}` para scripts adicionais

### 3. **Configuração em settings.py**
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Pasta de templates
        'APP_DIRS': True,
        ...
    },
]
```

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/viniciussilva2504/mysite.git
cd mysite
git checkout templates
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute as migrações
```bash
python manage.py migrate
```

### 5. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 6. Execute o servidor
```bash
python manage.py runserver
```

### 7. Acesse no navegador
- Aplicação: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 📚 Conceitos Django Implementados

- ✅ **Template Engine**: Sistema de templates do Django
- ✅ **Template Inheritance**: Herança com `{% extends %}`
- ✅ **Template Blocks**: Blocos reutilizáveis com `{% block %}`
- ✅ **Settings Configuration**: TEMPLATES configurado em settings.py
- ✅ **App Structure**: Organização modular com app 'blog'
- ✅ **Models**: Model Post com campos e Meta
- ✅ **Admin**: Configuração do Django Admin

## 🎓 Branch: templates

Esta branch demonstra especificamente a **integração entre arquivos HTML e o Django Templates**, mostrando como:
- Estruturar templates com herança
- Configurar o Django para encontrar os templates
- Usar template tags e blocos
- Organizar templates de forma profissional
