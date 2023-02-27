from django.db import models


class LandingPages(models.Model):
    title = models.CharField(
        max_length=100
        )
    slug = models.SlugField(
        max_length=100, 
        unique=True
        )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='criado em'
        )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='atualizado em'
        )
    
    class Meta:
        verbose_name = 'Landing Page'
        verbose_name_plural = 'Landing Pages'

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(
        max_length=100
        )
    slug = models.SlugField(
        max_length=100, 
        unique=True
        )
    active = models.BooleanField(
        default=True
        )
    landing_page = models.ForeignKey(
        LandingPages, 
        on_delete=models.PROTECT, 
        related_name='events'
        )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='criado em'
        )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='atualizado em'
        )
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    
    def __str__(self):
        return self.name
    
class UserRegistration(models.Model):
    name = models.CharField(
        max_length=100
        )
    email = models.EmailField(
        max_length=100
        )
    props = models.JSONField(
        null=True,
        blank=True
        )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='criado em'
        )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='atualizado em'
        )
    
    class Meta:
        verbose_name = 'Inscrição de Usuário'
        verbose_name_plural = 'Inscrições de Usuários'
    
    def __str__(self):
        return self.name