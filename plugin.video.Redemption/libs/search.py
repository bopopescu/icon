import byb_modules as BYB
import byb_api as BYBAPI  
import _Edit
import koding
import sys
import xbmcplugin
from libs._addon import *
from libs._common import *

# search functions use mode 400 - 500 

addDir = BYB.addDir

def index(url):
	if _Edit.Search_Tv == True:
		addDir(ChannelColor(local_string(30054)),url,401,icon_Search,fanart_Search,local_string(30075),'TV Shows','','')
	if _Edit.Search_Movies == True:
		addDir(ChannelColor(local_string(30055)),url,402,icon_Search,fanart_Search,local_string(30076),'Movies','','')
	if _Edit.Search_Content == True:
		addDir(ChannelColor('{} {}'.format(local_string(30040),addon_name)),url,40,icon_Search,fanart_Search,local_string(30077),'videos','','')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


def SearchTv(url):
	#search tv shows using TMDB api list
	SearchString = koding.Keyboard(SingleColor(local_string(30057),_Edit.DialogBoxColor1))
	BYBAPI.tmdb_search(url,search_type='tv',search_term=SearchString,total_pages=1)
	for items in BYBAPI.Details_list:
		addDir(ChannelColor(items.get('title','')).encode('utf-8'),'tmdb='+items.get('ID',''),404,items.get('poster_path',icon_Search),items.get('backdrop_path',fanart_Search),items.get('overview','').encode('utf-8'),str(items.get('Genres','')).encode('utf-8'),items.get('release_date','').encode('utf-8'),'')
	del BYBAPI.Details_list[:]




def SearchMovie(url):
	SearchString = koding.Keyboard(SingleColor(local_string(30058),_Edit.DialogBoxColor1))
	BYBAPI.tmdb_search(url,search_type='movie',search_term=SearchString,total_pages=1)
	for items in BYBAPI.Details_list:
		try:
			addDir(ChannelColor(items.get('title','')).encode('utf-8'),'tmdb='+items.get('ID',''),404,items.get('poster_path',icon_Search),items.get('backdrop_path',fanart_Search),items.get('overview','').encode('utf-8'),str(items.get('Genres','')).encode('utf-8'),items.get('release_date','').encode('utf-8'),'')
		except:pass
	del BYBAPI.Details_list[:]

