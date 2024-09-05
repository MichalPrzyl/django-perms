from user.models import Permission, Role, User
from rest_framework import generics
from rest_framework.response import Response


class BaseView(generics.GenericAPIView):
    queryset = None
    serializer_class = None

    def find_permissions_to_model(self, user):
        """
        Returns list of fields that are allowed to read
        to user.
        Example: ["name", "description"]
        """
        roles = user.roles.all()
        perms = Permission.objects.filter(
            role__in=roles,
            model__iexact=f"{self.get_queryset().query.model._meta.app_label}.{self.get_queryset().query.model._meta.model_name}"
        )
        read_fields_from_perms = []
        for perm in perms:
            read_fields_from_perms.append(perm.read)

        return ", ".join(read_fields_from_perms)

    def get(self, request):
        # TODO: This should be user from request.
        # req_user = request.user
        user = User.objects.get(id=1)

        fields_to_read = self.find_permissions_to_model(user)

        serializer = self.serializer_class(self.get_queryset(), many=True)

        fields_to_remove = []
        for field in serializer.child.fields:
            if field not in fields_to_read:
                fields_to_remove.append(field)
                
        for field in fields_to_remove:
            serializer.child.fields.pop(field)
        return Response(serializer.data)
