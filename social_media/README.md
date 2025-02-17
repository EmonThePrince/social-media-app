# Social Media Application

A simple social media application built with Django by Saim Ahmed Emon (GitHub: emontheprince).

## Features
- User registration and authentication
- Create, read, update, and delete posts
- Global feed showing all posts
- User profile showing only your posts
- Image upload support for posts

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/emontheprince/social-media-app.git
   cd social-media-app
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
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

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000`

## API Endpoints

### Authentication
- POST /login/ - User login
- POST /logout/ - User logout
- POST /register/ - User registration

### Posts
- GET / - List all posts (global feed)
- GET /post/<int:pk>/ - Retrieve a specific post
- POST /post/new/ - Create a new post
- PUT /post/<int:pk>/update/ - Update a post
- DELETE /post/<int:pk>/delete/ - Delete a post

### User Profile
- GET /profile/ - View user's profile and posts

## Testing Credentials
- Admin account:
  - Username: admin
  - Password: admin

- Sample user accounts:
  - Username: user1
  - Password: testpass123
  - Username: user2
  - Password: testpass123

## ER Diagram (Text Representation)

```
+----------------+            +----------------+
|     User       |            |     Post       |
+----------------+            +----------------+
| id             | <--------> | id             |
| username       |            | user_id        |
| password       |            | content        |
| email          |            | image          |
| first_name     |            | created_at     |
| last_name      |            | updated_at     |
| is_staff       |            +----------------+
| is_active      |
| date_joined    |
+----------------+

Relationships:
- A User can have many Posts (one-to-many)
- A Post belongs to one User
```

## Project Details
- **Developer**: Saim Ahmed Emon
- **GitHub**: [emontheprince](https://github.com/emontheprince)
- **Technology Stack**:
  - Backend: Django (Python)
  - Frontend: HTML, CSS, JavaScript
  - Database: SQLite
  - Authentication: Django's built-in authentication system
  - Media Handling: Django's FileField and ImageField

## License
MIT License
