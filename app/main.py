import json
from requests import Session
from neo4j import GraphDatabase

def get_cmc_data():
    headers = { 'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': <YOUR CMC KEY>
        }
    session = Session()
    session.headers.update(headers)
    response = session.get(
        'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
        params = {'limit' : '10', 'convert' : 'USD'})
    return json.loads(response.text)['data']

def insert_data_to_neo4j(top_coins):
    tags = set()
    for coin in top_coins:
        for tag in coin['tags']:
            tags.add(tag)
    driver = GraphDatabase.driver('neo4j://neo4j:7687', auth = ('neo4j', 'pass123'))
    with driver.session() as session:
        for tag in tags:
            session.run('CREATE (p:Prop {name : $p_name})', p_name = tag)
        for coin in top_coins:
            coin_name = coin['symbol']
            session.run('CREATE (c:Coin {name : $c_name})', c_name = coin_name)
            for tag in coin['tags']:
                session.run(
                    'MATCH (c:Coin), (p:Prop) WHERE c.name = $c_name AND p.name = $p_name CREATE (c)-[:related_to]->(p)',
                    c_name = coin_name, p_name = tag)

if __name__ == '__main__':
    insert_data_to_neo4j(get_cmc_data())
