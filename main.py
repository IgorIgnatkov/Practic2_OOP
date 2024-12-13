import os
import time
from data_reader import DataReader
from data_processor import DataProcessor
from statistics_reporter import StatisticsReporter

class Application:
    def __init__(self):
        self.data_reader = DataReader()
        self.data_processor = DataProcessor()
        self.statistics_reporter = StatisticsReporter()

    def run(self):
        while True:
            file_path = input("Введите путь до файла-справочника (или 'exit' для завершения): ")
            if file_path.lower() == 'exit':
                break

            if not os.path.exists(file_path):
                print("Файл не найден. Попробуйте еще раз.")
                continue

            start_time = time.time()

            if file_path.endswith('.xml'):
                data = self.data_reader.read_xml(file_path)
            elif file_path.endswith('.csv'):
                data = self.data_reader.read_csv(file_path)
            else:
                print("Неподдерживаемый формат файла. Поддерживаются только XML и CSV.")
                continue

            duplicates, floor_count = self.data_processor.process_data(data)
            processing_time = time.time() - start_time

            self.statistics_reporter.report_statistics(duplicates, floor_count, processing_time)

if __name__ == "__main__":
    app = Application()
    app.run()
