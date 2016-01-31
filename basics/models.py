from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


MAX_TITLE_LENGTH = 200
MAX_TEXT_LENGTH = 1000
MAX_CODE_LENGTH = 1000


class Tag(models.Model):
    text = models.CharField(max_length=MAX_TITLE_LENGTH)

    def __str__(self):
        return self.text

class Comment(models.Model):
    text = models.CharField(max_length=MAX_TEXT_LENGTH)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mod_time = models.DateTimeField('time last modified')
    parent = models.ForeignKey('self', null=True, blank=True) # whether this feed is a follow-up feed


class Question(models.Model):
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    description = models.CharField(max_length=MAX_TEXT_LENGTH)
    init_time = models.DateTimeField('time created')
    mod_time = models.DateTimeField('time last modified')
    status = models.BooleanField() # whether it has been reviewed by staff member
    starting_code = models.CharField(max_length=MAX_CODE_LENGTH, null=True)
    # Where we want to insert the answer back to the code
    answer_index = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(MAX_CODE_LENGTH)], null=True)
    tag = models.ManyToManyField(Tag)
    author = models.ManyToManyField(User)

    def save(self, *args, **kwargs):
        self.mod_date = datetime.now();
        super(Notebook, self).save(*args, **kwargs);

    def __str__(self):
        return self.title

# In case we want multiple choice questions
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=MAX_TEXT_LENGTH)
    correctness = models.NullBooleanField()
    comment = models.ManyToManyField(Comment)
    user_history = models.ManyToManyField(User)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=MAX_TEXT_LENGTH)
    correctness = models.NullBooleanField()
    mod_time = models.DateTimeField('time last modified')
    comment = models.ManyToManyField(Comment)
    vote = models.IntegerField()
    contributer = models.ManyToManyField(User)




class UserProfile(models.Model):
    realname = models.CharField(max_length=MAX_TITLE_LENGTH)
    user = models.OneToOneField(User)
    avatar_url = models.URLField(default='', blank=True)
    reputation = models.IntegerField(validators=[MinValueValidator(0),])

    def __str__(self):
        return self.user.username


class Class(models.Model):
    name = models.CharField(max_length=MAX_TITLE_LENGTH)
    question = models.ManyToManyField(Question)
    instructor = models.ManyToManyField(User, related_name="instructors")
    student = models.ManyToManyField(User, related_name="students")
