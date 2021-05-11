function greeting(){
        return "Hello";
        console.log("World");
    }
    var word = greeting();
    console.log(word);

    //predict "Hello" "World"------wrong
    //"Hello"   note: return ends the function immediately


    function add(num1, num2){
            console.log("Summing Numbers!");
            console.log("num1 is: " + num1);
            console.log("num2 is: " + num2);
            var sum = num1 + num2;
            return sum;
        }
        var result1 = add(3,5);
        var result2 = add(4,7);
        console.log(result1);
        console.log(result2);
        //predict
        //"Summing Numbers!" "num1 is: " + 3 "num2 is: " + 5, 8
        //"Summing Numbers!" "num1 is: " + 4 "num2 is: " + 5, 11---------correct






        function highFive(num){
                for(var i=0; i<num; i++){
                    if(i == 5){
                        console.log("High Five!");
                    }
                    else{
                        console.log(i);
                    }
                }
            }
        //predict 0,1,2,3,4 wrong 
        //note function needs a number in num paramater to run