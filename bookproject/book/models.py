from django.db import models
from .consts import MAX_RATE

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

# 「タプル（順番付きで値を並べる）」、choiesに渡すための候補一覧
CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'))

class Book(models.Model):
    # 「フィールド」とは、モデルの中に書く「データの項目」。タイトル、説明や本文、分類
    title = models.CharField(max_length=100) # 本のタイトルを入れる項目
    text = models.TextField() # 本の説明や本文を入れる項目
    thumbnail = models.ImageField(null=True, blank=True) # 画像を扱う、サムネイル
    # 本の分類を入れる項目
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # 「__str__」は特殊メソッド（オブジェクトの文字列表現を返す）
    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
