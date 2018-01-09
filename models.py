from cms.models.pluginmodel import CMSPlugin

from django.db import models

MAX_URL_LENGTH = 150

class Footer(CMSPlugin):
    header = models.CharField(max_length=50, default='')
    text = models.CharField(max_length=150, default='')
    link_header = models.CharField(max_length=50, default='')
    link_url = models.CharField(max_length=50, default='')
    link_text = models.CharField(max_length=50, default='')
    company_name = models.CharField(max_length=50, default='')

class CollectionItem(CMSPlugin):
    img_url = models.CharField(max_length=MAX_URL_LENGTH, default='')
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=50, default='')
    price = models.CharField(max_length=50, default='')

class Column(CMSPlugin):
    s = models.IntegerField(default=12)
    m = models.IntegerField(default=12)
    l = models.IntegerField(default=12)
    classes = models.CharField(max_length=120, null=True, default='')

class Navbar(CMSPlugin):
    company_name = models.CharField(max_length=50, default='')

class Parallax(CMSPlugin):
    img_url = models.CharField(max_length=MAX_URL_LENGTH, default='')

class Slide(CMSPlugin):
    img_url = models.CharField(max_length=MAX_URL_LENGTH, default='')
    tagline = models.CharField(max_length=50, default='')
    slogan = models.CharField(max_length=100, default='')

class SocialMediaBar(CMSPlugin):
    twitter_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')
    yelp_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')
    facebook_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')
    github_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')
    linkedin_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')

