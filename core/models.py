from django.db import models


class Class(models.Model):
    id_staff = models.ForeignKey(
        "Staff", models.DO_NOTHING, db_column="id_staff", blank=True, null=True
    )
    class_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = "class"

    def __str__(self):
        return self.class_name


class Lesson(models.Model):
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = "lesson"

    def __str__(self):
        return f"{self.pk}: {self.start_time} - {self.end_time}"


class Role1(models.Model):
    name1 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = "role1"

    def __str__(self):
        return self.name1


class Schedule(models.Model):
    id_wk = models.ForeignKey(
        "Weekday1", models.DO_NOTHING, db_column="id_wk", blank=True, null=True
    )
    id_lesson = models.ForeignKey(
        Lesson, models.DO_NOTHING, db_column="id_lesson", blank=True, null=True
    )
    id_class = models.ForeignKey(
        Class, models.DO_NOTHING, db_column="id_class", blank=True, null=True
    )
    id_section = models.ForeignKey(
        "Section", models.DO_NOTHING, db_column="id_section", blank=True, null=True
    )
    id_staff = models.ForeignKey(
        "Staff", models.DO_NOTHING, db_column="id_staff", blank=True, null=True
    )
    room_number = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "schedule"

    def __str__(self):
        return f"{self.pk} - {self.room_number}"


class Section(models.Model):
    id_staff = models.ForeignKey(
        "Staff", models.DO_NOTHING, db_column="id_staff", blank=True, null=True
    )
    advisor = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = "section"

    def __str__(self):
        return self.advisor


class Staff(models.Model):
    name_staff = models.CharField(max_length=20, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    roles = models.ManyToManyField(Role1, related_name="staffs")

    class Meta:
        db_table = "staff"

    def __str__(self):
        return self.name_staff


class Student(models.Model):
    id_section = models.ForeignKey(
        Section, models.DO_NOTHING, db_column="id_section", blank=True, null=True
    )
    name_student = models.CharField(max_length=20, blank=True, null=True)
    roll_no = models.CharField(max_length=20, blank=True, null=True)
    amount_fee = models.IntegerField(blank=True, null=True)
    fee_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.name_student


class Weekday1(models.Model):
    name_of_day = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = "weekday1"

    def __str__(self):
        return self.name_of_day
