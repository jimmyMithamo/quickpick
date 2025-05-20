# QuickPick - E-commerce Web Application

QuickPick is a Django-based e-commerce web application designed to provide a smooth and efficient online shopping experience. The platform supports product browsing, shopping cart management, and order processing, making it easy for users to find and purchase products.

## Features

- User-friendly product catalog with categories and search functionality
- Product detail pages with images and descriptions
- Shopping cart management
- User registration and authentication
- Order checkout and management
- Responsive design for mobile and desktop

## Technologies Used

### Backend
- Python 3.x
- Django framework
- SQLite (default, can be switched to PostgreSQL or others)

### Frontend
- HTML5, CSS3, JavaScript
- Bootstrap for responsive design

### Other
- `requirements.txt` for Python dependencies
- Static and media file handling with Django

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- (Optional) virtualenv or venv for isolated environment

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jimmyMithamo/quickpick.git
   cd quickpick

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (admin account):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- Browse products, add items to your cart, and proceed to checkout.
- Admin users can manage products, categories, and orders via the Django admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue or contact the maintainer at j1mithamo@gmail.com.