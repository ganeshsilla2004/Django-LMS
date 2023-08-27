from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, id_no, password, **extra_fields):
        if not id_no:
            raise ValueError('The given id_no must be set')
        
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(id_no=id_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user  
    
    def create_superuser(self, id_no, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(id_no, password, **extra_fields)
    