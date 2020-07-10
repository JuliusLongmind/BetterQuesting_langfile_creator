#!/usr/bin/env python

import simplejson as json
import sys, getopt

lang = ''

try:
    opts, args = getopt.getopt( sys.argv[1:], "l:h", ['lang=', 'help'] )
except getopt.GetoptError as e:
    print( str( e ) )
    print( "Usage: %s -l <lang>" % sys.argv[0] )
    sys.exit( 2 )

for opt, arg in opts:
    if opt in ("-h", "--help"):
        print( 'lan_creator.py -l <lang>' )
        sys.exit( 2 )
    elif opt in ("-l", "--lang"):
        lang = arg

with open( 'DefaultQuests.json', 'rb' ) as json_file:
    quest_db = json.load( json_file )
    json_file.close()

n = 0

with open( 'en_us.lang', 'w' ) as f, open( '%s' % lang + '.lang', 'w' ) as t:
    f.write( "# PARSE_ESCAPES\n\n" )
    t.write( "# PARSE_ESCAPES\n\n" )
    for quest_db_rec in quest_db['questDatabase:9']:
        n += 1
        name = quest_db['questDatabase:9'][quest_db_rec]['properties:10']['betterquesting:10']['name:8']
        desc = quest_db['questDatabase:9'][quest_db_rec]['properties:10']['betterquesting:10']['desc:8']
        f.write( "mypack.quest%d.name=%s\n" % (n, repr( name )[1:-1]) )
        f.write( "mypack.quest%d.desc=%s\n" % (n, repr( desc )[1:-1]) )
        t.write( "mypack.quest%d.name=\nmypack.quest%d.desc=\n" % (n, n) )

n = 0

with open( 'tmp.json', 'w' ) as tmp_file:
    for quest_db_rec in quest_db['questDatabase:9']:
        n += 1
        quest_db['questDatabase:9'][quest_db_rec]['properties:10']['betterquesting:10']['name:8'] = "mypack.quest%d" \
                                                                                                    ".name" % n
        quest_db['questDatabase:9'][quest_db_rec]['properties:10']['betterquesting:10']['desc:8'] = "mypack.quest%d" \
                                                                                                    ".desc" % n
    json.dump( quest_db, tmp_file, indent=2, separators=(',', ': '), ensure_ascii=False )

f.close
t.close
tmp_file.close
json_file.close
