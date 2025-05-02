from django.shortcuts import render,get_object_or_404
from .models import Student
from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 
# Create your views here.
def student_list(request):
    query=request.GET.get('q')
    subject=request.GET.get('subject')
    threshold=request.GET.get('threshold')
    students=Student.objects.all()
    if query:
        students=students.filter(name__icontains=query)
    if subject and threshold:
        try:
            threshold=int(threshold)
            if subject in ['subject1','subject2','subject3']:
                students=students.filter(**{f'{subject}__gte':threshold})
        except ValueError:
            pass



    students=students.order_by('-total')
    for i,student in enumerate(students,start=1):
        student.rank=i 

    paginator=Paginator(students,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'student_list.html',{'page_obj':page_obj})

def student_detail(request,pk):
    student=get_object_or_404(Student,pk=pk)
    students=list(Student.objects.all().order_by('-total'))
    rank=students.index(student)+1
    return render(request,'student_detail.html',{'student':student,'rank':rank})


def render_to_pdf(template_src,context_dict):
    template=get_template(template_src)
    html=template.render(context_dict)
    response=HttpResponse(content_type='application/pdf')
    pisa_status=pisa.CreatePDF(html,dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating response',status=500)
    return response

def student_pdf(request,pk):
    student=get_object_or_404(Student,pk=pk)
    students=list(Student.objects.order_by('-total'))
    rank=students.index(student)+1
    return render_to_pdf('student_pdf.html',{'student':student,'rank':rank})