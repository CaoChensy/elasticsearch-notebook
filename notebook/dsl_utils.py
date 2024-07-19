def search_query(search, query, columns):
    """该函数将按照 Query 进行检索并打印出指定字段"""
    s = search.query(query)
    response = s.execute()

    for hit in response.hits:
        for col in columns:
            print(f"{col}: {hit.to_dict().get(col)}")