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

