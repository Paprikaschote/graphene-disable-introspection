from django.conf import settings


class DisableIntrospectionMiddleware:
    def resolve(self, next, root, info, **args):
        if info.field_name in settings.DISABLED_INTROSPECTION_TYPES:
            raise Exception("Introspection is disabled")
        return next(root, info, **args)
