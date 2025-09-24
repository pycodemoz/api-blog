#!/usr/bin/env python
import os
import sys
import django

# Configurar Django (substitua 'seu_projeto' pelo nome real do seu projeto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Substitua 'core' pelo nome do seu projeto
django.setup()

def create_superuser():
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
    
    print("=== CREATING SUPERUSER ===")
    print(f"Username provided: {bool(username)}")
    print(f"Email provided: {bool(email)}")
    print(f"Password provided: {bool(password)}")
    
    if not all([username, email, password]):
        print("❌ Missing environment variables")
        sys.exit(1)
    
    try:
        # Deletar se existir
        if User.objects.filter(username=username).exists():
            print(f"Deleting existing user: {username}")
            User.objects.filter(username=username).delete()
        
        # Criar novo
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        
        print(f"✅ Superuser '{username}' created successfully!")
        print(f"   Active: {user.is_active}")
        print(f"   Staff: {user.is_staff}")
        print(f"   Superuser: {user.is_superuser}")
        
        # Teste de autenticação
        from django.contrib.auth import authenticate
        auth_test = authenticate(username=username, password=password)
        print(f"   Auth test: {'✅ PASSED' if auth_test else '❌ FAILED'}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating superuser: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = create_superuser()
    sys.exit(0 if success else 1)