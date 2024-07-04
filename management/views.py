from django.shortcuts import render, redirect
from .models import Student, Teacher, Expense

def index(request):
    return render(request, 'index.html')

def students(request):
    if request.method == 'POST':
        name = request.POST['name']
        fees_paid = request.POST['fees_paid']
        fees_pending = request.POST['fees_pending']
        Student.objects.create(name=name, fees_paid=fees_paid, fees_pending=fees_pending)
        return redirect('students')
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.fees_paid = request.POST['fees_paid']
        student.fees_pending = request.POST['fees_pending']
        student.save()
        return redirect('students')
    return render(request, 'update_student.html', {'student': student})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('students')

def teachers(request):
    if request.method == 'POST':
        name = request.POST['name']
        salary_paid = request.POST['salary_paid']
        salary_needed = request.POST['salary_needed']
        Teacher.objects.create(name=name, salary_paid=salary_paid, salary_needed=salary_needed)
        return redirect('teachers')
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def update_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        teacher.name = request.POST['name']
        teacher.salary_paid = request.POST['salary_paid']
        teacher.salary_needed = request.POST['salary_needed']
        teacher.save()
        return redirect('teachers')
    return render(request, 'update_teacher.html', {'teacher': teacher})

def delete_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect('teachers')

def expenses(request):
    if request.method == 'POST':
        description = request.POST['description']
        amount = request.POST['amount']
        Expense.objects.create(description=description, amount=amount)
        return redirect('expenses')
    expenses = Expense.objects.all()
    return render(request, 'expenses.html', {'expenses': expenses})

def update_expense(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == 'POST':
        expense.description = request.POST['description']
        expense.amount = request.POST['amount']
        expense.save()
        return redirect('expenses')
    return render(request, 'update_expense.html', {'expense': expense})

def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('expenses')

def calculate(request):
    total_fees = sum(student.fees_paid for student in Student.objects.all())
    pending_fees = sum(student.fees_pending for student in Student.objects.all())
    total_salary_paid = sum(teacher.salary_paid for teacher in Teacher.objects.all())
    total_salary_needed = sum(teacher.salary_needed for teacher in Teacher.objects.all())
    total_expenses = sum(expense.amount for expense in Expense.objects.all())
    profit = total_fees - total_salary_paid - total_expenses

    return render(request, 'calculate.html', {
        'total_fees': total_fees,
        'pending_fees': pending_fees,
        'total_salary_paid': total_salary_paid,
        'total_salary_needed': total_salary_needed,
        'total_expenses': total_expenses,
        'profit': profit
    })
