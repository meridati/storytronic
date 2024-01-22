import json
import requests

def fetch_data_with_auth(auth_token, json_text):
    json_data = json.loads(json_text)

    headers = {
        'Authorization': f'Bearer {auth_token}',
        'x-auth-token': auth_token,
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    title_request = {'title': json_data['title'], 'body': json_data['story']['start']['story_segment']}
    stories_url = 'https://story3.com/api/v2/stories'
    twists_url = 'https://story3.com/api/v2/twists'

    try:
        title_response = requests.post(stories_url, headers=headers, json=title_request)
        title_response.raise_for_status()
        data = title_response.json()
        story_hash = data['hashId']
        print("story hash:", story_hash)

        branch1_request = {
            'hashParentId': story_hash,
            'isExtraTwist': True,
            'title': json_data['story']['start']['branch_1'],
            'body': json_data['story']['branch_1']['story_segment']
        }

        branch2_request = {
            'hashParentId': story_hash,
            'isExtraTwist': True,
            'title': json_data['story']['start']['branch_2'],
            'body': json_data['story']['branch_2']['story_segment']
        }

        branch1_response = requests.post(twists_url, headers=headers, json=branch1_request)
        branch1_response.raise_for_status()
        branch1_data = branch1_response.json()

        branch2_response = requests.post(twists_url, headers=headers, json=branch2_request)
        branch2_response.raise_for_status()
        branch2_data = branch2_response.json()

        branch1_hash = branch1_data['hashId']
        branch2_hash = branch2_data['hashId']

        branch3_request = {
            'hashParentId': branch1_hash,
            'isExtraTwist': True,
            'title': json_data['story']['branch_1']['branch_3'],
            'body': json_data['story']['branch_3']['story_segment']
        }

        branch4_request = {
            'hashParentId': branch1_hash,
            'isExtraTwist': True,
            'title': json_data['story']['branch_1']['branch_4'],
            'body': json_data['story']['branch_4']['story_segment']
        }

        branch3_response = requests.post(twists_url, headers=headers, json=branch3_request)
        branch3_response.raise_for_status()
        branch3_data = branch3_response.json()
        branch3_hash = branch3_data['hashId']
        print("branch 3 complete")

        branch4_response = requests.post(twists_url, headers=headers, json=branch4_request)
        branch4_response.raise_for_status()
        branch4_data = branch4_response.json()
        branch4_hash = branch4_data['hashId']

        branch5_request = {
            'hashParentId': branch2_hash,
            'isExtraTwist': True,
            'title': json_data['story']['branch_2']['branch_5'],
            'body': json_data['story']['branch_5']['story_segment']
        }

        branch6_request = {
            'hashParentId': branch2_hash,
            'isExtraTwist': True,
            'title': json_data['story']['branch_2']['branch_6'],
            'body': json_data['story']['branch_6']['story_segment']
        }

        branch5_response = requests.post(twists_url, headers=headers, json=branch5_request)
        branch5_response.raise_for_status()
        branch5_data = branch5_response.json()
        branch5_hash = branch5_data['hashId']
        print("branch 5 complete")

        branch6_response = requests.post(twists_url, headers=headers, json=branch6_request)
        branch6_response.raise_for_status()
        branch6_data = branch6_response.json()
        branch6_hash = branch6_data['hashId']
        print("branch 6 complete")

        print("publishing twists...")

        publish_headers = {
            'Authorization': f'Bearer {auth_token}',
            'x-auth-token': auth_token,
            'accept': 'application/json'
        }

        story_publish_response = requests.post(f'https://story3.com/api/v2/twists/{story_hash}/publish',
                                               headers=publish_headers)
        story_publish_response.raise_for_status()
        print("story done processing")

        branch1_publish_response = requests.post(f'https://story3.com/api/v2/twists/{branch1_hash}/publish',
                                                 headers=publish_headers)
        branch1_publish_response.raise_for_status()
        print("Branch 1 done processing")

        branch2_publish_response = requests.post(f'https://story3.com/api/v2/twists/{branch2_hash}/publish',
                                                 headers=publish_headers)
        branch2_publish_response.raise_for_status()
        print("Branch 2 done processing")

        branch3_publish_response = requests.post(f'https://story3.com/api/v2/twists/{branch3_hash}/publish',
                                                 headers=publish_headers)
        branch3_publish_response.raise_for_status()
        print("Branch 3 done processing")

        branch4_publish_response = requests.post(f'https://story3.com/api/v2/twists/{branch4_hash}/publish',
                                                 headers=publish_headers)
        branch4_publish_response.raise_for_status()
        print("Branch 4 done processing")

        branch5_publish_response = requests.post(f'https://story3.com/api/v2/twists/{branch5_hash}/publish',
                                                 headers=publish_headers)
        branch5_publish_response.raise_for_status()
        print("Branch 5 done processing")

        branch6_publish_response = requests.post(f'https://story3.com/api/v2/twists/{branch6_hash}/publish',
                                                 headers=publish_headers)
        branch6_publish_response.raise_for_status()
        print("Branch 6 done processing")

        print(data)
        return data

    except Exception as error:
        print('Error fetching data:', error)

stories_url = 'https://story3.com/api/v2/stories'
twists_url = 'https://story3.com/api/v2/twists'
auth_token = ''  # Enter your api key

def upload_story(json_text):
    fetch_data_with_auth(auth_token, json_text)

if __name__ == "__main__":
    json_text_example = '{"title": "My Story", "story": {"start": {"story_segment": "Once upon a time..."}, "branch_1": {"story_segment": "Meanwhile..."}, "branch_2": {"story_segment": "In another place..."}, "branch_3": {"story_segment": "A twist in branch 1..."}, "branch_4": {"story_segment": "Another twist in branch 1..."}, "branch_5": {"story_segment": "A twist in branch 2..."}, "branch_6": {"story_segment": "Another twist in branch 2..."}}}'

    upload_story(json_text_example)
