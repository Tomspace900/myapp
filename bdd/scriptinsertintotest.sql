use masterproject ; 

-- QUESTIONNAIRE

INSERT INTO Questionnaires (id_questionnaire, tally_id_questionnaire, name_questionnaire, date_creation_questionnaire) VALUES (1, 1001, 'My self, My mind, My work', '2023-05-20');

-- QUESTION
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (1, 1001, 'Quel est ton niveau d''études ?', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (2,1002, 'Souhaites-tu répondre au sondage anonymement ?', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (3, 1003, 'Est-ce que je me sens écouté(e) par le personne de l''école ?', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (4, 1004, 'Est-ce que je me sens en confiance vis-à-vis du personne de l''école ?', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (5, 1005, 'Est-ce que me sens en sécurité au sein de l''établisement ?', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (6, 1006, 'Je suis stréssé(e) en étant à l''école ou en pensant à l''école.', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (7, 1007, 'Je subis de la pression venant de mes professeurs.', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (8, 1008, 'L''école me provoque des maux de tête ou de ventre.', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (9, 1009, 'Je me sens intégré(e) dans ma classe.', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (10, 1010, 'Mes camarades/professeurs me font me sentir inférieur/sans qualités.', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (11, 1011, 'Mes camarades/professeurs m''ont déjà jugé(e). Je me suis senti(e) ridiculisé(e)/rabaissé(e).', 'Text', TRUE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (12, 1012, 'Quel est ton prénom ?', 'Text', FALSE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (13, 1013, 'Quel est ton nom ?', 'Text', FALSE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (14, 1014, 'Souhaites-tu être contacté(e) ?', 'Text', FALSE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (15, 1015, 'Ton adresse e-mail :', 'Text', FALSE);
INSERT INTO Questions (id_question, tally_id_question, label_question, type_question, is_mandatory) VALUES (16, 1016, 'Ton numéro de téléphone :', 'Text', FALSE);

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
INSERT INTO results (id_question, id_response, results) VALUES (1, 1, 'Terminale');
INSERT INTO results (id_question, id_response, results) VALUES (2, 1, 'Oui');
INSERT INTO results (id_question, id_response, results) VALUES (3, 1, '4');
INSERT INTO results (id_question, id_response, results) VALUES (4, 1, '4');
INSERT INTO results (id_question, id_response, results) VALUES (5, 1, '5');
INSERT INTO results (id_question, id_response, results) VALUES (6, 1, '3');
INSERT INTO results (id_question, id_response, results) VALUES (7, 1, '3');
INSERT INTO results (id_question, id_response, results) VALUES (8, 1, '2');
INSERT INTO results (id_question, id_response, results) VALUES (9, 1, '5');
INSERT INTO results (id_question, id_response, results) VALUES (10, 1, '1');
INSERT INTO results (id_question, id_response, results) VALUES (11, 1, '1');

-- Pour id_response = 2
INSERT INTO results (id_question, id_response, results) VALUES (1, 2, 'Terminale');
INSERT INTO results (id_question, id_response, results) VALUES (2, 2, 'Oui');
INSERT INTO results (id_question, id_response, results) VALUES (3, 2, '5');
INSERT INTO results (id_question, id_response, results) VALUES (4, 2, '4');
INSERT INTO results (id_question, id_response, results) VALUES (5, 2, '5');
INSERT INTO results (id_question, id_response, results) VALUES (6, 2, '3');
INSERT INTO results (id_question, id_response, results) VALUES (7, 2, '3');
INSERT INTO results (id_question, id_response, results) VALUES (8, 2, '3');
INSERT INTO results (id_question, id_response, results) VALUES (9, 2, '3');
INSERT INTO results (id_question, id_response, results) VALUES (10, 2, '2');
INSERT INTO results (id_question, id_response, results) VALUES (11, 2, '3');

-- Pour id_response = 3
INSERT INTO results (id_question, id_response, results) VALUES (1, 3, 'Terminale');
INSERT INTO results (id_question, id_response, results) VALUES (2, 3, 'Non');
INSERT INTO results (id_question, id_response, results) VALUES (12, 3, 'Leyan');
INSERT INTO results (id_question, id_response, results) VALUES (13, 3, 'Very');
INSERT INTO results (id_question, id_response, results) VALUES (14, 3, 'Non');
INSERT INTO results (id_question, id_response, results) VALUES (3, 3, '4');
INSERT INTO results (id_question, id_response, results) VALUES (4, 3, '4');
INSERT INTO results (id_question, id_response, results) VALUES (5, 3, '4');
INSERT INTO results (id_question, id_response, results) VALUES (6, 3, '2');
INSERT INTO results (id_question, id_response, results) VALUES (7, 3, '4');
INSERT INTO results (id_question, id_response, results) VALUES (8, 3, '2');
INSERT INTO results (id_question, id_response, results) VALUES (9, 3, '4');
INSERT INTO results (id_question, id_response, results) VALUES (10, 3, '3');
INSERT INTO results (id_question, id_response, results) VALUES (11, 3, '3');

-- Pour id_response = 4
INSERT INTO results (id_question, id_response, results) VALUES (1, 4, 'Terminale');
INSERT INTO results (id_question, id_response, results) VALUES (2, 4, 'Oui');
INSERT INTO results (id_question, id_response, results) VALUES (3, 4, '4');
INSERT INTO results (id_question, id_response, results) VALUES (4, 4, '3');
INSERT INTO results (id_question, id_response, results) VALUES (5, 4, '4');
INSERT INTO results (id_question, id_response, results) VALUES (6, 4, '5');
INSERT INTO results (id_question, id_response, results) VALUES (7, 4, '4');
INSERT INTO results (id_question, id_response, results) VALUES (8, 4, '3');
INSERT INTO results (id_question, id_response, results) VALUES (9, 4, '4');
INSERT INTO results (id_question, id_response, results) VALUES (10, 4, '2');
INSERT INTO results (id_question, id_response, results) VALUES (11, 4, '2');

-- Pour id_response = 5
INSERT INTO results (id_question, id_response, results) VALUES (1, 5, '2nd');
INSERT INTO results (id_question, id_response, results) VALUES (2, 5, 'Non');
INSERT INTO results (id_question, id_response, results) VALUES (12, 5, 'Lola');
INSERT INTO results (id_question, id_response, results) VALUES (13, 5, 'Thiedey');
INSERT INTO results (id_question, id_response, results) VALUES (14, 5, 'Non');
INSERT INTO results (id_question, id_response, results) VALUES (3, 5, '4');
INSERT INTO results (id_question, id_response, results) VALUES (4, 5, '4');
INSERT INTO results (id_question, id_response, results) VALUES (5, 5, '4');
INSERT INTO results (id_question, id_response, results) VALUES (6, 5, '1');
INSERT INTO results (id_question, id_response, results) VALUES (7, 5, '2');
INSERT INTO results (id_question, id_response, results) VALUES (8, 5, '1');
INSERT INTO results (id_question, id_response, results) VALUES (9, 5, '5');
INSERT INTO results (id_question, id_response, results) VALUES (10, 5, '2');
INSERT INTO results (id_question, id_response, results) VALUES (11, 5, '1');

-- Pour id_response = 6
INSERT INTO results (id_question, id_response, results) VALUES (1, 6, '3e');
INSERT INTO results (id_question, id_response, results) VALUES (2, 6, 'Oui');
INSERT INTO results (id_question, id_response, results) VALUES (3, 6, '3');
INSERT INTO results (id_question, id_response, results) VALUES (4, 6, '3');
INSERT INTO results (id_question, id_response, results) VALUES (5, 6, '5');
INSERT INTO results (id_question, id_response, results) VALUES (6, 6, '1');
INSERT INTO results (id_question, id_response, results) VALUES (7, 6, '3');
INSERT INTO results (id_question, id_response, results) VALUES (8, 6, '1');
INSERT INTO results (id_question, id_response, results) VALUES (9, 6, '4');
INSERT INTO results (id_question, id_response, results) VALUES (10, 6, '1');
INSERT INTO results (id_question, id_response, results) VALUES (11, 6, '1');

-- Pour id_response = 7
INSERT INTO results (id_question, id_response, results) VALUES (1, 7, '6e');
INSERT INTO results (id_question, id_response, results) VALUES (2, 7, 'Oui');
INSERT INTO results (id_question, id_response, results) VALUES (3, 7, '5');
INSERT INTO results (id_question, id_response, results) VALUES (4, 7, '4');
INSERT INTO results (id_question, id_response, results) VALUES (5, 7, '5');
INSERT INTO results (id_question, id_response, results) VALUES (6, 7, '1');
INSERT INTO results (id_question, id_response, results) VALUES (7, 7, '1');
INSERT INTO results (id_question, id_response, results) VALUES (8, 7, '1');
INSERT INTO results (id_question, id_response, results) VALUES (9, 7, '5');
INSERT INTO results (id_question, id_response, results) VALUES (10, 7, '1');
INSERT INTO results (id_question, id_response, results) VALUES (11, 7, '1');

-- Pour id_response = 8
INSERT INTO results (id_question, id_response, results) VALUES (1, 8, '3e');
INSERT INTO results (id_question, id_response, results) VALUES (2, 8, 'Oui');
INSERT INTO results (id_question, id_response, results) VALUES (3, 8, '2');
INSERT INTO results (id_question, id_response, results) VALUES (4, 8, '2');
INSERT INTO results (id_question, id_response, results) VALUES (5, 8, '2');
INSERT INTO results (id_question, id_response, results) VALUES (6, 8, '4');
INSERT INTO results (id_question, id_response, results) VALUES (7, 8, '2');
INSERT INTO results (id_question, id_response, results) VALUES (8, 8, '4');
INSERT INTO results (id_question, id_response, results) VALUES (9, 8, '1');
INSERT INTO results (id_question, id_response, results) VALUES (10, 8, '4');
INSERT INTO results (id_question, id_response, results) VALUES (11, 8, '4');

-- Pour id_response = 9
INSERT INTO results (id_question, id_response, results) VALUES (1, 9, '4e');
INSERT INTO results (id_question, id_response, results) VALUES (2, 9, 'Oui');
INSERT INTO results (id_question, id_response, results) VALUES (3, 9, '3');
INSERT INTO results (id_question, id_response, results) VALUES (4, 9, '2');
INSERT INTO results (id_question, id_response, results) VALUES (5, 9, '2');
INSERT INTO results (id_question, id_response, results) VALUES (6, 9, '2');
INSERT INTO results (id_question, id_response, results) VALUES (7, 9, '2');
INSERT INTO results (id_question, id_response, results) VALUES (8, 9, '2');
INSERT INTO results (id_question, id_response, results) VALUES (9, 9, '2');
INSERT INTO results (id_question, id_response, results) VALUES (10, 9, '1');
INSERT INTO results (id_question, id_response, results) VALUES (11, 9, '2');