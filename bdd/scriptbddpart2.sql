use masterproject ; 

DROP TABLE IF EXISTS results;
DROP TABLE IF EXISTS own;
DROP TABLE IF EXISTS have_access;
DROP TABLE IF EXISTS Responses;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Questions;
DROP TABLE IF EXISTS Questionnaires;

CREATE TABLE Questionnaires (
   id_questionnaire INT,
   tally_id_questionnaire VARCHAR(6),
   name_questionnaire VARCHAR(100),
   date_creation_questionnaire DATE,
   PRIMARY KEY(id_questionnaire)
);

CREATE TABLE Questions (
   id_question INT,
   tally_id_question VARCHAR(6),
   label_question VARCHAR(1000),
   type_question VARCHAR(50),
   is_mandatory bit,
   PRIMARY KEY(id_question)
);

CREATE TABLE Users (
   id_user INT,
   tally_id_user VARCHAR(6),
   firstname_user VARCHAR(50),
   lastname_user VARCHAR(50),
   is_admin bit,
   PRIMARY KEY(id_user)
);

CREATE TABLE Responses (
   id_response INT,
   tally_id_responses VARCHAR(6),
   date_soumission DATE,
   id_user INT NOT NULL,
   id_questionnaire INT NOT NULL,
   PRIMARY KEY(id_response),
   FOREIGN KEY(id_user) REFERENCES Users(id_user),
   FOREIGN KEY(id_questionnaire) REFERENCES Questionnaires(id_questionnaire)
);

CREATE TABLE have_access (
   id_questionnaire INT,
   id_user INT,
   PRIMARY KEY(id_questionnaire, id_user),
   FOREIGN KEY(id_questionnaire) REFERENCES Questionnaires(id_questionnaire),
   FOREIGN KEY(id_user) REFERENCES Users(id_user)
);

CREATE TABLE own (
   id_questionnaire INT,
   id_question INT,
   PRIMARY KEY(id_questionnaire, id_question),
   FOREIGN KEY(id_questionnaire) REFERENCES Questionnaires(id_questionnaire),
   FOREIGN KEY(id_question) REFERENCES Questions(id_question)
);

CREATE TABLE results (
   id_response INT,
   niveau_etude varchar(20) not null,
   anonyme bit not null,
   prenom varchar(100),
   nom varchar(100),
   etre_contacte bit,
   adresse_mail varchar(100),
   numero_tel varchar(12),
   ecoute_par_personnel int not null,
   confiance_via_personnel int not null,
   securite_sein_etablissement int not null,
   stresse_a_lecole int not null,
   pression_venant_prof int not null,
   provoque_maladie int not null, 
   integre_dans_classe int not null,
   font_me_sentir_inferieur int not null,
   deja_jugee int not null,
   PRIMARY KEY(id_response),
   FOREIGN KEY(id_response) REFERENCES Responses(id_response)
);