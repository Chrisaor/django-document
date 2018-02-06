from django.contrib import admin

# Register your models here.
from many_to_many.models import Pizza, Topping, PostLike, Post, User

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
