import logic

print("Welcome to solver of integral!")


while 1:
    print("Available functionality:\n" +
          "\t1. Left side modification solve.\n" +
          "\t2. Right side modification solve.\n" +
          "\t3. Medium modification solve.\n" +
          "\t4. Exit.\n")
    try:
        answer = float(input("Please choose a variant: ").strip())
        if answer == 1:
            logic.leftSideModSolve()
            continue
        elif answer == 2:
            logic.rightSideModSolve()
            continue
        elif answer == 3:
            logic.mediumModeSolve()
            continue
        elif answer == 4:
            print("Exit...")
            break
    except TypeError:
        logic.getReadyAnswer(3)
        continue
    except ValueError:
        logic.getReadyAnswer(3)
        continue
