# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Account, Developer, Player

admin.site.register([Account, Developer, Player])