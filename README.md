# Electronic show  Website

A modern website for Electronic built with Django, featuring services, industries, and contact management.

## Features

- Responsive modern design
- Services showcase
- Industry solutions
- Contact form
- Admin interface for content management
- Interactive UI elements

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd transline
```

2. Create and activate a virtual environment:
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

```
transline/
├── manage.py
├── requirements.txt
├── README.md
├── transline/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   └── main/
│       ├── home.html
│       ├── about.html
│       ├── contact.html
│       ├── service_detail.html
│       └── industry_detail.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── img/
        ├── hero-image.svg
        ├── about-hero.svg
        ├── benefits.svg
        └── team-*.svg
```

## Admin Interface

1. Visit http://127.0.0.1:8000/admin
2. Log in with your superuser credentials
3. Manage services, industries, and contact submissions

## Customization

1. Edit templates in the `templates/` directory
2. Modify styles in `static/css/style.css`
3. Update JavaScript functionality in `static/js/main.js`
4. Add/modify models in `main/models.py`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Contributing
Anil kumar

