from django.db import models
app_name = 'example_app'

class GenericMethods():
    @classmethod
    def get_model_urls(cls):
        return {   
            'index':    f'{app_name}:{cls.__name__.lower()}_index'
            ,'create':  f'{app_name}:{cls.__name__.lower()}_create'
            ,'detail':  f'{app_name}:{cls.__name__.lower()}_detail'
            ,'update':  f'{app_name}:{cls.__name__.lower()}_update'
            ,'delete':  f'{app_name}:{cls.__name__.lower()}_delete'
            ,'list':    f'{app_name}:{cls.__name__.lower()}_list'
        }

    @classmethod
    def get_model_form_name(cls):
        return f'{cls.__name__}Form'

class GenderExample(models.Model, GenericMethods):
    id          = models.AutoField(primary_key=True)
    uuid        = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50)

    delete_flag = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uuid

    @classmethod
    def get_model_info(cls):
        return {
            'title': {
                'main':     ''
                ,'index':   'Género - Gestión'
                ,'detail':  'Género - Detalle'
                ,'create':  'Género - Nuevo'
                ,'update':  'Género - Editar'
                ,'delete':  'Género - Borrar'
                ,'list':    'Género - Listado'

            },
            'index': {
                'data_table': {
                    'objects': cls.objects.order_by('-updated_at'),
                    'object_info': [
                        {'label': 'Género'        ,'attr': 'uuid'         ,'exportable': True},
                        {'label': 'Descripción'   ,'attr': 'description'  ,'exportable': True}
                    ]
                }
            },
            'detail': {
                'object_info': [
                    {'label': 'Género: '        ,'attr': 'uuid'},
                    {'label': 'Descripción: '   ,'attr': 'description'}
                ]
            }
        }


class PersonExample(models.Model, GenericMethods):
    id 			= models.AutoField(primary_key=True)
    uuid 		= models.CharField(max_length=50, unique=True)
    firstName 	= models.CharField(max_length=50)
    lastName  	= models.CharField(max_length=50)
    gender      = models.ForeignKey(GenderExample, on_delete=models.CASCADE, null=True)

    delete_flag = models.BooleanField(default=False)
    created_at 	= models.DateTimeField(auto_now_add=True)
    updated_at 	= models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'DNI: ' + self.uuid + ' - ' + self.firstName + ' ' + self.lastName

    @classmethod
    def get_model_info(cls):
        return {
            'title': {
                'main':     ''
                ,'index':   'Personas - Gestión'
                ,'detail':  'Personas - Detalle'
                ,'create':  'Personas - Nueva'
                ,'update':  'Personas - Editar'
                ,'delete':  'Personas - Borrar'
                ,'list':    'Personas - Listado'

            },
            'index': {
                'data_table': {
                    'objects': cls.objects.order_by('-updated_at'),
                    'object_info': [
                        {'label': 'DNI'                     ,'attr': 'uuid'       ,'exportable': True},
                        {'label': 'Nombre '                 ,'attr': 'firstName'  ,'exportable': True},
                        {'label': 'Apellido'                ,'attr': 'lastName'   ,'exportable': True},
                        {'label': 'Género'                  ,'attr': 'gender'     ,'exportable': True},
                        {'label': 'Actualizado en'          ,'attr': 'updated_at' ,'exportable': True}
                    ]
                }
            },
            'detail': {
                'object_info': [
                    {'label': 'DNI'             ,'attr': 'uuid'},
                    {'label': 'Nombre '         ,'attr': 'firstName'},
                    {'label': 'Apellido'        ,'attr': 'lastName'},
                    {'label': 'Género'          ,'attr': 'gender'},
                    {'label': 'Actualizado en'  ,'attr': 'updated_at'},
                ]
            }
        }