from django.db import models

class Task(models.Model):
    # Priority choices
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    # Status choices
    STATUS_CHOICES = [
        ('done', 'Done'),
        ('in_progress', 'In Progress'),
        ('pending', 'Pending'),
        ('backlog', 'Backlog'),
        ('closed', 'Closed'),
    ]

    # Fields
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100,null=True,blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    deadline = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task (Priority: {self.priority}, Status: {self.status})"
