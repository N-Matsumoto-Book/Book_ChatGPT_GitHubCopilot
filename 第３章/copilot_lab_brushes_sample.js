function doSomething(x, y) {
    let temp = []
    for (let i = x; i < y; i++) {
        if (i % 3 == 0) {
            temp.push(i)
        } else {
            continue
        }
    }
    for (let j = 0; j < temp.length; j++) {
        temp[j] = temp[j] * 3
    }
    let result = 0
    for (let k = 0; k < temp.length; k++) {
        result = result + temp[k]
    }
    return result
}
console.log(doSomething(1, 15));