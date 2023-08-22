# Kazakh National Cuisine Website

## [https://kazakhcuisine.vercel.app](https://kazakhcuisine.vercel.app)

This is a web application for Kazakh National Cuisine, where users can explore traditional Kazakh dishes and recipes.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Kazakh National Cuisine website is a project aimed at promoting the rich culinary heritage of Kazakhstan. It provides users with a collection of traditional Kazakh dishes, along with their ingredients and recipes. The website is built using Django, a powerful web framework for Python.

## Features

- Browse a variety of traditional Kazakh dishes
- View detailed information about each dish, including its ingredients and recipe
- User-friendly and responsive design for seamless experience on different devices
- Contact form for users to get in touch with the website administrators
- Interactive photo gallery showcasing images of delicious dishes

## Technologies Used

- Django
- HTML
- CSS
- JavaScript
- Bootstrap
- Gunicorn (WSGI server)
- Render (Cloud platform for deployment)

## Installation

To run the Kazakh National Cuisine website locally on your machine, follow these steps:

1. Clone the repository:

```
git clone https://github.com/yourusername/kazakh-national-cuisine.git
cd kazakh-national-cuisine
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Apply database migrations:

```
python manage.py migrate
```

4. Create a superuser to access the Django admin panel:

```
python manage.py createsuperuser
```

5. Run the development server:

```
python manage.py runserver
```

6. Open your web browser and go to `http://127.0.0.1:8000/` to access the website.

## Usage

- To view the list of dishes, go to the homepage.
- Click on a dish to view its detailed information, including ingredients and recipe.
- Use the navigation menu to explore other sections of the website, such as About and Contact.
- Use the Contact page to send inquiries and feedback to the website administrators.

## Contributing

Contributions are welcome! If you find any bugs or want to add new features, feel free to create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
