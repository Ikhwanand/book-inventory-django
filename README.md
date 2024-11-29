# Book Inventory Management System

A Django-based web application for managing a book inventory system. This application allows users to perform CRUD operations on books, including managing authors, categories, and book details with image upload functionality.

## Features

- User Authentication (using django-allauth)
  - User registration
  - Login/Logout functionality
  - Password reset capability

- Book Management
  - Add new books with details (title, author, ISBN, etc.)
  - Upload book cover images
  - Edit existing book information
  - Delete books from inventory
  - View detailed book information

- Inventory Features
  - Track book stock levels
  - Manage book categories
  - Track book prices
  - ISBN validation

- Modern UI
  - Responsive design using Bootstrap 5
  - Clean and intuitive interface
  - Image preview functionality
  - Interactive forms with validation

## Technology Stack

- **Backend**: Django 4.2
- **Frontend**: 
  - Bootstrap 5
  - Font Awesome icons
- **Database**: SQLite (default)
- **Authentication**: django-allauth
- **Form Styling**: django-bootstrap5

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd book-inventory-django
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit http://127.0.0.1:8000 in your browser

## Project Structure

```
book-inventory-django/
├── bookstore/              # Project configuration
├── inventory/              # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── forms.py           # Form definitions
│   ├── urls.py            # URL routing
│   └── templates/         # HTML templates
├── templates/             # Global templates
│   ├── base.html         # Base template
│   └── account/          # Authentication templates
├── media/                 # Uploaded files
│   └── books/            # Book images
├── static/               # Static files
├── manage.py             # Django management script
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Usage

1. Register a new account or login with existing credentials
2. Navigate to the book list page
3. Use the "Add New Book" button to create new entries
4. Click on book titles to view details
5. Use the action buttons to edit or delete books
6. Manage inventory through the admin interface

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django documentation
- Bootstrap documentation
- Django-allauth documentation
- Font Awesome icons
