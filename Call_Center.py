
# You're creating a program for a call center. Every time a call comes in you need a way to track that call. 
# One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

# You will create two classes. One class should be Call, the other CallCenter.

# Call Class
# Create your call class with an init method. Each instance of Call() should have:
# Attributes: unique id, caller name, caller phone number, time of call, reason for call
import time
from datetime import datetime

class Call(object):
    id_counter = 1
    def __init__(self, call_center, caller_name, caller_number, call_reason):
        
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.call_reason = call_reason
        self.call_time = datetime.now()
        self.call_id = Call.id_counter
        Call.id_counter += 1
        call_center.add(self)

# Methods: display: that prints all Call attributes.
    #parse phoone number data for clear displaying (helper function)
    def numParse(self):         
        num = str(self.caller_number)
        parNum =  ('({}){}-{}').format(num[0:3], num[3:6], num[6:11])
        return parNum
    
    def display(self):
        print ("Call Id#: {}\nNew Data: {}\nCaller Number: {}").format(self.call_id, self.caller_name, self.numParse() )
        print ("Day/Time of Call: " + self.call_time.strftime("%a. %b. %d %Y, %I:%M:%S") )
        print ("Reason for Call: " + self.call_reason)
        print ("")
        return self

# CallCenter Class
# Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:
# Attributes: calls: should be a list of call objects, queue size: should be the length of the call list, 
class CallCenter(object):
    def __init__(self):
        self.queued_calls = []
        self.queue_size = len(self.queued_calls)

# Methods: 
# add: adds a new call to the end of the call list 
    def add(self, newCall):
        entry = (newCall.caller_number, newCall.caller_name, newCall.call_time)
        self.queued_calls.append(entry)
        self.queue_size += 1
        return self

# remove: removes the call from the beginning of the list (index 0),
    def remove(self):
        self.queued_calls.pop(0)
        self.queue_size = len(self.queued_calls)        
        return self

# info: prints the name and phone number for each call in the queue as well as the length of the queue.
    def info(self):
        for callInfo in self.queued_calls:
            num = str(callInfo[0])
            parNum =  ('({}){}-{}').format(num[0:3], num[3:6], num[6:11])
            print ('Queue position: {}').format(self.queued_calls.index(callInfo))
            print ("Caller Name: {}\nPhone Number: {}").format(callInfo[1], parNum)
            print ("")
        print ("Queue Length: {}").format(self.queue_size)
        return self



# Remember to build one piece at a time and test as you go for easier debugging!

# Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
    #remove parsing from entered phone number
    def deParse(self, number):
        sysNum = filter(lambda x: x.isdigit(), number)
        return sysNum
    def rmCallbyNum(self, number):
        sysNum = self.deParse(str(number))
        truNum = int(sysNum)
        killCount = 0
        for callItem in self.queued_calls:
            if truNum == callItem[0]:
                target = self.queued_calls.index(callItem)
                tData = self.queued_calls.pop(target)
                killCount += 1
                print "Queued call from {} @ {} has been dropped".format(tData[1], number)
                return self
        if killCount == 0:
            print "The phone number you entered, {}, is not in the queue".format(number)
            return self


## Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? 
## Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.
    def timeBreak(self):  #timeBreak method added for testing timeSort
        if len(self.queued_calls) > 1:
            temp = self.queued_calls[0]
            self.queued_calls[0] = self.queued_calls[1]
            self.queued_calls[1] = temp
        return self

    def timeSort(self):
        queuel = self.queued_calls
        for sortNum in range (0, len(queuel) ):
            for i in range(sortNum):
                if queuel[i][2] > queuel[i+1][2]:
                    temp = queuel[i] 
                    queuel[i] = queuel[i+1]
                    queuel[i+1] = temp
        self.queued_calls = queuel
        return self

        # for item in self.queued_calls:
        #     print item[2]

## You should be able to test your code to prove that it works. 
CenterBase = CallCenter()
#CenterBase.info()
call1 = Call(CenterBase, "Jason", 3215551234, "Service Assistance")
time.sleep(3)   #delay added for testing CallCenter.timeSort()
call2 = Call(CenterBase, 'Martha',2223334444, 'Billing Questions' )
time.sleep(3)   #delay added for testing CallCenter.timeSort()
call3 = Call(CenterBase, 'Thomas', 5555555555, 'Looking to buy')
#CenterBase.info()  #Compare info displayed before and after call instances **Pased

# call1.display()   #Compare displayed call data for all 3 calls
# call2.display()   #Does display expected values?
# call3.display()   # **Passed

#CenterBase.info.remove().info()  #Test: Compare info before and after the .remove() **passed

#call1 = Call(CenterBase, "Jason", 3215551234, "Service Assistance")
#CenterBase.info()  #Compare displayed info before and after call instance re-created.  **passed
#call1.display()    #Compare call ID and Queue position to original instance of this caller.  **passed

#print "="*100
##Ninaj Level Test
#CenterBase.rmCallbyNum('(222)333-4444')     #effective drop confirms function and deParsing  **Passed
#CenterBase.rmCallbyNum(3215551235)          #effective rejection confirms positive match requirement.  **Passed

print "="*100
print CenterBase.queued_calls   #base state for call queue
print '~~~'
CenterBase.timeBreak()          #time broken state for call queue.
print CenterBase.queued_calls   #Compare against base state if different,  **Passed
print '~~~'
CenterBase.timeSort()           #re-composed state for call queue.
print CenterBase.queued_calls   #compare to base state, if same, **Passed.