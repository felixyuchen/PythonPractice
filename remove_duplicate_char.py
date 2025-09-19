class RemoveDuplicateChar:
    def remove_duplicate_char(self, input_str):
        input_list = list(input_str)
        input_set = set()
        for ch in input_list:
            input_set.add(ch)
        return input_set

    def main(self):
        input_str = "please input a number"
        print(self.remove_duplicate_char(input_str))

if __name__=="__main__":
    rdc = RemoveDuplicateChar()
    rdc.main()