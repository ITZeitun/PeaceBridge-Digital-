from django.shortcuts import render

def index(request):
    return render(request, 'Peaceapp/index.html')  # include the app folder

def register_view(request):
    from django.contrib.auth.forms import UserCreationForm
    from django.shortcuts import redirect

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'Peaceapp/register.html', {'form': form})

