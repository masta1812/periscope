import TheSubDB
import BierDopje
import logging

logging.basicConfig(level=logging.DEBUG)

filename = "/burn/How.I.Met.Your.Mother.S06E11.HDTV.XviD-LOL.[VTV].avi"
'''
p = TheSubDB.TheSubDB()
subfname = filename[:-3]+"srt"
logging.info("Processing %s" % filename)
subs = p.process(filename, ["en", "pt"])

print subs

if not subs:
    p.uploadFile(filename, subfname, 'en')

if subs:
    p.createFile(subs[0]["link"], "/tmp/test.avi")
''' 

bd = BierDopje.BierDopje()
subs = bd.process(filename, ["en"])



