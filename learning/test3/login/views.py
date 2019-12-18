from django.shortcuts import render,redirect

def index(request):
    uname = request.session.get('myname')
    context = {
        'uname': uname
    }
    return render(request, 'login/index.html', context)

def edit_log(request):
    return render(request, 'login/edit.html')

def action(request):
    name = request.POST.get('uname')
    request.session['myname'] = name
    return redirect('login:index')

def logout(request):
    del request.session['myname']
    return redirect('login:index')