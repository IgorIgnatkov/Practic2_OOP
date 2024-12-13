class StatisticsReporter:
    def report_statistics(self, duplicates, floor_count, processing_time):
        print(f"Время обработки файла: {processing_time:.2f} секунд")

        print("\nДублирующиеся записи:")
        for key, count in duplicates.items():
            if count > 1:
                print(f"Город: {key[0]}, Улица: {key[1]}, Дом: {key[2]}, Количество повторений: {count}")

        print("\nКоличество зданий по этажности в каждом городе:")
        for city, floors in floor_count.items():
            print(f"Город: {city}")
            for floor, count in floors.items():
                print(f"  {floor}-этажных зданий: {count}")
