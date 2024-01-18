def order(data):
        # Returns the listed data in ascending order
        # data should be passed as an int array
        mergeSeperate(data)


def mergeSeperate(data):
        #Standard merge sort in place algorithm
        length = len(data)
        if(length>1):
                middle =length//2

                firstHalf = data[0:middle]
                mergeSeperate(firstHalf)

                secondHalf = data[middle:length]
                mergeSeperate(secondHalf)

                firstCounter = 0
                secondCounter = 0
                counter = 0

                firstTotal = len(firstHalf)
                secondTotal = len(secondHalf)

                while firstCounter < firstTotal and secondCounter < secondTotal:
                        if firstHalf[firstCounter] < secondHalf[secondCounter]:
                                data[counter] = firstHalf[firstCounter]
                                counter = counter + 1
                                firstCounter = firstCounter + 1
                        else:
                                data[counter] = secondHalf[secondCounter]
                                counter = counter + 1
                                secondCounter = secondCounter + 1

                while firstCounter < firstTotal:
                        data[counter] = firstHalf[firstCounter]
                        counter = counter + 1
                        firstCounter = firstCounter + 1
                while secondCounter < secondTotal:
                        data[counter] = secondHalf[secondCounter]
                        counter = counter + 1
                        secondCounter = secondCounter + 1

        #Nothing needs to be returned since it was merged in place
        return

def run_tests():
        # Test Empty list
        data = []
        order(data)
        assert data == []

        # Test Single list
        data = []
        order(data)
        assert data == []

        # Test Sorted int list
        data = [1, 2, 3, 4, 5]
        order(data)
        assert data == [1, 2, 3, 4, 5]

        # Test Sorted double list
        data = [1.1, 2.2, 3.3, 4.4, 5.5]
        order(data)
        assert data == [1.1, 2.2, 3.3, 4.4, 5.5]

        # Test Reverse int sorted list
        data = [5, 4, 3, 2, 1]
        order(data)
        assert data == [1, 2, 3, 4, 5]

        # Test Reverse double sorted list
        data = [5.5, 4.4, 3.3, 2.2, 1.1]
        order(data)
        assert data == [1.1, 2.2, 3.3, 4.4, 5.5]

        # Test Random list
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        order(data)
        assert data == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

        # Test int and double list
        data = [5, 2.5, 1, 3.75, 3, 1.5]
        order(data)
        assert data == [1, 1.5, 2.5, 3, 3.75, 5]

        print("All tests passed!")

run_tests()