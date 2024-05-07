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