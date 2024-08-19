# что можно улучшить? 
# нужно обработать все краевые случаи!
# можно ли запустить транзакцию прямо перед сохранением баланса? 
# то есть можно ли достать записи, проверить баланс, а потом сохранить это дело? (SELECT vs SELECT FOR UPDATE)

def transfer_money_view(request, user1_id, user2_id, money):
    u1 = User.objects.get(id=user1_id)
    u1.balance -= money
    u1.save()
    u2 = User.objects.get(id=user2_id)
    u2.balance += money
    u2.save()
    return JsonResponse({'status': 'ok'}, status=200)
