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



import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg to avoid GUI issues

import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
from .models import SchoolData

# View for rendering the histogram for Test Scores
def test_scores_histogram(request):
    schools = SchoolData.objects.all()
    test_scores = [school.test_scores for school in schools]

    plt.figure(figsize=(10, 6))
    plt.hist(test_scores, bins=10, edgecolor='black', color='green')
    plt.title('Histogram of Test Scores')
    plt.xlabel('Test Scores')
    plt.ylabel('Number of Schools')

    # Save the plot to a BytesIO object and return as a response
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')


import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg to avoid GUI issues

import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
from .models import SchoolData

def low_income_histogram(request):
    schools = SchoolData.objects.all()
    low_income_values = [school.low_income_percentage for school in schools]

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.hist(low_income_values, bins=10, edgecolor='black', color='blue')
    plt.title('Histogram of Low Income Percentage')
    plt.xlabel('Low Income Percentage')
    plt.ylabel('Number of Schools')

    # Save the plot to a BytesIO object and return as a response
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')


