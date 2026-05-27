# 🍽️ Simple Food Ordering Website

A full-stack food ordering web application built with **Django 5.1** and **SQLite**. It supports user registration/login, product browsing, cart management, favourites, and a separate admin panel for managing the menu and orders.

-----

## 📌 Features

### 👤 User Side

- Register and log in with email & password (session-based auth)
- View and edit profile (name, age, gender, address, profile image)
- Browse available food products with images, descriptions, and prices
- Add items to cart with quantity selection; cart auto-updates totalprice
- View personal cart with all ordered items
- Add products to a personal favourites list (duplicate-safe)
- Logout

### 🛠️ Admin Side

- Separate admin login (`ADMIN` / `admin` — hardcoded credentials)
- Dashboard home
- Add, edit, and delete food products (name, price, quantity, image, description, status)
- View all registered users
- View cart orders

-----

## 🗂️ Project Structure

```
Simple-food-ordering-website-main/
│
├── foodshop/                  # Django project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── foodshopapp/               # Main Django app
│   ├── models.py              # DB models: reg, product, cart, favourite
│   ├── views.py               # All view logic
│   ├── urls.py                # URL routing (21 routes)
│   ├── admin.py
│   ├── migrations/            # 5 migration files
│   ├── templates/             # HTML templates (17 pages)
│   └── static/                # CSS, JS, images, Bootstrap, libs
│
├── media/                     # Uploaded product & profile images
├── db.sqlite3                 # SQLite database (pre-seeded)
└── manage.py
```

-----

## 🧩 Data Models

|Model      |Fields                                                                               |
|-----------|-------------------------------------------------------------------------------------|
|`reg`      |name, age, gender, email (unique), password, image, address                          |
|`product`  |name, price, quantity, image, description, status (Available/Unavailable/Coming Soon)|
|`cart`     |user (FK), product (FK), quantity, totalprice, date_added                            |
|`favourite`|user (FK), product (FK), date_added — unique together                                |

-----

## 🛣️ URL Routes

|URL                     |View             |Description       |
|------------------------|-----------------|------------------|
|`/`                     |`index`          |Landing page      |
|`/registration/`        |`registration`   |User signup       |
|`/login/`               |`login`          |User login        |
|`/logout/`              |`logout`         |Session flush     |
|`/home/`                |`home`           |User home         |
|`/profile/`             |`profile`        |View profile      |
|`/editprofile/`         |`editprofile`    |Edit profile      |
|`/userproductlist/`     |`userproductlist`|Browse menu       |
|`/addtocart/<id>/`      |`addtocart`      |Add item to cart  |
|`/usercartlist/`        |`usercartlist`   |View user cart    |
|`/favourites/`          |`favourites`     |View favourites   |
|`/addtofavourites/<id>/`|`addtofavourites`|Add to favourites |
|`/adminlogin/`          |`adminlogin`     |Admin login       |
|`/adminhome/`           |`adminhome`      |Admin dashboard   |
|`/addproduct/`          |`addproduct`     |Add new product   |
|`/productlist/`         |`productlist`    |Admin product list|
|`/editproduct/<id>/`    |`editproduct`    |Edit product      |
|`/deleteproduct/<id>/`  |`deleteproduct`  |Delete product    |
|`/userlist/`            |`userlist`       |View all users    |
|`/admincartlist/`       |`admincartlist`  |Admin cart view   |

-----

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- pip

### Installation

```bash
# 1. Clone or extract the project
cd Simple-food-ordering-website-main

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install Django
pip install django==5.1.1

# 4. Apply migrations (db.sqlite3 is already included, but run this to be safe)
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

-----

## 🔐 Admin Credentials

The admin login is hardcoded in `views.py`:

|Field   |Value  |
|--------|-------|
|Email   |`ADMIN`|
|Password|`admin`|


> ⚠️ **Do not use this in production.** Replace with Django’s built-in auth system and environment-based secrets.

-----

## 🎨 Frontend Stack

- **Bootstrap 5** (bundled locally)
- **Owl Carousel** — product/testimonial sliders
- **Animate.css + WOW.js** — scroll animations
- **Tempus Dominus** — date/time picker
- **CounterUp + Waypoints** — animated counters
- Custom CSS at `foodshopapp/static/css/style.css`

-----

## ⚠️ Known Limitations

- **Passwords are stored in plain text** — no hashing used
- **Admin credentials are hardcoded** — not production safe
- **No payment gateway** — cart management only, no checkout flow
- **No Django authentication** — uses raw session + custom `reg` model
- `SECRET_KEY` is exposed in `settings.py` — must be moved to environment variables before deployment
- `DEBUG = True` — must be set to `False` in production

-----

## 🔧 Recommended Improvements

- Use Django’s built-in `User` model and `AbstractUser` for auth
- Hash passwords with `make_password` / `check_password`
- Move `SECRET_KEY` and admin credentials to `.env` using `python-decouple`
- Add a checkout/payment flow
- Add order history model
- Deploy with Gunicorn + Nginx, switch to PostgreSQL for production

-----

## 🛠️ Tech Stack

|Layer   |Technology                         |
|--------|-----------------------------------|
|Backend |Django 5.1 (Python 3.12)           |
|Database|SQLite3                            |
|Frontend|HTML, Bootstrap 5, vanilla JS      |
|Media   |Django FileField with `MEDIA_ROOT` |
|Auth    |Custom session-based authentication|

-----

## 📄 License

This project is for educational purposes. No license specified.
