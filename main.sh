#!/bin/bash
printf "Chose an option from the menu:\n"
echo 1")" Android
echo 2")" IOS


read -n1 -p "option >>" option 

if  [ "$option" = "1" ]
then 
    # install node dependencies
    printf "\nInstalling node dependencies\n"
    npm install
    wait 

    # cd android
    printf "\nChanging directory to android\n"
    cd android
    ./gradlew clean
    wait
    ./gradlew build
    wait

    # Make the apk
    printf "\nMaking the apk\n"
    ./gradlew assembleRelease
    
else
    # install node dependencies
    printf "\nInstalling node dependencies\n"
    npm install
    wait 

    # cd ios
    printf "\nChanging directory to ios\n"
    cd ios
    pod install
    wait 

    cd ..

    # build 
    printf "\nBuilding the project\n"
    npx react-native run-ios
fi
