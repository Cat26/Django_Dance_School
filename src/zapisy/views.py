from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Zapisy
from .forms import ZapisyForm

# Create your views here.

def zapisy_home(request):
    if not request.user.is_authenticated():
        zapisy_user = Zapisy.objects.filter(user=request.user)
    return render(request, "zapisy/list.html", {})

def zapisy_create(request):
    form = ZapisyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,

    }
    return render(request, "zapisy/form.html", context)

def zapisy_detail(request, id=None):
    instance = get_object_or_404(Zapisy, id=id)
    context = {
        "instance": instance,
    }
    return render(request, "zapisy/detail.html", context)


def zapisy_list(request):
    queryset_list = Zapisy.objects.all()#.order_by("")
    paginator = Paginator(queryset_list, 6)  # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
            "object_list": queryset,
            "title": "List",
            "page_request_var": page_request_var
         }

    return render(request, "zapisy/list.html", context)


def zapisy_update(request, id=None):
    instance = get_object_or_404(Zapisy, id=id)
    form = ZapisyForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Item Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, "zapisy/form.html", context)


def zapisy_delete(request, id=None):
    instance = get_object_or_404(Zapisy, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("zajecia:list")
    context = {
        "title": "Delete"
    }
    return render(request, "list.html", context)
