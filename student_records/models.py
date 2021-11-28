from django.db import models


class StudentRecord(models.Model):
  first_name        = models.CharField(max_length=50)
  last_name         = models.CharField(max_length=50)
  dob               = models.CharField(max_length=50)
  address           = models.CharField(max_length=100)
  phone             = models.CharField(max_length=50)
  email             = models.CharField(max_length=100)
  date_of_enrollment = models.DateField(auto_now_add=True)
  quiz_score        = models.IntegerField(default=0)
  python_entry_level = models.BooleanField(default=False)
  aws_practitioner_exam = models.BooleanField(default=False)
  python_associate_exam = models.BooleanField(default=False)
  blockchain_exam = models.BooleanField(default=False)
  aws_ml_exam = models.BooleanField(default=False)
  dissertation = models.BooleanField(default=False)
  date_of_graduation = models.DateField(auto_now_add=True)
  job_placement = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


