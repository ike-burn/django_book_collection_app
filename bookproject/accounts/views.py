from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm

class SignupView(CreateView):
	model = User
	# 「form_class」は「CreateView」の中で使う「Form」を指定する時に使う。
	# 「Form」はお問い合わせフォームのように、データは保存せずに、データのやり取りを行う。
	form_class = SignupForm
	template_name = 'accounts/signup.html'
	success_url = reverse_lazy('index')

# 「Model」はデータベースのデータを扱う時に使われる。
# 「ModelForm」は、ModelとFormの両方の性質を持っている。
# 「View」の中で「form_class」が定義されていない場合、「model=」というコードの中で定義したモデルに基づいた「ModelForm」が作成される。
