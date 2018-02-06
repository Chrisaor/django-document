from django.db import models

class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+',
    )

class Relation(models.Model):

    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'
    CHOICE_TYPE = (
        (RELATION_TYPE_FOLLOWING,'팔로잉'),
        (RELATION_TYPE_BLOCK, '차단'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=1, choices=CHOICE_TYPE)