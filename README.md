# AIR-Search-Engine
A search engine built using vector space model, supporting boolean queries, phrase queries, wildcard queries, and combination of these with spell check on the dataset https://www.kaggle.com/amritvirsinghx/environmental-news-nlp-dataset.
# Preprocessing
Run all cells in preprocessing.ipynb to create indexes required later to retrieve results. Change path location of the files with respect to your system.
# Retrieval of results
Run all the cells of Queries.ipynb after changing path locations of the files in the preprocessing step. Call the function ranked_results(query,k) to run the query on the search engine, to retrieve top k relevant results after executing all the cells.
# Sample Queries
1. climate change legislation AND wash\*ng\*on - (mixed query - phrase query and wildcard query and boolean)
2. vice president joe biden - (phrase query)
3. congres OR democra* - (mixed query with boolean query with spelling error and wildcard query)
4. NOT ( nuclear war OR diplomatic relations ) - (boolean query with phrase query)
5. mi\*ro\*bi\*gist - (wildcard query)
# Compare with elastic search engine
1. Install elasticsearch.
2. es_upload.py - to upload the documents onto elasticsearch
3. es_queries.py - different syntaxes to search different combinations of phrase, boolean, and wildcard queries.
4. compare_search_engines.py - to get accuracy measures. (prerequisite - retrieved results from Queries.ipynb named as text2.txt)
