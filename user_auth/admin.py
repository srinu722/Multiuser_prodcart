from django.contrib import admin

# Register your models here.
from user_auth.models import User
from To_Do_list.models import Products

# Register your models here.
class UserAdmin(admin.ModelAdmin):
     list_display=['username','email','phone_no','first_name','last_name','password1','password2']

admin.site.register(User,UserAdmin)



# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
     list_display=['name']

admin.site.register(Products,ProductsAdmin)

#class ProductsSelAdmin(admin.ModelAdmin):
#    list_display=['name']
#admin.site.register(ProductsSel,ProductsSelAdmin)
