from ..models import Usuario


def get_users():
    queryset = Usuario.objects.all()
    return (queryset)


def create_user(form):
    user = form.save()
    user.save()
    return ()