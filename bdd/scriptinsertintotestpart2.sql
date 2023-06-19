use masterproject ; 

-- QUESTIONNAIRE

INSERT INTO Questionnaires (id_questionnaire, tally_id_questionnaire, name_questionnaire, date_creation_questionnaire) VALUES (1, 1001, 'My self, My mind, My work', '2023-05-20');

-- QUESTION
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (1, 1001, 'Quel est ton niveau d''études ?', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (2,1002, 'Souhaites-tu répondre au sondage anonymement ?', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (3, 1003, 'Est-ce que je me sens écouté(e) par le personne de l''école ?', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (4, 1004, 'Est-ce que je me sens en confiance vis-à-vis du personne de l''école ?', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (5, 1005, 'Est-ce que me sens en sécurité au sein de l''établisement ?', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (6, 1006, 'Je suis stréssé(e) en étant à l''école ou en pensant à l''école.', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (7, 1007, 'Je subis de la pression venant de mes professeurs.', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (8, 1008, 'L''école me provoque des maux de tête ou de ventre.', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (9, 1009, 'Je me sens intégré(e) dans ma classe.', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (10, 1010, 'Mes camarades/professeurs me font me sentir inférieur/sans qualités.', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (11, 1011, 'Mes camarades/professeurs m''ont déjà jugé(e). Je me suis senti(e) ridiculisé(e)/rabaissé(e).', 'Text', 1);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (12, 1012, 'Quel est ton prénom ?', 'Text', 0);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (13, 1013, 'Quel est ton nom ?', 'Text', 0);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (14, 1014, 'Souhaites-tu être contacté(e) ?', 'Text', 0);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (15, 1015, 'Ton adresse e-mail :', 'Text', 0);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (16, 1016, 'Ton numéro de téléphone :', 'Text', 0);

-- USER
INSERT INTO Users (id_user, tally_id_user, firstname_user, lastname_user, is_admin) VALUES (1, 1001, 'Maelys', 'Very', 1);
INSERT INTO Users (id_user, tally_id_user, firstname_user, lastname_user, is_admin) VALUES (2, 1002, 'Ambre', 'Letellier', 1);
INSERT INTO Users (id_user, tally_id_user,is_admin) VALUES (3, 'ND5R2G', 0);
INSERT INTO Users (id_user, tally_id_user,is_admin) VALUES (4, '8zo7J5', 0);
INSERT INTO Users (id_user, tally_id_user,is_admin) VALUES (5, 'ND5GNp', 0);
INSERT INTO Users (id_user, tally_id_user,is_admin) VALUES (6, '8z1o2r', 0);
INSERT INTO Users (id_user, tally_id_user,is_admin) VALUES (7, 'xjXJ4d', 0);
INSERT INTO Users (id_user, tally_id_user,is_admin) VALUES (8, 'XrxYNg', 0);
INSERT INTO Users (id_user, tally_id_user,is_admin) VALUES (9, 'k9lNj1', 0);
INSERT INTO Users (id_user, tally_id_user,is_admin) VALUES (10, 'E5dbYq', 0);
INSERT INTO Users (id_user, tally_id_user,is_admin) VALUES (11, 'zN7Jlq', 0);

-- RESPONSES
INSERT INTO Responses (id_response, tally_id_responses, date_soumission, id_user, id_questionnaire) VALUES (1, '59kZrb', '2023-05-22', 3, 1);
INSERT INTO Responses (id_response, tally_id_responses, date_soumission, id_user, id_questionnaire) VALUES (2, '59kZrb', '2023-05-23', 4, 1);
INSERT INTO Responses (id_response, tally_id_responses, date_soumission, id_user, id_questionnaire) VALUES (3, 'MaO4N0', '2023-05-23', 5, 1);
INSERT INTO Responses (id_response, tally_id_responses, date_soumission, id_user, id_questionnaire) VALUES (4, 'd0AB6r', '2023-05-23', 6, 1);
INSERT INTO Responses (id_response, tally_id_responses, date_soumission, id_user, id_questionnaire) VALUES (5, 'd0AB6r', '2023-05-23', 7, 1);
INSERT INTO Responses (id_response, tally_id_responses, date_soumission, id_user, id_questionnaire) VALUES (6, 'rOE0qM', '2023-05-23', 8, 1);
INSERT INTO Responses (id_response, tally_id_responses, date_soumission, id_user, id_questionnaire) VALUES (7, 'rOE0qM', '2023-05-23', 9, 1);
INSERT INTO Responses (id_response, tally_id_responses, date_soumission, id_user, id_questionnaire) VALUES (8, '8Lj8xP', '2023-05-28', 10, 1);
INSERT INTO Responses (id_response, tally_id_responses, date_soumission, id_user, id_questionnaire) VALUES (9, 'GpQprQ', '2023-05-30', 11, 1);

-- HAVE ACCES
INSERT INTO have_access (id_questionnaire, id_user) VALUES (1,1);
INSERT INTO have_access (id_questionnaire, id_user) VALUES (1,2);


-- OWN
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 1);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 2);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 3);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 4);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 5);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 6);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 7);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 8);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 9);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 10);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 11);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 12);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 13);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 14);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 15);
INSERT INTO own (id_questionnaire, id_question) VALUES (1, 16);

-- RESULTS
-- Pour id_response = 1
INSERT INTO results (id_response,niveau_etude,anonyme,ecoute_par_personnel,confiance_via_personnel,securite_sein_etablissement,stresse_a_lecole,pression_venant_prof,provoque_maladie,integre_dans_classe,font_me_sentir_inferieur,deja_jugee) VALUES (1,'Terminale',1,4,4,5,3,3,2,5,1,1);

INSERT INTO results (id_response,niveau_etude,anonyme,ecoute_par_personnel,confiance_via_personnel,securite_sein_etablissement,stresse_a_lecole,pression_venant_prof,provoque_maladie,integre_dans_classe,font_me_sentir_inferieur,deja_jugee) VALUES (2,'Terminale',1,5,4,5,3,3,3,3,2,3);

INSERT INTO results (id_response, niveau_etude, anonyme,prenom,nom,etre_contacte,ecoute_par_personnel,confiance_via_personnel,securite_sein_etablissement,stresse_a_lecole,pression_venant_prof,provoque_maladie,integre_dans_classe,font_me_sentir_inferieur,deja_jugee) VALUES (3,'Terminale',0,'Leyan','Very',0,4,4,4,2,4,2,4,3,3);

INSERT INTO results (id_response, niveau_etude,anonyme,ecoute_par_personnel,confiance_via_personnel,securite_sein_etablissement,stresse_a_lecole,pression_venant_prof,provoque_maladie,integre_dans_classe,font_me_sentir_inferieur,deja_jugee) VALUES (4,'Terminale',1,4,3,4,5,4,3,4,2,2);

INSERT INTO results (id_response, niveau_etude,anonyme,prenom,nom,etre_contacte,ecoute_par_personnel,confiance_via_personnel,securite_sein_etablissement,stresse_a_lecole,pression_venant_prof,provoque_maladie,integre_dans_classe,font_me_sentir_inferieur,deja_jugee) VALUES (5,'2nd',0,'Lola','Thiedey',0,4,4,4,1,2,1,5,2,1);

INSERT INTO results (id_response, niveau_etude,anonyme,ecoute_par_personnel,confiance_via_personnel,securite_sein_etablissement,stresse_a_lecole,pression_venant_prof,provoque_maladie,integre_dans_classe,font_me_sentir_inferieur,deja_jugee) VALUES (6,'3e',1,3,3,5,1,3,1,4,1,1);

INSERT INTO results (id_response, niveau_etude,anonyme,ecoute_par_personnel,confiance_via_personnel,securite_sein_etablissement,stresse_a_lecole,pression_venant_prof,provoque_maladie,integre_dans_classe,font_me_sentir_inferieur,deja_jugee) VALUES (7,'6e',1,5,4,5,1,1,1,5,1,1);

INSERT INTO results (id_response, niveau_etude,anonyme,ecoute_par_personnel,confiance_via_personnel,securite_sein_etablissement,stresse_a_lecole,pression_venant_prof,provoque_maladie,integre_dans_classe,font_me_sentir_inferieur,deja_jugee) VALUES (8,'3e',1,2,2,2,4,2,4,1,4,4);

INSERT INTO results (id_response, niveau_etude, anonyme,ecoute_par_personnel,confiance_via_personnel,securite_sein_etablissement,stresse_a_lecole,pression_venant_prof,provoque_maladie,integre_dans_classe,font_me_sentir_inferieur,deja_jugee) VALUES (9,'4e',1,3,2,2,2,2,2,2,1,2);