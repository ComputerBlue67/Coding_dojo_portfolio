for(var num = 0; num < 15; num++){
    console.log(num);
}

//prediction 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14 correct

for(var i = 1; i < 10; i+=2){
    if(i % 3 == 0){
        console.log(i);
    }
}
//prediction 3,9  correct 


for(var j = 1; j <= 15; j++){
    if(j % 2 == 0){
        j+=2;
    }
    else if(j % 3 == 0){
        j++;
    }
    console.log(j);
}
//prediction something totes wrong 
//answer 1,4,5,8,10,11,14,16
//note 1 not divisible by 2 or 3 with %
//add immediately with j+2 or j++ after for loop and again wit j++