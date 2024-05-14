import requests
import json

def main():
    headers = {
        'accept': 'application/json',
        'authorization': 'Bearer secret',
        'content-type': 'application/json'
    }

    # =================

    # # POST: api/agents
    # url = "https://memgpt-service-nonprod-locuhjl2ja-ey.a.run.app/api/agents"
    # data = {
    #     "config": {
    #         "name": "Kilians-test-agent2",
    #         "preset": "memgpt_chat",
    #         "human": "Kilian",
    #         "persona": "sam_pov"
    #     }
    # }
    # response = requests.post(url, headers=headers, data=json.dumps(data))
    # data = response.json()
    # print(data)

    # =================

    # # Get: api/agents
    # url = "https://memgpt-service-nonprod-locuhjl2ja-ey.a.run.app/api/agents"
    # response = requests.get(url, headers=headers)
    # data = response.json()
    # print(data)

    # =================

    # POST: /api/agents/{agent_id}/messages
    url = "https://memgpt-service-nonprod-locuhjl2ja-ey.a.run.app/api/agents/c10d2390-9c7a-4676-996d-c76c6a90c139/messages"
    data = {
        "message": "How is the weather in Cologne?"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    data = response.json()
    print(data)

    # =================

    # # GET: /api/agents/{agent_id}/messages?start={start}&count={count}
    # url = "https://memgpt-service-nonprod-locuhjl2ja-ey.a.run.app/api/agents/70615617-00f0-4791-9590-1a600331a886/messages?start=0&count=10"
    # response = requests.get(url, headers=headers)
    # # assert response.status_code == 200
    # data = response.json()
    # print(data)

    # =================

    # # POST: /api/sources/source_id/attach?agent_id={agent_id}
    # url = "https://memgpt-service-nonprod-locuhjl2ja-ey.a.run.app/api/sources/source_id/attach?agent_id=4a19a3a0-e586-40d0-a608-286eb1f028f8"
    # response = requests.post(url, headers=headers)
    # data = response.json()
    # print(data)

if __name__ == "__main__":
    main()