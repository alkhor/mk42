# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/membership.py

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "MembershipAdmin",
]


class MembershipAdmin(admin.ModelAdmin):
    """
    Customize Membership model for admin area.
    """

    list_display = ["id", "user", "group", "created", ]
    list_filter = ["group", ]
    date_hierarchy = "created"
    readonly_fields = ["created", ]
    fieldsets = (
        [None, {"fields": ["user", "group", ], }, ],
        [_("Other"), {"fields": ["created", ], }, ],
    )
