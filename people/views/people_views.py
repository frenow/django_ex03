from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from ..models import Pessoa, Endereco

@require_http_methods(["GET","POST"])
def home(request):
	return HttpResponse("Olá, requisição feita com sucesso!")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	result = Pessoa.objects.all()
	#result = Pessoa.objects.retorna_C()
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar(request, id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)
	context = {'pessoa':pessoa}
	return render(request, 'detalhe.html', context)

#query costumizada filtro idade = 20
def querycustom1(request):
	pessoa = Pessoa.objects.filter(idade = 20)
	context = {'pessoa': pessoa}
	return render(request, 'detalhe.html', context)

#query costumizada filtro nasceu em 01/01/1980
def querycustom2(request):
	pessoa = Pessoa.objects.filter(data_nascimento = '1980-01-01')
	context = {'pessoa': pessoa}
	return render(request, 'detalhe.html', context)

#query costumizada listagem dos 3 primeiros registros
def querycustom3(request):
	result = Pessoa.objects.all()[:3]
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

#query costumizada filtro nome like/contem 'emerson'
def querycustom4(request):
	pessoa = Pessoa.objects.get(nome__contains='emerson')
	context = {'pessoa': pessoa}
	return render(request, 'detalhe.html', context)

def excluir(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		pessoa.delete()		
		return HttpResponse(f"Excluiu {pessoa.nome} (id={pessoa.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

def cadastro(request):
	sexos = ['Masculino','Feminino']
	template = loader.get_template('cadastrar.html')
	context = {
		'sexos': sexos,
	}
	return HttpResponse(template.render(context, request))

def cadastrar(request):
	dtNascimento = datetime.strptime(request.POST['dtNascimento'], "%d/%m/%Y").date()
	p = Pessoa.objects.nova(
			request.POST['nome'],
			request.POST['idade'],
			dtNascimento,
			request.POST['cpf'],
			request.POST['logradouro'],
			request.POST['numero'],
			request.POST['bairro'],
			request.POST['cep'])

	return HttpResponse(f"{p} cadastrado com sucesso")