
from datasets import load_dataset
import nltk
from nltk.tokenize import sent_tokenize
from transformers.pipelines import pipeline
from transformers.trainer_utils import set_seed
from typing import Any


def tokenize_sentence():
    nltk.download('punkt')
    nltk.download('punkt_tab')

    string = "The U.S. are a country. The U.N. is an organization."
    tokenized_sentences = sent_tokenize(string)
    return tokenized_sentences


def summarize_baseline(summaries: dict[str, Any], sample_text: str):
    def three_sentence_summary(text: str):
        return "\n".join(sent_tokenize(text)[:3])

    summaries["baseline"] = three_sentence_summary(sample_text)


def summarize_with_gpt2(summaries: dict[str, Any], sample_text: str):
    set_seed(42)
    pipe = pipeline("text-generation", model="gpt2")
    gpt2_query = sample_text + "\nTL;DR:\n"
    pipe_out = pipe(gpt2_query, max_length=512,
                    clean_up_tokenization_spaces=True)
    summaries["gpt2"] = sent_tokenize(
        pipe_out[0]["generated_text"][len(gpt2_query):])


def main():
    dataset = load_dataset("cnn_dailymail", "3.0.0")

    summaries: dict[str, Any] = {}
    sample_text: str = dataset["train"][1]["article"][:2000]

    tokenized_sentences = tokenize_sentence()
    print("Tokenized Sentences:", tokenized_sentences)

    summarize_baseline(summaries, sample_text)
    summarize_with_gpt2(summaries, sample_text)

    print("Summaries:", summaries)


if __name__ == "__main__":
    main()
