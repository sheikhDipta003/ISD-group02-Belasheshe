# Old Age Home Management

Welcome to the Old Age Home Management Project! This is a Django web project for providing medical care and assistance along with the oportunity to engage in a community and ensuring means of entertainment for the elderly.

## Getting Started

These instructions will help you set up the project on your local machine and collaborate using GitHub.

### Prerequisites

- Python 3.x
- Django (Install using `pip install django`)
- Verify Django version (Install using `python -m django --version`)
- Git (Download and install from https://git-scm.com/)

### Contribute to the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/sheikhDipta003/Bela-Sheshe.git
    ```
2. Naviagate to the project folder
    ```bash
    cd belasheshe
    ```
3. Open command prompt or powershell and run the command
    ```bash
    python manage.py runserver
    ```
4. Access the project in your browser at http://localhost:8000/nurse/dashboard and http://localhost:8000/doctors/dashboard
5. To modify templates, styles, and scripts, edit the appropriate files in the templates and static directories. To modify views, edit doctors/views.py and nurse/views.py
6. Edit doctors/models.py and nurse/models.py to create and database tables.
7. Apply the database changes
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
8. Create superuser or admin
    ```bash
    python manage.py createsuperuser
    ```
6. For more information about Django, visit the official documentation: https://docs.djangoproject.com/
9. [Collaborating on GitHub](https://youtu.be/MnUd31TvBoU)
10. [The Ultimate Github Collaboration Guide](https://medium.com/@jonathanmines/the-ultimate-github-collaboration-guide-df816e98fb67)