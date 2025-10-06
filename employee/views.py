
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee    

# Create your views here.
# create view for home page

def create_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
            return redirect('list')
    else:
        form = EmployeeForm()
    return render(request, 'create.html', {'form': form})


# create view for list page
def list_employee(request):
    employee = Employee.objects.all()
    return render(request, 'list.html', {'employees': employee}) 

# create view for update page
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form': form})

# create view for delete page
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('list')
    return render(request, 'delete.html', {'employee': employee})



