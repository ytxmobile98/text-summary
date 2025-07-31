
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
    print("Summary with GPT-2:", pipe_out)

    summaries["gpt2"] = sent_tokenize(
        pipe_out[0]["generated_text"][len(gpt2_query):])


def summarize_with_t5(summaries: dict[str, Any], sample_text: str):
    pipe = pipeline("summarization", model="t5-small")
    pipe_out = pipe(sample_text)
    print("Summary with T5:", pipe_out)

    summaries["t5"] = "\n".join(sent_tokenize(pipe_out[0]["summary_text"]))


def summarize_with_bart(summaries: dict[str, Any], sample_text: str):
    pipe = pipeline("summarization", model="facebook/bart-base")
    pipe_out = pipe(sample_text)
    print("Summary with BART:", pipe_out)

    summaries["bart"] = "\n".join(sent_tokenize(pipe_out[0]["summary_text"]))


def summarize_with_pegasus(summaries: dict[str, Any], sample_text: str):
    pipe = pipeline("summarization", model="google/pegasus-cnn_dailymail")
    pipe_out = pipe(sample_text)
    print("Summary with PEGASUS:", pipe_out)

    summaries["pegasus"] = pipe_out[0]["summary_text"].replace(" .<n>", ".\n")


def main():
    dataset = load_dataset("cnn_dailymail", "3.0.0")

    summaries: dict[str, Any] = {}
    sample_text: str = dataset["train"][1]["article"][:2000]

    tokenized_sentences = tokenize_sentence()
    print("Tokenized Sentences:", tokenized_sentences)

    summarize_baseline(summaries, sample_text)
    summarize_with_gpt2(summaries, sample_text)
    summarize_with_t5(summaries, sample_text)
    summarize_with_bart(summaries, sample_text)
    summarize_with_pegasus(summaries, sample_text)

    print("Summaries:", summaries)


if __name__ == "__main__":
    main()
