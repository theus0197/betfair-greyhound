from django.contrib import admin
from .models import Greyhound, Races, racesDay, collectHistoryDay, collectOddsDay, hackedProfile  # Importe seus modelos aqui

class GreyhoundAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_greyhound', 'gender', 'gender_abbreviation', 'color', 'color_abbreviation', 'birth_date', 'birth_year', 'birth_month', 'birth_day', 'dam_name', 'sire_name')
    # Adicione outros campos conforme necessário

class RacesAdmin(admin.ModelAdmin):
    search_fields = ['id', 'race_id', 'race_greyhound', 'id_greyhound', 'race_date', 'track_name']
    list_display = (
        'id', 
        'race_id', 
        'race_greyhound', 
        'id_greyhound', 
        'greyhound', 
        'avaible', 
        'avaible_calculate', 
        'race_date', 
        'uk_time', 
        'br_time', 
        'track_name',
        'track', 
        'category', 
        'distance', 
        'result', 
        'start', 
        'final_time', 
        'recovery'
    )
    # Adicione outros campos conforme necessário

class RacesDayAdmin(admin.ModelAdmin):
    list_display = ('race_id', 'race_title', 'track_id', 'track_name', 'main_title', 'race_date')
    # Adicione outros campos conforme necessário

class collectHistoryDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'fake_id', 'greyhound', 'last_refresh', 'len_history')

class collectOddsDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'market_id', 'race_id_betfair', 'market_name', 'start_time', 'result', 'status', 'meeting_id', 'name', 'venue', 'country_code', 'event_type_id', 'identify', 'race_id', 'date_added', 'timer_added')

class hackedProfileAdmin(admin.ModelAdmin):
    search_fields = ['email', 'user']
    list_display = ('id', 'email',  'user', 'password')

# Registre os modelos no admin
admin.site.register(Greyhound, GreyhoundAdmin)
admin.site.register(Races, RacesAdmin)
admin.site.register(racesDay, RacesDayAdmin)
admin.site.register(collectHistoryDay, collectHistoryDayAdmin)
admin.site.register(collectOddsDay, collectOddsDayAdmin)
admin.site.register(hackedProfile, hackedProfileAdmin)

