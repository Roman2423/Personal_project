from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Quiz
from .forms import QuizForm


def quiz_list(request):
    sort_by = request.GET.get('sort', 'created_at') 
    creator_name = request.GET.get('creator')

    quizzes = Quiz.objects.all()

    if creator_name:
        quizzes = quizzes.filter(creator__username__icontains=creator_name)

    if sort_by in ['created_at', 'title', 'topic', 'creator__username']:
        quizzes = quizzes.order_by(sort_by)

    return render(request, 'quiz_user/main_page.html', {'quizzes': quizzes})


@login_required
def quiz_create(request):
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.creator = request.user
            quiz.save()
            return redirect('quiz_detail', quiz_id=quiz.id)  
    else:
        form = QuizForm()
    
    return render(request, 'quiz_creator/quiz_creation.html', {'form': form})


# <a href="{% url 'profile' %}">Профиль</a>
#                 {% if user.account.permission == "moderator" %}
#                     <a href="{% url 'mod_panel' %}">Модерация</a>
#                 {% endif %}
#                 <a href="{% url 'logout' %}">Выйти</a>
#             {% else %}
#                 <a href="{% url 'login' %}">Войти</a>
#                 <a href="{% url 'register' %}">Регистрация</a>