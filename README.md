# ERP System for Discrete Manufacturing Companies

## Follow instructions to run the application on your PC

## Requirements
- Python 3.10 
- MySQL

### Setup

To run this project, you need to have Python 3.10 installed on your computer. open a command prompt window, then follow these steps:

1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/ziyanoffl/ERPsystem.git
    cd ERPsystem
    ```
2. Create a virtual environment with the command `python -m venv venv`
3. Activate the virtual environment with the command `venv/Scripts/activate`
4. Install the requirements with the command `pip install -r requirements.txt`
5. Create a `.env` file in the project root and set the necessary environment variables. 
   ```env
    OPENAI_API_KEY=your_openai_key
    SECRET_KEY='django-insecure-^!+b-i-si6ape9v8*+c*nvbn^s#usv(+m&(6@v(5ih+93mpmu@'
   
    #database settings
    DB_NAME=erp_system
    DB_USER=root
    DB_PASSWORD=123456789
    DB_HOST=localhost
    DB_PORT=3306
   ```
6. Create a database in mysql with the name "erp_system"
   ```bash
    mysql -u root -p -e "CREATE DATABASE erp_system"
    ```
7. Import sample data from mysql file to the database
   ```bash
    mysql -u root -p erp_system < erp_system.sql
    ```
8. Apply database migrations:

    ```bash
    python manage.py makemigrations
    ```
   ```bash
    python manage.py migrate
    ```
9. Create a superuser account for the Django admin:

    ```bash
    python manage.py createsuperuser
    ```
10. Run the application with the command `python manage.py runserver`
11. Open your browser and go to `http://127.0.0.1:8000`

# Screenshots

![image](https://github.com/user-attachments/assets/d95dfdbb-3ab6-49ad-9d8d-76abfe0fe833)

![image](https://github.com/user-attachments/assets/1a17f8e7-9d7f-4aa2-8818-5034ef3c029f)

![image](https://github.com/user-attachments/assets/9206858b-dbba-4816-909c-b890b50b1ae7)




