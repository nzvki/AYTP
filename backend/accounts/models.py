from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must provide an email address!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        # Hashed passwords
        user.set_password(password)
        # user.save(using=self._db) => Use this if the application will be used with more than one db
        user.save()
        return user
    
    # Creating super user
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user
        
# User model
class UserAccount(AbstractBaseUser, PermissionsMixin):
    # Db model for the users
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # User account manager
    objects =  UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email

    
class Schools(models.model)
    # Db model for the schools created by admin for school owners
    school_name = models.CharField(max_length=254)
    reg_number = models.CharField(max_length=254)
    owned_by = models.CharField(max_length=254)
    
class Courses(models.model)
    # Db model for the courses created by the tutors for the students
    course_name = models.CharField(max_length=254)


class Lecturer(models.model)
    # Db model for the lecturers created by the school owner for tutors
    tutor_name = models.CharField(max_length=254)
    idnumber = = models.IntegerField()
    subject = models.CharField(max_length=254)
    


class Students(models.model)
    # Db model for the students
    student_name = models.CharField(max_length=254)
    id_num = models.CharField(max_length=254)
