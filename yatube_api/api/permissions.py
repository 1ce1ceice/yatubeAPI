from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return getattr(obj, 'author', None) == request.user
    
class IsAuthenticatedOrReadOnlyCreateUpdateDelete(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return super().has_permission(request, view)