create database banco1;
\c banco1;

 create table cliente(id serial primary key, nome varchar (50), email varchar (50));

insert into cliente (nome, email) values ('belem','belem@gmail.com');

insert into cliente (nome, email) values ('ana','ana@gmail.com');

\dt
\d cliente

select * from cliente;


