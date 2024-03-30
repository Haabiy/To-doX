**To-doX Overview**

This project delves into the fundamental aspects of Django framework, offering a comprehensive exploration of its core components. 

1. `Django Basics:` 

    - Get into the foundational elements of Django, dissecting models, views, and templates. Establish a robust architectural framework for web applications, leveraging the Model-View-Controller (MVC) pattern to segregate concerns effectively.

2. `Database Management:` 

    - Master database interaction with Django's built-in Object-Relational Mapping (ORM) layer. Navigate database migrations seamlessly, executed data queries proficiently, and established optimized model relationships to ensure application scalability.

3. `CRUD Operations:` 

    - Acquire proficiency in the fundamental CRUD operations (Create, Read, Update, Delete), and learn to implement them seamlessly with models and objects within Django applications.

4. `Integration of Static Files:` 

    - Elevate web application quality by seamlessly integrating CSS and JavaScript files, enhancing styling and interactivity.

5. `User Registration and Authentication:` 

    - Implement robust user authentication and authorization systems to strengthen Django applications' security posture. Learn to manage user registration, facilitate seamless login/logout functionality, and safeguard sensitive user data effectively.

6. `Form Handling:` 

    - Cultivate expertise in constructing and handling forms within Django applications, facilitating smooth user data input and interaction.

## Creating a Virtual Environment
1. Open Terminal.

2. Navigate to your project directory.

3. Run the following command to create a virtual environment named `myenv`:
    ```bash
    python3 -m venv myenv
    ```

## Activating the Virtual Environment
1. Open Terminal.

2. Navigate to your project directory if you're not already there.

3. Run the following command to activate the virtual environment:
    ```bash
    source myenv/bin/activate
    ```

## Deactivating the Virtual Environment
1. If the virtual environment `myenv` is currently activated, run the following command to deactivate it:
    ```bash
    deactivate
    ```

## Installing Dependencies from requirements.txt
1. Make sure the virtual environment `myenv` is activated.

2. Navigate to your project directory.

3. Run the following command to install dependencies from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

   Replace `requirements.txt` with the actual filename if it's different in your project.

## Project Structure
```
├── db.sqlite3
├── manage.py
├── media
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── app.js
├── todo
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── todoApp
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    ├── models.py
    ├── templates
    │   └── todoApp
    │       ├── create.html
    │       ├── dashboard.html
    │       ├── delete.html
    │       ├── delete_account.html
    │       ├── index.html
    │       ├── my_login.html
    │       ├── navbar.html
    │       ├── profile_management.html
    │       ├── read.html
    │       ├── register.html
    │       ├── reset_password.html
    │       ├── reset_password_complete.html
    │       ├── reset_password_form.html
    │       ├── reset_password_sent.html
    │       └── update.html
    ├── tests.py
    ├── urls.py
    └── views.py

```

### Prerequisites
Make sure you have Python 3.x installed on your system. If not, you can download and install it from [Python's official website](https://www.python.org/downloads/).

### Steps to Run the Application
1. **Clone the Repository:**
   ```
   git clone https://github.com/Haabiy/To-doX.git
   ```
2. **Activate the virtual environment**
   ```
   source myenv/bin/activate
   ```
3. **Install Dependencies:**
   Before running the server, make sure to install the required dependencies. You can install them using pip:
   ```
   pip install -r requirements.txt
   ```
4. **Navigate to the Project Directory:**
   ```
   cd todo/
   ```
5. **Run the Server:**
   Once the dependencies are installed, run the Django server using the following command:
   ```
   python3 manage.py runserver
   ```
   This command will start the Django development server.

6. **Access the Application:**
   via `http://localhost:8000` in your web browser.


### AWS S3, RDS, and Redshift Integration (AWS-cloud Branch)

The AWS-cloud branch includes integration with AWS S3 for storage management. Static files and media files are stored on Amazon S3, and the project uses `django-storages` library for handling file storage on AWS S3.

For detailed instructions, please refer to the README.md file in the `AWS-cloud` branch.



