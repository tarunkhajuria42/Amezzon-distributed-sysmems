INSERT INTO `amezzon`.`person` (`person_username`, `person_passwordhash`, `person_firstname`, `person_lastname`,
                                `person_mail`, `person_isukukood`)
VALUES ('zane', '$2b$12$OujOIw7Vm8/kWuO4dHydSelD7kBqslRKFv7su5pHLOLP9nEkQfXRa', 'Zane', 'Rush', 'zane.rush@mail.com',
        NULL);
INSERT INTO `amezzon`.`person` (`person_username`, `person_passwordhash`, `person_firstname`, `person_lastname`,
                                `person_mail`, `person_isukukood`)
VALUES ('kristopher', '$2b$12$wIA/lxYGxhbbE9Q7cCWIEOxGXhSRWX1ygG5GnwFwGmELRcPBS8ZFG', 'Kristopher', 'Kaufman',
        'kristopher.kaufan@mail.com', NULL);
INSERT INTO `amezzon`.`person` (`person_username`, `person_passwordhash`, `person_firstname`, `person_lastname`,
                                `person_mail`, `person_isukukood`)
VALUES ('keane', '$2b$12$uDRVp9mr9DeHeRzJbnsWKunFFrzuuJhxRMmKWiXE7pn.lOg5bNMLa', 'Keane', 'Ellwood',
        'keane.elwood@mail.com', NULL);
INSERT INTO `amezzon`.`person` (`person_username`, `person_passwordhash`, `person_firstname`, `person_lastname`,
                                `person_mail`, `person_isukukood`)
VALUES ('arley', '$2b$12$j4aOI2Yq4zd3PNvL89Iq4eQ1mje2D.8IiIIjstLUefwOqA/ynAnCa', 'Arley', 'Singleton',
        'arley.singleton@mail.com', NULL);
INSERT INTO `amezzon`.`person` (`person_username`, `person_passwordhash`, `person_firstname`, `person_lastname`,
                                `person_mail`, `person_isukukood`)
VALUES ('tashan', '$2b$12$JrM7ulmpiXtrjyvlItzNV.DbRITxKkf9xjD1CtliHqIYhCH8sR9Bq', 'Tashan', 'Corbett',
        'tashan.corbett@mail.com', NULL);
INSERT INTO `amezzon`.`person` (`person_username`, `person_passwordhash`, `person_firstname`, `person_lastname`,
                                `person_mail`, `person_isukukood`)
VALUES ('phebe', '$2b$12$uhrFV1AddRQVWK12u/QbC.2AR6ArrE9dZKCSV75A3NNVZ4zKCYA7y', 'Phebe', 'Chandler',
        'phebe.chandler@mail.com', NULL);
INSERT INTO `amezzon`.`person` (`person_username`, `person_passwordhash`, `person_firstname`, `person_lastname`,
                                `person_mail`, `person_isukukood`)
VALUES ('dan', '$2b$12$dC0wfOhzWiJW9UgIskz6.efot2XkhsPXeCwNScYYrHyfQHs2Fvc5S', 'Dan', 'Findlay', 'dan.findlay@mail.com',
        NULL);
INSERT INTO `amezzon`.`person` (`person_username`, `person_passwordhash`, `person_firstname`, `person_lastname`,
                                `person_mail`, `person_isukukood`)
VALUES ('dominika', '$2b$12$eLNYJJsMCg25sWDnj0e.pu21GGRyv2g618jRyqFwzlYKHPLC5ABnu', 'Dominika', 'Farrow',
        'dominika.farrow@mail.com', NULL);
INSERT INTO `amezzon`.`person` (`person_username`, `person_passwordhash`, `person_firstname`, `person_lastname`,
                                `person_mail`, `person_isukukood`)
VALUES ('lilly', '$2b$12$03xK7QG6CSNrLzrMdnXUwuitrpNc0.01MuxXxSTK7EcPAeNtwRjbG', 'Lilly-May', 'Anderson',
        'lillymay.anderson@mail.com', NULL);
INSERT INTO `amezzon`.`person` (`person_username`, `person_passwordhash`, `person_firstname`, `person_lastname`,
                                `person_mail`, `person_isukukood`)
VALUES ('chace', '$2b$12$PeDJu1BRlRbFvMSWQaFaIeu66LlQMXeyinJLxn8kfGTGDT47DYADe', 'Chace', 'Marquez',
        'chace.marquez@mail.com', NULL);

INSERT INTO `amezzon`.`product_type` (`product_type`)
VALUES ('Vegetable');
INSERT INTO `amezzon`.`product_type` (`product_type`)
VALUES ('Fruit');
INSERT INTO `amezzon`.`product_type` (`product_type`)
VALUES ('Grain');
INSERT INTO `amezzon`.`product_type` (`product_type`)
VALUES ('Nut');
INSERT INTO `amezzon`.`product_type` (`product_type`)
VALUES ('Seeds');

INSERT INTO `amezzon`.`transaction_type` (`transaction_type`)
VALUES ('BUYING');
INSERT INTO `amezzon`.`transaction_type` (`transaction_type`)
VALUES ('SELLING');

INSERT INTO `amezzon`.`product` (`product_type`, `product_name`, `product_description`, `product_base_sell`,
                                 `product_base_buy`)
VALUES ('Fruit', 'Apple', 'Granny-Schmidt', 0.20000000, 0.15000000);
INSERT INTO `amezzon`.`product` (`product_type`, `product_name`, `product_description`, `product_base_sell`,
                                 `product_base_buy`)
VALUES ('Fruit', 'Pear', 'Conference', 0.20000000, 0.15000000);
INSERT INTO `amezzon`.`product` (`product_type`, `product_name`, `product_description`, `product_base_sell`,
                                 `product_base_buy`)
VALUES ('Grain', 'Wheat', NULL, 0.05000000, 0.03250000);
INSERT INTO `amezzon`.`product` (`product_type`, `product_name`, `product_description`, `product_base_sell`,
                                 `product_base_buy`)
VALUES ('Grain', 'Oats', NULL, 0.05500000, 0.04000000);
INSERT INTO `amezzon`.`product` (`product_type`, `product_name`, `product_description`, `product_base_sell`,
                                 `product_base_buy`)
VALUES ('Nut', 'Brazil Nut', NULL, 0.02000000, 0.01500000);
INSERT INTO `amezzon`.`product` (`product_type`, `product_name`, `product_description`, `product_base_sell`,
                                 `product_base_buy`)
VALUES ('Nut', 'Peanut', NULL, 0.02000000, 0.01500000);
INSERT INTO `amezzon`.`product` (`product_type`, `product_name`, `product_description`, `product_base_sell`,
                                 `product_base_buy`)
VALUES ('Fruit', 'Strawberry', NULL, 0.10000000, 0.08000000);
INSERT INTO `amezzon`.`product` (`product_type`, `product_name`, `product_description`, `product_base_sell`,
                                 `product_base_buy`)
VALUES ('Seeds', 'Sunflower seeds', 'sun dried', 0.80000000, 0.60000000);
INSERT INTO `amezzon`.`product` (`product_type`, `product_name`, `product_description`, `product_base_sell`,
                                 `product_base_buy`)
VALUES ('Vegetable', 'Potato', 'Mireille', 0.05000000, 0.03500000);
INSERT INTO `amezzon`.`product` (`product_type`, `product_name`, `product_description`, `product_base_sell`,
                                 `product_base_buy`)
VALUES ('Vegetable', 'Onion', NULL, 0.01000000, 0.05000000);

INSERT INTO `amezzon`.`product_history` (`product_history_product_id`, `product_history_buy`, `product_history_sell`,
                                         `product_history_quantity`, `product_history_timestamp`)
VALUES (1, 0.05000000, 0.04000000, 500, '2018-12-02 16:57:17');
INSERT INTO `amezzon`.`product_history` (`product_history_product_id`, `product_history_buy`, `product_history_sell`,
                                         `product_history_quantity`, `product_history_timestamp`)
VALUES (2, 0.05000000, 0.04000000, 600, '2018-12-02 16:57:49');

INSERT INTO `amezzon`.`transaction` (`transaction_type`, `transaction_client`, `transaction_product`,
                                     `transaction_price`, `transaction_quantity`, `transaction_timestamp`)
VALUES ('SELLING', 1, 1, 0.05000000, 500, '2018-12-02 16:59:10');
INSERT INTO `amezzon`.`transaction` (`transaction_type`, `transaction_client`, `transaction_product`,
                                     `transaction_price`, `transaction_quantity`, `transaction_timestamp`)
VALUES ('SELLING', 3, 2, 0.05000000, 600, '2018-12-02 16:59:26');


