from django.contrib import admin
from .models import Band,Member
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('name', 'instrument')
    list_filter = ('band',)

class BandAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('name', 'can_rock')

admin.site.register(Band,BandAdmin)  # Use the default options
admin.site.register(Member, MemberAdmin)  # Use the customized options

