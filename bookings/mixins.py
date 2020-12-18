from rest_framework import mixins, viewsets


class BookingViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass
