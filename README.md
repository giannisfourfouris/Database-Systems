# Database-Systems

## Useful Links / Material

- [OpenNMT Tutorial](https://www.youtube.com/watch?v=DwOxgegFg18&pp=ygUQZ29vZ2xlIG5tdCBndWlkZQ%3D%3D): Used for the automated translation process.
- [RatSQL Paper](https://arxiv.org/pdf/1911.04942.pdf)
- [RatSQL Github Repo](https://github.com/microsoft/rat-sql)
- [VSpirer Paper](https://arxiv.org/pdf/2010.01891.pdf)
- [VSpider Code Repo](https://github.com/VinAIResearch/ViText2SQL): Contains _only the dataset_
- [CSpirer Paper](https://arxiv.org/pdf/1909.13293.pdf)
- [A Multilingual Translator to SQL with Database Schema Pruning to Improve Self-Attention](https://arxiv.org/pdf/2306.14256v1.pdf): This is the updated version of the Portuguese. Includes 2 more languages
- [mRAT-SQL+GAP:A Portuguese Text-to-SQL Transformer](https://arxiv.org/pdf/2110.03546.pdf)
- [gap-text2sql](https://github.com/C4AI/gap-text2sql/tree/main): Code for the _two papers above_
- [Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation](https://arxiv.org/pdf/2308.15363.pdf): The _DAIL-SQL paper_
- [DAIL-SQL Code Repo](https://github.com/BeachWang/DAIL-SQL)
- [SQL Generation from Natural Language: A Sequence-to Sequence Model Powered by the Transformers Architecture and Association Rules](https://thescipub.com/pdf/jcssp.2021.480.489.pdf)
- [Open-NMT: A seq2seq translation model](https://opennmt.net/)

## Selecting the best LLM for Question Translation

We experimented with 3 different LLMs:
1. GPT-3.5 Turbo
2. Meltemi
3. LLama3

In order to determine the best for our task we performed the following experiment:
1. 3 different schemas were translated by hand
2. 260 questions were translated by the models, *using the translated schemas for added context*
3. We picked separately the best model(s) for each question
4. We cross validated our picks
5. We gathered statistics and selected the best one.

### Observations

#### Llama3

- This model whould ofter provider correct translation but use "Τι" at the start instead of "Ποιός", "Ποιά" etc, thus forcing us to reject the translation

- Somethimes the greek translation contains non - greek characters (i.e. Πόσο επιταχύνει το όχημα πουสรήθηκε από AMC Hornet Sportabout ?). This translation is again, invalid.

#### Meltemi

- In some cases Meltemi gave the correct translation of the requested question, but allong with other un-asked questions in the target language or other irrelevant information, thus forcing us to reject the translation

## Notes about the code
- [saver.py:save_checkpoint](gap-text2sql/mrat-sql-gap/seq2struct/utils/saver.py): The main parameter in this method is the `keep_every_n`. Using this parameters, checkpoints with last_step >= keep_every_n are removed. For example if the save_method is called every 100 steps and the keep_every_n is set to 1000 the 10 latest checkpoints will be kept at all times.
- [train.py](gap-text2sql/mrat-sql-gap/seq2struct/commands/train.py)
    - For the whole training process, the parameter that desides how many times the batches will be given to the model is the `max_steps`
        - For the `mT5` models this parameter is set to 51000 by default.
- [infer.py](gap-text2sql/mrat-sql-gap/seq2struct/commands/infer.py)
    - This is the first step of the eval process.
    - The output of the infer is written into two separate files. For example for mT5-base:
        - ie_dirs/mT5-base-en-train/mT5-base-en-train_en-eval_1_true_1-step2.infer: The full output is contained here, along with the original question
        - ie_dirs/mT5-base-en-train/mT5-base-en-train_en-eval_1_true_1-step2.txt: Only the re-constructed sql is saved here. These queries will be compared with gold.txt line by line.
        - ie_dirs/mT5-base-en-train/mT5-base-en-train_en-eval_1_true_1-step2.json: Here pais of Question - Constructed SQL are saved.
- [eval.py](gap-text2sql/mrat-sql-gap/seq2struct/commands/eval.py)
    - Here, metrics for the infer step are calculated and saved into appropriate files.

## External Files

Dataset files as well as the evaluation xlsx files can be found under this [gdrive folder](https://drive.google.com/drive/folders/1Rw3nWzqD2wd20b6zflQj10TA80lpZiBP?usp=drive_link)

## Schema Linking Observations:

Gr - Spider
- train.json
    
    - 94/857 without q_col_match
    - 289/857 without q_tab_match

Eng - Spider
- train.json

    - 12/924 without q_col_match
    - 117/924 without q_tab_match
