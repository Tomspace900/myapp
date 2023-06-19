use masterproject ; 

DROP TABLE IF EXISTS results;
DROP TABLE IF EXISTS own;
DROP TABLE IF EXISTS have_access;
DROP TABLE IF EXISTS Responses;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Questions;
DROP TABLE IF EXISTS Questionnaires;
DROP TABLE IF EXISTS Emails;

CREATE TABLE Questionnaires (
   id_questionnaire INT NOT NULL AUTO_INCREMENT,
   tally_id_questionnaire VARCHAR(6),
   name_questionnaire VARCHAR(100),
   date_creation_questionnaire DATE,
   PRIMARY KEY(id_questionnaire)
);

CREATE TABLE Questions (
   id_question INT NOT NULL AUTO_INCREMENT,
   tally_id_question VARCHAR(6),
   label_question VARCHAR(1000),
   type_question VARCHAR(50),
   is_mandatory BOOLEAN,
   PRIMARY KEY(id_question)
);

CREATE TABLE Users (
   id_user INT NOT NULL AUTO_INCREMENT,
   tally_id_user VARCHAR(6),
   firstname_user VARCHAR(50),
   lastname_user VARCHAR(50),
   email_user VARCHAR(100),
   phone_user VARCHAR(10),
   username_user VARCHAR(100),
   password_user VARCHAR(100),
   is_admin BOOLEAN,
   PRIMARY KEY(id_user)
);

CREATE TABLE Responses (
   id_response INT NOT NULL AUTO_INCREMENT,
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
   id_question INT,
   id_response INT,
   results VARCHAR(100),
   PRIMARY KEY(id_question, id_response),
   FOREIGN KEY(id_question) REFERENCES Questions(id_question),
   FOREIGN KEY(id_response) REFERENCES Responses(id_response)
);

CREATE TABLE Emails (
   id_email INT NOT NULL AUTO_INCREMENT,
   email VARCHAR(100),
   PRIMARY KEY(id_email)
);

-- Contraintes d'unicité
ALTER TABLE Emails ADD CONSTRAINT unique_email UNIQUE (email);

-- Insertion des données de test
INSERT INTO Users (firstname_user, lastname_user, email_user, is_admin, username_user, password_user) VALUES ('admin', 'admin', 'myselfmindwork@gmail.com', 1, 'admin', '6a158d9847a80e99511b2a7866233e404b305fdb7c953a30deb65300a57a0655');
INSERT INTO Emails (email) VALUES ('myselfmindwork@gmail.com');