from cProfile import label
from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Project, Reviews

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image','description', 'source_link', 'demo_link', 'tag']
        widgets = {
            'tag':forms.CheckboxSelectMultiple(), 
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'input'})
        self.fields['featured_image'].widget.attrs.update({'class':'input'})
        self.fields['description'].widget.attrs.update({'class':'input'})
        self.fields['source_link'].widget.attrs.update({'class':'input'})
        self.fields['demo_link'].widget.attrs.update({'class':'input'})
        '''
        Another way:
        ------------
        for name, field in fields.items():
            field.widget.attrs.update({'class' : 'input'})
        '''

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['value', 'body']
        labels = {
            'value':'Place your vote',
            'body':'Add a comment with your vote '
        }
    
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})

