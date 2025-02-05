# Calculator Web App [APP](https://calculator-demo-35a6b599d4cd.herokuapp.com/)

A simple web-based calculator built with Django, deployed on Heroku. The app allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, and exponentiation. It also supports power operations (`x10^x`).

## Features

- Basic arithmetic operations: `+`, `-`, `*`, `/`.
- Exponentiation: `x10^x` (multiplies by 10 raised to the power of `x`).
- Clear screen functionality (`C`).
- Delete last input (`DEL`).
- Responsive design and mobile-friendly layout.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (for styling), and JavaScript (for dynamic functionality)
- **Database**: PostgreSQL (on Heroku)
- **Deployment**: Heroku

## Installation

Follow these steps to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/jibekgupta/Calculator.git
cd Calculator
```

### 2. Install the required dependencies
```bash
pip install -r requirements.txt
```

### 3. Apply database migrations
```bash
python manage.py migrate
```

### 4.Run the development server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser to see the app in action.


## Deployment
The app is deployed on Heroku. You can access the live version at:
https://calculator-demo-35a6b599d4cd.herokuapp.com/

### Steps to deploy on Heroku (if you'd like to deploy your own version):
 1. Install the Heroku CLI.
 2. Log in to Heroku:
    ```bash
    heroku login
    ```

 3. Create a Heroku app:
    ```bash
    heroku create your-app-name
    ```

 4. Push your code to Heroku:
    ```bash
    git push heroku master
    ```
 5. Run the migrations on Heroku:
    ```bash
    heroku run python manage.py migrate
    ```
 6. Open your app in the browser:
    ```bash
    heroku open
    ```



