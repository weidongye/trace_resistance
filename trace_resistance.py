
#write script to parse file and report the smallest resistance from driver to any receiver
#assume one driver and no resistor loops

#file format:
#net-name net-name resistance-in-ohms
#receivers are called "rcv*"
#driver net1 1  (one resistor)
#net1 net2 14
#....

#       -<r
# d>----|
#       ----------<r
#            |
#             ------------------<r

# driver net1 1
# net1 rcvr1 1
# net1 rcvr2 5


import re
# file parse into this dictionary of arrays
# netDict = {'driver': ['net1',1], 'net1': ['rcvr1',5,'rcvr2',1]}
netDict = {
    'driver': ['net1',1], 
    'net1': ['net2',5],
    'net2': ['rcvr1',1,'net3',3],
    'net3': ['rcvr2',3,'net4',3],
    'net4': ['rcvr3',5]
            }

# string="test"
# regex = re.compile('rcvr.')


def trace_resistance(name):
    resistance_tracking_stack=[0]
    net_tracking_stack=[]
    net_tracking_stack.append(name)
    bool_receiver=False
    receiver_resistance_dict={}
    # "do while" loop in python 
    while(len(net_tracking_stack)>0):
        name=net_tracking_stack.pop()
        for i in range(len(netDict[name])):
            #check for branch
            if len(netDict[name])>2:
                #we have a branch
                #even maps to net name strings
                if i%2==0:
                    #check for receiver
                    if bool(re.match(re.compile('rcvr.'), netDict[name][i])):
                        bool_receiver=True
                        net_tracking_stack.append(netDict[name][i])
                    #not receiver, continue
                    else:
                        bool_receiver=False
                        #push stack to next net 
                        net_tracking_stack.append(netDict[name][i])
                #odd maps to resistance values
                else:
                    #accumulate reisstance 
                    if(bool_receiver==True):
                        receiver_resistance_dict[net_tracking_stack.pop()]=sum(resistance_tracking_stack)+netDict[name][i]
                    else:
                        resistance_tracking_stack.append(netDict[name][i])

            #non-branch case
            else:
                #even maps to net name strings
                if i%2==0:
                    #check for receiver
                    if bool(re.match(re.compile('rcvr.'), netDict[name][i])):
                        bool_receiver=True
                        net_tracking_stack.append(netDict[name][i])
                        #not receiver, continue
                    else:
                        bool_receiver=False
                        net_tracking_stack.append(netDict[name][i])

                    #push next net to stack
                #odd maps to resistance values
                else:
                    if(bool_receiver==True):
                        receiver_resistance_dict[net_tracking_stack.pop()]=sum(resistance_tracking_stack)+netDict[name][i]
                    else:
                        resistance_tracking_stack[-1]+=int(netDict[name][i])


    print(receiver_resistance_dict)        
    sorted_dict={}
    sorted_keys= sorted(receiver_resistance_dict, key=receiver_resistance_dict.get) 
    # print(sorted_keys)
    print("smallest resistance driver is:" + sorted_keys[0] + " with resistance value of:" + str(receiver_resistance_dict[sorted_keys[0]]))
        # #get each net and res value
        # cumulative_resistance[count]+=resvalue 
        # #check for branch 
        # if len(case)>1:
        #     #we hit a branch
        #     ++count      
        # #check if we hit reciever
        # if len(resistor(net)
        
        # while(!bool(re.match(regex, netDict(name))))

trace_resistance('driver')





