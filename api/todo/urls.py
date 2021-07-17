from rest_framework import routers
from.views import TodoViewset

router = routers.DefaultRouter()#allow us to register views and create our url partterns
router.register('todo',TodoViewset)#register a url pattern


