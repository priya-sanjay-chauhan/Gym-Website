from django.contrib import admin
from .models import data
from .models import contact_detail


#   save the data in the database according to class we have created
class takeaction(admin.ModelAdmin):

    list_display=("Name", "Email", "Phone", "Gender", "DOB", "Address")

admin.site.register(data,takeaction)


class contactdetail(admin.ModelAdmin):

    list_display=("Username","Email","Message")

admin.site.register(contact_detail,contactdetail)


