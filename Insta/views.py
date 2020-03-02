from django.views.generic import TemplateView
# Create your views here.
#调用父类
class HelloWorld (TemplateView):
    template_name = 'Test.html'