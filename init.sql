CREATE TABLE refercode (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid VARCHAR(36) NOT NULL,
    status TINYINT NOT NULL CHECK (status IN (0, 1, 2))
);