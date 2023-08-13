from django.urls import path

from .views import NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, NewsSearch, Login, Subscribed

urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   #path('create', create_news, name = 'news_create'),
   path('create/', NewsCreate.as_view(), name = 'news_single_create'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   #for news search using the same template as for newslist
   path('search/', NewsSearch.as_view(), name = 'news_single_search'),
   path('login/', Login.as_view(), name = 'login'),
   #new_view for subscribing

   path('subscribe/', Subscribed.as_view(), name = 'subscribe'),

]