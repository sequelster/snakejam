from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Teams(models.Model):
    name = models.CharField(unique=True, max_length=150, db_index=True)

    class Meta:
        db_table = "teams"
    def __str__(self):
        return self.name

class Members (models.Model):
    full_name = models.CharField(unique=True, max_length=150, db_index=True)
    derby_name = models.CharField(unique=True, null=True, blank=True, max_length=100, db_index=True)
    teams = models.ManyToManyField('Teams', through='TeamMember')

    class Meta:
        db_table = "members"

    def __str__(self):
        return self.full_name

class TeamMember(models.Model):
    ROLES = (
        (1, 'pivot'),
        (2, 'jammer'),
        (3, 'blocker'),
        (4, 'coach'),
        (5, 'captain'))
    full_name = models.ForeignKey('Members', to_field='full_name', db_column='full_name', related_name='member_name', on_delete=models.CASCADE)
    team = models.ForeignKey('Teams', to_field='name', related_name='membership', on_delete=models.CASCADE)
    role = MultiSelectField(max_length=5, max_choices=5, choices=ROLES)
    class Meta:
        db_table = 'team_members'
        ordering = ['team', 'full_name']