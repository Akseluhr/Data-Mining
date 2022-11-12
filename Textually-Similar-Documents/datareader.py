import string
import os


class DataReader:

    def __int__(self):
        pass

    @staticmethod
    def preprocess_document(_self, document):
        document = ''.join(char for char in document if char not in string.punctuation)
        document = ' '.join(document.split())
        return document

    def preprocess_all_documents(self, documents):
        return [self.preprocess_document(self, document) for document in documents]

    @staticmethod
    def read_text_file(_self, file_path):
        with open(file_path, 'r') as f:
            return [f.read()]

    def read_all_text_files(self, path_to_files):
        all_documents = []
        for file in os.listdir(path_to_files):
            if file.endswith(".txt"):
                file_path = f"{path_to_files}/{file}"
                document = self.read_text_file(self, file_path)
                all_documents.append(document)

        return all_documents

    def read_and_pre_process_all_documents(self, path_to_files):
        all_documents = self.read_all_text_files(path_to_files)
        pre_processed_documents = self.preprocess_all_documents(all_documents)
        return pre_processed_documents

