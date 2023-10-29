-- Create the "sales" table
CREATE TABLE sales (
    brand VARCHAR NOT NULL,
    segment VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (brand, segment, country)
);

-- Insert records for 5 different brands, 5 different segments, and 5 different countries

-- Brand 1, Segment 1, Country 1
INSERT INTO sales (brand, segment, country, quantity)
VALUES ('Brand1', 'Segment1', 'Country1', 10);

-- Brand 2, Segment 2, Country 2
INSERT INTO sales (brand, segment, country, quantity)
VALUES ('Brand2', 'Segment2', 'Country2', 15);

-- Brand 3, Segment 3, Country 3
INSERT INTO sales (brand, segment, country, quantity)
VALUES ('Brand3', 'Segment3', 'Country3', 20);

-- Brand 4, Segment 4, Country 4
INSERT INTO sales (brand, segment, country, quantity)
VALUES ('Brand4', 'Segment4', 'Country4', 25);

-- Brand 5, Segment 5, Country 5
INSERT INTO sales (brand, segment, country, quantity)
VALUES ('Brand5', 'Segment5', 'Country5', 30);

-- Display the "sales" table after inserting records
SELECT * FROM sales;

-- Create a data cube using UNION ALL
SELECT brand, segment, country, SUM(quantity) AS total_quantity
FROM sales
GROUP BY brand, segment, country
ORDER BY brand, segment, country;

drop table sales;