# Editor Guide

For Editors a [simple guide](https://paulbeck.info/en/portfolio/djangocms-materializecss-manual/) is was written. 

# Setup
 
 To use this app in your djangocms clone or download it and copy it into your django project. 
 
 As with every app, add djangocms-materializecss to your installed apps:
 
 ``` python
 
 INSTALLED_APPS = (
  ...
  'djangocms-materializecss',
  ...
 )
 ```
 
 Migrate:
 
 ```
 python manage.py makemigrations djangocms-materializecss
 python manage.py migrate
 ```
 
 Now the new plugins should be viewable in the cms frontend. 
 
 # Add Basic Templates
 
 If you want to use the basic templates you have to add them to the CMS_TEMPLATES in your settings.py file.
 ``` python
 CMS_TEMPLATES = (
    ...
    ('sidebar.html', 'Sidebar')
    ...
)
```
 
 # Other Settings
 
 If you want to use the base file included in this project simply delete or rename the one created by djangocms.
 
 # License
 
 This project is under MIT license.
 ___
 Greets [Paul Beck](https://www.paulbeck.info)
