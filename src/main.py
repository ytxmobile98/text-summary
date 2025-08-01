from datasets import load_dataset
import evaluate
import nltk
from nltk.tokenize import sent_tokenize
from transformers.pipelines import pipeline
from transformers.trainer_utils import set_seed


def tokenize_sentence():
    nltk.download('punkt')
    nltk.download('punkt_tab')

    string = "The U.S. are a country. The U.N. is an organization."
    tokenized_sentences = sent_tokenize(string)
    return tokenized_sentences


def summarize(sample_text: str) -> dict[str, str]:
    summaries: dict[str, str] = {}

    summarize_baseline(summaries, sample_text)
    summarize_with_gpt2(summaries, sample_text)
    summarize_with_t5(summaries, sample_text)
    summarize_with_bart(summaries, sample_text)
    summarize_with_pegasus(summaries, sample_text)

    return summaries


def summarize_baseline(summaries: dict[str, str], sample_text: str):
    def three_sentence_summary(text: str):
        return "\n".join(sent_tokenize(text)[:3])

    summaries["baseline"] = three_sentence_summary(sample_text)


def summarize_with_gpt2(summaries: dict[str, str], sample_text: str):
    set_seed(42)
    pipe = pipeline("text-generation", model="gpt2")
    gpt2_query = sample_text + "\nTL;DR:\n"
    pipe_out = pipe(gpt2_query, max_length=512,
                    clean_up_tokenization_spaces=True)
    print("Summary with GPT-2:", pipe_out)

    summaries["gpt2"] = "\n".join(sent_tokenize(
        pipe_out[0]["generated_text"][len(gpt2_query):]))


def summarize_with_t5(summaries: dict[str, str], sample_text: str):
    pipe = pipeline("summarization", model="t5-small")
    pipe_out = pipe(sample_text)
    print("Summary with T5:", pipe_out)

    summaries["t5"] = "\n".join(sent_tokenize(pipe_out[0]["summary_text"]))


def summarize_with_bart(summaries: dict[str, str], sample_text: str):
    pipe = pipeline("summarization", model="facebook/bart-base")
    pipe_out = pipe(sample_text)
    print("Summary with BART:", pipe_out)

    summaries["bart"] = "\n".join(sent_tokenize(pipe_out[0]["summary_text"]))


def summarize_with_pegasus(summaries: dict[str, str], sample_text: str):
    pipe = pipeline("summarization", model="google/pegasus-cnn_dailymail")
    pipe_out = pipe(sample_text)
    print("Summary with PEGASUS:", pipe_out)

    summaries["pegasus"] = pipe_out[0]["summary_text"].replace(" .<n>", ".\n")


def evaluate_summaries(summaries: dict[str, str], highlights: str):
    results = {}

    evaluate_with_bleu(results, summaries, highlights)
    evaluate_with_rouge(results, summaries, highlights)

    print("Evaluation Results:", results)


def evaluate_with_bleu(results: dict[str, str],
                       summaries: dict[str, str], highlights: str):
    bleu_metric = evaluate.load("sacrebleu")
    bleu_metric.add_batch(
        predictions=list(summaries.values()),
        references=[highlights]*len(summaries),
    )
    results["bleu"] = bleu_metric.compute()


def evaluate_with_rouge(results: dict[str, str],
                        summaries: dict[str, str], highlights: str):
    rouge_metric = evaluate.load("rouge")
    rouge_metric.add_batch(
        predictions=list(summaries.values()),
        references=[highlights]*len(summaries),
    )
    results["rouge"] = rouge_metric.compute()


def main():
    tokenized_sentences = tokenize_sentence()
    print("Tokenized Sentences:", tokenized_sentences)

    dataset = load_dataset("cnn_dailymail", "3.0.0")

    test_item = dataset["train"][1]
    sample_text: str = test_item["article"][:2000]
    highlights: str = test_item["highlights"]

    summaries: dict[str, str] = summarize(sample_text)
    print("Summaries:", summaries)

    evaluate_summaries(summaries, highlights)


if __name__ == "__main__":
    main()
