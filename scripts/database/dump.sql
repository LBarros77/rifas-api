-- CreateTable
CREATE TABLE IF NOT EXISTS Users (
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
  created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Products (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  price DECIMAL,
  status VARCHAR,
  quantity INTEGER NOT NULL,
  processed INTEGER NOT NULL,
  type_raffles VARCHAR,
  favorite BOOLEAN DEFAULT FALSE,
  game_mode VARCHAR,
  minimum INTEGER,
  maximum INTEGER,
  user_id VARCHAR,
  draw_date TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(user_id) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS PaymentPix (
  key_pix VARCHAR NOT NULL,
  participant_id iNTEGER NOT NULL UNIQUE,
  FOREIGN KEY(participant_id) REFERENCES Participate(id)
);

CREATE TABLE IF NOT EXISTS Order (
  participant_id INTEGER PRIMARY KEY,
  key_pix VARCHAR,
  dates VARCHAR,
  price DECIMAL DEFAULT 0.0,
  FOREIGN KEY(participant_id) REFERENCES Participate(id)
);

CREATE TABLE IF NOT EXISTS Participate (
  id SERIAL PRIMARY KEY,
  number_list VARCHAR NOT NULL,
  reserveds INTEGER NOT NULL,
  payeds INTEGER NOT NULL,
  conferred BOOLEAN DEFAULT TRUE,
  FOREIGN KEY(number_list) REFERENCES Products(participate),
  FOREIGN KEY(reserveds) REFERENCES Order(participant),
  FOREIGN KEY(payeds) REFERENCES Raffles(participant),
  FOREIGN KEY(conferred) REFERENCES PaymentPix(participant),
  UNIQUE(number_list, reserveds, conferred),
  CHECK(conferred in (TRUE, FALSE))
);

CREATE TABLE IF NOT EXISTS Raffles (
  product_id INTEGER,
  participant_id INTEGER,
  PRIMARY KEY(product_id, participant_id)
  FOREIGN KEY(product_id) REFERENCES Products(id),
  FOREIGN KEY(participant_id) REFERENCES Participate(id),
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
  created_at
) VALUES (
  'b5163063-f94e-4e70-ad42-06065fa7e3c7',
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

INSERT INTO Products (
  id,
  name,
  price,
  status,
  quantity,
  processed,
  type_raffles,
  favorite,
  game_mode,
  minimum,
  maximum,
  user_id,
  draw_date,
  created_at
) VALUES (
  1,
  'Product one',
  3.40,
  'pendente',
  4,
  2,
  'Gamer',
  FALSE,
  'números',
  1,
  200,
  'b5163063-f94e-4e70-ad42-06065fa7e3c7',
  '2024-9-11 08:43:21',
  '2024-3-11 08:43:21'
);

SELECT * FROM users;
