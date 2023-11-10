from django.contrib import admin
from .models import Person, Address, Region, AddressHistory, EmailAccount, EmailHistory, MobileAccount, MobileHistory, PersonalDocument, SocialMediaAccount

class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    search_fields = ('first_name',)  # Campos pesquisáveis
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ["street", "city", "state", "country"]
    search_fields = ('street',)  # Campos pesquisáveis

class RegionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ('name',)  # Campos pesquisáveis    

class AddressHistoryAdmin(admin.ModelAdmin):
    list_display = ["start_date"]    

class EmailAccountAdmin(admin.ModelAdmin):
    list_display = ["email_address"]
    search_fields = ('email_address',)  # Campos pesquisáveis

class EmailHistoryAdmin(admin.ModelAdmin):
    list_display = ["start_date"]

class MobileAccountAdmin(admin.ModelAdmin):
    list_display = ["mobile_number"]
    search_fields = ('mobile_number',)  # Campos pesquisáveis

class MobileHistoryAdmin(admin.ModelAdmin):
    list_display = ["start_date"]

class PersonalDocumentAdmin(admin.ModelAdmin):
    list_display = ["document_type", "document_number"]
    search_fields = ('document_number',)  # Campos pesquisáveis    

class SocialMediaAccountAdmin(admin.ModelAdmin):
    list_display = ["platform_name", "username"]
    search_fields = ('first_name',)  # Campos pesquisáveis    

# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(AddressHistory, AddressHistoryAdmin)
admin.site.register(EmailAccount, EmailAccountAdmin)
admin.site.register(EmailHistory, EmailHistoryAdmin)
admin.site.register(MobileAccount, MobileAccountAdmin)
admin.site.register(MobileHistory, MobileHistoryAdmin)
admin.site.register(PersonalDocument, PersonalDocumentAdmin)
admin.site.register(SocialMediaAccount, SocialMediaAccountAdmin)
