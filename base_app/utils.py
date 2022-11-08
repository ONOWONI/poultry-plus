def sumOfArr(arr, modelType):
    if len(arr) == 0:
        return 0
    left, mid, right, n = 0,len(arr) // 2,(len(arr) //2), len(arr)
    total_max = 0
    if modelType == "amount":
        while right < n:
            if left < mid:
                current_sum = arr[left].amount + arr[right].amount
                total_max += current_sum
                left +=1
                right += 1
            else:
                total_max +=arr[right].amount
                right +=1
    elif modelType == "quantity":
        while right < n:
            if left < mid:
                current_sum = arr[left].quantity + arr[right].quantity
                total_max += current_sum
                left +=1
                right += 1
            else:
                total_max +=arr[right].quantity
                right +=1
    else:
        print("amount and quantity are your only options")
    return total_max


def age_math(age_week, age_day):
    if age_day > 7:
        age_week += 1
        age_day =0
    week_in_days = age_week * 7
    total_age_in_days = week_in_days + age_day
    return total_age_in_days