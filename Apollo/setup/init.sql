CREATE TABLE IF NOT EXISTS details(
    id                       INT NOT NULL,
    standing_people_capacity INT NOT NULL,
    sitting_people_capacity  INT NOT NULL,
    disabled_people_capacity INT NOT NULL,
    average_people_count     INT NOT NULL,
    PRIMARY KEY (id));


CREATE TABLE IF NOT EXISTS bus_to_number(
    id        INT NOT NULL AUTO_INCREMENT,
    bus_id    INT NOT NULL,
    number    INT NOT NULL,
    PRIMARY KEY (id));


INSERT INTO details(id, standing_people_capacity, sitting_people_capacity, disabled_people_capacity, average_people_count)
VALUES
(1, 20, 30, 5, 50),
(2, 30, 40, 5, 50),
(3, 40, 20, 5, 50),
(4, 20, 20, 5, 50),
(5, 30, 30, 5, 60),
(6, 50, 50, 5, 60),
(7, 30, 40, 5, 60),
(8, 20, 20, 5, 60),
(9, 10, 30, 5, 60),
(10, 30, 80, 5, 55),
(11, 30, 80, 5, 55),
(12, 30, 80, 5, 55),
(13, 30, 80, 5, 55),
(14, 30, 80, 5, 55),
(15, 30, 80, 5, 55),
(16, 30, 80, 5, 55),
(17, 30, 80, 5, 75),
(18, 30, 80, 5, 75),
(19, 30, 80, 5, 75),
(20, 30, 80, 5, 75),
(21, 30, 80, 5, 75),
(22, 30, 80, 5, 75),
(23, 30, 80, 5, 100),
(24, 30, 80, 5, 100);

INSERT INTO bus_to_number(bus_id, number)
VALUES
(1,  94),
(2,  94),
(3,  94),
(4,  94),
(5,  280),
(6,  280),
(7,  280),
(8,  280),
(9,  280),
(10, 14),
(11, 14),
(12, 14),
(13, 413),
(14, 413),
(15, 413),
(16, 413),
(17, 413),
(18, 413),
(19, 72),
(20, 72),
(21, 72),
(22, 72),
(23, 72),
(24, 72);

