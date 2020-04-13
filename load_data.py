from app import create_app
from app.data.models import State, City, Doctors
from collections import defaultdict
import csv
import os

app = create_app()

def load_doctors():

    with open(os.path.join('initial_data', 'Doctors.csv')) as f:
        reader = csv.reader(f)
        l = tuple(reader)

        print("adding new doctors..")

        for s in l[1:]:
            st = s[2].strip()
            
            state, created = State.get_or_save(state=st)
            city, created = City.get_or_save(city=s[3], state=state)

            # source_link = s[9]
            # if source_link in source_links:
            #     source_link_valid = source_links[source_link]
            # else:
            #     source_link_valid = False
                # try:
                #     req = requests.get(source_link, verify=False, timeout=5)
                #     if req.status_code == 200:
                #         source_link_valid = True
                #     else:
                #         print(f"{source_link} is not 200\n")
                # except:
                #     print(f"{source_link} can't reach\n")
                #     pass
            
                # source_links[source_link] = source_link_valid

            doc = Doctors(state_id=state.id, city_id=city.id, name=s[4], sub_category=s[5],\
                email_id_1=s[6], phone_1=s[7], phone_2=s[8], source_url=s[9], source=s[10],\
                description=s[11])
                
            doc.save()

        print("Added new doctors!")

with app.app_context():
    load_doctors()
