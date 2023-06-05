from django.shortcuts import render
from .models import Terminals



def switch_status(request):
    terminals = Terminals.objects.all()
    return render(request, 'switch_app/switch_status.html', {'terminals': terminals})

def alert_report(request):
    unreachable_switches = Terminals.objects.filter(t1=0, t2=0, t3=0, t4=0, t5=0)
    return render(request, 'switch_app/alert_report.html', {'unreachable_switches': unreachable_switches})


