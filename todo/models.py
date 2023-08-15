from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=40)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text + ("  ✅" if self.completed else "  ❌")
