from django.contrib.auth.forms import UserCreationForm
# 新しくユーザーが登録された際に「User」モデルにデータを追加することを「Django」に伝える。
from django.contrib.auth.models import User

# 「SignupForm」は「UserCreationForm」を継承している。
# 「UserCreationForm」は「ModelForm」である。
# デフォルトで３つのフィールドが準備されている（①username,②password1,③password2）。
class SignupForm(UserCreationForm):
	# 「class Meta」は、一般的に本来の実装とは関係ない情報を載せる際に使われる。
	# また、以下のような記述をすることで、コードを使い回すことが出来る。
	class Meta:
		model = User
		fields = ('username',)