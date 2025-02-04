from response_processor import ResponseProcessor
import logging
import sys

def main():
    try:
        processor = ResponseProcessor(
            input_file="input.csv",
            output_file="output.csv"
        )
        processor.process()
    except Exception as e:
        logging.error(f"Application error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
