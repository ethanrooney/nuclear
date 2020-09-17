#!/usr/bin/Rscript

l1=scan("l1.dat")
l05=scan("l05.dat")
l15=scan("l15.dat")

png(file="hist.png", width = 800, height = 800)
par(mfrow=c(2,2))
hist(l1, 
     main="Equilateral Triangle",
     xlab=paste(expression(Theta)," (rad)"),
     col="red",
     cex.main=2,
     cex.axis=1.5,
     cex.lab=1.5,
     )

hist(l05,
     main="Isosceles Triangle side 0.5",
     xlab=paste(expression(Theta)," (rad)"),
     col="green",
     cex.main=2,
     cex.axis=1.5,
     cex.lab=1.5,
     )

hist(l15,
     main="Isosceles Triangle side 1.5",
     xlab=paste(expression(Theta)," (rad)"),
     col="blue",
     cex.main=2,
     cex.axis=1.5,
     cex.lab=1.5,
     )

dev.off()
