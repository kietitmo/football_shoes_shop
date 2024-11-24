from django.db import models
import uuid
from django.utils.timezone import now, timedelta
from users.models import User

def expires_time():
    return now() + timedelta(hours=24)

class EmailVerificationToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="email_verification_token")
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=expires_time)

    def is_valid(self):
        return now() < self.expires_at
