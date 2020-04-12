from app import create_app
from app.data.models import InfoType, Location, Entry
import csv
from collections import defaultdict

app = create_app()

with app.app_context():
    with open('DATA_NEW_2.csv') as f:
        reader = csv.reader(f)
        l = tuple(reader)

        print("adding new data..")
        source_links = defaultdict(bool)

        for s in l[1:]:
            st = s[0].replace('&', 'and').strip()
            
            loc, created = Location.get_or_save(state=st, city=s[1].strip())
            i, created = InfoType.get_or_save(name=s[2])

            # Check if Entry has a valid source link
            if s[10] in source_links:
                source_link_valid = source_links[s[10]]
            else:
                source_link_valid = False
                try:
                    req = requests.get(s[10], verify=False, timeout=5)
                    if req.status_code == 200:
                        source_link_valid = True
                    else:
                        print(f"{s[10]} is not 200\n")
                except:
                    print(f"{s[10]} can't reach\n")
                    pass
            
                source_links[s[10]] = source_link_valid

            e = Entry(location_id=loc.id, infotype_id=i.id, name=s[3].strip(), occupation=s[4], email_id_1=s[5], email_id_2=s[6], phone_1=s[7], phone_2=s[8], extension=s[9], source_link=s[10], source_link_valid=source_link_valid, source=s[11])
            e.save()

        print("Added new data!")
