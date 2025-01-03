if __name__ == "__main__":
    from main.processors.model_processor import ModelProcessor

    processor = ModelProcessor()
    processor.train_and_save_model()
