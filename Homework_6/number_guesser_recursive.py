def guesser(start, stop, step=0):
    if step == 0:
        while True:
            command = input('Think of a number between 1 and 999. Input 0 once you’re ready to play.')
            if command == '0':
                break

    if step < 10:
        step += 1
        guess = (start + stop) // 2
        print(f'My guess number {step}: {guess}')
        hint = input()

        if hint == '0':
            print(f'I guessed in {step} steps.')
        elif hint == '-1':
            guesser(start, guess - 1, step)
        elif hint == '1':
            guesser(guess + 1, stop, step)
        else:
            print('Invalid hint!')
            step -= 1
            guesser(start, stop, step)
    else:
        print("I couldn’t guess in 10 steps! This means you cheated!")


guesser(1, 999)
