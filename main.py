#hello
print("maded by tiny_mauss")
print("-------------------")
print(" ")

def main():

  marks = input("Input your mark: ")

  try:

    m=int(marks)

    # <1
    if m<1:
      level="wtf? Your level is so low that I can't even deduce this value!"

    #1, 2, 3
    elif m<=3 and m>0:
      level="low"

    #4, 5, 6
    elif m>3 and m<7:
      level="middle"

    #7, 8, 9
    elif m>6 and m<10:
      level="adequate"

    #10, 11, 12
    elif m>9 and m<13:
      level="high"

    #>13
    else:
      level="you are god in your school"

    #output
    print("Your level is: " + level)

  #m!=int
  except ValueError:
    print("you input NaN")
    print(" ")
    main()


main()

#bye
print("thx for using this useless program")
print("bye")
