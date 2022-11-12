/**
 * @param {string} s
 * @return {number}
 */
 var romanToInt = function(s) {
    const key = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    let isTrigger = false
    let val = 0
    let sChar = s.split('')

    return sChar.reduce((total, str, index) => {
        console.log(isTrigger, val)
        if(!isTrigger && index != sChar.length && str == 'I' ||str == 'X' || str == 'C' ){
            val = str
            isTrigger = true
            return total
        }
        else if(isTrigger && val == 'I'){
            isTrigger = false
            if(str == 'V'){
                return total + 4
            } else if(str == 'X'){
                return total + 9
            }
        }
        else if(isTrigger && val == 'X'){
            isTrigger = false
            if(str == 'L'){
                return total + 40
            } else if(str == 'C'){
                return total + 90
            }
        }
        else if(isTrigger && val == 'C'){
            isTrigger = false
            if(str == 'D'){
                return total + 400
            } else if(str == 'M'){
                return total + 900
            }
        }
        
        if(isTrigger){
            isTrigger = false
            return total + key[val] + key[str]
        }

        return total + key[str]
    }, 0)
};