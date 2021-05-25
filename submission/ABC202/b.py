S = str(input())
arr = {
    "6": "9",
    "9": "6"
}


rslt = S[::-1]
res = ""
for s in rslt:
    if arr.get(s) is not None:
        res = res + arr[s]
    else:
        res = res + s

print(res)