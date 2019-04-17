from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Teams(models.Model):

    TEAM_OPTIONS = (
        (1, 'Wicked_Pissahs'),
        (2, 'Cosmonaughties'),
        (3, 'Nutcrackers'),
        (4, 'Harbor_Horrors'),
        (5, 'Boston_Massacre'),
        (6, 'Boston_B_Party'),
        (7, 'Boston_Common')
    )
    name = models.CharField(
        unique=True,
        max_length=150,
        db_index=True,
        choices=TEAM_OPTIONS,
    )

    class Meta:
        db_table = "teams"
    def __str__(self):
        return self.name


class Members (models.Model):

    # Personal Info
    full_name = models.CharField(unique=True, max_length=150, db_index=True)
    derby_name = models.CharField(unique=True, blank=True, max_length=100, db_index=True)
    nickname = models.CharField(unique=True, blank=True, max_length=100)
    derby_number = models.CharField(unique=True, blank=True, max_length=4)

    # Derby Specific Info
    teams = models.ManyToManyField('Teams', through='TeamMember')

    MEMBER_TYPES = (
        (1, 'skater'),
        (2, 'official'),
        (3, 'volunteer'),
    )

    member_type = models.CharField(
        choices=MEMBER_TYPES,
        blank=False,
        max_length=30
    )
    STATUS_TYPES = (
        (1, 'active'),
        (2, 'injury'),
        (3, 'executive_board'),
        (4, 'inactive'),
        (5, 'skills'),
        (6, 'transfer'),
        (7, 'retired'),
        (8, 'no_job_required'),
        (9, 'committee_head')
    )

    status = models.CharField(choices=STATUS_TYPES, max_length=15, blank=False)
    jobs = models.ManyToManyField('Jobs', through='Employment')

    # Contact Info
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    dues_email = models.EmailField(blank=True, unique=True)

    # Emergency Contact Info
    emergency_contact_name = models.CharField(unique=True, max_length=150, null=False)
    emergency_contact_relationship = models.CharField(unique=True, max_length=150, null=False)
    emergency_contact_number = PhoneNumberField(null=False, blank=False, unique=True)

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
    full_name = models.ForeignKey(
        'Members',
        to_field='full_name',
        db_column='full_name',
        related_name='member_name',
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        'Teams',
        to_field='name',
        related_name='membership',
        on_delete=models.CASCADE
    )
    role = MultiSelectField(max_choices=5, choices=ROLES)
    class Meta:
        db_table = 'team_members'
        ordering = ['team', 'full_name']


class Jobs(models.Model):

    class Meta:
        db_table = "jobs"

    name = models.CharField(null=False, unique=True, max_length=150)

    COMMITTEES = (
        (1, 'PR'),
        (2, 'finance'),
        (3, 'membership'),
        (4, 'bout_production'),
        (5, 'merchandise'),
    )

    committee = models.CharField(choices=COMMITTEES, null=True, max_length=50)

    manager = models.ForeignKey(
        'Members',
        to_field='full_name',
        db_column='full_name',
        related_name='member_manager',
        on_delete=models.CASCADE
    )

    time_commitment = models.IntegerField(null=False)
    duties_desc = models.TextField(null=False)


class Employment(models.Model):

    # Through table for jobs x members
    member_name = models.ForeignKey(
        'Members',
        to_field='full_name',
        db_column='full_name',
        related_name='employed_member',
        on_delete=models.CASCADE
    )

    job_name = models.ForeignKey(
        'Jobs',
        to_field='name',
        db_column='name',
        related_name='name_of_job',
        on_delete=models.CASCADE
    )