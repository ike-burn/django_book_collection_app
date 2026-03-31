from django.urls import path

from . import views

urlpatterns = [
    path('book/', views.ListBookView.as_view()),
    # 「pk」はプライマリーキー（重複しない通し番号）、Djangoが自動的に作成するidに紐付けられる（「0002_auto_20260329_1434.py」を参照）
    path('book/<int:pk>/detail/', views.DetailBookView.as_view()),
]

# ブランチ切り替え
