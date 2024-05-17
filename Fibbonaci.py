
legth_of_sequence = int(input("How many numbers of the sequence do you want to generate: "))

last_number_of_sequence = 0
second_last_number_of_sequence = 0

for i in range(legth_of_sequence):
    xc = (last_number_of_sequence+second_last_number_of_sequence)
    print(xc)
    if xc==0:
        second_last_number_of_sequence = last_number_of_sequence
        last_number_of_sequence = 1
    
    second_last_number_of_sequence = last_number_of_sequence
    last_number_of_sequence = xc