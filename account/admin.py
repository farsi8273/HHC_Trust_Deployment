from django.contrib import admin
from .models import  *
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django import forms



class UsersAdmin(admin.ModelAdmin):
    list_display = ['username']



class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ['image_tag']
    list_display = ['title', 'image_tag']

class VolunteersForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(),
        }

class VolunteersAdmin(admin.ModelAdmin):
    form = VolunteersForm
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(),
        }
    
class Social_VoluteersAdmin(admin.ModelAdmin):
    list_display=('volunteers','account' )

class ContactsAdmin(admin.ModelAdmin):
    list_display=('name','subject' )
    class Meta:
        widgets = {
            'phone_number': PhoneNumberPrefixWidget(),
        }

class Feature_CampaignsAdmin(admin.ModelAdmin):
    list_display=('tag','title' )

class Certificate_80gAdmin(admin.ModelAdmin):
    list_display=('donater','Certificate_80G_no' )
# class DonationAdmin(admin.ModelAdmin):
#     list_display=('id','name','phone_number','amount' ,'campaigns','pay_status',)
#     class Meta:
#         widgets = {
#             'phone_number': PhoneNumberPrefixWidget(),
#         }


class DonationsAdmin(admin.ModelAdmin):
    list_display=('id','name','phone_number','amount' ,'campaigns', 'donation_date')
    class Meta:
        widgets = {
            'phone_number': PhoneNumberPrefixWidget(),
        }        


# Register your models here.

admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Volunteers,VolunteersAdmin)
admin.site.register(Social_Voluteers,Social_VoluteersAdmin)
admin.site.register(Contacts,ContactsAdmin)
admin.site.register(Feature_Campaigns,Feature_CampaignsAdmin)
# admin.site.register(Donation,DonationAdmin)
admin.site.register(Certificate_80g,Certificate_80gAdmin)
admin.site.register(Donations,DonationsAdmin)
admin.site.register(Users,UsersAdmin)