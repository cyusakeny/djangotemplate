from .models import Users
from django.db.models import Q
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password


class CustomAuthentication(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        return "User not found"

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None
