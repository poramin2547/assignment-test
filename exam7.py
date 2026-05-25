# หาก AI แนะนำค่าส่งที่แพงเกินไปจนผิดกฎหมายคุ้มครองผู้บริโภค จะวาง Hard-coded Guardrails อย่างไร?

max_delivery_fee = 100

def calculateFinalFee(aiFee) :

    if (aiFee > max_delivery_fee) :
        return max_delivery_fee;

    return aiFee
