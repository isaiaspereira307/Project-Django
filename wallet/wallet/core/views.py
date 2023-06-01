from django.shortcuts import render
from django.db.models import Sum
from .models import Transacao, Investimento, Bitcoin
import requests
from datetime import date


def carteira(request):
    receita = Transacao.objects.filter(tipo__exact='receita').aggregate(Sum('valor'))['valor__sum'] or 0
    despesa = Transacao.objects.filter(tipo__exact='despesa').aggregate(Sum('valor'))['valor__sum'] or 0
    saldo = receita - despesa
    context = {'receita': receita, 'despesa': despesa, 'saldo': saldo}
    return render(request, 'core/carteira.html', context)


def investimentos(request):
    investimentos = Investimento.objects.all()
    total_rendimentos = 0
    for investimento in investimentos:
        rendimento = (investimento.valor_investido * investimento.rentabilidade) / 100
        dias = (date.today() - investimento.data_investimento).days
        rendimento_total = rendimento * dias / 365
        total_rendimentos += rendimento_total
        investimento.rendimento_total = rendimento_total
    context = {'investimentos': investimentos, 'total_rendimentos': total_rendimentos}
    return render(request, 'core/investimentos.html', context)


def bitcoin(request):
    cotacao = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BRL.json').json()['bpi']['USD']['rate_float']
    cotacao_real = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BRL.json').json()['bpi']['BRL']['rate_float']
    bitcoins = Bitcoin.objects.all()
    total_bitcoins = 0
    total_dolares = 0
    total_reais = 0
    for bitcoin in bitcoins:
        total_bitcoins += float(bitcoin.quantidade)
        total_dolares += float(bitcoin.quantidade) * cotacao
        total_reais += float(bitcoin.quantidade) * cotacao_real
    context = {
        'total_bitcoins': total_bitcoins,
        'total_dolares': total_dolares,
        'total_reais': total_reais
    }
    return render(request, 'core/bitcoin.html', context)



def dashboard(request):
    transacoes = Transacao.objects.all()
    investimentos = Investimento.objects.all()
    bitcoins = Bitcoin.objects.all()
    context = {
        'transacoes': transacoes,
        'investimentos': investimentos,
        'bitcoins': bitcoins
    }
    return render(request, 'core/dashboard.html', context)
