from django.db  import models

__all__ = (
    'InstagramUser',
)

class InstagramUser(models.Model):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField(
        'self',
        # 대칭관계가 아님
        symmetrical=False,
        related_name = 'followers',
    )

    def __str__(self):
        return self.name
    #
    # def followers(self):
    #     # 자신을 following하고 있는 사람들을 리턴
    #     # 문자열이 아닌 쿼리 자체
    #
    #     return self.instagramuser_set.all()
    #
