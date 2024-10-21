from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image
from .models import Rectangle

def index(request):
    class thumbnail:
        def __init__(self, image):
            self.name = image.name
            self.rectangles = image.rectangles.all()
            for rec in self.rectangles:
                rec.x = rec.x / image.width * 100
                rec.y = rec.y / image.height * 100
                rec.width = rec.width / image.width * 100
                rec.height = rec.height / image.height * 100
            
    params = request.GET.dict()
    page_order = params['order'] if 'order' in params else ''
    page_number = params['page'] if 'page' in params else 1
    if 'tag' in request.POST:
        page_tag = request.POST['tag']
    else:
        page_tag = params['tag'] if 'tag' in params else ''
    print(params)
    
    images_list = Image.objects.all()
    if page_order == 'desc':
        images_list = images_list.order_by('-publication_date')
    elif page_order == 'asc':
        images_list = images_list.order_by('publication_date')
    
    if page_tag != '':
        for image in images_list:
            if not image.containstag(page_tag):
                images_list = images_list.exclude(name=image.name)

    thumbnails = [thumbnail(image) for image in images_list]
    paginator = Paginator(thumbnails, 2)
        
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj,
               'order': page_order,
               'tag': page_tag}
    return render(request, 'images/paginator.html', context)

def image(request, img_name):
    image = Image.objects.get(name=img_name)
    rectangles = image.rectangles.all()
    context = {'image': image,
               'rectangles': rectangles}
    return render(request, 'images/image.html', context)

@login_required
def myimages(request):
    user = request.user
    user_images = Image.objects.filter(authors=user)
    context = {'images_list': user_images, 'user' : user}
    return render(request, 'images/myimages.html', context)

@login_required
def imageedit(request, imagename):
    image = Image.objects.get(name=imagename)
    user = request.user
    rectangles = image.rectangles.all()
    context = {'image': image,
               'gooduser' : image.authors.filter(username=user.username),
               'rectangles': rectangles}
    return render(request,'images/imageedit.html', context)

@login_required
def addrectangle(request, imagename):
    image = Image.objects.get(name=imagename)
    user = request.user
    
    if image.authors.filter(username=user.username).exists():
        rec = Rectangle(picture=image, height=int(request.POST['height']), width=int(request.POST['width']), color=request.POST['color'], x=int(request.POST['x']), y=int(request.POST['y']))
        rec.save()
    return HttpResponseRedirect('/myimages/' + imagename + '/')

@login_required
def delrectangle(request, recid):
    user = request.user
    rec = Rectangle.objects.get(id=recid)
    image = rec.picture
    if image.authors.filter(username=user.username).exists():
        rec.delete()
    return HttpResponseRedirect('/myimages/' + image.name + '/')