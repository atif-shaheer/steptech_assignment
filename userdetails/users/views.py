from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import User

def users_table(request):
    if request.method == 'POST':
        # Insert data into the database
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        user = User(name=name, email=email, role=role)
        user.save()
        return HttpResponse('User Inserted Successfully!')

    else:
        # Retrieve data from the database
        users = User.objects.all()
        return render(request, 'users_table.html', {'users': users})


def user_details(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_details.html', {'user': user})