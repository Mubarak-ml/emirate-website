from django.forms import ModelForm
from .models import News
from django.contrib.auth.models import User


class NewsForm(ModelForm):
	class Meta:
		model = News
		fields = '__all__'
		#exclude =['host', 'participant']
		

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']