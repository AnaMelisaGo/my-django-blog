from django.db import models
from django.contri.auto.models import User
from cloudinary.models import cloudinaryField


STATUS = ((0, 'draft'), (1, 'published'))
