# 🐍 Medius Tech Pvt Ltd DevTest Repository

Welcome to the Themedius Backend repository! This repository contains the Python Django code for our backend application, powering the endpoints:

- [devtest.themedius.ai](https://devtest.themedius.ai)


It's designed to provide a solid foundation for building robust and scalable web applications.

## Table of Contents
- [📋 Overview](#overview)
- [🚀 Features](#features)
- [⚙️ Setup](#setup)
- [📝 API Documentation](#api-documentation)
- [🤝 Contributing](#contributing)
- [📄 License](#license)

## 📋 Overview

The Themedius Backend is a Python Django application that serves as the backbone for our services. It includes various features and endpoints to support the functionalities of:

- [devtest.themedius.ai](https://devtest.themedius.ai): Endpoint for general API functionalities.


## 🚀 Features

- **User Authentication:** Secure user authentication system.
- **API Endpoints:** Well-defined endpoints for handling general API requests.
- **Campaign Management:** Functionality to create, update, and track campaigns.

## ⚙️ Setup

To set up the Themedius Backend locally, follow these steps:

1. Clone this repository to your local machine.
2. Python Version: 3.10
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv enven
   source enven/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt

4. Apply migrations and create the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Run the development server:
   ```bash
   python manage.py runserver

## 📝 API Documentation

Detailed API documentation for each endpoint is available in the API Documentation file. Please refer to this documentation for information on request and response formats, authentication, and usage examples.

## 🤝 Contributing

We welcome contributions from the Themedius team. If you find issues or have improvements to suggest, please follow our [contribution guidelines](CONTRIBUTING.md).

## 📄 License

This repository is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.
