
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import NewsForm
from .models import News
from .filters import  NewNewsFilter #NewsFilter

class Subscribed(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'to_subscribe.html', {})

    def post(self, reqest, *args, **kwargs):
        email_receive = News(
            name = reqest.POST['name'],
            description = reqest.POST['description'],
            subscribers = reqest.POST['subscribers']
        )
        email_receive.save()

        send_mail(
            subject=f'{email_receive.name}',
            message= email_receive.description,
            from_email='artsemlemesh@yandex.by',
            recipient_list=['bublikteam1@gmail.com']
        )

        return redirect('news/to_subscribe')

class NewsList(ListView):
    model = News
    ordering = 'publish_date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 5

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = NewsFilter(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context
class NewsDetail(DetailView):
    model = News
    template_name = 'news_single.html'
    context_object_name = 'news_single'








# def create_news(request):
#     form = NewsForm()
#
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/news/')
#
#     return render(request, 'news_edit.html', {'form': form})

class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_single_edit.html'

class NewsUpdate(LoginRequiredMixin, UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'

class NewsDelete(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class NewsSearch(ListView):
    model = News
    ordering = 'publish_date'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewNewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class Login(LoginView):
    template_name = 'login.html'

