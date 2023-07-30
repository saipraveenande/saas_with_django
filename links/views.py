from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, LinkForm
from .models import Category, Link


@login_required
def links(request):
    category = request.GET.get('category ', '')
    name = request.user.username
    links = Link.objects.filter(created_by=request.user)

    if category:
        links = links.filter(category_id=category)

    return render(request, 'links/links.html', {
        'links': links,
        'category': category,
        'name' : name,
    })

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit = False)
            category.created_by = request.user
            category.save()

            return redirect('/links/categories/')
    else: 
        form = CategoryForm()

    return render(request, 'links/create_category.html',{'form':form, 'title':'Create category',})


@login_required
def create_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            link = form.save(commit = False)
            link.created_by = request.user
            link.save()

            return redirect('/dashboard/')
    else:
        form = LinkForm()
        form.fields['category'].queryset = Category.objects.filter(created_by = request.user)

    return render(request, 'links/create_link.html',{'form':form, 'title': 'Create Link'})


@login_required
def edit_link(request, pk):
    link = get_object_or_404(Link, created_by = request.user, pk = pk)

    if request.method == 'POST':
        form = LinkForm(request.POST, instance = link)

        if form.is_valid():
            form.save()

            return redirect('/links/')
    else:
        form = LinkForm(instance = link)
        form.fields['category'].queryset = Category.objects.filter(created_by = request.user)

    return render(request, 'links/create_link.html',{'form':form, 'title':"Edit Link"})


@login_required
def delete_link(request, pk):
    link = get_object_or_404(Link, created_by = request.user, pk=pk)
    link.delete()
    return redirect("/links/")


@login_required
def categories(request):
    categories = Category.objects.filter(created_by = request.user)
    return render(request, 'links/categories.html', {'categories':categories,})


@login_required
def edit_category(request, pk):
    category = get_object_or_404(Category, created_by = request.user, pk =pk)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance = category)
        
        if form.is_valid():
            form.save()

            return redirect('/links/categories/')
    else:
        form = CategoryForm(instance = category)

    return render(request, 'links/create_category.html', {'form': form, 'title': 'Edit category',})


@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, created_by = request.user, pk =pk)
    category.delete()
    return redirect('/links/categories/')

