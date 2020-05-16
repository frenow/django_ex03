from django.urls import path

from .views import people_views as pv

urlpatterns = [
	path('', pv.home, name="index"),
	path('listar/', pv.listar, name="listar"),
	path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
	path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
	path('cadastro/', pv.cadastro, name="cadastro"),
	path('cadastrar/', pv.cadastrar, name="cadastrar"),
	path('querycustom1/', pv.querycustom1, name="querycustom1"),
	path('querycustom2/', pv.querycustom2, name="querycustom2"),
	path('querycustom3/', pv.querycustom3, name="querycustom3"),
	path('querycustom4/', pv.querycustom4, name="querycustom4")
]