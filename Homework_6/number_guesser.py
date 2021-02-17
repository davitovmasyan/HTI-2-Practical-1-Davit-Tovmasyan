def guesser(start, stop):
    while True:
        command = input('Think of a number between 1 and 999. Input 0 once you’re ready to play.')
        if command == '0':
            break

    step = 0
    guessed = False

    while step < 10:
        step += 1
        guess = (start + stop) // 2
        print(f'My guess number {step}: {guess}')
        hint = input()

        if hint == '0':
            print(f'I guessed in {step} steps.')
            guessed = True
            break
        elif hint == '-1':
            stop = guess - 1
        elif hint == '1':
            start = guess + 1
        else:
            print('Invalid hint!')
            step -= 1

    if not guessed:
        print("I couldn’t guess in 10 steps! This means you cheated!")


guesser(1, 999)
