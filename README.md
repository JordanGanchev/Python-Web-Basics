# python-web-basics

Check PYTHONPATH

Ensure your Python environment is pointing to the correct paths:

python -c "import sys; print(sys.path)"

Verify that the path to your virtual environment or project directory is included.


Common Mistake: Missing Virtual Environment

If no virtual environment is set up, create one and install dependencies:

----------------------------------------------------------------------

    Create a virtual environment:

python -m venv venv

Activate the virtual environment:

source venv/bin/activate

Install Django:

pip install django

Run the server:

python manage.py runserver
