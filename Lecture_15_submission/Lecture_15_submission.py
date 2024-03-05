""" Лекція 15. DB """

print(f"\n=======================| Task 1 |=======================")

#   Create a data model for a AirBnb.com system.
#       Your model should give ability to store information about
#           the users
#           the rooms
#           the reservations
#           and the reviews
#       You should have two types of users:
#           Hosts
#           Guests
#
#   Host should be able
#       to create rooms with different attributes (amount of residents, price, A/C, refrigerator, etc.)
#   Guest should be able to make a
#       Check availability of any roomsMake
#       Reservation for a room.
#
#   For each table you should describe
#       what is the primary key and
#       what are the foreign keys (if any).
#
#   Result of the work might be description in a table.
#   You can create tables in text file with description of each field.
#   You also can you any graphic tool that you might use to create data model.
#   I usually use DRAW.io for such thing, but might choose another tool.
#
#   (Optional): Add these possibilities for a guest
#       Pay for reservation
#       Review for the host.

#   List of this tool: https://www.holistics.io/blog/top-5-free-database-diagram-design-tools/


# =====================================================================
# Result
# =====================================================================

# Hosts:
# host_id	        int	        Primary Key, Unique Identifier
# host_name	        varchar	    Name of the host

# Guests:
# guest_id	        int	        Primary Key, Unique Identifier
# guest_name	    varchar	    Name of the guest

# Rooms:
# room_id	        int	        Primary Key, Unique Identifier
# host_id	        int	        Foreign Key to Hosts table (host_id)
# price	            decimal	    Price per night
# capacity	        int	        Maximum number of residents
# ac	            boolean	    Availability of air conditioning
# refrigerator	    boolean	    Availability of refrigerator
# wifi	            boolean	    Availability of WiFi
# private_bathroom	boolean	    Availability of private bathroom
# pet_friendly	    boolean	    Pet-friendly accommodation

# Reservations Table:
# reservation_id	int	        Primary Key, Unique Identifier
# guest_id	        int	        Foreign Key to Guests table (guest_id)
# room_id	        int	        Foreign Key to Rooms table (room_id)
# check_in_date	    date	    Date of check-in
# check_out_date	date	    Date of check-out
# total_price	    decimal	    Total price of reservation

# Payments Table:

# payment_id	    int	        Primary Key, Unique Identifier
# guest_id	        int	        Foreign Key to Guests table (guest_id)
# reservation_id	int	        Foreign Key to Reservations table (reservation_id)
# amount	        decimal	    Amount paid for reservation
# payment_date	    date	    Date of payment

# Reviews Table:
# review_id	        int	        Primary Key, Unique Identifier
# host_id	        int	        Foreign Key to Hosts table (host_id)
# room_id	        int	        Foreign Key to Rooms table (room_id)
# guest_id          int	        Foreign Key to Guests table (guest_id)
# rating	        int	        Rating given by guest
# comment	        text	    Review comment

