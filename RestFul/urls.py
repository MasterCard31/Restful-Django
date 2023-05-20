
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Los serializadores definen la representación de la API.
# Le permite serializar y deserializar fácilmente objetos Python complejos hacia y desde JSON, XML u otros tipos de contenido.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# Los ViewSets definen el comportamiento de la vista.
#facilitan la definición de la lógica para manejar diferentes operaciones de API (por ejemplo, GET, POST, PUT, DELETE) y 
# especifican cómo se deben serializar/deserializar los datos.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Los enrutadores proporcionan una manera fácil de determinar automáticamente la URL conf.
# Genera automáticamente URL de API basadas en sus conjuntos de vistas y 
# le permite manejar fácilmente recursos anidados y patrones de URL personalizados.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Conecte nuestra API mediante el enrutamiento automático de URL.
# Además, incluimos direcciones URL de inicio de sesión para la API navegable.
urlpatterns = [
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('series.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



