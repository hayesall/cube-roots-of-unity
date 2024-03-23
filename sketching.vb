for xcoord = -4.5 to 7.4 step (1/120) {
    for ycoord = -5.2 to 3.3 step (1/120) {
        z = complex(xcoord, ycoord)
        for iter = 1 to 12 {
            if (abs(z) < 1.1 and abs(z) > 0.9) {
                if (iter == 1)       color = gold
                else if (iter < 3)   color = yellow
                else if (iter < 5)   color = green
                else if (iter < 7)   color = blue
                else if (iter < 9)   color = purple
                else if (iter < 11)  color = magenta
                else color = red
                ' go to Plot
            }

            z = ((1-i)*z^4+(7+i)*z)/(2*z^3+6)
        }
        color = black
    }
}