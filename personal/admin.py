from django.contrib import admin
from .models import Person, Address, Region, AddressHistory, EmailAccount, EmailHistory, MobileAccount, MobileHistory, PersonalDocument, SocialMediaAccount

class PersonAdmin(admin.ModelAdmin):
    list_display = ["person_id", "first_name", "last_name"]
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ["address_id", "person_id", "street", "city", "state", "country"]

class RegionAdmin(admin.ModelAdmin):
    list_display = ["region_id", "address_id", "name"]

class AddressHistoryAdmin(admin.ModelAdmin):
    list_display = ["address_history_id", "person_id", "address_id", "start_date"]

class EmailAccountAdmin(admin.ModelAdmin):
    list_display = ["email_id", "person_id", "email_address"]

class EmailHistoryAdmin(admin.ModelAdmin):
    list_display = ["email_history_id", "person_id", "email_id", "start_date"]

class MobileAccountAdmin(admin.ModelAdmin):
    list_display = ["mobile_id", "person_id", "mobile_number"]

class MobileHistoryAdmin(admin.ModelAdmin):
    list_display = ["mobile_history_id", "person_id", "mobile_id", "start_date"]

class PersonalDocumentAdmin(admin.ModelAdmin):
    list_display = ["document_id", "person_id", "document_type", "document_number"]

class SocialMediaAccountAdmin(admin.ModelAdmin):
    list_display = ["social_media_id", "person_id", "platform_name", "username"]

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
