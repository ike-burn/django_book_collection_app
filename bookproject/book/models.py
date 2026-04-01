from django.db import models

# 「タプル（順番付きで値を並べる）」、choiesに渡すための候補一覧
CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'))

class Book(models.Model):
        # 「フィールド」とは、モデルの中に書く「データの項目」。タイトル、説明や本文、分類
        title = models.CharField(max_length=100) # 本のタイトルを入れる項目
        text = models.TextField() # 本の説明や本文を入れる項目
        category = models.CharField(
            max_length=100,
            choices = CATEGORY
        ) # 本の分類を入れる項目

        # 「__str__」は特殊メソッド（オブジェクトの文字列表現を返す）
        def __str__(self):
            return self.title

# ブランチ切り替え
