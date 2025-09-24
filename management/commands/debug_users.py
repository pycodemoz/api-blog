# management/commands/debug_users.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Debug user creation and environment variables'

    def handle(self, *args, **options):
        # Verificar variáveis de ambiente
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL') 
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        
        self.stdout.write("=== ENVIRONMENT VARIABLES ===")
        self.stdout.write(f'USERNAME: {username}')
        self.stdout.write(f'EMAIL: {email}')
        self.stdout.write(f'PASSWORD: {"*" * len(password) if password else "NOT SET"}')
        
        # Verificar usuários existentes
        self.stdout.write("\n=== EXISTING USERS ===")
        users = User.objects.all()
        self.stdout.write(f'Total users in database: {users.count()}')
        
        for user in users:
            self.stdout.write(
                f'Username: {user.username} | Email: {user.email} | '
                f'Staff: {user.is_staff} | Superuser: {user.is_superuser} | '
                f'Active: {user.is_active}'
            )
        
        # Tentar criar superusuário se não existir
        if username and email and password:
            if not User.objects.filter(username=username).exists():
                try:
                    user = User.objects.create_superuser(
                        username=username,
                        email=email,
                        password=password
                    )
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ Superuser {username} created successfully!')
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'✗ Error creating superuser: {e}')
                    )
            else:
                self.stdout.write(
                    self.style.WARNING(f'User {username} already exists')
                )
        else:
            self.stdout.write(
                self.style.ERROR('✗ Missing environment variables for superuser creation')
            )