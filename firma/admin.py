from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display=('status','phone')

admin.site.register(User,UserAdmin)
admin.site.register(Ishturi_or_Bolim)
admin.site.register(Mahsulot)
admin.site.register(Xato)
admin.site.register(Xodim)
admin.site.register(Workinspection)
admin.site.register(Bulim)