from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        '''
        Read only permission are allowed for any requests
        '''

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author == request.user