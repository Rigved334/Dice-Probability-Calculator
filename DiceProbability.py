class DiceProbability:
    def __init__(self):
        self.sample_space = []

    # Probability of throwing one dice 
    def probability_for_one_dice(self):
        for i in range(1, 7):
            self.sample_space.append(i)

        self.event = []
        n = int(input("enter the number on dice: "))
        self.event.append(n)

        probability = len(self.event) / len(self.sample_space)
        print("probability for one dice:", probability)        
    
    # Probability for throwing two dice 
    def probability_for_two_dice(self):
        for i in range(1, 7):
            for j in range(1, 7):
                self.sample_space.append((i, j))

        self.event_list = []
        n1 = int(input("enter the number on dice 1: "))
        n2 = int(input("enter the number on dice 2: "))
        self.event_list.append((n1, n2))

        probability = len(self.event_list) / len(self.sample_space)
        print("probability for two dice:", probability)

    # Probability of throwing multiple dice 
    def many_dies(self):
        event = []
        number_of_dies = int(input("enter number of dies: "))
        for i in range(number_of_dies):
            num = int(input(f"enter the number on dice {i + 1}: "))
            event.append(num)

        sample_space = 6 ** number_of_dies
        favourable_outcome = 1

        probability = favourable_outcome / sample_space
        print("probability:", probability)

dp = DiceProbability()
dp.probability_for_one_dice()
dp.probability_for_two_dice()
dp.many_dies()