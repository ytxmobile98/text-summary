from spacy.lang.zh import Chinese
from summarizer import Summarizer
from summarizer.text_processors.sentence_handler import SentenceHandler
from transformers import AutoConfig, AutoTokenizer, AutoModel

custom_config = AutoConfig.from_pretrained('bert-base-chinese')
custom_config.output_hidden_states = True
custom_tokenizer = AutoTokenizer.from_pretrained('bert-base-chinese')
custom_model = AutoModel.from_pretrained(
    'bert-base-chinese', config=custom_config)

custom_sentence_handler = SentenceHandler(language=Chinese)

model = Summarizer(custom_model=custom_model,
                   custom_tokenizer=custom_tokenizer,
                   sentence_handler=custom_sentence_handler)
zh_text = "喜闻东京上野动物园大熊猫“真真”顺利诞下双胞胎幼仔，对此表示衷心祝贺！我们同广大日本朋友一样，" \
          "对两只熊猫宝宝的到来感到兴奋和喜悦。大熊猫是中国的国宝和名片，深受中日两国人民喜爱。" \
          "今年正值中国大熊猫“真真”和“力力”旅日十周年，“香香”也于日前迎来4周岁生日。" \
          "感谢日本人民特别是上野动物园长期以来对大熊猫的悉心照料。衷心祝愿新诞生的两只熊猫宝宝健康成长，" \
          "早日同公众见面，为日本民众带来更多欢乐，成为传递中日友谊的使者，为增进两国人民友好感情发挥独特作用。"
print(model(zh_text))
