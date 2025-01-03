if __name__ == "__main__":
    from app.processors.model_processor import ModelProcessor

    processor = ModelProcessor()
    processor.train_and_save_model()
