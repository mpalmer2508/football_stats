from abc import ABC, abstractmethod

class League_Table(ABC):
    def __init__(self, year):
        self.year = year
        self.teams = []

    def add_data(self, data):
        self.teams.append(data)

    def get_table_difference(self):
        return self.teams[0][-1] - self.teams[-1][-1]


class EPL():
    def __init__(self):
        self.tables_by_year = []

    def add_table(self, table):
        self.tables_by_year.append(table)

    def get_tables_by_year(self):
        return self.tables_by_year

    def get_smallest_difference_year(self):
        year = self.tables_by_year[0]
        for i in self.tables_by_year:
            if i.get_table_difference() < year.get_table_difference():
                year = i
        return year

def main():
    epl = EPL()
    file = "scores.txt"
    with open(file) as f:
        for line in f:
            split_line = line.strip("\n").split(",")
            if split_line[0] == "epl":
                first = f.readline().split(",")
                last = f.readline().split(",")

                first_place_name = first[0]
                first_place_points = int(first[1])

                last_place_name = last[0]
                last_place_points = int(last[1])

                table = League_Table(split_line[1])
                table.add_data([first_place_name, first_place_points])
                table.add_data([last_place_name, last_place_points])
                epl.add_table(table)
                
    epl_tables = epl.get_tables_by_year()
    for i in epl_tables:
        print(i.year)
        print(i.get_table_difference())
    print(epl.get_smallest_difference_year().year)
    print(epl.get_smallest_difference_year().get_table_difference())

if __name__ == "__main__":
    main()
