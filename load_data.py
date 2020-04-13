from app import create_app
from app.data.models import State, City, Doctors, Hospitals, Laboratories, Helplines, Government, Fever_Clinics
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


def load_hospitals():

    with open(os.path.join('initial_data', 'Hospitals.csv')) as f:
        reader = csv.reader(f)
        l = tuple(reader)

        print("adding new hospitals..")

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

            h = Hospitals(state_id=state.id, city_id=city.id, name=s[4], point_of_contact=s[5],email_id_1=s[6],email_id_2=s[7], phone_1=s[8], phone_2=s[9], address=s[10], source_url=s[11], source=s[12],description=s[13])

            h.save()

        print("Added new hospitals!")


def load_labs():

    with open(os.path.join('initial_data', 'Labs.csv')) as f:
        reader = csv.reader(f)
        l = tuple(reader)

        print("adding new labs..")

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

            l = Laboratories(state_id=state.id, city_id=city.id, sub_category=s[4],name=s[5],point_of_contact=s[6], email_id_1=s[7],
                          email_id_2=s[8], phone_1=s[9], phone_2=s[10], address=s[11], source_url=s[12], source=s[13], description=s[14])

            l.save()

        print("Added new labs!")


def load_lines():
    #id,category,state,area,subCategory,phone1,phone2,sourceUrl,source,description
    with open(os.path.join('initial_data', 'Helpline.csv')) as f:
        reader = csv.reader(f)
        l = tuple(reader)

        print("adding new lines..")

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
            #id,category,state,area,subCategory,phone1,phone2,sourceUrl,source,description
            hl = Helplines(state_id=state.id, city_id=city.id, sub_category=s[4], phone_1=s[5], phone_2=s[6], source_url=s[7], source=s[8], description=s[9])

            hl.save()

        print("Added new lines!")


def load_gvts():
    with open(os.path.join('initial_data', 'Government_Contacts.csv')) as f:
        reader = csv.reader(f)
        l = tuple(reader)

        print("adding new gvtss..")

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
            #id,category,state,area,subCategory,phone1,phone2,sourceUrl,source,description
            g = Government(state_id=state.id, city_id=city.id, sub_category=s[4], point_of_contact=s[5], email_id_1=s[6], email_id_2=s[7], phone_1=s[8], phone_2=s[9], source_url=s[10], source=s[11],
                           description=s[12])

            g.save()

        print("Added new gvts!")

def load_clinics():
    with open(os.path.join('initial_data', 'Fever_Clinics.csv')) as f:
        reader = csv.reader(f)
        l = tuple(reader)

        print("adding new clinics..")

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
            #id,category,state,area,subCategory,name,pointOfContact,email1,email2,phone1,phone2,address,sourceUrl,source,description
            fc = Fever_Clinics(state_id=state.id, city_id=city.id, sub_category=s[4], name=s[5],point_of_contact=s[6], email_id_1=s[7], email_id_2=s[8], phone_1=s[9], phone_2=s[10], address=s[11],source_url=s[12], source=s[13],
                           description=s[14])

            fc.save()
            print(fc)

        print("Added new clinics!")

with app.app_context():
    load_doctors()
    load_hospitals()
    load_labs()
    load_lines()
    load_gvts()
    load_clinics()
