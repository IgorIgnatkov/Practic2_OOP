class DataProcessor:
    def process_data(self, data):
        duplicates = {}
        floor_count = {}

        for record in data:
            key = (record[0], record[1], record[2])
            if key in duplicates:
                duplicates[key] += 1
            else:
                duplicates[key] = 1

            if record[0] not in floor_count:
                floor_count[record[0]] = {str(i): 0 for i in range(1, 6)}
            floor_count[record[0]][record[3]] += 1

        return duplicates, floor_count
