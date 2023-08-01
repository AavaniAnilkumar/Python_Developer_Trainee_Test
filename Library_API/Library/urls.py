

from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDeleteView,form
from .import views
urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-retrieve-update-delete'),
    path('',views.form,name='form'),
    path('formsave/',views.formsave,name='formsave'),
    path('formtable/',views.formtable,name='formtable'),
    path('formedit/<int:dataid>/',views.formedit,name='formedit'),
    path('formupdate<int:dataid>/',views.formupdate,name='formupdate'),
    path('formdelete/<int:dataid>/',views.formdelete,name='formdelete')
    
 
    
    
]
