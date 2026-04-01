from django.shortcuts import render
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
# ブランチ切り替え
