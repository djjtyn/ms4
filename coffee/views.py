from django.shortcuts import render, get_object_or_404, redirect
from .models import Range, Intensity, Coffee, Comment
from .forms import CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
#view to show 9 coffees in database per page with pagination for navigating next and previous pages
def all_coffee(request):
    all_coffee = Coffee.objects.all().order_by('name')
    paginator = Paginator(all_coffee, 9)
    page = request.GET.get('page', 1)
    all_coffee = paginator.page(page)
    return render(request,'all_coffee.html', {'all_coffee':all_coffee})

#A view that returns a single coffee page based on the coffee ID rendered to the 'coffeereview.html' template
def coffee_review(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    comments = Comment.objects.filter(coffee =coffee, created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'coffeereview.html', {'coffee': coffee, 'comments': comments})

#View to add users comment to coffee review page. Login required for this
@login_required
def add_comment_to_coffee(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.coffee = coffee
            comment.author = request.user
            comment.save()
            return redirect(coffee_review, coffee.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_coffee.html', {'form': form})
