create database amezzon;

create table if not exists person
(
	person_id mediumint auto_increment
		primary key,
	person_username varchar(40) not null,
	person_passwordhash varchar(40) not null,
	person_firstname varchar(50) not null,
	person_lastname varchar(250) not null,
	person_mail varchar(250) not null
)
;

create index person__authentication
	on person (person_username, person_passwordhash)
;

create table if not exists product_type
(
	product_type varchar(10) not null
		primary key
)
;

create table if not exists product
(
	product_id mediumint auto_increment
		primary key,
	product_type varchar(10) not null,
	product_name varchar(50) not null,
	product_description varchar(255) null,
	constraint product_product_name_uindex
		unique (product_name),
	constraint product_product_type_product_type_fk
		foreign key (product_type) references product_type (product_type)
			on delete cascade
)
;

create table if not exists pile
(
	pile_id mediumint not null
		primary key,
	pile_product mediumint not null,
	pile_sell decimal(19,8) not null,
	pile_buy decimal(19,8) not null,
	constraint pile_pile_product_uindex
		unique (pile_product),
	constraint pile_product_product_id_fk
		foreign key (pile_product) references product (product_id)
)
;

create table if not exists transaction_type
(
	transaction_type varchar(10) not null
		primary key
)
;

create table if not exists transaction
(
	transaction_id mediumint auto_increment
		primary key,
	transaction_type varchar(10) not null,
	transaction_client mediumint not null,
	transaction_product mediumint not null,
	transaction_price decimal(19,8) not null,
	transaction_quantity int not null,
	transaction_timestamp datetime not null,
	constraint transaction_person_person_id_fk
		foreign key (transaction_client) references person (person_id),
	constraint transaction_product_product_id_fk
		foreign key (transaction_product) references product (product_id),
	constraint transaction_transaction_type_transaction_type_fk
		foreign key (transaction_type) references transaction_type (transaction_type)
)
;

create index transaction_transaction_client_index
	on transaction (transaction_client)
;

create index transaction_transaction_product_index
	on transaction (transaction_product)
;


