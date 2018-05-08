from django.shortcuts import render
from django.views.generic import ListView
from .models import Zapisy

# Create your views here.
class ZapisyListView(ListView):
    queryset = Zapisy.objects.all()
    template_name = "zapisy/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZapisyListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context



def zapisy_list_view(request):
    queryset = Zapisy.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, "zapisy/list.html", context)