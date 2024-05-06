import numpy as np

def inpt(user_input = ''):
    user_input = input('Enter 9 float or whole numbers separated by commas. Negative numbers are valid entries. If entries are insufficient, random numbers will be generated in it\'s place: ')
    if user_input == '!0': user_input = '0,1,2,3,4,5,6,7,8,9'
    elif user_input == '!1': user_input = ',1,,-..2,,,3,,,,--4,,,,,5...,,,,,,6,,,,,,,7,,,,,,,,.-8,,,,,,,,,99-99....-...7-89'
    elif user_input == '!2': user_input = '-.2,-3.,-4.4.-4,5.,.6,7.7.7,-8-8,99.-99.7-8.9'
    elif user_input == '!3': user_input = '01,test,02,rigi.d03,4t,,5.5,6,7,,,0ds8,9sss,hello,12,13'
    elif user_input == '!4': user_input = ',test,02,rigi.d03,.7.7,-8-8,99.-99.7-8.9'
    return user_input
def DEBUG(to_prnt='', activate_raw_inpt=False): #### NOT FINISHED, NEED TO REFINE THE ERRORS CAUGHT
    raw_inpt = raw_input
    if raw_inpt == '': raw_inpt = 'Input was empty, numbers were generated randomly'
    if activate_raw_inpt == True:
        print('Name: Raw input\n', 'Contents: ',raw_inpt,'\n============', sep='')
    else:
        pass

    variable_name = [name for name, value in globals().items() if value is to_prnt] # To get the variable's name
    try: 
        len(to_prnt) >= 1
        try: length_v = len(to_prnt)
        except:
            if TypeError: length_v = 'N/A'
            if IndexError: length_v = 'N/A - OUT OF RANGE'
            length_v = len(to_prnt)
        print('Name: ',variable_name,'\n','Type: ',type(to_prnt),'\n','Length: ',length_v,'\n','Contents:\n ',to_prnt, sep='')
    except (IndexError, TypeError, ValueError):
        print('Name: ',variable_name,'\n','Type: ',type(to_prnt),'\n','Length: N/A','\n','Contents: ',to_prnt, sep='')
inpt = raw_input = inpt()

def remove_dupe(input_value, valid_entries=None):
    input_value = inpt
    if valid_entries == None : valid_entries = '0123456789,.-'

    #=== Checks to see if there's any input and if the first input is a comma, skip the first input ===#
    if len(input_value) > 0 and input_value[0] == ',':
        input_value = input_value[1:]
    
    #=== Checks to see if any of the inputs are valid entries and leaves out those that are not ===#
    valid_inpts = ''
    for iP_v in input_value:
        for iV_e in valid_entries:
            if iP_v == iV_e:
                valid_inpts = valid_inpts + iP_v
    input_value = valid_inpts

    #=== Checks the inputs and makes sure of these conditions: ===#
    a = start_pos = 0
    b = compare_pos = a+1
    new_inpt = []
    while b < len(input_value)-2:
        if a == 0: #== 1) if comma is the first character of the input, then discard it
            if input_value[a] == ',':
                pass
            else:
                new_inpt.append(input_value[a])
        elif input_value[a] != input_value[b]: #== 2) if it's a unique character, keep it
            new_inpt.append(input_value[a])
        elif input_value[a] == input_value[b]: #== 3) if it's a repeating character but not a number, discard it
            try: 
                int(input_value[b])
                new_inpt.append(input_value[a])
            except:
                pass
        a = a+1 ; b = b+1
        if b >= len(input_value):
            break 
    new_inpt.append(input_value[a:])
    input_value = ''.join(new_inpt)

    #=== Checks the inputs, if no number is in it, then discard the input entirely ===#
    correct = 0
    for i in input_value:
        if i in '1234567890':
            correct = 1
            break
        else:
            continue
    if correct > 0:
        pass
    else:
        input_value = ''

    return input_value
inpt = remove_dupe(inpt) ; #print('===01f===',inpt)

def cleanup_data(the_list, element=None):
    indices = []
    if element == None:
        element = ','

    #=== To capture the position of the commas, and use these numbers to fill in the new list. Does this until the list has atleast 8 commas ===#
    if len(the_list) > 0:
        for k, v in enumerate(the_list): #for i in range(len(the_list)):
            if len(indices) >= 9:
                break
            if the_list[k] == element:
                indices.append(k)
        if len(indices) < 9: # If the list has less than 9 values, it first checks if the last character is a comma or not and if it's not, then 'add' a comma
            if the_list[-1] != element:
                indices.append(k+1)
    else: # If the list is empty, then start by 'adding' one comma
        indices.append(1)
    #=== If the list has less than 8 commas, then 'add' one until there's 8 of them ===#
    length = len(indices)
    if  length < 9:
        while length < 9:
            indx = indices[-1]
            c = indx+2
            indices.append(c)
            length = len(indices)
            if length >= 10:
                break
    # *add/adding in this context means adding a new value to place the comma in the new, corrected list to be used for this operation 

    #=== This adds any input numbers/values into anew list ===#
    # 1) if the input is complete or longer # 
    New_list = []
    indx_val = 0
    i = 0
    if len(the_list) >= indices[-1]: ### captures both complete and long
        while len(New_list) < len(indices):
            if i >= len(indices):
                break
            if i == 0:
                New_list.append(the_list[:indices[i]])
            else:
                New_list.append(the_list[indices[i-1]+1:indices[i]])
            i=i+1
    # 2) if the input is incomplete/shorter or null #
    if len(the_list) < indices[-1]: ### captures both short and null
            while len(New_list) < len(indices):
                if i >= len(indices):
                    break
                if i < len(the_list):
                    if i == 0:
                        New_list.append(the_list[:indices[i]])
                    else:
                        New_list.append(the_list[indices[i-1]+1:indices[i]])
                else:
                    New_list.append('')
                i=i+1
    the_list = New_list

    #=== This checks if the ne- and/or decimal symbols are placed correctly and discards otherwise ===#
    Ntive = 0 ; Point = 0 ; First = 0 # Ntive = this is updated if the first character is a'-' or otherwise  ; Point = is for decimal point ; First = the first character for the value, if this is updated as 1, then it will update 'Ntive' as well to prevent any '-' symbols appearing in the middle of the value/number to avoid it being an invalid input 
    New_list = []
    Fixed = []
    for value in the_list: # every word
        for i in value: # every letter
            if i == '-':
                if Ntive == 1 or First == 1:
                    pass
                else:
                    Ntive = 1
                    First = 1
                    Fixed.append(i+'0')
            if i == '.':
                if Point == 1:
                    pass
                else:
                    Point = 1
                    First = 1
                    Fixed.append(i)
            if i in '0123456789':
                First = 1
                Fixed.append(i)
        New_list.append(''.join(Fixed))
        Fixed.clear() ; Ntive = 0 ; Point = 0 ; First = 0 # clears for said value before moving on to the next
    the_list = New_list
    #=== Next part, removing any duplicate '.' ===#
    for k,v in enumerate(the_list):
        if v == '.':
            the_list.pop(k)
            the_list.insert(k,'')
        else:
            pass

    #=== For every missing value (needs 9), this will generate a random one ===#
    empty_inpt = 0
    for k, v in enumerate(the_list): #for i in range(len(the_list)):
        if the_list[k] == '':
            the_list[k] = str(round(random.uniform(-999.999,999.999),3))
            empty_inpt + 1
    
    return the_list
inpt_lst = cleanup_data(inpt) ; #print('===02f===',inpt_lst)

def convert_data(the_list, number_type=0, output_type=0):
    ## Converts numbers/values in list to floats or integers as defined in the def's parameter ## (!! NOT TESTED !!)
    if number_type == 0:
        the_list = [float(i) for i in the_list]
    if number_type == 1:
        the_list = [int(i) for i in the_list]

    #=== Converts the list to a matrix or array as defined in the def's parameter ===#
    if output_type == 0 or output_type == 1:
        the_list = list((the_list[0:3], the_list[3:6], the_list[6:]))
        if output_type == 0:
            arr = the_list = np.array(the_list)
        if output_type == 1:
            M = the_list = np.matrix(the_list)

    return the_list
inpt_lst = convert_data(inpt_lst,0,1) ; #print('===03f===',inpt_lst)

def calculate(the_list, rounded=''):
    #=== Rounds the number if the parameter for it is set ===#
    if rounded != '':
        rounded_ipt = round(the_list,rounded)
        the_list = rounded_ipt
    else:
        pass
    
    #=== This function converts matrix input, to a dictionary ===#
    def conversion(subject):
        subject = [element.tolist() if isinstance(element, np.matrix) else element for element in subject]
        temp_list = []
        for vll in subject:
            if type(vll) == list:
                for vl in vll:
                    for v in vl:
                        temp_list.append(v)
            else:
                temp_list.append(vll)
        subject = [temp_list[:3], temp_list[3:6], temp_list[6]]
        return subject

    #=== Calculation process starts here ===#
    cal_mean = [the_list.mean(0), the_list.mean(1), the_list.mean()] # y ; x ; whole
    cal_var = [the_list.var(0), the_list.var(1), the_list.var()]
    cal_std = [the_list.std(0), the_list.std(1), the_list.std()]
    cal_min = [the_list.min(0), the_list.min(1), the_list.min()]
    cal_max = [the_list.max(0), the_list.max(1), the_list.max()]
    cal_sum = [the_list.sum(0), the_list.sum(1), the_list.sum()]

    cal_mean = conversion(cal_mean)
    cal_var = conversion(cal_var)
    cal_std = conversion(cal_std)
    cal_min = conversion(cal_min)
    cal_max = conversion(cal_max)
    cal_sum = conversion(cal_sum)

    calculations = {
    'mean' : cal_mean,
    'variance' : cal_var,
    'standard_deviations' : cal_std,
    'min' : cal_min,
    'max' : cal_max,
    'sum' : cal_sum,
    }

    return(calculations)
pre_cal = inpt_lst ; #print(pre_cal)
inpt_lst = calculate(inpt_lst)

##============END============##
DEBUG(inpt_lst,1)
