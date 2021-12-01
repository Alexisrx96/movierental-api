from django.contrib import admin

from .models import Category, Chapter, Film, FilmCast, Season


class ChaptersInline(admin.StackedInline):
    model = Chapter
    extra = 0

    def get_max_num(self, request, obj: Season, **kwargs):
        if obj and obj.film.category.name != "serie":
            return 0


class SeasonInline(admin.StackedInline):
    model = Season
    extra = 0


class FilmCastInline(admin.StackedInline):
    model = FilmCast
    extra = 0


class SeasonAdmin(admin.ModelAdmin):
    inlines = (ChaptersInline,)

    class Meta:
        model = Season


class FilmAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['availability', 'category']
        else:
            return []

    inlines = (FilmCastInline, SeasonInline,)

    def availability(self, obj: Film, *args, **kwargs):
        return obj.availability

    class Meta:
        model = Film


admin.site.register(Film, FilmAdmin)
admin.site.register(Category)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Chapter)
