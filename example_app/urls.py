from django.urls import path
from generic import views
app_name = 'example_app'

generic_models = ['PersonExample', 'GenderExample']

urlpatterns = []
for model in generic_models:
    urlpatterns = urlpatterns + [
        path('{0}/'.format(model.lower()), views.GenericIndexView.as_view(model=model), name='{0}_index'.format(model.lower())),
        path('{0}/create'.format(model.lower()), views.GenericCreateView.as_view(model=model), name='{0}_create'.format(model.lower())),
        path('{0}/list'.format(model.lower()), views.GenericListView.as_view(model=model), name='{0}_list'.format(model.lower())),
        path('{0}/<pk>'.format(model.lower()), views.GenericDetailView.as_view(model=model), name='{0}_detail'.format(model.lower())),
        path('{0}/<pk>/update'.format(model.lower()), views.GenericUpdateView.as_view(model=model), name='{0}_update'.format(model.lower())),
        path('{0}/<pk>/delete'.format(model.lower()), views.GenericDeleteView.as_view(model=model), name='{0}_delete'.format(model.lower())),
    ]