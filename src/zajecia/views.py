from django.shortcuts import render
from django.views.generic import ListView
from .models import Zajecia
from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404
# Create your views here.


class ZajeciaListView(ListView):
    queryset = Zajecia.objects.all()
    template_name = "zajecia/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZajeciaListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context



def zajecia_list_view(request):
    queryset = Zajecia.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, "zajecia/list.html", context)


class ZajeciaDetailView(DetailView):
    queryset = Zajecia.objects.all()
    template_name = "zajecia/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZajeciaDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def zajecia_detail_view(request, pk=None, *args, **kwargs):
    instance =get_object_or_404(Zajecia, pk=pk)# jak pk istnieje zwraca detail jak nie error
    context = {
        'object': instance,
    }
    return render(request, "zajecia/detail.html", context)