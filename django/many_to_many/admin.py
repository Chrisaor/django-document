from django.contrib import admin

# Register your models here.
from .models import (
    # basic
    Pizza, Topping,
    # intermediate
    PostLike, Post, User,
    # self
    FacebookUser,
    TwitterUser, Relation
)


admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
admin.site.register(FacebookUser)
admin.site.register(TwitterUser)
admin.site.register(Relation)