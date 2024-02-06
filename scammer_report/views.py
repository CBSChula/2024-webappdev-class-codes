from django.shortcuts import render
from .models import ScammerReport
from django.http import HttpResponseRedirect

def report_list(request):
    reports = ScammerReport.objects.all()
    return render(request, 'scammer_report/report_list.html', {'reports': reports})

def add_report(request):
    if request.method == "POST":
        reporter_name = request.POST.get('reporter_name')
        scammer_phone = request.POST.get('scammer_phone')
        telecom_provider = request.POST.get('telecom_provider')
        description = request.POST.get('description')
        ScammerReport.objects.create(reporter_name=reporter_name, scammer_phone=scammer_phone, 
        telecom_provider=telecom_provider, description=description)
        return HttpResponseRedirect('/scammer_reports')
    return render(request, 'scammer_report/add_report.html')