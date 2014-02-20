import json

address_book = {}
contact_list_first = []
contact_list_last = []

data_write = [address_book, contact_list_first, contact_list_last]
fp_write = open("data.txt", "w")
json.dump(data_write, fp_write)
fp_write.close()

fp_read = open("data.txt", "r")
data_read = json.load(fp_read)
fp_read.close()

address_book = data_read[0]
contact_list_first = data_read[1]
contact_list_last = data_read[2]
