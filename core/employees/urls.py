from django.urls import path
from .views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('', EmployeeListView.as_view(), name='employee-list'),
]
