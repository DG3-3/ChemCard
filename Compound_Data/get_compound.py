import requests
import json
import csv
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def get_reactions_by_reactant_ids(reactant_ids, offset=0):
    base_url = "https://chemequations.com/api/search-reactions-by-compound-ids"
    params = {
        "reactantIds": reactant_ids,
        "productIds": "",
        "offset": offset
    }
    
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    
    try:
        response = session.get(base_url, params=params, timeout=10)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Request failed for reactant IDs {reactant_ids} with offset {offset}: {e}")
        return []
    
    data = response.json()
    
    if isinstance(data, dict) and 'searchResults' in data:
        search_results = data['searchResults']
        
        if isinstance(search_results, list):
            result_count = data.get('resultCount', 0)
            print(f"Fetched {result_count} reactions for reactant IDs {reactant_ids} with offset {offset}")
            # 只返回 equationStr
            return [reaction['equationStr'] for reaction in search_results if 'equationStr' in reaction]
        else:
            print("Unexpected data structure for searchResults")
            return []
    else:
        print("Unexpected data structure")
        return []

def fetch_all_reactions(reactant_ids):
    all_reactions = []
    offset = 0
    
    while True:
        reactions = get_reactions_by_reactant_ids(reactant_ids, offset)
        
        if not reactions:
            break
        
        all_reactions.extend(reactions)
        offset += len(reactions)
    
    print(f"Total reactions fetched for reactant IDs {reactant_ids}: {len(all_reactions)}")
    return all_reactions

if __name__ == "__main__":
    for reactant_id in range(1, 20000):
        print(f"Fetching reactions for reactant ID: {reactant_id}")
        reactions = fetch_all_reactions(reactant_id)

        if reactions:
            file_name = f'reactions_id_{reactant_id}.csv'
            with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['EquationStr'])
                for reaction in reactions:
                    csvwriter.writerow([reaction])
            print(f"Saved {file_name}")

    print(f"所有反应已保存到 reactions_id_*.csv 文件中")