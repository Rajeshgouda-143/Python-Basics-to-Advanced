'''WAP FOR TICKET BOOKING APP IF THE AGE IS LESS THAN 7 THE TICKET PRICE IS 20% DISCOUNT , IF THE GENDER IS A FEMALE THE TICKET PRICE WILL
BE FARE , AND IF THE GENDER IS MALE THE TICKET PRICE WILL BE 5 * NO.OF STATION .'''

print("\t\t\t WELCOME TO MTC TICKET BOOKING APPLICATION")

stations = {"CHROMEPET":1,"PALLAVARAM":2,"AIRPORT":3,"GUINDY":4,"TAMBARAM":5}

start_station = input("FROM : ").lower()
end_station = input("END : " ).lower()

no_of_station = stations[end_station] - stations[start_station]

gender = input("Enter Your Gender: ").lower()

if gender == "male":
    age = int(input("Enter your age: "))
    if age <= 7:
        total_amount = 5 * no_of_station
        discount_amount = total_amount * 20//100
        fare = total_amount - discount_amount
    else:
        fare = 5 * no_of_station
elif gender == "female":
    fare = 0

print("\t\t\t----Ticket-----")
print("-"*20)
print(f"FROM : {start_station} TO : {end_station}")
print(f"FARE : {abs(fare)} RS")




