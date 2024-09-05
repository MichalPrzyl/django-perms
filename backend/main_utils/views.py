from user.models import Permission, Role
from django.contrib.auth.models import User

from rest_framework import generics

class BaseView(generics.GenericAPIView):
    queryset = None
    serializer_class = None

    def find_permissions_to_model(self, user):
        roles = user.roles.all()
        perms = Permission.objects.filter(
            role__in=roles,
            model=f"{self.queryset.query.model._meta.app_label}.{self.queryset.query.model._meta.model_name}"
        )

    def get(self, request):
        req_user = request.user
        user = User.objects.get(id=req_user)

        fields_to_read = self.find_permissions_to_model(user)

        fields_to_remove = []
        for field in self.serializer_class.fields:
            if field not in fields_to_read:
                fields_to_remove.append(field)

                
        for field in fields_to_remove:
            self.serializer_class.fields.pop(field)

        serializer = self.serializer_class
        data = serializer(self.queryset, many=True).data
        return Response(data)
