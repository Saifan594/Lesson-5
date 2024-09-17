print ( "\033c" )

temperature = input ( "enter temperature (C°) : " )
temperature = float ( temperature )

if temperature < 20 :
    print ( "\nyou should wear jacket and pullover" )

else :
    print ( "\nyou should wear light cloth" )