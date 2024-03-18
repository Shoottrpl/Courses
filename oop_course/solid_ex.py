from solid import Computer, SaveComputerToFile, SaveComputerToDB, OmenHP

class Main():
    comp = Computer("IBM TXT", 5000)
    # saver = SaveComputerToDB()
    # saver.save("out.dat", comp)


    @staticmethod
    def test(self):
        comp = Computer("IBM TXT", 5000)
        comp2 = OmenHP("OmenHp", 5000)
        comp2.set_data("IBM XT")

        if comp.name == comp2.name and comp.memory_size == comp2.memory_size:
            print("test OK")
        else:
            print("test FAIL")
    test()
