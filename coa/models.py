from django.db import models

# Create your models here.
class facilityGoal(models.Model):
    facility = models.CharField(max_length=10)
    goalType = models.CharField(max_length=100)
    goalDuration = models.CharField(max_length=100)
    goalAmount = models.IntegerField()

    def __str__(self):
        return(self.goalType + ' - ' + self.facility)

class coaEntry(models.Model):
        #these 2 will be added behind the scenes
        dateEntered = models.DateField(auto_now_add=True, verbose_name='Date Entered')
        facility = models.CharField(max_length=10, verbose_name='Facility')
        enteringUser = models.CharField(max_length=10, verbose_name='Interviewer')


        #these will be filled in from the question back
        questionOne = models.CharField(max_length=1000, verbose_name='Question One')
        questionTwo = models.CharField(max_length=1000, verbose_name='Question Two')
        questionThree = models.CharField(max_length=1000, verbose_name='Question Three')

        #these are the fields entered
        askedUser = models.CharField(max_length=10, verbose_name='Associate Login')
        answerOne = models.CharField(max_length=1000, verbose_name='Answer One')
        answerTwo = models.CharField(max_length=1000, verbose_name='Answer Two')
        answerThree = models.CharField(max_length=1000, verbose_name='Answer Three')

        def __str__(self):
            return(self.facility + ' - ' + self.enteringUser + ' - ' + self.askedUser + ' - ' + str(self.dateEntered))

class coaQuestionBank(models.Model):
        facility = models.CharField(max_length=10)
        startDate = models.DateField()
        endDate = models.DateField()

        questionOne = models.CharField(max_length=1000)
        questionTwo = models.CharField(max_length=1000)
        questionThree = models.CharField(max_length=1000)

        def __str__(self):
            return(self.facility + ' Start Date: ' + str(self.startDate) + ' End Date: ' + str(self.endDate))