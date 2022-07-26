from django.contrib import admin

from foodgram.settings import EMPTY

from recipes.models import (Ingredient, IngredientsRecipe, Recipe, Tag,
                            TagsRecipe)

from .models import CustomUser, Follow


class IngredientsInline(admin.TabularInline):
    model = IngredientsRecipe
    extra = 1


class TagsInline(admin.TabularInline):
    model = TagsRecipe
    extra = 1


@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'first_name', 'last_name', 'email')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')
    empty_value_display = EMPTY


@admin.register(Follow)
class FollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    list_filter = ('user', 'author')
    search_fields = ('user', 'author')
    empty_value_display = EMPTY


@admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'count_recipes_favorite')
    list_filter = ('name', 'author', 'tags')
    search_fields = ('name', 'author', 'tags')
    empty_value_display = EMPTY
    inlines = [
        TagsInline, IngredientsInline
    ]
    readonly_fields = ['count_recipes_favorite']

    def count_recipes_favorite(self, obj):
        return obj.favorite_recipes.count()

    count_recipes_favorite.short_description = 'Популярность'


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    inlines = [
        TagsInline
    ]
    list_display = ('name', 'color')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Ingredient)
class IngredientsAdmin(admin.ModelAdmin):
    inlines = [
        IngredientsInline
    ]
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)
