from cms.models.pluginmodel import CMSPlugin

from django.db import models

MAX_URL_LENGTH = 150

class Card(CMSPlugin):
    s = models.IntegerField(default=12, blank=True)
    m = models.IntegerField(default=12, blank=True)
    l = models.IntegerField(default=12, blank=True)
    classes = models.CharField(max_length=120, blank=True, default='')

class CollectionItem(CMSPlugin):
    img_url = models.CharField(max_length=MAX_URL_LENGTH, default='')
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=50, default='')
    price = models.CharField(max_length=50, default='')

class Column(CMSPlugin):
    s = models.IntegerField(default=12, blank=True)
    m = models.IntegerField(default=12, blank=True)
    l = models.IntegerField(default=12, blank=True)
    classes = models.CharField(max_length=120, blank=True, default='')
    center = models.BooleanField(default=False, blank=True)

class ImageCard(CMSPlugin):
    s = models.IntegerField(default=12, blank=True)
    m = models.IntegerField(default=12, blank=True)
    l = models.IntegerField(default=12, blank=True)
    classes = models.CharField(max_length=120, blank=True, default='')
    name = models.CharField(max_length=50, default='')
    text = models.CharField(max_length=250, default='')
    img_url = models.CharField(max_length=MAX_URL_LENGTH, default='')
    link_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')

class Footer(CMSPlugin):
    header = models.CharField(max_length=50, default='')
    text = models.CharField(max_length=150, default='')
    link_header = models.CharField(max_length=50, default='')
    link_url = models.CharField(max_length=50, default='')
    link_text = models.CharField(max_length=50, default='')
    company_name = models.CharField(max_length=50, default='')


class Navbar(CMSPlugin):
    company_name = models.CharField(max_length=50, default='')
    fixed = models.BooleanField(default='False')

class Parallax(CMSPlugin):
    img_url = models.CharField(max_length=MAX_URL_LENGTH, default='')
    headline = models.CharField(max_length=50, blank=True, default='')

class Sidebar(CMSPlugin):
    img_url = models.CharField(max_length=MAX_URL_LENGTH, default='', blank=True)

class Slide(CMSPlugin):
    img_url = models.CharField(max_length=MAX_URL_LENGTH, default='')
    tagline = models.CharField(max_length=50, default='')
    slogan = models.CharField(max_length=100, default='')
    link_url = models.CharField(max_length=MAX_URL_LENGTH, default='')

class Slider(CMSPlugin):
    fullscreen = models.BooleanField(default='False')

class SocialMediaBar(CMSPlugin):
    twitter_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')
    yelp_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')
    facebook_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')
    github_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')
    linkedin_url = models.CharField(max_length=MAX_URL_LENGTH, blank=True, default='')

