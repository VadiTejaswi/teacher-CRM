from django.shortcuts import render,redirect

from .models import Teacher
def teach(request):
    all_teachers=Teacher.objects.all()
    return render(request,'index.html',{"teachers":all_teachers})


def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')  # for file upload like image

        teacher = Teacher(
            name=name,
            subject=subject,
            contact=contact,
            email=email,
            image=image if image else None
        )
        teacher.save()
        return redirect("all-teachers")

    return render(request, 'index.html')


def edit_teacher(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')  # for file upload like image

        teacher = Teacher(
            id=id,
            name=name,
            subject=subject,
            contact=contact,
            email=email,
            image=image if image else None
        )
        teacher.save()
        return redirect("all-teachers",)

    return render(request, 'index.html',{'teacher':"teacher"})

def deleted(request, id):
    Teacher.objects.filter(id=id).delete()  # this deletes all matches (usually one)
    return redirect("all-teachers")

   
    

    