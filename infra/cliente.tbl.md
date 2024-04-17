create database banco1;
\c banco1;

create table cliente(id serial primary key, nome varchar (50), email varchar (50));

insert into cliente (nome, email) values ('belem','belem@gmail.com');

insert into cliente (nome, email) values ('ana','ana@gmail.com');

\dt
\d cliente
                                   Table "public.cliente"
 Column |         Type          | Collation | Nullable |               Default
--------+-----------------------+-----------+----------+-------------------------------------
 id     | integer               |           | not null | nextval('cliente_id_seq'::regclass)
 nome   | character varying(50) |           |          |
 email  | character varying(50) |           |          |
Indexes:
    "cliente_pkey" PRIMARY KEY, btree (id)



select * from cliente;

