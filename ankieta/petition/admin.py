from django.contrib import admin
from .models import Signature


@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'email')
    readonly_fields = ('location_picker', )

    def location_picker(self, obj):
        return '<input class="vTextField" id="locationinput" type="text"><br>' + \
            '<div id="map_canvas"></div>'
    location_picker.allow_tags = True

    class Media:
        js = [
            'https://maps.googleapis.com/maps/api/js?sensor=false&libraries=places',
            'http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js',
            'https://cdn.rawgit.com/Logicify/jquery-locationpicker-plugin/master/src/locationpicker.jquery.js',
            '/static/petition/map_admin.js',
        ]
        css = {"all": ('/static/petition/map_admin.css', )}
