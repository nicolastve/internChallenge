CREATE TABLE users (
    id INT AUTO_INCREMENT NOT NULL,
    dni VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE entryMarks (
    id INT AUTO_INCREMENT NOT NULL,
    user_id INT,
    date DATE NOT NULL,
    time TIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE exitMarks (
    id INT AUTO_INCREMENT NOT NULL,
    user_id INT,
    date DATE NOT NULL,
    time TIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE reports (
    id INT AUTO_INCREMENT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status VARCHAR(255) NOT NULL,
    path VARCHAR(255),
    PRIMARY KEY (id)
);