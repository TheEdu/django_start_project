from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy

from example_app.models import *
from example_app.forms import *


# Template View with model attribute
class TemplateViewWithModel(TemplateView):
    model = None


class GenericIndexView(TemplateViewWithModel):

    def __init__(self, *args, **kwargs):
        super(GenericIndexView, self).__init__(*args, **kwargs)
        self.model = eval(self.model)
        self.template_name = 'generic/template.html'
        # MODEL_URLS
        model_urls = self.model.get_model_urls()
        self.detail_url = model_urls['detail']
        self.update_url = model_urls['update']
        self.delete_url = model_urls['delete']
        self.create_url = model_urls['create']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_url'] = self.detail_url
        context['update_url'] = self.update_url
        context['delete_url'] = self.delete_url
        context['create_url'] = self.create_url

        # MODEL_INFO
        model_info = self.model.get_model_info()
        context['title'] = model_info['title']['main']
        context['index_title'] = model_info['title']['index']
        context['data_table'] = model_info['index']['data_table']

        return context


class GenericCreateView(CreateView):

    def __init__(self, *args, **kwargs):
        super(GenericCreateView, self).__init__(*args, **kwargs)
        model_name = self.model
        self.model = eval(model_name)
        self.form_class = eval(self.model.get_model_form_name())
        self.template_name = 'generic/form.html'

        # MODEL_URLS
        model_urls = self.model.get_model_urls()
        self.success_url = reverse_lazy(model_urls['index'])
        self.return_url_name = model_urls['index']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return_url_name'] = self.return_url_name

        # MODEL_INFO
        model_info = self.model.get_model_info()
        context['title'] = model_info['title']['main']
        context['form_title'] = model_info['title']['create']

        return context


class GenericUpdateView(UpdateView):

    def __init__(self, *args, **kwargs):
        super(GenericUpdateView, self).__init__(*args, **kwargs)
        model_name = self.model
        self.model = eval(model_name)
        self.form_class = eval(self.model.get_model_form_name())
        self.template_name = 'generic/form.html'

        # MODEL_URLS
        model_urls = self.model.get_model_urls()
        self.success_url = reverse_lazy(model_urls['index'])
        self.return_url_name = model_urls['index']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return_url_name'] = self.return_url_name

        # MODEL_INFO
        model_info = self.model.get_model_info()
        context['title'] = model_info['title']['main']
        context['form_title'] = model_info['title']['update']

        return context


class GenericDetailView(DetailView):

    def __init__(self, *args, **kwargs):
        super(GenericDetailView, self).__init__(*args, **kwargs)
        self.model = eval(self.model)
        self.template_name = 'generic/detail.html'

        # MODEL_URLS
        model_urls = self.model.get_model_urls()
        self.return_url_name = model_urls['index']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return_url_name'] = self.return_url_name

        # MODEL_INFO
        model_info = self.model.get_model_info()
        context['title'] = model_info['title']['main']
        context['detail_title'] = model_info['title']['detail']
        context['object_info'] = model_info['detail']['object_info']

        return context


class GenericListView(ListView):

    def __init__(self, *args, **kwargs):
        super(GenericListView, self).__init__(*args, **kwargs)
        self.model = eval(self.model)
        self.template_name = 'generic/list.html'

        # MODEL_URLS
        model_urls = self.model.get_model_urls()
        self.return_url_name = model_urls['index']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return_url_name'] = self.return_url_name

        # MODEL_INFO
        model_info = self.model.get_model_info()
        context['title'] = model_info['title']['main']
        context['list_title'] = model_info['title']['list']
        context['data_table'] = model_info['index']['data_table']

        return context


class GenericDeleteView(DeleteView):

    def __init__(self, *args, **kwargs):
        super(GenericDeleteView, self).__init__(*args, **kwargs)
        self.model = eval(self.model)
        self.template_name = 'generic/delete.html'

        # MODEL_URLS
        model_urls = self.model.get_model_urls()
        self.success_url = reverse_lazy(model_urls['index'])
        self.return_url_name = model_urls['index']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return_url_name'] = self.return_url_name

        # MODEL_INFO
        model_info = self.model.get_model_info()
        context['title'] = model_info['title']['main']
        context['delete_title'] = model_info['title']['delete']

        return context