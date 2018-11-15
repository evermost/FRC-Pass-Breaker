from django.db import models


class Word(models.Model):
    """
    Used to store the word in a database
    """
    item = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.item


class Status(models.Model):
    """
    Store the status of the server. One object indicates if password has been found and saves that password if so
    """
    id = models.IntegerField(default=0, primary_key=True)
    completed = models.BooleanField(default=False)
    password = models.CharField(max_length=255, default='')

    def __str__(self):
        return str(self.completed)
