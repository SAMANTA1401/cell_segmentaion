from dataclasses import dataclass

@dataclass
class DataIngestionArtifact: # embed two return path strings in a single class
    data_zip_file_path:str
    feature_store_path:str


