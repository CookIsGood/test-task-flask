
-- auto-generated definition

drop table if exists "animal" cascade;


create table "animal"(
    id    serial  not null
        constraint animal_pk
            primary key,
    name  varchar not null,
    type varchar not null,
    speed integer not null,
    predator boolean not null
);

alter table "animal"
    owner to postgres;

create unique index animal_id_uindex
    on "animal" (id);


INSERT INTO "animal" (name, type, speed, predator) VALUES ('Лось', 'Млеко', 20, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Лось', 'Млеко', 19, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Лось', 'Млеко', 21, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Лось', 'Млеко', 18, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Лось', 'Млеко', 25, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Рысь', 'Млеко', 100, True);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Рысь', 'Млеко', 110, True);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Рысь', 'Млеко', 102, True);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Рысь', 'Млеко', 99, True);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Рысь', 'Млеко', 98, True);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Жаба', 'НеМлеко', 5, True);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Жаба', 'НеМлеко', 6, True);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Жаба', 'НеМлеко', 4, True);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Жаба', 'НеМлеко', 5, True);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Жаба', 'НеМлеко', 3, True);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Окунь', 'НеМлеко', 8, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Окунь', 'НеМлеко', 5, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Окунь', 'НеМлеко', 9, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Окунь', 'НеМлеко', 7, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Олень', 'Млеко', 22, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Олень', 'Млеко', 24, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Олень', 'Млеко', 25, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Олень', 'Млеко', 23, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Курицы', 'НеМлеко', 15, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Курицы', 'НеМлеко', 16, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Курицы', 'НеМлеко', 14, False);
INSERT INTO "animal" (name, type, speed, predator) VALUES ('Курицы', 'НеМлеко', 13, False);