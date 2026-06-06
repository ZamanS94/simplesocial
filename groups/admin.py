from django.contrib import admin
from . import models


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupMemberInline]
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


admin.site.register(models.Group, GroupAdmin)
