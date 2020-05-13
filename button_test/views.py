from django.shortcuts import render
from django.contrib import messages
from .forms import AppleIdForm
from .models import AppleId


def add(request):
	if request.method == 'POST':
		form = AppleIdForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			try:
				AppleId.objects.get(apple_id=cd['apple_id'])
				messages.error(request, 'Пользователь с Apple Id - {} уже есть в базе.'.format(cd['apple_id']))
				return render(request, 'button_test/add.html', {'form': form})
			except:
				data = AppleId(apple_id=cd['apple_id'], first_name=cd['first_name'], last_name=cd['last_name'])
				data.save()
				messages.success(request, 'Спасибо, Ваши данные успешно сохранены.')
				return render(request, 'button_test/add.html', {'form': form})
	else:
		form = AppleIdForm()
		return render(request, 'button_test/add.html', {'form': form})

