#Start time 9 20 pm end time 11 54 pm
import os
def main():
    averageItemPrice = 0.0
    Error_msg = ''

   # try:
    #Get the name of a file
    filename = input('Enter input file name: ')
    outfilename = input('Enter output file name: ')

    if os.path.exists(filename):
        try:
           os.remove(filename)
        except OSError:
            pass
    mode = 'w'
    outfile = open(outfilename, mode)
    # Open the file
    # Read the file's contents
    with open(filename) as f:
        #skip header
        next(f)
        lines = [x for x in f if x and not x.strip().startswith('!')]
        print ('order_id', 'order_date', 'User_id', 'Avg_Item_price','Start_page_url' ,'Error_msg')
        lst1 = ['order_id', 'order_date', 'User_id', 'Avg_Item_price','Start_page_url', 'Error_msg']
        ac1 = '\t'.join(lst1)
        outfile.write(ac1 + '\n')
        for line in lines:
            Error_msg = ''
            Start_page_url = ''
            spl = line.split()
            #if URL is invalid
            if "http://www.insacart.com" not in line:
                Error_msg = 'Invalid URL'
            else:
                Start_page_url = spl[-1]
                # if number of columns are less than the input columns
            if len(line.split()) != 7:
                Error_msg = 'Missing Data'
            # if number of columns are less than the number of input columns

            # if first column is missing data
            if spl[0] =='':
                Error_msg = 'Invalid Order Details'
            else:
                orderlst = [x for x in spl[0].split(":") if x != '']
                if len(orderlst) == 2:
                    order_id = orderlst[0]
                    order_date = orderlst[1]
                else:
                    # if first column is having invalid data
                    Error_msg = "Invalid Order Details"
                userid = spl[1]
            if Error_msg == '':
                spl[2:6] = map(float,spl[2:6])
                averageItemPrice = float(avgItemPrice(spl[2:6]))
            lst = [order_id, order_date,userid, averageItemPrice,Start_page_url, Error_msg]
            ac = '\t'.join([str(x) for x in lst])
            outfile.write(ac + '\n')

    outfile.close()



def avgItemPrice(lst):
    itemList = [x for x in lst if x !=0 and type(x) is float]
    if len(itemList) != 0:
        return sum(itemList)/len(itemList)
    else:
        return 0



main()