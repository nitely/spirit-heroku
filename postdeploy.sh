python manage.py migrate
python manage.py createcachetable
echo "import os; from django.contrib.auth.models import User; User.objects.create_superuser(os.environ['ADMIN_USERNAME'], os.environ['ADMIN_EMAIL'], os.environ['ADMIN_PASSWORD'])" | ./manage.py shell
