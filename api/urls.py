from django.urls import path, include
from .views import TaskViewSet, CategoryViewSet, SignUpView
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('tasks', TaskViewSet)
# router.register('categories', CategoryViewSet)


router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignUpView.as_view(), name='signup'),
]