from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quiz


def quiz_list(request):
    sort_by = request.GET.get('sort', 'created_at') 
    creator_name = request.GET.get('creator')

    quizzes = Quiz.objects.all()

    if creator_name:
        quizzes = quizzes.filter(creator__username__icontains=creator_name)

    if sort_by in ['created_at', 'title', 'topic', 'creator__username']:
        quizzes = quizzes.order_by(sort_by)

    return render(request, 'quiz_list.html', {'quizzes': quizzes})

def quiz_redirect(request):
    return render(request, 'quiz/quiz_redirect.html')


@login_required
def quiz_creation(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        topic = request.POST.get('topic')
        content = request.POST.get('content')
        attachment = request.POST.get('attachment')
        if title:
            Thread.objects.create(title=title, content=content, attachment=attachment, created_by=request.user)
            return redirect('forum_main_page')
        else:
            return HttpResponse("Title is required for post.")
    return redirect('forum_main_page')
