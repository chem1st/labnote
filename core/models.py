#encoding: UTF-8
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class Reactive(models.Model):
	cas = models.CharField(u'Регистрационный номер CAS', max_length=12, 
		validators=[RegexValidator(r'^\d+-\d\d-\d$')])
	iupac = models.CharField(u'Наименование по номенклатуре ИЮПАК', max_length=300)
	rational = models.CharField(u'Наименование по рациональной номенклатуре', max_length=300, blank=True)
	trivial = models.CharField(u'Тривиальное наименование', max_length=300, blank=True)
	formula = models.CharField(u'Брутто формула', max_length=50)
	img = models.ImageField(u'Графическое изображение', blank=True)
	mm = models.FloatField(u'Молярная масса, г/моль')
	density = models.FloatField(u'Плотность, г/мл')
	appearance = models.CharField(u'Внешний вид', max_length=150, blank=True)
	mp = models.SmallIntegerField(u'Температура плавления, С', blank=True, null=True)
	bp = models.SmallIntegerField(u'Температура кипения, С', blank=True, null=True)

	def __unicode__(self):
		return self.iupac

	class Meta:
		ordering = ['cas', 'iupac']
		verbose_name = 'Реактив'
		verbose_name_plural = 'Реактивы'


class LabEquipment(models.Model):
	EQUIPMENT_CHOICES = (
        ('GLASS', 'стеклянная посуда'),
        ('METAL', 'металлическая посуда'),
        ('ADD', 'дополнительное'),
    )
	equipment_type = models.CharField(max_length=5, choices=EQUIPMENT_CHOICES)
	item = models.CharField(max_length=50)

	class Meta:
		verbose_name = 'Лабораторное оборудование'
		verbose_name_plural = 'Лабораторное оборудование'


class Edition(models.Model):
	PUBFORM_CHOICES = (
        ('JRN', 'Журнал'),
        ('BK', 'Книга'),
        ('RW', 'Очерк'),
        ('THS', 'Тезисы'),
        ('PRT', 'Презентация'),
    )
	pubform = models.CharField(u'Формат издания', max_length=3, choices=PUBFORM_CHOICES)
	title = models.CharField(u'Название', max_length=100)
	publisher = models.CharField(u'Издатель', max_length=100, blank=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['title']
		verbose_name = 'Издание'
		verbose_name_plural = 'Издания'


class Literature(models.Model):
	edition = models.ForeignKey(Edition, verbose_name='Издание')
	title = models.CharField(u'Название', max_length=300)
	author = models.CharField(u'Автор(ы)', max_length=100)
	url = models.URLField(blank=True)

	def __unicode__(self):
		return '%s (%s)' % (self.title, self.author)

	class Meta:
		ordering = ['title']
		verbose_name = 'Литература'
		verbose_name_plural = 'Литература'


class GroupSynthesis(models.Model):
	name = models.CharField(u'Наименование', max_length=100)
	description = models.TextField(u'Описание (макс. 1000 символов)', max_length=1000)
	tags = models.CharField(u'Теги', max_length=500, blank=True)
	literature = models.ManyToManyField(Literature, verbose_name='Литература', blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'Группа'
		verbose_name_plural = 'Группы синтезов'


class Synthesis(models.Model):
	date = models.DateField(u'Дата синтеза')
	group = models.ForeignKey(GroupSynthesis, verbose_name='Группа', blank=True)
	description = models.TextField(u'Описание (макс. 1000 символов)', max_length=1000, blank=True)
	reactives = models.ManyToManyField(Reactive, verbose_name='Реактивы')   #through!!!
	tags = models.CharField(u'Теги', max_length=500, blank=True)
	literature = models.ManyToManyField(Literature, verbose_name='Литература', blank=True)
	yield_percent = models.IntegerField(
		validators=[MinValueValidator(0), MaxValueValidator(100)], 
		verbose_name='Выход целевого продукта, %')

	def __unicode__(self):
		return u'Опыт %s' % str(self.date)

	class Meta:
		ordering = ['-date']
		verbose_name = 'Синтез'
		verbose_name_plural = 'Синтезы'


class Stage(models.Model):
	synthesis = models.ForeignKey(Synthesis, related_name='stages')
	date = models.DateField(u'Дата начала стадии')
	name = models.CharField(u'Наименование', max_length=300)
	description = models.TextField(u'Полное описание')
	reactives = models.ManyToManyField(Reactive, verbose_name='Реактивы', 
		related_name='reactives')   #through!!!
	solvents = models.ManyToManyField(Reactive, verbose_name='Растворитель', 
		related_name='solvents', blank=True)    #through!!!
	is_complex = models.BooleanField(u'У процесса сложный режим температуры и/или давления', 
		default=False)
	t = models.IntegerField(u'Температура, C', default=20)
	p = models.IntegerField(u'Давление, мм.рт.ст.', default=765)
	start = models.TimeField(u'Время начала')
	end = models.TimeField(u'Время окончания')
	yield_percent = models.IntegerField(u'Выход на стадии, %', blank=True, null=True,
		validators=[MinValueValidator(0), MaxValueValidator(100)])

	def __unicode__(self):
		return '%s / %s' % (self.name, self.synthesis)

	class Meta:
		verbose_name = 'Стадия'
		verbose_name_plural = 'Стадии синтеза'


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
    method = models.CharField(u'Метод анализа', max_length=5, choices=METHOD_CHOICES)
    sample_id = models.CharField(u'Номер образца', max_length=10)
    spectrum_id = models.CharField(u'Номер спектра', max_length=10)
    data = models.FileField(u'Полученные данные')
    img = models.ImageField(u'Изображение')

    def __unicode__(self):
        return '%s - образец %s' % (self.method, self.sample_id)

    class Meta:
        ordering = ['sample_id']
        verbose_name = 'Анализ'
        verbose_name_plural = 'Методы анализа'
