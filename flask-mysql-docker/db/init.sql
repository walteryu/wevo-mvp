CREATE DATABASE wevo;
use wevo;

CREATE TABLE votes (
  project_name VARCHAR(255),
  vote BOOLEAN,
  vote_date DATE,
  lat DECIMAL(10, 4),
  lng DECIMAL(10, 4),
  comment VARCHAR(255)
);

INSERT INTO votes
  (
    project_name,
    vote,
    vote_date,
    lat,
    lng,
    comment
  )
VALUES
  ('Aggie Square', 1, '2019-07-01', 38.574740, -121.493580, 'Needs additional community feedback.'),
  ('Aggie Square', 0, '2019-07-01', 38.574740, -121.493580, 'May negatively affect residents.');
