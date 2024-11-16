from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, PositionViewSet, PermissionViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'positions', PositionViewSet, basename='position')
router.register(r'permissions', PermissionViewSet, basename='permission')
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = router.urls
