from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def login(request):
	print request.method
	if request.method == "POST":
		input_email = request.POST['email']
		input_pwd = request.POST['pwd']
		if input_email == 'lei@qq.com' and input_pwd == "123":
			from django.shortcuts import redirect
			return redirect("http://www.baidu.com")
		else:
			return render(request, 'login.html',{'status':'ERROR Incorrect username or password'})

	return render(request,'login.html')

def son(request):
	return render(request,'son1.html')

def home(request):
	#return HttpResponse('ok')
	dic = {'name':'alex','age':'20','user_list':['alex','eric','haha']}
	return render(request,'home.html',dic)
