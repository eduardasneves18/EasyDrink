import urllib2
import json

def update_user_social_data(request, *args, **kwargs):
    print('Args -> ', args)
    print('Kwargs ->' ,kwargs)
    user = kwargs['user']
    if not kwargs['is_new']:
        return
    user = kwargs['user']
    if kwargs['backend'].__class__.__name__ == 'FacebookBackend':
        fbuid = kwargs['response']['id']
        access_token = kwargs['response']['access_token']

        url = 'https://graph.facebook.com/{0}/' \
              '?fields=email,gender,name' \
              '&access_token={1}'.format(fbuid, access_token,)

        photo_url = "http://graph.facebook.com/%s/picture?type=large" \
            % kwargs['response']['id']
        request = urllib2.Request(url)
        response = urllib2.urlopen(request).read()
        email = json.loads(response).get('email')
        name = json.loads(response).get('name')
        gender = json.loads(response).get('gender')