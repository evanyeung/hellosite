from cms.models.pluginmodel import CMSPlugin

from django.db import models

class CommentList(CMSPlugin):
    country = models.CharField(max_length=50)