CREATE DATABASE wevo;
use wevo;

CREATE TABLE votes (
  project VARCHAR(20),
  vote VARCHAR(10),
  comment VARCHAR(255)
);

INSERT INTO votes
  (project, vote, comment)
VALUES
  ('Aggie Square', 'yes', 'Needs additional community feedback.'),
  ('Aggie Square', 'no', 'May negatively affect residents.');
