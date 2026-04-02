from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	DeleteView,
	UpdateView,
)
from .models import Book, Review

class ListBookView(ListView):
    template_name = 'book/book_list.html'
    model = Book

class DetailBookView(DetailView):
    template_name = 'book/book_detail.html'
    model = Book

class CreateBookView(CreateView):
    template_name = 'book/book_create.html'
    # 「model = Book」を定義する理由は、ユーザーが入力した情報をどのテーブルに保存するかを指定する必要があるため
    model = Book
    fields = ('title', 'text', 'category')
    #formの項目の作成が完了した後に遷移させるURLを指定するには、viewの中で「success_url」という変数を定義する必要がある。
	#「reverse関数」と使うとエラーになるが、「reverse_lazy」関数であれば「クラス変数」として定義することが出来るので、エラーにならない。
    # 「'list-book'」は、urls.pyの「name='list-book'」と紐付く。
    success_url = reverse_lazy('list-book')

class DeleteBookView(DeleteView):
    template_name = 'book/book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('list-book')

class UpdateBookView(UpdateView):
    template_name = 'book/book_update.html'
    model = Book
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('list-book')

def index_view(request):
    # BookはBookモデルを示す。
    # 「order_by('category')」により、カテゴリごとに並び替えて表示することが出来る。
    object_list = Book.objects.order_by('category')
    # 「render」関数を使う時、１つ目の引数は「request」を記述する。
    # ２つ目の引数にhtmlファイルを「template」として使うことが出来る。
    # ３つ目の引数には「context」を指定する。辞書型データ（左がkey、右がvalue）である。keyを呼び出すことでvalueを呼び出す。
    # 「 {'object_list': object_list}」はBookモデルの全データを「object_list」（右）で呼び出せるようにしている。
    return render(request, 'book/index.html', {'object_list': object_list})

class CreateReviewView(CreateView):
    model = Review
    fields = ('book', 'title', 'text', 'rate')
    template_name = 'book/review_form.html'

    # 「context」は辞書型のデータ。
    # 「**kwargs」はキーワード引数。「urls.py」の「path('book/<int:book_id>/review/', views.CreateReviewView.as_view(), name='review'),」の<int:book_id>が「view」に渡される。
    def get_context_data(self, **kwargs):
        # 「super()」は継承元（CreateViewクラス)のメソッドを呼び出すことを意味する。
        # すなわち、「get_context_data」というメソッドを上書きするために「CreateViewクラス（親クラス）」の「get_context_data」を呼び出す。
        context = super().get_context_data(**kwargs)
        # 「context['book'] 」は、辞書型のデータ（context）にオブジェクトを追加することを意味し、右側にどのオブジェクトを追加するかを記述する。
        # また、「Book.objects.get」という部分は、Bookモデルの全てのデータから「getメソッド」を指定したデータを取得するために記述する。
        # 「kwargs['book_id']」は、URLの中で定義した<int:book_id>に対応し、入力された数字に対応した書籍のデータを取得することが出来る。
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context

	# 「form_valid」はフォームが送信され、その入力内容に間違いが無い場合に、データが保存される前に呼び出されるメソッド。
    def form_valid(self, form):
        # 以下の記述は、「form（Formクラス）」の「instance（フォームが作成された時に作られるデータ」に「user」という属性でデータを追加することを意味する。
        # 「self.request.user」は、ユーザーがログインしている場合の「request」オブジェクトに入っている「user」の情報（ログインしているユーザーの情報）を意味する。
        form.instance.user = self.request.user

        return super().form_valid(form)

	# クラス変数にコードを書く時は「reverse_lazy」を使用していたが、今回は「get_success_url」のメソッドの中にコードを書くため、「reverse」を使う。
    def get_success_url(self):
        # 「kwargs={'pk': self.object.book.id}」の形でキーワード引数に書籍のidの番号を渡す。
        return reverse('detail-book', kwargs={'pk': self.object.book.id})
