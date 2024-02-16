-- CreateTable
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    phone_number VARCHAR(11) NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    email VARCHAR UNIQUE,
    password VARCHAR NOT NULL,
    cpf VARCHAR(15) UNIQUE,
    pix VARCHAR,
    affiliate BOOLEAN DEFAULT FALSE,
    remember_token VARCHAR,
    timestamps TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


-- Seed
INSERT INTO users (
  id,
  name,
  phone_number,
  status,
  email,
  password,
  cpf,
  pix,
  affiliate,
  remember_token,
  timestamps
) VALUES (
  '9rfvGL08-gfgk5486-0348dg',
  'lbdev',
  '31996676094',
  true,
  'lbdev@company.com',
  'password',
  '103490327814',
  'pixkey',
  true,
  'fgpspfmrgm0',
  '2024-3-11 08:43:21'
);

SELECT * FROM users;
