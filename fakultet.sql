CREATE TABLE
    fakultet (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nomi VARCHAR(200) NOT NULL
    );

CREATE TABLE
    talaba (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ism VARCHAR(100) NOT NULL,
        jins VARCHAR(10) NOT NULL,
        faol BOOLEAN NOT NULL,
        fakultet_id INT,
        FOREIGN KEY (fakultet_id) REFERENCES fakultet (id)
    );