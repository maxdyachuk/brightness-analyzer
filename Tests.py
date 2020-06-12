import ImageAnalyzer



def testsForBrightness(path):
    ImageAnalyzer.sortImages(path)
    with open("results.xml", "rt") as res:
        try:
            if 1 == int(res.readline().split(" ")[3]):
                print("TEST 1 COMPLETE SUCCESSFULLY")
            else:
                print("TEST 1 FAILED")
            if 5 == int(res.readline().split(" ")[3]):
                print("TEST 2 COMPLETE SUCCESSFULLY")
            else:
                print("TEST 2 FAILED")
        except:
            print("test images aren't correct")
