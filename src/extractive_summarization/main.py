import argparse
from spacy.lang.zh import Chinese
from summarizer import Summarizer
from summarizer.text_processors.sentence_handler import SentenceHandler
import time
from transformers import AutoConfig, AutoTokenizer, AutoModel

MODEL_NAME = 'bert-base-chinese'


def load_model(model_name: str):
    custom_config = AutoConfig.from_pretrained(model_name)
    custom_config.output_hidden_states = True
    custom_tokenizer = AutoTokenizer.from_pretrained(model_name)
    custom_model = AutoModel.from_pretrained(
        model_name, config=custom_config)

    custom_sentence_handler = SentenceHandler(language=Chinese)

    model = Summarizer(
        custom_model=custom_model,
        custom_tokenizer=custom_tokenizer,
        sentence_handler=custom_sentence_handler,
    )
    return model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Extractive Summarization')

    parser.add_argument('--file', type=str, required=True,
                        help='Input text file')

    return parser.parse_args()


def main():
    args = parse_args()

    print('Start loading model...')
    start_time = time.time()
    model = load_model(MODEL_NAME)
    end_time = time.time()
    print(f'Model loaded in {end_time - start_time} seconds')

    with open(args.file, 'r', encoding='utf-8') as f:
        text = f.read()

    print(f'Start summarizing text, text length: {len(text)},'
          f' model: {MODEL_NAME}...')
    start_time = time.time()
    summary = model(text)
    end_time = time.time()
    print(f"Time taken for summarization: {end_time - start_time} seconds")

    print("Summary:")
    print(summary)


if __name__ == '__main__':
    main()
