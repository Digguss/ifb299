from django.shortcuts import render, redirect
from resetpassword.forms import resetpasswordform
from django.contrib.auth.models import User
# Create your views here.






def resetpasswordpage(request):
    if request.user.is_authenticated:
        return redirect('/welcome/')
    if request.method == 'POST':
        form = resetpasswordform(request.POST)
        usernamefield = form.data['username']
        emailfield = form.data['email']
        if (User.objects.filter(username=usernamefield).exists()):
            user1 = User.objects.get(username=usernamefield)
            if (user1.email == emailfield):
                user1.set_password('abc123')
                user1.save()
                return redirect('/resetpassword/success/')
    else:
        form = resetpasswordform()
    return render (request, 'resetpasswordpage.html', {'form' : form})

def resetsuccesspage(request):
    return render (request, 'resetsuccesspage.html')
