from django.contrib import admin
from .models import Share
# Register your models here.


class ShareAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model =Share 



admin.site.register(Share, ShareAdmin)
