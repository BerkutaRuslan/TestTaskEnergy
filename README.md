# Test_4_energy

To start this project you have to:

1 - git clone https://github.com/BerkutaRuslan/TestTaskEnergy.git

2 - add venv

3 - add Database

4 - pip install -r requirements.txt

5 - python manage.py migrate

6 - python manage.py runserver ( don't forget to add url before start celery beat )

7 - celery -A ukr_project worker --beat --scheduler django --loglevel=info

Enjoy the project
