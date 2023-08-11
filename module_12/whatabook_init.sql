"William Eckert
08/11/2023
Whatabook_init script"


-- dropping the test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- creating whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- granting all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- dropping contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- dropping tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


/*


    Creating table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('5408 W. Dupont Rd, Fort Wayne, IN, 46818');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Way of Kings', 'Brandon Sanderson', 'Book one of the Stormlight Archives');

INSERT INTO book(book_name, author, details)
    VALUES('Words of Radiance', 'Brandon Sanderson', 'Book two of the Stormlight Archives');

INSERT INTO book(book_name, author, details)
    VALUES('Oathbringer', 'Brandon Sanderson', "Book three of the Stormlight Archives");

INSERT INTO book(book_name, author, details)
    VALUES('Rhythm of War', 'Brandon Sanderson', "Book four of the Stormlight Archives");

INSERT INTO book(book_name, author, details)
    VALUES('Well of Darkness', 'Margaret Weis & Tracy Hickman', 'Book one of the Soverign Stone Trilogy');

INSERT INTO book(book_name, author, details)
    VALUES('Guardians of the Lost', 'Margaret Weis & Tracy Hickman', 'Book two of the Soverign Stone Trilogy');

INSERT INTO book(book_name, author, details)
    VALUES('Journey to the Void', 'Margaret Weis & Tracy Hickman', 'Book three of the Soverign Stone Trilogy');

INSERT INTO book(book_name, author)
    VALUES('Eragon', 'Christopher Paolini');

INSERT INTO book(book_name, author)
    VALUES('The Name of the Wind', 'Patrick Rothfuss');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Kaladin', 'Stormblessed');

INSERT INTO user(first_name, last_name)
    VALUES('Shallan', 'Davar');

INSERT INTO user(first_name, last_name)
    VALUES('Dalinar', 'Kholin');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Kaladin'), 
        (SELECT book_id FROM book WHERE book_name = 'The Way of Kings')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Shallan'),
        (SELECT book_id FROM book WHERE book_name = 'Words of Radiance')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Dalinar'),
        (SELECT book_id FROM book WHERE book_name = 'Oathbringer')
        );