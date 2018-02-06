from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)

class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+',
    )

    def __str__(self):
        return self.name

    @property
    def following(self):
        following_relations = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        following_pk_list = following_relations.values_list('to_user', flat=True)
        following_users = TwitterUser.objects.filter(pk__in=following_pk_list)
        return following_users

    def follow(self, to_user):
        '''
        to_user에 주어진 TwitterUser를 follow함
        :param to_user:
        :return:
        '''
        self.relations_by_from_user.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        # Relation.objects.create(
        #     from_user=self,
        #     to_user=to_user,
        #     type=Relation.RELATION_TYPE_FOLLOWING,
        # )

    @property
    def block(self, to_user):
        self.relation_by_from_user.filter(to_user=to_user).delete()
        self.relations_by_from_user.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_BLOCK,
        )



    # @property
    # def block_users(self):
    #     # 내가 블락하고 있는 TwitterUser목록을 가져옴
    #
    #     pk_list = self.relations_by_from_user.filter(
    #         type=Relation.RELATION_TYPE_BLOCK).values_list('to_user', flat=True)
    #
    #     return TwitterUser.objects.filter(pk__in=pk_list)



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
        # 자신이 from_user인 경우에 Relation목록을 가져오고 싶을 경우
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 to_user인 경우에 Relation목록을 가져오고 싶을 경우
        related_name='relations_by_to_user',
    )
    type = models.CharField(max_length=1, choices=CHOICE_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            # from_user와 to_user의 값이 이미 있을 경우
            # DB에 중복 데이터 저장을 막음
            # ex) from_user가 1, to_user가 3인 데이터가 이미 있다면
            # 두 항목의 값이 모두 같은 또 다른 데이터가 존재할 수 없음
            ('from_user', 'to_user')
        )