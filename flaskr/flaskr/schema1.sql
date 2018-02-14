drop table if exists entires;
create table entries(
    "id" serial primary key,
    title text not null,
    "text" text not null
);
