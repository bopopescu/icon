# -*- coding: UTF-8 -*-
#######################################################################
 # ----------------------------------------------------------------------------
 # # -*- coding: UTF-8 -*-
'''
    A Resource for SelflessLive.

    Updated and refactored by someone.
    Originally created by others.
'''

 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Selfless Live
# Addon id: plugin.video.selfless
# Addon Provider: Kodi Ghost
import json
from resources.lib.modules import client

URL_PATTERN = 'http://thexem.de/map/single?id=%s&origin=tvdb&season=%s&episode=%s&destination=scene'

def get_scene_episode_number(tvdbid, season, episode):

    try:
        url = URL_PATTERN % (tvdbid, season, episode)
        r = client.request(url)
        r = json.loads(r)
        if r['result'] == 'success':
            data = r['data']['scene']
            return data['season'], data['episode']            
    except:
        pass

    return season, episode    
