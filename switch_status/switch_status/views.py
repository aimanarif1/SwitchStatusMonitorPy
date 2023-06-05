import matplotlib.pyplot as plt
import io
import urllib, base64



def switch_status(request):
    terminals = Terminals.objects.all()
    switch_labels = []
    switch_statuses = []
    for terminal in terminals:
        switch_labels.append(terminal.switch_label)
        switch_statuses.append(1 if terminal.t1 + terminal.t2 + terminal.t3 + terminal.t4 + terminal.t5 > 0 else 0)

    # Generate chart
    plt.bar(switch_labels, switch_statuses)
    plt.xlabel('Switch')
    plt.ylabel('Status')
    plt.title('Switch Status Chart')

    # Save chart to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    # Convert buffer to image URL
    buffer.seek(0)
    image_url = base64.b64encode(buffer.read()).decode()
    image_url = 'data:image/png;base64,' + image_url

    return render(request, 'switch_app/switch_status.html', {'terminals': terminals, 'chart_image': image_url})

def alert_report(request):
    unreachable_switches = Terminals.objects.filter(t1=0, t2=0, t3=0, t4=0, t5=0)
    return render(request, 'switch_app/alert_report.html', {'unreachable_switches': unreachable_switches})
