from .views import login , sample_api , all_news , post_a_news , delete_a_news , update_a_news


from django.urls import path


urlpatterns = [

	path('login' , login),
    path('sampleapi' , sample_api),
    path('news' , all_news ),
    path('post_news' , post_a_news),
    path('news/<int:id>/delete' , delete_a_news),
    path('news/<int:id>/update' , update_a_news),

]