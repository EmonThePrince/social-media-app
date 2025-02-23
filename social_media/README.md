# Social Media Platform

A simple social media platform built with Django that allows users to create, share, and interact with posts.

## Features

- User registration and authentication
- Create, update, and delete posts
- Post filtering by:
  - Text content
  - Media type (text or image)
  - Username
  - Date (newest/oldest first)
- User profile pages
- Responsive design
- Image upload support

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/social-media-platform.git
   cd social-media-platform
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000`

## Project Structure

```
social_media/
├── media/               # Uploaded media files
├── posts/                # Posts app
│   ├── migrations/       # Database migrations
│   ├── templates/        # Post-related templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── social_media/          # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/               # Static files
│   ├── css/
│   ├── images/
│   └── js/
├── templates/            # Base templates
├── manage.py
└── requirements.txt
```

## Technologies Used

- Python 3
- Django
- Bootstrap 5
- SQLite (development)
- HTML5/CSS3
- JavaScript

## License

MIT License
