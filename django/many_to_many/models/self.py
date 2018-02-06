from django.db import models

__all__ = (
    'FacebookUser',
)

class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')

    def __str__(self):
        # name이 '이한영'이며
        # 친구로 '박보영', '아이유'를 가지는 경우
        # -> 이한영 (친구: 박보영, 아이유)
        # __str__의 결과가 위처럼 출력될 수 있도록 작성
        # result = ''
        # for friend in self.friends.all():
        #     result += friend.name
        #     result += ', '
        # result = result[:-2]
        # return '{name} (친구: {friends}'.format(
        #     name=self.name,
        #     friends=result,
        # )
        # list comprehenstion 사용
        # result = ', '.join([friend.name for friend in self.friends.all()])

        # Manager의 values_list를 사용 <제일 효율적>
        # DB에서 모든 friends의 'name'필드 값만 가져옴
        result = ', '.join(self.friends.value_list('name', flat=True))

        return '{name} (친구: {friends})'.format(
            name=self.name,
            friends=result,
        )