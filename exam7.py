max_delivery_fee = 100

def calculateFinalFee(aiFee) :

    if (aiFee > max_delivery_fee) :
        return max_delivery_fee;

    return aiFee
