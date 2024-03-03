from django.contrib import admin
from .models import Data,Target
# Register your models here.





@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = [
        "id","url","redirect_url","form_id","btn_id",
        "username_id_name","password_id_name","date_time"
    ]


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = [
        "id","url","data","ip","date_time"
    ]

