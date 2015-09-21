from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class Reactive(models.Model):
	cas = models.CharField(u'Регистрационный номер CAS', max_length=12, 
		validators=[RegexValidator(r'^\d\d-\d\d-\d$')])
	iupac = models.CharField(u'Наименование по номенклатуре ИЮПАК', max_length=300)
	rational = models.CharField(u'Наименование по рациональной номенклатуре', max_length=300, blank=True)
	trivial = models.CharField(u'Тривиальное наименование', max_length=300, blank=True)
	formula = models.CharField(u'Брутто формула', max_length=50)
	img = models.ImageField(u'Графическое изображение', blank=True)
	mm = models.PositiveIntegerField(u'Молярная масса')
	appearance = models.CharField(u'Внешний вид', max_length=150, blank=True)
	mp = models.SmallIntegerField(u'Температура плавления', blank=True)
	bp = models.SmallIntegerField(u'Температура кипения', blank=True)

	def __unicode__(self):
		return self.iupac


class LabEquipment(models.Model):
	EQUIPMENT_CHOICES = (
        ('GLASS', 'стеклянная посуда'),
        ('', 'стеклянная посуда'),
        ('glass', 'стеклянная посуда'),
    )
	equipment_type = models.CharField(max_length=5, choices=EQUIPMENT_CHOICES)
	item = models.CharField(max_length=50)


class Analysis(models.Model):
	METHOD_CHOICES = (
        ('NMR', 'ЯМР'),
        ('IR', 'ИК'),
        ('GPC', 'ГПХ'),
        ('ELEM', 'Элементный'),
        ('MASS', 'Масс-спектроскопия'),
        ('MALDI', 'MALDI-TOF спектроскопия'),
        ('CMASS', 'Хромато-масс спектроскопия'),
    )
    stage = models.ForeignKey(Stage)
    method = models.CharField(max_length=5, choices=METHOD_CHOICES)
    sample_id = models.CharField(max_length=10)
    spectrum_id = models.CharField(max_length=10)
    data = models.FileField()
    img = models.ImageField()

    def __unicode__(self):
		return self.method


class Synthesis(models.Model):
	date = models.DateField()
	description = models.TextField(u'Краткое описание', max_length=1000, blank=True)
	products = ManyToManyField(Reactive, through=)   #!!!
	tags = models.CharField(max_length=500)
	literature = models.ManyToManyField(Literature)
	yield_percent = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])


def __unicode__(self):
		return self.date


class Stage(models.Model):
	synthesis = models.ForeignKey(Synthesis)
	date = models.DateField()
	name = models.CharField(max_length=300)
	description = models.TextField(max_length=1000)
	reactives = ManyToManyField(through=)   #!!!
	solvent = ManyToManyField(through=)    #!!!
	is_complex = models.BooleanField(default=False)
	t = models.IntegerField(default=20)
	p = models.IntegerField(default=765)
	start = models.TimeField()
	end = models.TimeField()
	yield_percent = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

