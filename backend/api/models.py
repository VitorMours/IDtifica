from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid

class CustomUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError("O email é obrigatório")
        
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
        
    if password:
      user.set_password(password)
    else:
      user.set_password(self.make_random_password())
        
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)
    
    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superusuário deve ter is_staff=True')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superusuário deve ter is_superuser=True')
    
    return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
  """
  Modelo de usuario personalizado para o sistema 
  """  
  username = None

  STATE_CHOICES = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
  ]

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  first_name = models.CharField(_('first name'), max_length=50, blank=False, null=False)
  last_name = models.CharField( _('last name'), max_length=50, blank=False, null=False)
  email = models.EmailField( _('email address'), unique=True, blank=False, null=False)
  birthday = models.DateField(_('birthday'), null=True, blank=True)
  phone = models.CharField(_('phone number'), max_length=20, blank=True, null=True)
  city = models.CharField(_('city'), max_length=100, blank=True, null=True)
  state = models.CharField(_('state'), max_length=2, blank=True, null=True, choices=STATE_CHOICES)
  created_at = models.DateTimeField(_('created at'), auto_now_add=True)
  updated_at = models.DateTimeField(_('updated at'), auto_now=True)
      
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  objects = CustomUserManager()

  class Meta:
    verbose_name = _("user")
    verbose_name_plural = _("users")
    ordering = ['-created_at']


  def get_full_name(self) -> str:
    return f"{self.first_name} {self.last_name}"

  def __str__(self):
    return self.email