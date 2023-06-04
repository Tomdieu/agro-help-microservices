from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Forum, ForumComment, User
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Register your models here.
User = get_user_model()


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "type")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "type", "password1", "password2"),
            },
        ),
    )
    list_display = ("username", "email", "type", "is_staff")

    search_fields = ("username", "first_name", "last_name", "email", "type")


admin.site.register(User, MyUserAdmin)


class ForumCommentInline(admin.TabularInline):
    model = ForumComment
    extra = 0


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    inlines = [ForumCommentInline]
    list_display = ("id", "author", "content", "created_at")


@admin.register(ForumComment)
class ForumCommentAdmin(admin.ModelAdmin):
    list_display = ["forum", "author", "parent", "content", "created_at"]

    list_filter = ["created_at", "forum"]
