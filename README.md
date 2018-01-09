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
 
 Greets [Paul Beck](paulbeck.info)
