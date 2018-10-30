#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error=[]
    new_net=[]
    new_age=[]
    new_pred=[]
    count=0

    errors = (net_worths-predictions)**2
    cleaned_data =zip(ages,net_worths,errors)
    print cleaned_data[2][0]
    cleaned_data = sorted(cleaned_data,key=lambda x:x[2][0], reverse=True)
    limit = int(len(net_worths)*0.1)
    
    
    return cleaned_data[limit:]
    """for i in range(0, 89):
        error.append(predictions[i]-net_worths[i])
        print error[i]
    ac=sorted(error)
    print ac
    

    error=error[0:80]

    for i in range(0,89):
        if(predictions[i]-net_worths[i]) in error:
            count+=1
            new_net.append(net_worths[i])
            new_age.append(ages[i])
            new_pred.append(predictions[i])"""
    
    #cleaned_data=[new_age, new_net, error]
    #print "New num of items:", count

    

    return cleaned_data[limit:]



