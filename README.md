The English Worldwide Newswire dataset, as featured in `Do "English" Named Entity Recognizers Work Well on Global Englishes?` (EMNLP 2023) by Shan et. al. 

Alex Shan (azshan@cs.stanford.edu) is the correspondence author and maintainer of this repository.

This dataset is composed of 1100 news articles from around the world, sourced from non-Western newswire. This dataset is specifically designed to exclude Western sourced texts and focuses on uncommon contexts of the English language. Below is a detailed breakdown of article origins.

To process the dataset, check out StanfordNLP's Stanza library which contains the dataset preparation script: https://github.com/stanfordnlp/stanza/blob/main/stanza/utils/datasets/ner/prepare_ner_dataset.py

| **South America: 94**              |                        |     |
|------------------------------------|------------------------|-----|
|                                    | Argentina              | 20  |
|                                    | Bolivia                | 3   |
|                                    | Chile                  | 12  |
|                                    | Colombia               | 10  |
|                                    | Ecuador                | 10  |
|                                    | Guyana                 | 3   |
|                                    | Paraguay               | 13  |
|                                    | Peru                   | 10  |
|                                    | Uruguay                | 5   |
|                                    | Venezuela              | 8   |
| **Central and North America: 178** |                        |     |
|                                    | Costa Rica             | 20  |
|                                    | Cuba                   | 15  |
|                                    | El Salvador            | 20  |
|                                    | Honduras               | 14  |
|                                    | Mexico                 | 29  |
|                                    | Nicaragua              | 20  |
|                                    | Panama                 | 20  |
|                                    | Indigenous Canadian    | 40  |
| **Africa: 265**                    |                        |     |
|                                    | General                | 65  |
|                                    | Pan-Africa             | 20  |
|                                    | Algeria                | 20  |
|                                    | Ghana                  | 20  |
|                                    | Kenya                  | 23  |
|                                    | Mauritius              | 20  |
|                                    | Egypt                  | 22  |
|                                    | Ethiopia               | 9   |
|                                    | Namibia                | 28  |
|                                    | South Africa           | 38  |
| **Asia: 347**                      |                        |     |
|                                    | General                | 14  |
|                                    | China                  | 104 |
|                                    | Japan                  | 15  |
|                                    | India                  | 71  |
|                                    | Korea                  | 37  |
|                                    | Taiwan                 | 26  |
|                                    | Malaysia               | 11  |
|                                    | Bangladesh             | 31  |
|                                    | Thailand               | 27  |
|                                    | Mongolia               | 11  |
| **Middle East: 167**               |                        |     |
|                                    | Oman                   | 12  |
|                                    | Jordan                 | 21  |
|                                    | Israel                 | 20  |
|                                    | Iran                   | 16  |
|                                    | UAE                    | 17  |
|                                    | Saudi Arabia           | 27  |
|                                    | Pakistan               | 2   |
|                                    | Qatar                  | 16  |
|                                    | Kuwait                 | 36  |
| **Oceania: 48**                    |                        |     |
|                                    | Indigenous Australia   | 28  |
|                                    | Indigenous New Zealand | 20  |

If you use this dataset, please use the following citation:
```
@inproceedings{Shan_2023,
   title={Do “English” Named Entity Recognizers Work Well on Global Englishes?},
   url={http://dx.doi.org/10.18653/v1/2023.findings-emnlp.788},
   DOI={10.18653/v1/2023.findings-emnlp.788},
   booktitle={Findings of the Association for Computational Linguistics: EMNLP 2023},
   publisher={Association for Computational Linguistics},
   author={Shan, Alexander and Bauer, John and Carlson, Riley and Manning, Christopher},
   year={2023} }
   ```
