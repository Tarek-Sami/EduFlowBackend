from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "headline",
        "priority",
        "status",
        "progress",
        "made_by",
        "assigned_to",
        "deadline",
        "created_at",
    )
    list_filter = ("status", "priority", "deadline")
    search_fields = ("headline", "description", "made_by", "assigned_to")
    ordering = ("-created_at",)