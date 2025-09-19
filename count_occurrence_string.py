class CountOccurrence:
    def count_occurrence_string(self, input_str):
        input_list = list(input_str)
        occurrence_dict = {}
        for i in input_list:
            if i in occurrence_dict:
                occurrence_dict[i] += 1
            else:
                occurrence_dict[i] = 1
        return occurrence_dict

    def main(self):
        input = "please enter a number"
        print(self.count_occurrence_string(input))

if __name__=="__main__":
    occ = CountOccurrence()
    occ.main()