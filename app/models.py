from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Greyhound(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    type_greyhound = models.CharField(max_length=50)
    gender = models.CharField(max_length=15)
    gender_abbreviation = models.CharField(max_length=5, null=True, blank=True)
    color = models.CharField(max_length=20)
    color_abbreviation = models.CharField(max_length=10, null=True, blank=True)
    birth_date = models.CharField(max_length=50)
    birth_year = models.IntegerField(null=True, blank=True)
    birth_month = models.IntegerField(null=True, blank=True)
    birth_day = models.IntegerField(null=True, blank=True)
    dam_name = models.CharField(max_length=100, null=True, blank=True)
    sire_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Greyhound'
        verbose_name_plural = 'Greyhounds'


class Races(models.Model):
    id = models.AutoField(primary_key=True)
    race_id = models.IntegerField()
    race_greyhound = models.CharField(max_length=100, default='')
    id_greyhound = models.CharField(max_length=100, default='', blank=True)
    greyhound = models.ForeignKey(Greyhound, on_delete=models.CASCADE)
    avaible = models.BooleanField(default=False)
    avaible_calculate = models.BooleanField(default=False)
    race_date = models.DateField()
    uk_time = models.TimeField()
    br_time = models.TimeField()
    track = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    weight = models.CharField(max_length=50, null=True, blank=True)
    trap = models.IntegerField()
    post_pick_racing_post = models.CharField(max_length=50)
    rpr = models.IntegerField(null=True, blank=True)
    win = models.FloatField(null=True, blank=True)
    timeform_prediction = models.CharField(max_length=50)
    timeform_stars = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    observations = models.TextField()
    odd_back = models.CharField(max_length=10)
    odd_lay = models.CharField(max_length=10)
    num_greyhounds = models.IntegerField()
    start = models.CharField(max_length=20)
    final_time = models.CharField(max_length=20)
    recovery = models.CharField(max_length=20, null=True, blank=True)  # Recuperação
    brt = models.CharField(max_length=20,null=True, blank=True)  # BRT (Brazilian Racing Time)
    avg_position = models.CharField(max_length=10)  # Média Posição
    best_time = models.CharField(max_length=20,null=True, blank=True)  # Melhor tempo
    last_time = models.CharField(max_length=50, blank=True)  # Último Tempo
    avg_time = models.CharField(max_length=50, blank=True)   # Média Tempo
    best_start = models.CharField(max_length=50, blank=True)  # Melhor largada
    last_start = models.CharField(max_length=50, blank=True)  # Ultima Largada
    avg_start = models.CharField(max_length=50, blank=True)  # Média Largada
    last_recovery = models.CharField(max_length=50, blank=True)  # Ultima Recup
    avg_recovery = models.CharField(max_length=50, blank=True)  # Recup Média
    fav_odd_back = models.CharField(max_length=10)  # Fav Odd Back
    fav_odd_lay = models.CharField(max_length=10)  # Fav Odd Lay
    overall_recovery = models.CharField(max_length=550, blank=True) # Overall Recuperação
    overall_brt = models.CharField(max_length=550, blank=True)  # Overall BRT
    overall_avg_position = models.CharField(max_length=550)  # Overall Média Posição
    overall_best_time = models.CharField(max_length=550, blank=True)  # Overall Melhor tempo
    overall_last_time = models.CharField(max_length=550, blank=True)  # Overall Último Tempo
    overall_avg_time = models.CharField(max_length=550, blank=True)  # Overall Média Tempo
    overall_best_start = models.CharField(max_length=550, blank=True)  # Overall Melhor largada
    overall_last_start = models.CharField(max_length=550, blank=True)  # Overall Ultima Largada
    overall_avg_start = models.CharField(max_length=550, blank=True)  # Overall Média Largada
    overall_last_recovery = models.CharField(max_length=550, blank=True)  # Overall Ultima Recup
    overall_avg_recovery = models.CharField(max_length=550, blank=True)  # Overall Recup Média
    overall = models.CharField(max_length=550, blank=True)
    gb_favorite = models.CharField(max_length=550, blank=True)  # Favorito GB (Great Britain)

    def __str__(self):
        return f"{self.race_date} - {self.track}"

    class Meta:
        verbose_name = 'Race'
        verbose_name_plural = 'Races'


class racesDay(models.Model):
    race_id = models.IntegerField(primary_key=True)
    race_title = models.CharField(max_length=100)
    track_id = models.IntegerField()
    track_name = models.CharField(max_length=100)
    main_title = models.CharField(max_length=100)
    race_date = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.race_id} - {self.race_title}"

    class Meta:
        verbose_name = 'RaceDay'
        verbose_name_plural = 'RacesDay'

class collectHistoryDay(models.Model):
    id = models.IntegerField(primary_key=True)
    fake_id = models.CharField(max_length=50, default='')
    greyhound = models.ForeignKey(Greyhound, on_delete=models.CASCADE)
    last_refresh = models.DateField()
    len_history = models.IntegerField()

    def __str__(self):
        return f"{self.greyhound_id} - {self.last_refresh}"

    class Meta:
        verbose_name = 'collectHistoryDay'
        verbose_name_plural = 'collectHistoryDay'
