from django.contrib import admin
from api import models

admin.site.register([
    models.Tag,
    models.Problem,
    models.UploadTC,
    models.Submission
])
