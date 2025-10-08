from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from cryptography.fernet import Fernet
import base64


class User(AbstractUser):
    """Custom user model with optional face recognition data"""
    face_descriptor = models.BinaryField(null=True, blank=True)

    def set_face_data(self, face_data):
        """Encrypt and store face descriptor"""
        if face_data:
            key = settings.FACE_ENCRYPTION_KEY.encode()
            f = Fernet(key)
            encrypted = f.encrypt(face_data.encode())
            self.face_descriptor = encrypted

    def get_face_data(self):
        """Decrypt and return face descriptor"""
        if self.face_descriptor:
            key = settings.FACE_ENCRYPTION_KEY.encode()
            f = Fernet(key)
            decrypted = f.decrypt(self.face_descriptor)
            return decrypted.decode()
        return None

    def delete_face_data(self):
        """Remove face recognition data"""
        self.face_descriptor = None
        self.save()


class DiaryEntry(models.Model):
    """Diary entry model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='diary_entries')
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name_plural = 'Diary Entries'

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.title}"


class LibraryItem(models.Model):
    """Library PDF book model"""
    GENRE_CHOICES = [
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('comics', 'Comics'),
        ('romance', 'Romance'),
        ('fantasy', 'Fantasy'),
        ('mystery', 'Mystery'),
        ('scifi', 'Science Fiction'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='library_items')
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    file = models.FileField(upload_to='library/%Y/%m/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.user.username} - {self.title}"
