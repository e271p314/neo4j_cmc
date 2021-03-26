### Data visualization from CoinMarketCap using neo4j and python

[Data visualization from coinmarketcap using neo4j and python on medium](https://e271p314.medium.com/data-visualization-from-coinmarketcap-using-neo4j-and-python-49bcae7c8658)

* clone this repository
* edit `app/main.py`, replace `<YOUR CMC KEY>` with your CMC key
* build docker, `sudo docker-compose up --build -d`
* run application, `sudo docker exec -it neo4j_cmc_app_1 bash -c "python3 main.py"`
* open browser, `http://localhost:7474`, username/password is neo4j/pass123
* use `MATCH r=()-[:related_to]->() RETURN r` to view all relations
* use `MATCH r=(c:Coin)-[:related_to]->(p:Prop) WHERE size(()-[:related_to]->(p)) > 1 RETURN r` to view relations with non leaf properties
