class TestEncoding:
    def input8():
        return [0,  0,  90, 74,
                68, 50, 43, 205,
                64, 145,145,145,
                100,145,145,145]
    def Result8():
        return ["1100000000000000000000000110110010",
                "00000000100",
                "0001000111",
                "00000000111",
                "00000000000000000000000101011101",
                "00000000000000000000000110111011",
                "100110",
                "00000000000000000000000110111100",
                "000110",
                "00000000000000000000000101110110",
                "000000000000000000100",
                "100010",
                "11"]