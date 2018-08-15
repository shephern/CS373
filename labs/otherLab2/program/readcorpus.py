#!/usr/bin/python

import json, sys, getopt, os

def usage():
    print("Usage: %s --file=[filename]" % sys.argv[0])
    sys.exit()

def main(argv):

    file=''

    myopts, args = getopt.getopt(sys.argv[1:], "", ["file="])

    for o, a in myopts:
        if o in ('-f, --file'):
            file=a
        else:
            usage()

    if len(file) == 0:
        usage()

    corpus = open(file)
    urldata = json.load(corpus, encoding="latin1")

    guesses = []
    baddies = 0
    malicous = 0
    total = 0

    # popular_tokens = ['com', 'www', 'co', 'cn', 'jp', 'net', 'yahoo', 'sina',
    #                   'de', 'org', '163', 'sohu', 'house', 'wordpress', 'it',
    #                   'taobao', 'cnn', 'auto', 'paypal', 'br']

    for record in urldata:
        # Really simple, just like add points and take away points for malicous ness
        record["my_score"] = 0
        # Do something with the URL record data...

        i = record["url"].find(".exe")
        if i != -1:
            # If they have exe in their url for sure baddies
            record["my_score"] += 1

        age = record["domain_age_days"]
        if age < 700:
            record["my_score"] += 1

        # Low or non existant alexa_rank
        alexa_rank = record["alexa_rank"]
        if alexa_rank is None or int(alexa_rank) > 150000:
            record["my_score"] += 1

        ips = record["ips"]
        if ips is None or len(ips) == 0:
            record["my_score"] += 1

        if record["fragment"] is not None:
            record["my_score"] += 1

        if record["port"] not in [80,443]:
            record["my_score"] += 1

        if record["my_score"] >= 1:
            baddies += 1
            guesses.append((record["url"], 1))
        else:
            guesses.append((record["url"], 0))
        total += 1
        
    f = open("output.txt","w+")
    for guess in guesses:
        f.write("%s, %d\n" % guess)
    f.close()

    # print "Actual: "
    # print malicous
    print float(baddies) / float(total)
    corpus.close()

if __name__ == "__main__":
    main(sys.argv[1:])
