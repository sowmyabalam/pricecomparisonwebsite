import requests



def search(item):
	search_url='https://www.googleapis.com/youtube/v3/search'
	video_url='https://www.googleapis.com/youtube/v3/videos'

	YOUTUBE_API_KEY='Type your Api key'

	search_params={
		'key':YOUTUBE_API_KEY,
		'q': item[0],
		'part':'snippet',
		'maxResults':3,
		'type':'video'
	}

	r=requests.get(search_url,params=search_params)

	results=r.json()['items']

	video_ids=[]

	for result in results:
		video_ids.append(result['id']['videoId'])

	video_params={
		'key':YOUTUBE_API_KEY,
		'id' : ','.join(video_ids),
		'part':'snippet,contentDetails',
		'maxResults':3
	}
	r=requests.get(video_url,params=video_params)
	results=r.json()['items']
	video_list=list()
	for result in results:
		video_data1={
			'id' : result['id'],
			'url' : 'https://www.youtube.com/watch?v='+result['id'],
			'thumbnail':result['snippet']['thumbnails']['high']['url'],
			'duration' : result['contentDetails']['duration'],
			'title' : result['snippet']['title'],
			}
		video_data=dict()
		video_data['id']=video_data1['id']
		video_data[1]=video_data1['url']
		video_data['thumbnail']=video_data1['thumbnail']
		video_data['duration']=video_data1['duration']
		video_data['title']=video_data1['title']

		video_list.append(video_data)
	return video_list
	print(video_list)
'''
text=input("enter any product item you want to test")		
search([text])'''

