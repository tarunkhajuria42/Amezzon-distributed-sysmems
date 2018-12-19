-- we don't know how to generate schema amezzon (class Schema) :(
create table if not exists person
(
  person_id
  mediumint
  auto_increment
  primary
  key,
  person_username
  varchar
(
  40
) not null,
  person_passwordhash varchar
(
  60
) not null,
  person_firstname varchar
(
  50
) not null,
  person_lastname varchar
(
  250
) not null,
  person_mail varchar
(
  250
) not null,
  person_isukukood varchar
(
  11
) null,
  constraint person_isukukood_uindex
  unique
(
  person_isukukood
),
  constraint person_person_username_uindex
  unique
(
  person_username
)
  )
;

create
index
person__authentication
on
person
(
person_username,
person_passwordhash
)
;

create table if not exists product_type
(
  product_type varchar
(
  10
) not null
  primary key
  )
;

create table if not exists product
(
  product_id
  mediumint
  auto_increment
  primary
  key,
  product_type
  varchar
(
  10
) not null,
  product_name varchar
(
  50
) not null,
  product_description varchar
(
  255
) null,
  product_base_sell decimal
(
  19,
  8
) not null,
  product_base_buy decimal
(
  19,
  8
) not null,
  constraint product_product_name_uindex
  unique
(
  product_name
),
  constraint product_product_type_product_type_fk
  foreign key
(
  product_type
) references product_type
(
  product_type
)
  on delete cascade
  )
;

create table if not exists product_history
(
  product_history_id
  mediumint
  auto_increment
  primary
  key,
  product_history_product_id
  mediumint
  not
  null,
  product_history_buy
  decimal
(
  19,
  8
) not null,
  product_history_sell decimal
(
  19,
  8
) not null,
  product_history_quantity int not null,
  product_history_timestamp datetime not null,
  constraint product_history_product_product_id_fk
  foreign key
(
  product_history_product_id
) references product
(
  product_id
)
  )
;

create
index
product_history_product_history_timestamp_index
on
product_history
(
product_history_timestamp
)
;

create table if not exists transaction_type
(
  transaction_type varchar
(
  10
) not null
  primary key
  )
;

create table if not exists transaction
(
  transaction_id
  mediumint
  auto_increment
  primary
  key,
  transaction_type
  varchar
(
  10
) not null,
  transaction_client mediumint not null,
  transaction_product mediumint not null,
  transaction_price decimal
(
  19,
  8
) not null,
  transaction_quantity int not null,
  transaction_timestamp datetime not null,
  constraint transaction_person_person_id_fk
  foreign key
(
  transaction_client
) references person
(
  person_id
),
  constraint transaction_product_product_id_fk
  foreign key
(
  transaction_product
) references product
(
  product_id
),
  constraint transaction_transaction_type_transaction_type_fk
  foreign key
(
  transaction_type
) references transaction_type
(
  transaction_type
)
  )
;

create
index
transaction_transaction_client_index
on
transaction
(
transaction_client
)
;

create
index
transaction_transaction_product_index
on
transaction
(
transaction_product
)
;

create
or
replace
view
product_price
as
SELECT *
FROM product_history
       INNER JOIN (SELECT product_history_product_id, MAX(product_history_timestamp) AS product_history_timestamp
                   FROM product_history
                   GROUP BY product_history_product_id) AS latest
                  USING (product_history_product_id, product_history_timestamp)


