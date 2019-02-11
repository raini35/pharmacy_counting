def write_output(file, header, info, sortInfo=False):
    file.write("%s,%s,%s\n" %(header[3], 'num_prescriber','total_cost'))

    if sortInfo:
        for item in sorted(info.items(), key=lambda x: x[1][1], reverse=True):
            drug = item[0]
            prescriberCount = item[1][0]
            totalPrice = item[1][1]
            file.write("%s,%d,%.0f\n" %(drug, prescriberCount, totalPrice))
    else:
        for drug in info.keys():
            prescriberCount = info[drug][0]
            totalPrice = info[drug][1]
            file.write("%s,%d,%.0f\n" %(drug, prescriberCount, totalPrice))

    return
