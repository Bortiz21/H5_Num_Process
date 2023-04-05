# Homework 5: Numeric Processing
# Program By: Brandon Ortiz
# File Name: H5_Num_Process.py
# Function: This program reads and writes to files.


# Read all numbers from the file and display them to the screen
def display_numbers(file):
    file.seek(0)
    for x in file:
        x = int(x)
        print(x)


# Count the amount of numbers stored in the file and display to the screen
def number_amount(file):
    file.seek(0)
    count = 0
    for x in file:
        count += 1
    return count


# Calculate the sum of all the numbers in the file and display it to the screen
def total_amount(file):
    file.seek(0)
    final_amount = 0
    for x in file:
        x = int(x)
        final_amount += x
    return final_amount


# Calculate the average of all numbers in the file and display them to the screen
def average(sum_of_values, number_of_values):
    average_f = (sum_of_values / number_of_values)
    if average_f != 0:
        return average_f
    else:
        print("Error, please try again!")


# Display and write the amounts both in the current file and into a new file (Result)
def display_and_write(total_amount_num, sum_of_all_numbers, average_disp):
    out_file = open('Results.txt', 'w')

    print(f"There are {total_amount_num} numbers within the file")
    print(f"The sum of all numbers in the file is {sum_of_all_numbers}")
    print(f"The average of all numbers in the file is {average_disp:.0f}")
    print(f"The results have been written to file {out_file.name}")

    out_file.write(f"There are {total_amount_num} numbers within the file\n")
    out_file.write(f"The sum of all numbers in the file is {sum_of_all_numbers}\n")
    out_file.write(f"The average of all numbers in the file is {average_disp:.0f}\n")
    out_file.close()


def main():
    # print("This is main\n-------------------------\n")
    random_nums = open('Random.txt', 'r')
    print(f"Reading from {random_nums.name}")

    display_numbers(random_nums)
    n_amount = (number_amount(random_nums))
    t_amount = (total_amount(random_nums))
    a_amount = average(t_amount, n_amount)
    random_nums.close()
    display_and_write(n_amount, t_amount, a_amount)


# Write the results from the prior functions (amount, sum, average) to a file
if __name__ == '__main__':
    main()
