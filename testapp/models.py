from django.db import models

# Create your models here.

type_choices = (
    ('Легковой', 'Легковой'),
    ('Грузовой', 'Грузовой'),
    ('Тягач', 'Тягач'),
)

payment_choices = (
    ('Налик', 'Налик'),
    ('Картой', 'Картой'),
    ('СБП', 'СБП'),
)

status_choices = (
    ('Ожидание ответа', 'Ожидание ответа'),
    ('В обработке', 'В обработке'),
    ('Услуга оказана', 'Услуга оказана'),
)


class Zayavka(models.Model):
    type = models.CharField(max_length=30, verbose_name="Тип авто", choices=type_choices)
    datetime = models.DateTimeField(verbose_name="Дата и время записи")
    payment = models.CharField(max_length=30, verbose_name="Способ оплаты", choices=payment_choices)
    status = models.CharField(max_length=30, verbose_name="Статус заявки", choices=status_choices, default="Ожидание ответа")

    def __str__(self):
        return f"{self.type} | {self.status}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"