from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, ProductReview

REVIEW_CHOICES = [('1' ,'1' ), ('2' ,'2' ), ('3' ,'3' ), ('4' ,'4' ), ('5' ,'5' )]

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'birth_date', 'avatar')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        
class ProductReviewForm(forms.ModelForm): 
    class Meta:
        model = ProductReview
        fields = [ 'title', 'content', 'rating' ]
        widgets = {
            'title': forms.TextInput(attrs={
               'class' : 'form-control shadow px-2',
               'placeholder' : 'Title of the review'
            }),
            'content' : forms.Textarea(attrs={
                    'class' : 'form-control shadow px-2' ,
                    'rows' : 6,
                    'placeholder' : 'Write your review here...'
                }
            ),
            'rating' : forms.RadioSelect(choices=REVIEW_CHOICES, attrs={'class' : 'd-none'})
              }