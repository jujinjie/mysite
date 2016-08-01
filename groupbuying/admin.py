from django.contrib import admin

# Register your models here.
from .models import Notice
from .models import ProductInfo
from .models import Orders
from .models import User
from .models import Admin
admin.site.register(Notice)
admin.site.register(ProductInfo)
admin.site.register(Orders)
admin.site.register(User)
admin.site.register(Admin)