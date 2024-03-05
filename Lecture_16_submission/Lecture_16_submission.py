""" Лекція 16. SQL """

print(f"\n=======================| Task 1 |=======================")

#   1. Write SQL queries for table creation
#       for a data model that you created for prev homework (Airbnb model)


# CREATE TABLE IF NOT EXISTS Hosts (
#     host_id SERIAL PRIMARY KEY,
#     host_name VARCHAR(255)
# );
#
# CREATE TABLE IF NOT EXISTS Guests (
#     guest_id SERIAL NOT NULL PRIMARY KEY,
#     guest_name VARCHAR(255)
# );
#
# CREATE TABLE IF NOT EXISTS Rooms (
#     room_id SERIAL PRIMARY KEY,
#     host_id INT,
#     price DECIMAL(10, 2),
#     capacity INT,
#     ac BOOLEAN,
#     refrigerator BOOLEAN,
#     wifi BOOLEAN,
#     private_bathroom BOOLEAN,
#     pet_friendly BOOLEAN,
#     FOREIGN KEY (host_id) REFERENCES Hosts(host_id)
# );
#
# CREATE TABLE IF NOT EXISTS Reservations (
#     reservation_id SERIAL PRIMARY KEY,
#     guest_id INT,
#     room_id INT,
#     check_in_date DATE,
#     check_out_date DATE,
#     total_price DECIMAL(10, 2),
#     FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
#     FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
# );
#
# CREATE TABLE IF NOT EXISTS Payments (
#     payment_id SERIAL PRIMARY KEY,
#     guest_id INT,
#     reservation_id INT,
#     amount DECIMAL(10, 2),
#     payment_date DATE,
#     FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
#     FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
# );
#
# CREATE TABLE IF NOT EXISTS Reviews (
#     review_id SERIAL PRIMARY KEY,
#     guest_id INT,
#     host_id INT,
#     room_id INT,
#     rating INT,
#     comment TEXT,
#     FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
#     FOREIGN KEY (host_id) REFERENCES Hosts(host_id),
#     FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
# );


print(f"\n=======================| Task 2 |=======================")

#   2. Write 3 rows (using INSERT queries)
#       for each table in the data model


# INSERT INTO Hosts (host_name) VALUES
# ('John Doe'),
# ('Jane Smith'),
# ('Michael Johnson');

# INSERT INTO Guests (guest_name) VALUES
# ('Alice Brown'),
# ('Bob Green'),
# ('Charlie White');

# INSERT INTO Rooms (host_id, price, capacity, ac, refrigerator, wifi, private_bathroom, pet_friendly) VALUES
# (1, 100.00, 2, 1, 1, 1, 1, 0),
# (1, 120.00, 3, 1, 1, 1, 1, 1),
# (2, 80.00, 1, 0, 1, 1, 0, 0);

# INSERT INTO Reservations (guest_id, room_id, check_in_date, check_out_date, total_price) VALUES
# (1, 1, '2024-03-10', '2024-03-15', 500.00),
# (2, 2, '2024-03-12', '2024-03-14', 240.00),
# (3, 3, '2024-03-08', '2024-03-11', 240.00);

# INSERT INTO Reviews (guest_id, host_id, room_id, rating, comment) VALUES
# (1, 1, 1, 4, 'Great host and comfortable room.'),
# (2, 1, 2, 5, 'Amazing stay! Highly recommended.'),
# (3, 2, 3, 3, 'Room was clean but a bit small.');

# INSERT INTO Payments (guest_id, reservation_id, amount, payment_date) VALUES
# (1, 1, 500.00, '2024-03-10'),
# (2, 2, 240.00, '2024-03-12'),
# (3, 3, 240.00, '2024-03-08');


print(f"\n=======================| Task 3 |=======================")

#   3. Create the next analytic queries:
#       1. Find a user who had the biggest amount of reservations. Return user_name and user_id
#       2. (Optional) Find a host who earned the biggest amount of money for the last month. Return hostname and host_id
#       3. (Optional) Find a host with the best average rating. Return hostname and host_id


#       1. Find a user who had the biggest amount of reservations. Return user name and user_id
# SELECT g.guest_id, g.guest_name
# FROM Guests g
# JOIN (
#     SELECT guest_id, COUNT(*) AS reservation_count
#     FROM Reservations
#     GROUP BY guest_id
#     ORDER BY reservation_count DESC
#     LIMIT 1
# ) AS max_reservations ON g.guest_id = max_reservations.guest_id;

#       2. (Optional) Find a host who earned the biggest amount of money for the last month. Return hostname and host_id
# SELECT h.host_id, h.host_name
# FROM Hosts h
# JOIN (
#     SELECT r.host_id, SUM(p.amount) AS total_earnings
#     FROM Reservations res
#     JOIN Rooms r ON res.room_id = r.room_id
#     JOIN Payments p ON res.reservation_id = p.reservation_id
#     WHERE DATE_TRUNC('month', p.payment_date) = DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1' MONTH)
#     GROUP BY r.host_id
#     ORDER BY total_earnings DESC
#     LIMIT 1
# ) AS max_earnings ON h.host_id = max_earnings.host_id;

#       3. (Optional) Find a host with the best average rating. Return hostname and host_id
# SELECT h.host_id, h.host_name
# FROM Hosts h
# JOIN (
#     SELECT host_id, AVG(rating) AS avg_rating
#     FROM Reviews
#     GROUP BY host_id
#     ORDER BY avg_rating DESC
#     LIMIT 1
# ) AS best_avg_rating ON h.host_id = best_avg_rating.host_id;
