from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):
        """ ...  """
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        other_fields.setdefault('is_restaurant', True)      # можно потом удалить
        other_fields.setdefault('is_purchaser', True)       # можно потом удалить
        other_fields.setdefault('is_courier', True)         # можно потом удалить

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)


    def create_user(self, email, user_name, password, **other_fields):
        """ ... """
        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user