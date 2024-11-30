from django.db import models

# Создайте в приложении task1 следующие модели:
# 1. Buyer - модель представляющая покупателя.
class Buyer(models.Model):
    # Обладает следующими полями:
    # name - имя покупателя(username аккаунта)
    name = models.CharField(max_length=100)
    # balance - баланс(DecimalField)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    # age - возраст.
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# 2. Game - модель представляющая игру.
class Game(models.Model):
    # Обладает следующими полями:
    # title - название игры
    title = models.CharField(max_length=100)
    # cost - цена(DecimalField)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    # size - размер файлов игры(DecimalField)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    # description - описание(неограниченное кол-во текста)
    description = models.TextField()
    # age_limited - ограничение возраста 18+ (BooleanField, по умолчанию False)
    age_limited = models.BooleanField(default=False)
    # buyer - покупатель обладающий игрой (ManyToManyField).
    # У каждого покупателя может быть игра и у каждой игры может быть несколько обладателей.
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
