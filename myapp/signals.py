from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.timezone import now
from myapp.models import Profile  

# Signal receiver that creates a Profile instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print(f"Signal received, creating profile for user: {instance.username} at {now()}")
        Profile.objects.create(user=instance, bio="This is a test profile.")

# Function to simulate transaction rollback
def create_user_and_rollback():
    try:
        with transaction.atomic():
            print(f"Creating user at {now()}")
            user = User.objects.create(username="test_user")
            print(f"User created at {now()}")
            raise Exception("Simulating an error, rolling back transaction")
    except Exception as e:
        print(f"Exception occurred: {e}")

# Checking if profile creation is rolled back with the transaction
create_user_and_rollback()

# Check if Profile was created after the rollback
profile_exists = Profile.objects.filter(user__username="test_user").exists()
print(f"Profile exists after rollback: {profile_exists}")
