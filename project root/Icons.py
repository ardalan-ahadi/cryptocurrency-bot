import os
import json
import time
import requests

API_KEY = "e38e42eb-9d97-40f4-b092-7c9bafbaf4bb"
BASE = "https://pro-api.coinmarketcap.com"
HEADERS = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": API_KEY}

LIMIT = 2500          # top N coins
PAGE_SIZE = 500       # max per request
INFO_BATCH = 200      # number of IDs per /v2/info call
SLEEP_SEC = 1         # seconds between API calls
OUT_FILE = "ICONS.json"


def get_top_ids(limit=1000, page_size=500):
    """Fetch the top N cryptocurrency IDs + symbols by market cap"""
    ids = []
    symbols = {}
    for start in range(1, limit + 1, page_size):
        params = {"start": start, "limit": min(page_size, limit - len(ids)), "sort": "market_cap"}
        r = requests.get(f"{BASE}/v1/cryptocurrency/listings/latest", headers=HEADERS, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()["data"]
        for d in data:
            ids.append(str(d["id"]))
            symbols[str(d["id"])] = d["symbol"]
        time.sleep(SLEEP_SEC)
    return ids, symbols


def get_info_for_ids(id_list):
    """Fetch metadata (including logos) for a list of IDs"""
    infos = {}
    for i in range(0, len(id_list), INFO_BATCH):
        chunk = id_list[i : i + INFO_BATCH]
        params = {"id": ",".join(chunk)}
        r = requests.get(f"{BASE}/v2/cryptocurrency/info", headers=HEADERS, params=params, timeout=30)
        r.raise_for_status()
        payload = r.json()["data"]
        infos.update(payload)
        time.sleep(SLEEP_SEC)
    return infos


def main():
    print("Fetching top 2500 coins...")
    ids, symbols = get_top_ids(LIMIT, PAGE_SIZE)
    print(f"Collected {len(ids)} IDs.")

    print("Fetching metadata (logos)...")
    info = get_info_for_ids(ids)

    data = []
    for _id in ids:
        meta = info.get(_id)
        if not meta:
            continue
        symbol = symbols.get(_id, "")
        logo_url = meta.get("logo", "")
        data.append({"tcoin": symbol, "ticon": logo_url})

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Exported {len(data)} entries to {OUT_FILE}")


if __name__ == "__main__":
    main()