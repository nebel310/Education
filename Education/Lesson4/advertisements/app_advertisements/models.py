from django.db import models

class Advertisements(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, default=0)  # Значение по умолчанию
    auction = models.BooleanField('торг', help_text='Выберете, если возможен торг')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})>"

    class Meta:
        db_table = 'advertisements'
