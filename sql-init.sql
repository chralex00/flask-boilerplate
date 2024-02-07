CREATE TABLE IF NOT EXISTS people (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    `first_name` VARCHAR(64) NOT NULL,
    `last_name` VARCHAR(64) NOT NULL,
    `birthday_year` INTEGER NOT NULL,
    `gender` VARCHAR(32) NOT NULL,
    `email` VARCHAR(256) NOT NULL
);
