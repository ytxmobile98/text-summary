# Text summarization using Transformers

## Setup

```bash
# Initialize project
uv init

# Install dependencies
uv add 'transformers[torch]' evaluate nltk
```

## Run Example

```bash
# Evaluation of different summarization models
python3 src/eval/main.py
```