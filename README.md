# 🛒 Magazincha.uz  -  E-commerce Web Application
[Magazincha.uz](https://magazincha.uz/)  is a full-stack e-commerce web application built with Django.
It allows users to browse products, add them to cart, and make secure online payments.

## Features
- User regisration & authentication
- Product listing with categories
- Shopping cart functionality
- Secure checkout with PayPal integration
- Order management system
- Admin panel for managing products and orders

## Tech Stack
Backend
- Python 3
- Django
- Django ORM

Frontend
- HTML5
- CSS3
- Bootstrap
- JavaScript (AJAX for dynamic updates)

Database
- PostgreSQL (AWS RDS)

Storage
- AWS S3 (Media files)

Deployment
- AWS Elastic Beanstalk

Payment
- PayPal Payment Gateway

## Architecture Overview
- Django handles backend logic and APIs
- PostgreSQL (RDS) stores relational data
- AWS S3 stores media files (product images)
- Elastic Beanstalk handles deployment and scaling

## Payment Integration
The application uses PayPal to process secure online transactions.
After succesful payment:
- Order is saved to the database
- User receives confirmation

## Deployment
The project is deployed on AWS Elastic Beanstalk.
Services used:
- Elastic Beanstalk
- RDS (PostgreSQL)
- S3 Bucket

## Installation (Local Setup)
Clone repository
`git clone https://github.com/your-username/magazincha.git`

Go to project directory
`cd magazincha`

Create virtual environment
`python -m venv venv`

Activate environment
- `source venv/bin/activate` -  Linux/macOS
- `venv\Scripts\activate` -  Windows

Install dependencies
`pip install -r requirements.txt`

Run migrations
`python manage.py migrate`

Run server
`python manage.py runserver`




