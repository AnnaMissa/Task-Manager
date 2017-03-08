from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    MANAGER = "M"
    DEVELOPER = "D"
    ROLES = (
        (MANAGER, "Manager"),
        (DEVELOPER, "Developer"),
    )
    # add role to User Django
    role = models.CharField(max_length=10, choices=ROLES, default=DEVELOPER)

    def __str__(self):
        return self.username


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)  # for sorting projects
    person = models.ManyToManyField(UserProfile, verbose_name='belongs to user')

    class Meta:
        ordering = ('create_date',)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)  # for sorting tasks
    due_date = models.DateField()
    project = models.ForeignKey(Project, verbose_name='refers to project')
    person = models.ForeignKey(UserProfile, verbose_name='belongs to user')

    class Meta:
        ordering = ('create_date',)

    def __str__(self):
        return self.title
