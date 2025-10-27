from spacy.lang.zh import Chinese
from summarizer import Summarizer
from summarizer.text_processors.sentence_handler import SentenceHandler
from transformers import AutoConfig, AutoTokenizer, AutoModel

MODEL_NAME = 'bert-base-chinese'

custom_config = AutoConfig.from_pretrained(MODEL_NAME)
custom_config.output_hidden_states = True
custom_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
custom_model = AutoModel.from_pretrained(
    MODEL_NAME, config=custom_config)

custom_sentence_handler = SentenceHandler(language=Chinese)

model = Summarizer(custom_model=custom_model,
                   custom_tokenizer=custom_tokenizer,
                   sentence_handler=custom_sentence_handler)

text = '''
　　党的二十届四中全会在北京胜利闭幕啦。全会最重要的成果是审议通过了《中共中央关于制定国民经济和社会发展第十五个五年规划的建议》（以下简称《建议》），为新征程上未来关键的五年擘画了宏伟蓝图。全会精准标注“十五五”时期在基本实现社会主义现代化进程中承前启后的历史方位，深入分析国内外发展环境变化，科学谋划目标任务，明确提出思路举措，是乘势而上、接续推进中国式现代化建设的又一次总动员、总部署，必将指引和激励全党全国各族人民笃行不怠、勇毅前行，向着宏伟目标不断迈进。

　　大国发展，规划先行。习近平总书记高度重视“十五五”规划编制工作，亲自担任文件起草组组长，亲自擘画、全程指导、把脉定向，倾注了大量心血。《建议》凝聚全党智慧，广泛汇聚包括党外人士、广大网民在内的全社会力量，是回应人民期待的又一重要纲领性文件。《建议》的起草过程，是全过程人民民主的生动实践。

　　五年砥砺奋进，五年成绩非凡。“十四五”时期，面对错综复杂的国际形势和艰巨繁重的国内改革发展稳定任务，以习近平同志为核心的党中央团结带领全党全国各族人民，迎难而上、砥砺前行，经受住世纪疫情严重冲击，有效应对一系列重大风险挑战，推动党和国家事业取得新的重大成就。我国经济实力、科技实力、综合国力跃上新台阶，中国式现代化迈出新的坚实步伐，第二个百年奋斗目标新征程实现良好开局。

　　即将开启的“十五五”时期，是我国基本实现社会主义现代化夯实基础、全面发力的关键时期，具有承前启后的重要地位。从现在起到2035年，只有10年时间，前五年发展好了，我们就能争取更大主动。我们既要乘势而上，又要迎难而上，要充分发挥中国特色社会主义制度优势、超大规模市场优势、完整产业体系优势、丰富人才资源优势，把各方面优势转化为高质量发展的实际效能。

　　秉纲而目自张。《建议》从七个方面明确“十五五”时期经济社会发展主要目标，即高质量发展取得显著成效、科技自立自强水平大幅提高、进一步全面深化改革取得新突破、社会文明程度明显提升、人民生活品质不断提高、美丽中国建设取得新的重大进展、国家安全屏障更加巩固。各地区各部门要锚定目标任务，以时不我待、只争朝夕的时代紧迫感和历史主动精神，积极识变应变求变，推动经济实现质的有效提升和量的合理增长，形成发展合力，增强综合效力，在推动人的全面发展、全体人民共同富裕上迈出坚实步伐，确保基本实现社会主义现代化取得决定性进展。

　　实现社会主义现代化是一个阶梯式递进、不断发展进步的历史过程，需要全党全国各族人民不懈努力、接续奋斗。让我们更加紧密地团结在以习近平同志为核心的党中央周围，深入学习贯彻党的二十届四中全会精神，勇担时代历史使命，牢牢把握战略主动，集中力量办好自己的事，一件事情接着一件事情办，一个五年规划接着一个五年规划干，不断开创以中国式现代化全面推进强国建设、民族复兴伟业新局面。'''

print(model(text))
