from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	DeleteView,
	UpdateView,
)
from .models import Book

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

def logout_view(request):
    logout(request)
    return redirect('index')
