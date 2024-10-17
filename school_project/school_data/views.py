from django.shortcuts import render

# Create your views here.
# school_data/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import SchoolData
from .forms import SchoolDataForm

def create_school(request):
    form = SchoolDataForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('school_list')
    return render(request, 'school_data/school_form.html', {'form': form})

def update_school(request, schl):
    school = get_object_or_404(SchoolData, schl=schl)
    form = SchoolDataForm(request.POST or None, instance=school)
    if form.is_valid():
        form.save()
        return redirect('school_list')
    return render(request, 'school_data/school_form.html', {'form': form})

def delete_school(request, schl):
    school = get_object_or_404(SchoolData, schl=schl)
    school.delete()
    return redirect('school_list')

def school_list(request):
    schools = SchoolData.objects.all()
    return render(request, 'school_data/school_list.html', {'schools': schools})

def school_detail(request, schl):
    school = get_object_or_404(SchoolData, schl=schl)
    return render(request, 'school_data/school_detail.html', {'school': school})
