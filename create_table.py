#! /usr/bin/python
# -*- coding: utf-8 -*-

import random

n = 100

Prenom = ['Rosemarie', 'Zoe', 'Agathe', 'Etienne', 'Scoville', 'Chrisitan',
          'Mercer', 'Fusberta', 'Laetitia', 'Senapus', 'Victoire', 'Dreux',
          'Isabelle', 'Monique', 'Campbell', 'Huette', 'Namo', 'Florus',
          'Damiane', 'Erembourg', 'Kari', 'Burnell', 'Benoit', 'Daisi',
          'Cinderalla', 'Laure', 'Susanne', 'Hortense', 'Charles', 'Merlin',
          'Martin', 'Alphonse', 'Sacripant', 'Searlas', 'Loyal', 'Xavier',
          'Peppin', 'Ray', 'Serge', 'Franck', 'Pevrell', 'Parfait',
          'Beltanne', 'Faustin', 'Langley', 'Theodore', 'Romain', 'Percy',
          'Dexter', 'Gaetan', 'Ferragus', 'Avenal', 'Theo', 'Arthur', 'Michel',
          'Lance', 'Joseph', 'Agathe', 'Claire', 'Angele', 'Sophie', 'Enora',
          'Lucie', 'Marjolaine', 'Solene', 'Sarah', 'Juliette', 'Jean', 'Pierre',
          'Francois', 'Julien', 'Nathan', 'Cyrille', 'Allan', 'Zlatan',
          'Lionel', 'Andres', 'Rio', 'David', 'Franck', 'Jeremie', 'Adrien',
		  'Bertrand', 'Melvin', 'Nicolas', 'Rodolphe', 'Aymeric', 'Renaud',
	      'Marianne', 'Lisa', 'Imane', 'Pauline', 'Thomas', 'Bruno', 'Maxime',
          'Nathan', 'Lucas', 'Enzo', 'Leo', 'Louis', 'Hugo', 'Gabriel',
          'Ethan', 'Mathis', 'Emma', 'Lea', 'Chloe', 'Manon', 'Ines', 'Lola',
          'Jade', 'Camille', 'Sarah', 'Jules', 'Louise',
          'Robert', 'Gerard', 'Jean-Pierre', 'Florent', 'Florian', 'Luc',
          'Teddy', 'Monique', 'Christophe', 'Frederic', 'Gaetan', 'Virginie',
          'Johann', 'Laurent', 'Maurice', 'Jamel', 'Dany', 'Stanley', 'Alfredo',
          'Raymond', 'Luis', 'Omar', 'Josef', 'Lev', 'Denis', 'Bobby',
          'Florian', 'George', 'Gianni', 'Gerd', 'Franz', 'Oleg', 
          'Allan', 'Kevin', 'Karl', 'Paolo', 'Marco', 'Roberto',
          'Michael', 'Pavel', 'Andrei', 'Massimo', 'Yannick', 'Josephine',
          'Pascal', 'Zoe', 'William', 'France']

Nom = ['Doiron', 'Giguere', 'Cressac', 'Quinn', "Daoust", 'Ouellet',
       'Hetu', 'Therriault', 'Tachel', 'Loiseau', 'Aucoin', 'Lejeune',
       'Gingras', 'Houle', 'Sauve', 'Dandonneau', 'Garnier', 'Lanois',
       'Guernon', 'Chouinard', 'Duhamel', 'Hache', 'Sciverit', 'Bazinet',
       'Dostie', 'Arnoux', 'Bondy', 'Lafontaine', 'Dufresnes', 'Bourgeau',
       'Donat', 'Demers', 'Bergeron', 'Cinqmars', 'Paulet', 'Moise',
       'Michaud', 'Clavette', 'Allaire', 'Adler', 'Chadonnay', 'Lizotte',
       'Cailot', 'Roux', 'Desforges', 'Rene', 'Sanchargin', 'Racicot',
       'Ratte', 'Plourde', 'Roux', 'Lebel', 'Lanois', 'Ibrahimovic',
       'Zidane', 'Platini', 'Papin', 'Maradona', 'Pele', 'Cantona',
       'Beckham', 'Messi', 'Giresse', 'Djorkaeff', 'Dessailly', 'Thuram',
       'Makelele', 'Vieira', 'Ribery', 'Dhorassoo', 'Chirac', 'Sarkozy',
       'Domenech', 'Martin', 'Bernard', 'Dubois', 'Thomas', 'Robert',
       'Richard', 'Petit', 'Durand', 'Leroy', 'Moreau', 'Simon', 'Laurent',
       'Lefebvre', 'Michel', 'Garcia', 'David', 'Bertrand', 'Roux', 'Fournier',
       'Morel', 'Girard', 'Andre', 'Lefevre', 'Mercier', 'Dupont', 'Lambert',
       'Bonnet', 'Francois', 'Martinez', 'Legrand', 'Garnier', 'Faure', 
       'Rousseau', 'Blanc', 'Guerin', 'Muller', 'Henry', 'Roussel', 'Nicolas',
       'Olivier', 'Giroud', 'Chamakh', 'Gervinho', 'Gourcuff', 'Traore',
       'Eto', 'Makoun', 'Ronaldinho', 'Ronaldo', 'Romario', 'Zico', 'Trezeguet',
       'Armstrong', 'Wiggins', 'Lemond', 'Rolland', 'Ullrich', 'Riis', 'Cruyff',
       'Jalabert', 'Manaudou', 'Leboeuf', 'Barthez', 'Lama', 'Boghossian', 
       'Brochard', 'Tello', 'Robben', 'Damico', 'Jobs', 'Gates', 'Wozniak', 
       'Doherty', 'Dickinson', 'Windsor', 'Potter', 'Auclair', 'Brisbois',
       'Riolo', 'Dimecco', 'Larque', 'Cazarre', 'Aleatoire', 'Innocent',
       'Marton', 'Julien', 'Simpson', 'Morgan', 'Freeman',
       'Chirac', 'DeGaulles', 'Pompidou', 'Giscard', 'Bush',
       'Deno', 'Reagan', 'Clinton', 'Einsenhower', 'Davis',
       'Noah', 'Marques', 'Anthony', 'Pearce', 'Butler',
       'Gibson', 'Hamilton', 'Robinson', 'Rose', 'Teague', 'Cannavaro',
       'Nedved', 'Owen', 'Figo', 'Rivaldo', 'Sammer', 'Klinsmann',
       'van Basten', 'Gullit', 'Belanov', 'Law', 'Lax', 'Masopust',
       'Albert', 'Best', 'Rivera', 'Beckenbauer', 'Simonsen', 'Keegan',
       'Rummenigge', 'Rossi', 'Greaves', 'Amaro', 'Suarez', 'Riva',
       'Bergkamp', 'Kopa', 'Edwards', 'Fontaine', 'Schuster', 'Viktor']

ue_S5 = ['ALG-1', 'DPP-1', 'ELE-1', 'INP-1', 'LCI-1', 'MAT-1', 'MGP-1', 'PHO-1',
         'PHQ-1', 'SPM-1']

ue_S5_credits = [3, 2, 3, 3, 3, 3, 4, 3, 3, 3]

ue_S6 = ['DPP-2', 'EAO-2', 'ECO-2', 'LCI-2', 'MAT-2', 'MCO-2', 'MGP-2', 'PHS-2',
         'PJT-2', 'RMS-2', 'STG-2', 'THS-2']

ue_S6_credits = [1, 3, 3, 3, 2, 2, 4, 2, 1, 4, 2, 3]

ue_S7 = ['ASL-3', 'DPP-3', 'EAO-31', 'EAO-32', 'EAO-33', 'EAO-34', 'EAO-35',
         'LCI-3', 'MAT-3', 'MNG-3', 'PJT-3', 'STD-3']

ue_S7_credits = [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 2]

def generate_name():
    full_name = random.sample(Prenom, 1)[0] + " " + random.sample(Nom, 1)[0]
    return full_name
    
sql_end = ");"

def sql_start(table_name):
    return "insert into " + table_name + " values ("

f = open('populate_table.sql', 'w')

f.write("drop table if exists gpa;\n")
f.write("drop table if exists gpa;\n")
f.write("drop table if exists eleves;\n")
f.write("drop table if exists notes_details;\n")
f.write("drop table if exists contentieux;\n\n")
f.write("create table eleves (\n")
f.write("nom varchar(255),\n")
f.write("civil integer,\n")
f.write("bac_code varchar(10),\n")
f.write("bac_mention varchar(20),\n")
f.write("entree_fil varchar(30),\n")
f.write("entree_prep varchar(20),\n")
f.write("personne_id varchar(50),\n")
f.write("primary key (personne_id)\n")
f.write(");\n\n")
f.write("create table notes_details (\n")
f.write("cycle varchar(9), \n")
f.write("sem varchar(5),\n")
f.write("nom varchar(255), \n")
f.write("code_ue varchar(10),\n")
f.write("moy_ue float,\n")
f.write("grade_gpa float,\n")
f.write("grade_ects varchar(2),\n")
f.write("credits_ects integer,\n")
f.write("session integer\n")
f.write(");\n\n")
f.write("create table gpa (\n")
f.write("cycle varchar(9),\n")
f.write("sem varchar(5),\n")
f.write("nom varchar(255),\n")
f.write("gpa float,\n")
f.write("primary key (cycle, sem, nom)\n")
f.write(");\n\n")
f.write("create table contentieux (\n")
f.write("cycle varchar(9),\n")
f.write("sem varchar(5),\n")
f.write("nom varchar(255),\n")
f.write("code_ue varchar(10)\n")
f.write(");\n\n")

def fill():
    full_name = generate_name()
    eleve_string_sql = fill_eleves(full_name)
    f.write(eleve_string_sql)
    f.write("\n")
    notes_details_list_sql = fill_notes_details(full_name)
    for enregistrement in notes_details_list_sql:
        f.write(enregistrement)
        f.write("\n")
    gpa_list_sql = fill_gpa(full_name)
    for enregistrement in gpa_list_sql:
        f.write(enregistrement)
        f.write("\n")       

def fill_eleves(full_name):
    [prenom, nom] = full_name.split(' ')
    login = prenom[0].lower() + nom.lower()
    nbre_aleatoire = random.randint(1, 10)
    if nbre_aleatoire <= 9:
        entree_fil = "MP"
    else:
        entree_fil = "etranger"
    eleve_sql = sql_start("eleves") + add_quote(full_name) + ", " + str(1) + ", " + add_quote("S") + ", " + add_quote("Tres bien") + ", "
    eleve_sql += add_quote(entree_fil) + ", " + add_quote("MP") + ", " + add_quote(login) + sql_end
    return eleve_sql

def add_quote(mot):
    mot_ = "'" + mot + "'"
    return mot_

def fill_contentieux():
    pass

def fill_gpa():
    pass

def fill_notes_details(full_name):
    cycle1 = '2011-2012'
    cycle2 = '2012-2013'
    ue_list = []
    for (index, ue) in enumerate(ue_S5):
        semestre = 'SEM-5'
        i = random.randint(1, 10)
        if i <= 5:
            s = generate_sql_notes_details(cycle1, semestre, full_name, ue, ue_S5_credits[index], 1, True)
            ue_list.append(s)
        elif i <= 9:
            s = generate_sql_notes_details(cycle1, semestre, full_name, ue, 0, 1, False)
            ue_list.append(s)
            s = generate_sql_notes_details(cycle1, semestre, full_name, ue, ue_S5_credits[index], 2, True)
            ue_list.append(s)
        else:
            s = generate_sql_notes_details(cycle1, semestre, full_name, ue, 0, 1, False)
            ue_list.append(s)
            s = generate_sql_notes_details(cycle1, semestre, full_name, ue, ue_S5_credits[index], 99, False)
            ue_list.append(s)
    for (index, ue) in enumerate(ue_S6):
        semestre = 'SEM-6'
        i = random.randint(1, 10)
        if i <= 5:
            s = generate_sql_notes_details(cycle1, semestre, full_name, ue, ue_S6_credits[index], 1, True)
            ue_list.append(s)
        elif i <= 9:
            s = generate_sql_notes_details(cycle1, semestre, full_name, ue, 0, 1, False)
            ue_list.append(s)
            s = generate_sql_notes_details(cycle1, semestre, full_name, ue, ue_S6_credits[index], 2, True)
            ue_list.append(s)
        else:
            s = generate_sql_notes_details(cycle1, semestre, full_name, ue, 0, 1, False)
            ue_list.append(s)
            s = generate_sql_notes_details(cycle1, semestre, full_name, ue, ue_S6_credits[index], 99, False)
            ue_list.append(s)
    for (index, ue) in enumerate(ue_S7):
        semestre = 'SEM-7'
        i = random.randint(1, 14)
        if i <= 5:
            s = generate_sql_notes_details(cycle2, semestre, full_name, ue, ue_S7_credits[index], 1, True)
            ue_list.append(s)
        elif i <= 9:
            s = generate_sql_notes_details(cycle2, semestre, full_name, ue, 0, 1, False)
            ue_list.append(s)
            s = generate_sql_notes_details(cycle2, semestre, full_name, ue, ue_S7_credits[index], 2, True)
            ue_list.append(s)
        elif i <= 10:
            s = generate_sql_notes_details(cycle2, semestre, full_name, ue, 0, 1, False)
            ue_list.append(s)
            s = generate_sql_notes_details(cycle2, semestre, full_name, ue, ue_S7_credits[index], 99, False)
            ue_list.append(s)
        else:
            s = generate_sql_notes_details(cycle2, semestre, full_name, ue, 0, 1, False)
            ue_list.append(s)
            s = generate_sql_notes_details(cycle2, semestre, full_name, ue, 0, 2, False)
            ue_list.append(s)
            s = generate_contentious(cycle2, semestre, full_name, ue)
            ue_list.append(s)
    return ue_list

def generate_sql_notes_details(cycle, semestre, full_name, ue, credit, session, success):
    s = sql_start("notes_details") + add_quote(cycle) + ", " + add_quote(semestre) + ", " + add_quote(full_name) + ", "
    if success:
        grade_gpa = random.sample([2.67, 3.0, 3.33, 3.67, 4.0], 1)[0]
    else:
        grade_gpa = random.sample([1.0, 1.33, 1.67, 2.0, 2.33], 1)[0]    
    s += add_quote(ue) + ", " + str(11.32) + ", " + str(grade_gpa) + ", " + add_quote('A') + ", " + str(credit) + ", " + str(session)
    s += sql_end
    return s

def generate_contentious(cycle, semestre, full_name, ue):
    s = sql_start("contentieux") + add_quote(cycle) + ", " + add_quote(semestre) + ", " + add_quote(full_name) + ", " + add_quote(ue)
    s += sql_end
    return s

def fill_gpa(full_name):
    sql_list = []
    for (index, semestre) in enumerate(['SEM-5', 'SEM-6', 'SEM-7']):
        if index != 2:
            cycle = "2011-2012"
        else:
            cycle = "2012-2013"
        grade_gpa = round(2.0 + random.random() * 2, 2)
        s = sql_start("gpa") + add_quote(cycle) + ", " + add_quote(semestre) + ", " + add_quote(full_name) + ", " + str(grade_gpa) + sql_end
        sql_list.append(s)
    return sql_list



for i in range(175):
    fill()
f.close()  
        

    
