import csv
def x():
    x = 0
    s = 0
    da = 0
    f = 1
    number = 2
    model = []
    events = []
    event_log = {}
    num_ev = []
    petri = []
    c = 0
    eventList = {}

    e = open('events.csv')  #changeable 
    event = csv.reader(e)
    name = []
    nLogs = 0
    
    for line in event:
        if event.line_num <=1:
            nLogs = len(line)
            for ic in range(nLogs):
                name.append("Log"+str(ic+1))
                eventList[name[ic]] = list()

        for ic in range(nLogs):
            eventList[name[ic]].append(line[ic])

    print eventList
    for nmbrlen in range(0,c):
        e = open('events.csv')   
        event = csv.reader(e)
        events.append([])
        model.append([])
        ID = 1
        for row in event:
            # Dictionary
            if row[s] not in event_log and row[s]!=str(''):
                
                event_log[row[s]] = chr(97+da)
                da = da + 1
                
                        
                       
            else:
                pass
            if row[s]!=str('') :
                activity = row[s]
                a = 'Case ID:', ID, 'Activity:', activity #Prints the last activity twice if list2<list1
            ID = ID+1    
            # Event Log List
            if str(ID) not in events:       
                events[s].append(a)

            #Model List
            model[s].append(event_log[activity])
            
           
        
        s=s+1
            
    

    print event_log
  
   
        
    print('_____Event Logs_____')
    for nmbre in range(0,s):
        print ' Event Log #', f
        f = f + 1
        for nmbra in range(0,len(events[nmbre])):
            print events[nmbre][nmbra]

            
    print('_____Models_____')
    for c in range(0,int(number)):
        print model[c]
        num_ev.append(len(model[c]))


    print('_____Petri Net_____')
    for a in range(0, len(model[0])):
        petri.append([])
        for l in range(0, len(model)):
            for q in model[l][a]:
                if q not in petri[a]:
                    petri[a].append(q)
    for p in range(0,len(petri)):
        print petri[p]

x()
