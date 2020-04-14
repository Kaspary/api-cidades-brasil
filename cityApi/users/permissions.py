import copy 
from rest_framework import permissions


# Example pemissions on base class
# perms_map = {
# 	  'GET': [], #'%(app_label)s.view_%(model_name)s'
#     'OPTIONS': [],
#     'HEAD': [],
#     'POST': ['%(app_label)s.add_%(model_name)s'],
#     'PUT': ['%(app_label)s.change_%(model_name)s'],
#     'PATCH': ['%(app_label)s.change_%(model_name)s'],
#     'DELETE': ['%(app_label)s.delete_%(model_name)s'],
# }


class UserModelPermission(permissions.DjangoModelPermissions):

    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map) # you need deepcopy when you inherit a dictionary type 
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['POST'] = []



# https://github.com/1flow/sparks/blob/master/sparks/django/rest.py

class IsSelf(permissions.BasePermission):

    """ Grant permission only if the current instance is the request user.
    Used to allow users to edit their own account, nothing to others (even
    superusers).
    """

    def has_permission(self, request, view):
        """ Always return True here.
        The fine-grained permissions are handled in has_object_permission().
        """

        return True

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id



class IsSelfOrAdmin(IsSelf):

    """ Grant R/W to self and superusers/staff members. Deny others. """

    def has_object_permission(self, request, view, obj):

        user = request.user

        if user.is_superuser or user.is_staff:
            return True

        return IsSelf.has_object_permission(self, request, view, obj)
