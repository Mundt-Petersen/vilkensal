from icalendar import Calendar
import datetime as dt
import requests

URL = 'vilkensal/schema.ics'
salar = ['E:1144', 'E:1145', 'E:4115', 'E:4116', 'E:4118', 'E:4119', 'E:4121']
hus = 'E:'


print('-------')



with open(URL, 'r') as ics:
    #todays_date = dt.datetime.today().date()
    todays_date = dt.date(2024, 5, 8)
    tmrw_date = dt.date(2024, 5, 9)


    print('Hämtar kalenderdata.... \n')
    print('Alla event för', todays_date, 'kommer nedan! \n')
    
    for comp in Calendar.from_ical(ics.read()).walk('VEVENT'):
        
        try:
            event_date = comp.decoded('dtstart').date()
            if  event_date == todays_date:
                plats = comp['LOCATION']
                parts = plats.split()
                plats_lista = [part.strip('.') for part in parts if part.startswith(hus)]
                print('Händelse:' ,comp.get('summary'))
                print('Plats:', plats)
                for p in plats_lista:
                    if p in salar:
                        print('Idag är', p, 'upptaget!')
                        salar.remove(p)
                print('------------------')
        except:
            if not salar:
                print('Tyvärr finns det inga fina salar helt lediga idag....')
            else:
                print('Dagens lediga salar är:', salar)
            break