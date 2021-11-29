from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import StudentRecord 
from blockchain_records.models import Block


def get_student_fields(request) -> dict:
  student_fields = dict(first_name=request.POST['firstname'],
                        last_name=request.POST['lastname'],
                        dob=request.POST['dob'],
                        address=request.POST['address'],
                        phone=request.POST['phone'],
                        email=request.POST['email'],
                        date_of_enrollment=request.POST['date_of_enrollment'],
                        quiz_score=request.POST['quiz_score'],
                        python_entry_level=request.POST['python_entry_level'],
                        aws_practitioner_exam=request.POST.get('aws_practitioner_exam', False),
                        python_associate_exam=request.POST['python_associate_exam'],
                        blockchain_exam=request.POST['blockchain_exam'],
                        aws_ml_exam=request.POST['aws_ml_exam'],
                        # dissertation=request.POST['dissertation'],
                        date_of_graduation=request.POST['date_of_graduation'],
                        job_placement=request.POST['job_placement'],
                        # bio = request.POST.get('bio', False),
                        )
  return student_fields

@login_required(login_url='/')
def add_record(request):
  if request.method == 'POST':
    student_fields = get_student_fields(request)

    student = StudentRecord.objects.create(
                **student_fields
              )

    block_qs = Block.objects.all()

    previous_block = None
    if len(block_qs) > 0:
      previous_block = Block.objects.order_by('-timestamp')[0]

    Block.objects.create(
        previous_block=previous_block, 
        action="Add",
        data=student, 
        nonce=len(block_qs)
      )

  return redirect('transactions')

@login_required(login_url='/')
def update_record(request):
  if request.method =='POST':
    record_id = request.POST['id']
    # student_bio = request.POST.get('bio', False)
    student_fields = get_student_fields(request)
    # student_fields['bio'] = student_bio

    # get and update the record fields
    record_qs = StudentRecord.objects.filter(id=record_id)
    record_qs.update(**student_fields)

    block_queryset = Block.objects.all()
    previous_block = Block.objects.order_by('-timestamp')[0]

    Block.objects.create(
      previous_block=previous_block, 
      action="Update",
      data=record_qs[0],
      nonce=len(block_queryset)
    )

  return redirect('student', id=record_id)

@login_required(login_url='/')
def delete_record(request):
  if request.method =='POST':
    record_id = request.POST['id']
    record = StudentRecord.objects.get(id=record_id)

    block_queryset = Block.objects.all()
    previous_block = Block.objects.order_by('-timestamp')[0]

    Block.objects.create(
      previous_block=previous_block, 
      action="Remove",
      data=record,
      nonce=block_queryset
    )
    record.delete()

  return redirect('transactions')
