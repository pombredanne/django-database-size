from django.db import models

class StringWithTitle(str):
    """
    String class with a title method. Can be used to override 
    admin app names.

    http://ionelmc.wordpress.com/2011/06/24/custom-app-names-in-the-django-admin/
    """

    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

APP_LABEL = StringWithTitle('database_size', 'Database Size')

class DatabaseSizeTable(models.Model):
    
    id = models.CharField(max_length=1000, primary_key=True)
    schema_name = models.CharField(max_length=500)
    table_name = models.CharField(max_length=500)
    table_owner = models.CharField(max_length=500)
    size_in_bytes = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'database_size_table'
        ordering = ('-size_in_bytes',)
        app_label = APP_LABEL
        verbose_name = 'table'