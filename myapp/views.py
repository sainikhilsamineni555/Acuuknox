from django.shortcuts import render

# Create your views here.
import threading
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid

"""def create_user():
    print(f"Creating user at {now()} in thread {threading.get_ident()}")
    User.objects.create(username="test_user")
    print(f"User created at {now()}")
"""

def create_user():
    unique_username = f"test_user_{uuid.uuid4().hex[:6]}"  # Generate a unique username
    print(f"Creating user at {now()} in thread {threading.get_ident()}")
    User.objects.create(username=unique_username)
    print(f"User created at {now()} with username: {unique_username}")
    
from django.http import HttpResponse
from .models import Profile

def create_user_view(request):
    create_user()
    profile_exists = Profile.objects.filter(user__username="test_user").exists()
    return HttpResponse(f"Profile exists after creation: {profile_exists}")

from django.db import transaction

def create_user_with_rollback():
    try:
        with transaction.atomic():
            print(f"Creating user at {now()} in thread {threading.get_ident()}")
            user = User.objects.create(username="test_user_rollback")
            print(f"User created at {now()}")
            raise Exception("Simulated error, rolling back transaction")
    except Exception as e:
        print(f"Exception occurred: {e}")

def create_user_rollback_view(request):
    create_user_with_rollback()
    profile_exists = Profile.objects.filter(user__username="test_user_rollback").exists()
    return HttpResponse(f"Profile exists after rollback: {profile_exists}")
