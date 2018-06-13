# a = obj()
# a.save()
# id = a.pk

# falcon rest api
# https://habr.com/post/347064/


# model class meta

# index_together = ["pub_date", "deadline"]
# Unique_together = ['text', 'checked']

# abstract = True, эта модель будет абстрактной моделью

# Название таблицы в базе данных для этой модели:
# db_table = 'music_album'

# proxy = True, модель унаследованная от другой модели
# будет создана как proxy-модель.


# Fields

# help_text="Please use the following format: <em>YYYY-MM-DD</em>."
# валидатор полей
# Field.validators

# Field.choices
# YEAR_IN_SCHOOL_CHOICES = (
#     ('FR', 'Freshman'),
#     ('SO', 'Sophomore'),
#     ('JR', 'Junior'),
#     ('SR', 'Senior'),
# )

# DurationField => timedelta
# datetime.datetime.timedelta()

# придумати проект

# CASCADE, SET_NULL, PROTECT, SET_DEFAULT, DO_NOTHING

# objects =models.Manager()
# Book.with_author.all()
# Book.with_author.filter()

# Book.with_author.with_tag('test')

# .agregate()
# .anotate()
# models.Q(book__int__gt=10) | models.Q(book__int__lt=2)
# models.F() сравнить 2 филды одной модели
