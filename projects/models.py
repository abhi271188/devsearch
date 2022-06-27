from email.policy import default
from tkinter import CASCADE
from django.db import models
from users.models import Profile
import uuid

class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    featured_image = models.ImageField(default = 'default.jpg', null=True, blank = True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    total_vote = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    tag = models.ManyToManyField('Tags', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        # ordering = ['created']
        ordering = ['-vote_ratio', '-total_vote', 'title']
    
    @property
    def getVoteCount(self):
        review_count = self.reviews_set.all()
        totalVote = review_count.count()
        upVote = review_count.filter(value = 'up').count()
        ratio = (upVote / totalVote) * 100

        self.total_vote = totalVote
        self.vote_ratio = ratio
        self.save()

class Reviews(models.Model):
    VOTE_TYPE = (
        ('up', 'upVote'),
        ('down', 'downVote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField()
    value = models.CharField(max_length=20, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    '''To see the uniqueness in reviews in project page'''
    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.value

class Tags(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
