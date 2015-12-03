from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.list import ListView
from django.http import JsonResponse
from main.models import Dvd
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import string
# Create your views here.


def dvd_list_dbv(request):
    context = {}

    dvd_list = Dvd.objects.all()[:100]

    context['dvd_list'] = dvd_list

    paginator = Paginator(dvd_list, 10)

    page = int(request.GET.get("page", '1'))

    try:
        dvd_list = paginator.page(page)
    except (InvalidPage, EmptyPage):
        dvd_list = paginator.page(paginator.num_pages)

    context['dvd_list'] = dvd_list

    return render_to_response('dvd_list_dbv.html',context, context_instance=RequestContext(request))

class DvdListView(ListView):  
    model = Dvd
    queryset = Dvd.objects.all()[:2000]
    template_name = "dvd_list_cbv.html"
    context_object_name = "dvd_list"
    template_name = "dvd_list_cbv.html"
    paginate_by = 10


def dvd_list_mysql(request):
    context = {}
    dvd_list = Dvd.objects.all()[:2000]
    context['dvd_list'] = dvd_list
    return render_to_response('dvd_list.html', context, context_instance=RequestContext(request))


def dvd_detail_mysql(request, pk):
    context = {}
    dvd= Dvd.objects.get(pk=pk)
    context['dvd'] = dvd
    return render_to_response('dvd_detail.html', context, context_instance=RequestContext(request))

#JSON handlebars
def dvd_search(request):
    context = {}
    api_dict = {}
    page = int(request.GET.get("page", '1'))
    search_term = request.GET.get('search_term', '')
    print search_term
    dvds = Dvd.objects.filter(title__istartswith=search_term)[:200]

    paginator = Paginator(dvds, 10)

    try:
        dvds = paginator.page(page)
    except (InvalidPage, EmptyPage):
        dvds = paginator.page(paginator.num_pages)  

    #setting pagination display variables
    try:
        api_dict['next_page'] = dvds.next_page_number()
    except:
        pass

    try:
        api_dict['previous_page'] = dvds.previous_page_number()
    except:
        pass

    api_dict['current_page'] = dvds.number

    api_dict['all_pages'] = dvds.paginator.num_pages
    dvd_list = []
    
    for dvd in dvds:
        dvd_list.append({'title' : dvd.title,
        'pk': dvd.pk,
        })

    api_dict['dvds'] = dvd_list

    api_dict['letters'] = list(string.ascii_uppercase)

    api_dict['digits'] = list(string.digits)

    api_dict['punctuation'] = ['!', '#', '$', "'", '*', '+', '.', ':', '>', '@', '[']

    return JsonResponse(api_dict)


#JSON handlebars
def dvd_list(request):
    context = {}
    api_dict = {}

    letter = request.GET.get('letter', 'A')
    #pagination
    
    page = int(request.GET.get("page", '1'))

    dvds = Dvd.objects.filter(title__istartswith=letter)

    print page 

    paginator = Paginator(dvds, 10)

    try:
        dvds = paginator.page(page)
    except (InvalidPage, EmptyPage):
        dvds = paginator.page(paginator.num_pages)  

    #setting pagination display variables
    try:
        api_dict['next_page'] = dvds.next_page_number()
    except:
        pass

    try:
        api_dict['previous_page'] = dvds.previous_page_number()
    except:
        pass

    api_dict['current_page'] = dvds.number

    api_dict['all_pages'] = dvds.paginator.num_pages

    #setting dvd_list
    dvd_list = []
    for dvd in dvds:
        dvd_list.append({'title' : dvd.title,
        'pk': dvd.pk,
        })

    api_dict['dvds'] = dvd_list


    #directory
    api_dict['letters'] = list(string.ascii_uppercase)

    api_dict['digits'] = list(string.digits)

    api_dict['punctuation'] = ['!', '#', '$', "'", '*', '+', '.', ':', '>', '@', '[']

    return JsonResponse(api_dict)

#JSON
def dvd_detail(request, pk):
    dvd = Dvd.objects.get(pk=pk)

    dvd_dict = {'title' : dvd.title,
    'pk': dvd.pk,
    'dvd_id': dvd.dvd_id,
    'studio' : dvd.studio.studio,
    'released': dvd.released,
    'status': dvd.status,
    'sound': dvd.sound,
    'versions': dvd.versions,
    'price': dvd.price,
    'rating': dvd.rating,
    'year': dvd.year,
    'genre': dvd.genre.genre,
    'aspect': dvd.aspect,
    'upc': dvd.upc,
    'dvd_release_date': dvd.dvd_release_date,
    'timestamp': dvd.timestamp
    }

    return JsonResponse(dvd_dict)


def dvd_directory(request):

    dvds = Dvd.objects.all()[:100]

    api_dict = {}

    dvd_list = []

    api_dict['letters'] = list(string.ascii_uppercase)

    api_dict['digits'] = list(string.digits)

    api_dict['punctuation'] = list(string.punctuation)

    return JsonResponse(api_dict)


def dvd_direct(request, char):

    dvds = Dvd.objects.filter(title__startswith=char)[:30]

    api_dict = {}

    dvd_list = []

    api_dict['dvds'] = dvd_list

    for dvd in dvds:
        dvd_list.append({'title' : dvd.title,
        'pk': dvd.pk,
        'dvd_id': dvd.dvd_id,
        'studio' : dvd.studio,
        'released': dvd.released,
        'status': dvd.status,
        'sound': dvd.sound,
        'versions': dvd.versions,
        'price': dvd.price,
        'rating': dvd.rating,
        'year': dvd.year,
        'genre': dvd.genre,
        'aspect': dvd.aspect,
        'upc': dvd.upc,
        'dvd_release_date': dvd.dvd_release_date,
        'timestamp': dvd.timestamp
        })


    return JsonResponse(api_dict)