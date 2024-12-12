import json

from django.shortcuts import render

from django.core.paginator import Paginator
from django.db.models import Count, Avg
import matplotlib.pyplot as plt
import io
import urllib, base64
from .models import SchoolData
from django.shortcuts import render, get_object_or_404, redirect
from .models import SchoolData
from .forms import SchoolDataForm


# def create_school(request):
#     form = SchoolDataForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('school_list')
#     return render(request, 'school_data/school_form.html', {'form': form})
#
# def update_school(request, schl):
#     school = get_object_or_404(SchoolData, schl=schl)
#     form = SchoolDataForm(request.POST or None, instance=school)
#     if form.is_valid():
#         form.save()
#         return redirect('school_list')
#     return render(request, 'school_data/school_form.html', {'form': form})
#
# def delete_school(request, schl):
#     school = get_object_or_404(SchoolData, schl=schl)
#     school.delete()
#     return redirect('school_list')
#
# def school_list(request):
#     schools = SchoolData.objects.all()
#     return render(request, 'school_data/school_list.html', {'schools': schools})
#
# def school_detail(request, schl):
#     school = get_object_or_404(SchoolData, schl=schl)
#     return render(request, 'school_data/school_detail.html', {'school': school})


def school_list(request):
    query = request.GET.get('q', '')
    if query:
        schools = SchoolData.objects.filter(name__icontains=query)
    else:
        schools = SchoolData.objects.all()

    paginator = Paginator(schools, 10)  # Show 10 schools per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Generate statistics and plot
    total_schools = schools.count()
    avg_enrollment = schools.aggregate(Avg('school_enrollment'))['school_enrollment__avg'] or 0
    fig, ax = plt.subplots()
    ax.bar(['Total Schools', 'Average Enrollment'], [total_schools, avg_enrollment])
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    context = {
        'query': query,
        'page_obj': page_obj,
        'statistics_image': uri,
        'income_compare_image': income_compare(schools)
    }
    return render(request, 'school_list.html', context)


def income_compare(schools):
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
    string = base64.b64encode(buffer.read())
    uri = urllib.parse.quote(string)
    return uri


def school_detail(request, pk):
    school = get_object_or_404(SchoolData, schl=pk)
    return render(request, 'school_detail.html', {'school': school})


def school_create(request):
    if request.method == "POST":
        form = SchoolDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolDataForm()
    return render(request, 'school_form.html', {'form': form})


def school_update(request, pk):
    school = get_object_or_404(SchoolData, schl=pk)
    if request.method == "POST":
        form = SchoolDataForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolDataForm(instance=school)
    return render(request, 'school_form.html', {'form': form})


def school_delete(request, pk):
    school = get_object_or_404(SchoolData, schl=pk)
    if request.method == "POST":
        school.delete()
        return redirect('school_list')
    return render(request, 'school_confirm_delete.html', {'school': school})


def get_counties(request, district):
    counties = SchoolData.objects.filter(district_name=district).values_list('school_address_city',
                                                                             flat=True).distinct()
    return JsonResponse(list(counties), safe=False)

def region_comparison(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            regions_data = data.get('regions', {})
            region_1_name = regions_data.get('region_1')
            region_2_name = regions_data.get('region_2')

            if not region_1_name or not region_2_name:
                return JsonResponse({"error": "Please select two regions."}, status=400)

            selected_fields = data.get('fields', [])
            if not isinstance(selected_fields, list) or not selected_fields:
                return JsonResponse({"error": "Please select at least one field to compare."}, status=400)
            def calculate_region_average(region_name):
                schools_in_region = SchoolData.objects.filter(district_name=region_name)
                averages = {}
                for field in selected_fields:
                    values = schools_in_region.values_list(field, flat=True).exclude(**{field: None})
                    averages[field] = sum(values, 0) / len(values) if values else 0
                return averages

            region_1_avg = calculate_region_average(region_1_name)
            region_2_avg = calculate_region_average(region_2_name)

            fig, ax = plt.subplots(figsize=(10, 6))
            bar_width = 0.35
            index = range(len(selected_fields))

            for idx, field in enumerate(selected_fields):
                value_region_1 = region_1_avg[field]
                value_region_2 = region_2_avg[field]

                ax.bar([idx - bar_width/2], [value_region_1], bar_width, label=f'{region_1_name}' if idx == 0 else "", color='b')
                ax.bar([idx + bar_width/2], [value_region_2], bar_width, label=f'{region_2_name}' if idx == 0 else "", color='r')

                ax.text(idx - bar_width/2, value_region_1, f'{value_region_1:.2f}', ha='center', va='bottom')
                ax.text(idx + bar_width/2, value_region_2, f'{value_region_2:.2f}', ha='center', va='bottom')

            ax.set_xlabel('Fields')
            ax.set_ylabel('Average Values')
            ax.set_title(f'Comparison between {region_1_name} and {region_2_name}')
            ax.set_xticks(index)
            ax.set_xticklabels([field for field in selected_fields])
            ax.legend()

            buf = io.BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            string = base64.b64encode(buf.read()).decode('utf-8')
            comparison_image = f"data:image/png;base64,{urllib.parse.quote(string)}"

            return JsonResponse({
                'comparison_image': comparison_image,
                'selected_fields': selected_fields,
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

    elif request.method == 'GET':
        districts = SchoolData.objects.values_list('district_name', flat=True).distinct()
        return render(request, 'region_comparison.html', {
            'regions': list(districts),
        })

    else:
        return JsonResponse({"error": "Method not allowed."}, status=405)

def get_schools(request, district, county):
    schools = SchoolData.objects.filter(district_name=district, school_address_city=county).values('schl', 'name')
    return JsonResponse(list(schools), safe=False)


def school_comparison(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # 直接获取并验证学校信息
            schools_data = data.get('schools', {})
            school_1_data = schools_data.get('school_1')
            school_2_data = schools_data.get('school_2')

            if not school_1_data or not school_2_data:
                return JsonResponse({"error": "Please select two schools."}, status=400)

            # 获取学校ID并查询数据库
            try:
                school_1 = SchoolData.objects.get(pk=school_1_data['school'])
                school_2 = SchoolData.objects.get(pk=school_2_data['school'])
            except SchoolData.DoesNotExist:
                return JsonResponse({"error": "One of the selected schools does not exist."}, status=400)

            # 获取并验证比较字段
            selected_fields = data.get('fields', [])
            if not isinstance(selected_fields, list) or not selected_fields:
                return JsonResponse({"error": "Please select at least one field to compare."}, status=400)

            # 确保我们有两所学校和至少一个字段用于比较
            if not (school_1 and school_2 and selected_fields):
                return JsonResponse({"error": "Invalid data for comparison."}, status=400)

            # 生成对比图表
            fig, ax = plt.subplots(figsize=(10, 6))
            bar_width = 0.35
            index = range(len(selected_fields))

            bars_school_1 = []
            bars_school_2 = []

            for idx, field in enumerate(selected_fields):
                values_school_1 = getattr(school_1, field, 0)
                values_school_2 = getattr(school_2, field, 0)

                # 分别为每个学校绘制柱状图，并保存返回的BarContainer对象用于后续添加文本
                bar1 = ax.bar([idx - bar_width / 2], [values_school_1], bar_width,
                              label=f'School 1: {field}' if idx == 0 else "", color='b')
                bar2 = ax.bar([idx + bar_width / 2], [values_school_2], bar_width,
                              label=f'School 2: {field}' if idx == 0 else "", color='r')

                bars_school_1.append(bar1)
                bars_school_2.append(bar2)

                # 在每个柱子上方添加数值标签
                ax.text(idx - bar_width / 2, values_school_1, f'{values_school_1}', ha='center', va='bottom')
                ax.text(idx + bar_width / 2, values_school_2, f'{values_school_2}', ha='center', va='bottom')

            ax.set_xlabel('Fields')
            ax.set_ylabel('Values')
            ax.set_title('Comparison between Schools')
            ax.set_xticks(index)
            ax.set_xticklabels([field.replace('_', ' ').capitalize() for field in selected_fields])
            ax.legend()

            buf = io.BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight')  # 使用bbox_inches='tight'以确保标签不会被裁剪
            buf.seek(0)
            string = base64.b64encode(buf.read()).decode('utf-8')
            comparison_image = f"data:image/png;base64,{urllib.parse.quote(string)}"

            # 返回JSON响应
            return JsonResponse({
                'comparison_image': comparison_image,
                'selected_fields': selected_fields,
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

    elif request.method == 'GET':
        districts = SchoolData.objects.values_list('district_name', flat=True).distinct()
        return render(request, 'school_comparison.html', {
            'districts': districts,
        })

    else:
        return JsonResponse({"error": "Method not allowed."}, status=405)

def index(request):
    return render(request, 'index.html')


import matplotlib

matplotlib.use('Agg')  # Set the backend to Agg to avoid GUI issues

import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
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
