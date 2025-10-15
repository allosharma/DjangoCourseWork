from django.shortcuts import render, redirect
from tracker.models import Transaction
from django.contrib import messages
from django.db.models import Sum, Case, When, F, Value, FloatField

# Create your views here.
def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        amount = float(amount)

        print(description, amount, type(amount))

        if description is None or amount is None: # or type(amount) == str:
            messages.info(request, 'Please enter valid data')
            return redirect('/')
        
        if amount < 0:
            transaction_type = 'Expense'
        else:
            transaction_type = 'Income'
        
        Transaction.objects.create(
            description=description,
            amount=abs(amount),
            transaction_type=transaction_type # .lower()
        )
        return redirect('/')

    context = {
    'transactions': Transaction.objects.all().order_by('created_at'),
    # 'balance': Transaction.objects.aggregate(total_balance=Sum('amount'))['total_balance'] or 0,
    'balance': Transaction.objects.aggregate(
    total_balance=Sum(
        Case(
            When(transaction_type='Income', then=F('amount')),
            When(transaction_type='Expense', then=-F('amount')),
            default=Value(0),
            output_field=FloatField()
            )
        )
    )['total_balance'] or 0,
    'income': Transaction.objects.filter(transaction_type='Income').aggregate(total_income=Sum('amount'))['total_income'] or 0,
    'expense': Transaction.objects.filter(transaction_type='Expense').aggregate(total_expense=Sum('amount'))['total_expense'] or 0,
}


    # print(context)
    return render(request, 'index.html', context)

def delete_transaction(request, uuid):
    transaction = Transaction.objects.get(uuid=uuid)
    transaction.delete()
    return redirect('/')