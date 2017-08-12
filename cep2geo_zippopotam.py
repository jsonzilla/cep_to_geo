# -*- coding: utf-8 -*-

import sys
import getopt
import csv
import json
import requests

def request_location(cep):
    """
    Query a single cep to Zippopotam API.
    :param cep the page index to be queried
    :return a dictionary representation of the data queried
    """
    cep = '{0}-{1}'.format(cep[:-3], cep[-3:])

    url = "http://api.zippopotam.us/BR/" + cep
    print "Find geodata for CEP:" + cep

    response = requests.get(url)
    try:
        return json.loads(response.content.decode("utf-8"))
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except ValueError:
        print "Could not convert data to an integer."
    else:
        print "Unexpected error:", sys.exc_info()[0]

def read_cep_from_csv(file_in_csv, file_out_csv):
    """
    Query a single cep to Zippopotam API.
    :param file_in_csv file to read cep information
    :param file_out_csv file to save cep and geo information
    """
    with open(file_out_csv, 'w') as file_out:
        with open(file_in_csv, 'rb') as file_in:
            reader = csv.reader(file_in, delimiter=",")
            for row in reader:
                cep = row[0]
                json_data = request_location(cep)
                print json_data
                data = extract_data(json_data)
                print data
                writer = csv.writer(file_out)
                writer.writerow(row + data)

def extract_data(json_data):
    """
    Extract JSON information
    :param json_data the page index to be queried
    :return filtered data
    """
    try:
        if json_data and json_data[u"places"]:
            result = json_data[u"places"][0]
            lat = result[u"latitude"]
            lng = result[u"longitude"]
        geo_data = [lat, lng]
        return geo_data
    except ValueError:
        print "Could not convert data to an integer."
    else:
        geo_data = ["", ""]
        return geo_data

def main(argv):
    """
    :param argv
    """
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'cep2geo_zippopotam.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'cep2geozippopotam.py -i <inputfile> -o<inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            read_cep_from_csv(inputfile, outputfile)
    sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
