import io
import requests
import bugsnag

from django.core.management.base import BaseCommand

from cards.models import Card, CardType
from cardsources.models import Booster

class Command(BaseCommand):
    bugsnag.configure(api_key='')

    def handle(self, *args, **options):
        try:
            file = io.open('cardlist.txt', 'rt')
            errors = io.open('failed.txt', 'w')

            booster = None
            count = 0
            fail_count = 0

            for line in file:
                if line.strip() == '':
                    continue
                if line.startswith('###'):
                    booster_name = line.strip('# \n')
                    print booster_name
                    booster = Booster.objects.get(name=booster_name)
                    continue

                count += 1

                try:
                    response = requests.get('http://yugiohprices.com/api/card_data/' + line.strip())
                    json = response.json()
                except Exception, e:
                    bugsnag.notify(e, context='CardImport', meta_data={ 'card': line, 'booster_name': booster_name, 'response': response.text })
                    json = None

                card = Card(name=line.strip())

                if json and json['status'] == 'success':
                    card.description = json['data']['text']

                    if json['data']['card_type'] == 'monster':
                        card.attack = json['data']['atk']
                        card.defense = json['data']['def']
                        card.attribute = json['data']['family'].lower()
                        card.level = json['data']['level']
                        card.save()

                        types = []
                        for t in json['data']['type'].split('/'):
                            ct = CardType.objects.get(name=t.strip())
                            types.append(ct.id)
                        card.card_types = types
                    else:
                        card.effect_type = ('{} {}'.format(json['data']['property'], json['data']['card_type'])).lower()
                else:
                    errors.write(line)
                    errors.flush()
                    fail_count += 1

                card.save()
                card.boosters = [ booster.id ]
                card.save()

                print '{} - {} ({})'.format(booster.name, line.strip(), str(count))
        except Exception, e:
            bugsnag.notify(e, context='CardImport', meta_data={ 'card': line, 'booster_name': booster_name, 'response': response.text })
        finally:
            file.close()
            errors.close()
