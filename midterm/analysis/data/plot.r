rm(list=ls())
exp.titles = c("Schmainz", "SLACker", "Horsay", "JayLab", "Daisy")
exp.xlab = "q^2 (GeV^2)"
require("gplots") || install.packages("gplots")
par(mfrow=c(1,5))
for (i in 0:4){
  data = read.table(paste('exp',i,'.dat', sep=""))
  x=data[,1]
  y=data[,2]
  dy=data[,3]
  plot(x=x,y=y, xlab=exp.xlab, ylab="|G^p_E|^2", main=exp.titles[i+1])
}

f0=function(x){x}
f1=function(x){x}
f2=function(x){x}
f3=function(x){x}
f4=function(x){x}
nukfit = c(f0,f1,f2,f3,f4)


radvec=c(1,2,3,4,5)
leadingco=c(1,2,3,4,5)
readline(prompt="[enter] to continue")
par(mfcol=c(3,5))
for (i in 0:4){
  data = read.table(paste('exp',i,'.dat', sep=""))
  x=data[,1]
  y=data[,2]
  dy=data[,3]
  wnlmod <- nls(y ~ (A + B*x + C*x*x)^2, start = list(A = 1, B = -6, C = 0), weights = dy^-2)
  plot(x=x,y=y, xlab=exp.xlab, ylab="|G^p_E|^2", main = paste(exp.titles[i+1],"\nRadius", round(sqrt(-6*summary(wnlmod)$coefficient[[2]])*.197, 3)))
  arrows(x0=x, y0=y-dy, x1=x, y1=y+dy, code=3, lwd=1, angle=90, length=0.02)
  radvec[i+1]=(sqrt(-6*summary(wnlmod)$coefficients[[2]])*.197)
  leadingco[i+1]=((summary(wnlmod)$coefficients[[1]]))
  yint=summary(wnlmod)$coefficients[[1]]
  slope=summary(wnlmod)$coefficients[[2]]
  dslope=summary(wnlmod)$coefficients[[3]]
  fun=function(x){(yint+slope*x+dslope*x*x)^2}
  nukfit[[i+1]]=fun
  curve(fun, col = "red", add=TRUE)
  data = read.table(paste('exp',i,'.dat', sep=""))
  x=data[,1]
  y=data[,2]-nukfit[[i+1]](x)
  dy=data[,3]
  plot(x=x,y=y, xlab=exp.xlab, ylab="|G^p_E|^2", col = ifelse(abs(dy)-abs(y) > 0, 'black', 'blue'), main= paste('Residuals for ',exp.titles[i+1],'', sep=""))
  arrows(x0=x, y0=y-dy, x1=x, y1=y+dy, code=3, lwd=1, angle=90, length=0.02, col = ifelse(abs(dy)-abs(y) > 0, 'black', 'blue'))
  abline(h=0, col = "red")
  periodogram(data[1], xlab="period", ylab="Signal Strenght", main=paste("Period for",exp.titles[i+1]))
}

install.packages("TSA")
library(TSA)

sprintf("independent predictions of radius: %f %f %f %f %f (in fm)", radvec[1], radvec[2],radvec[3],radvec[4],radvec[5])
sprintf("mean radius %f+-%f fm",mean(radvec[1:5]), sd(radvec[1:5]))


readline(prompt="[enter] to continue")
par(mfrow = c(1,3))
for (i in 0:4)
{
  data = read.table(paste('exp',i,'.dat', sep=""))
  x=data[,1]
  y=data[,2]/leadingco[i+1]^2
  dy=data[,3]/leadingco[i+1]^2
  if(i==0){
    x_all=x
    y_all=y
    dy_all=dy
  } else {
    x_all=append(x_all,x)
    y_all=append(y_all,y)
    dy_all=append(dy_all,dy)
  }

}

plot(x=x_all,y=y_all, main=paste("Combined Data (Normalized)\nRadius", format(round(sqrt(-6*summary(wnlmod)$coefficient[[2]])*.197, 3), nsmall=3)), xlab=exp.xlab, ylab="|G^p_E|^2")
arrows(x0=x_all, y0=y_all-dy_all, x1=x_all, y1=y_all+dy_all, code=3, lwd=1, angle=90, length=0.02)
wnlmod <- nls(y_all  ~ (A + B*x_all + C*x_all*x_all)^2, start = list(A = 1, B = -6, C = 0), weights = dy_all^-2)
curve( (summary(wnlmod)$coefficient[[1]] +summary(wnlmod)$coefficient[[2]]*x+summary(wnlmod)$coefficient[[3]] *x*x)^2, col = "red", add=TRUE)
sprintf("Combined Data Set with Normalization factors Radius: %f (fm)",sqrt(-6*summary(wnlmod)$coefficients[[2]])*.197)



df=data.frame(cbind(x_all,y_all,dy_all))
sample.row = function(df,n){
    return(df[sample(nrow(df),n, replace = TRUE),])
  }

trials = 10000
dp = 100
bootstrap_rad = rep(0,trials)
for(i in 0:trials){
  bsdf=sample.row(df,dp)
  trust = rnorm(dp,1,0.01)
  x_all=bsdf[[1]]
  y_all=bsdf[[2]]*trust+bsdf[[3]]*rnorm(dp,0,1)
  dy_all=bsdf[[3]]*trust
  x_all2 = x_all*x_all
  wnlmod <- nls(y_all  ~ (A +B*x_all + C*x_all*x_all)^2,start = list(A=1, B= -6, C=0), weights = dy_all^-2)
  bootstrap_rad[i]=sqrt(-6*summary(wnlmod)$coefficients[[2]])*.197
}

summary(wnlmod)
mean(bootstrap_rad)
sigm=sd(bootstrap_rad)
sigm
sigm/sqrt(trials)
hist(bootstrap_rad, main=paste("Bootstrap of Normalized Data\nMean:", round(mean(bootstrap_rad),3),"\u00B1", round(sigm,3), "fm") , xlab="Radius (fm)", ylab=paste("Counts per", trials), breaks=30)

for (i in 0:4){
  data = read.table(paste('exp',i,'.dat', sep=""))
  x=data[,1]
  y=data[,2]
  dy=data[,3]
  if(i==0){
    x_all=x
    y_all=y
    dy_all=dy
  } else {
    x_all=append(x_all,x)
    y_all=append(y_all,y)
    dy_all=append(dy_all,dy)
  }
}

bootstrap_rad = rep(0,trials)
for(i in 0:trials){
  bsdf=sample.row(df,dp)
  trust = rnorm(dp,1,0.01)
  x_all=bsdf[[1]]
  y_all=bsdf[[2]]*trust+bsdf[[3]]*rnorm(dp,0,1)
  dy_all=bsdf[[3]]*trust
  x_all2 = x_all*x_all
  wnlmod <- nls(y_all  ~ (A+B*x_all+C*x_all*x_all)^2,start = list(A = 1, B = -5, C = 10), weights = dy_all^-2)
  bootstrap_rad[i]=sqrt(-6*summary(wnlmod)$coefficients[[2]])*.197
}

mean(bootstrap_rad)
sigm=sd(bootstrap_rad)
sigm
sigm/sqrt(trials)
hist(bootstrap_rad, main=paste("Bootstrap Histogram of Raw Data\nMean:", round(mean(bootstrap_rad),3),"\u00B1", round(sigm,3), "fm") , xlab="Radius (fm)", ylab=paste("Counts per", trials), breaks=30)

trials=100
par(mfrow=c(1,5))
for (i in 0:4){
  i=3
  data = read.table(paste('exp',i,'.dat', sep=""))
  x=data[,1]
  y=data[,2]
  dy=data[,3]
  df=data.frame(cbind(x,y,dy))
  df
  bootstrap_rad = rep(0,trials)
  for(j in 0:trials){
    bsdf=sample.row(df,dp)
    systematics = rnorm(1,1,0.01); systematics
    con = bsdf[[3]]*rnorm(dp,0,1)
    x_all=bsdf[[1]]
    y_all=(bsdf[[2]]+bsdf[[3]]*rnorm(dp,0,1))*systematics
    dy_all=bsdf[[3]]*trust
    wnlmod <- nls(y_all  ~ (A+B*x_all+C*x_all*x_all)^2,start = list(A = 1, B = -5, C = 10), weights = dy_all^-2)
    bootstrap_rad[j]=sqrt(-6*summary(wnlmod)$coefficients[[2]])*.197
  }
  mean(bootstrap_rad)
  sigm=sd(bootstrap_rad)
  hist(bootstrap_rad, main=paste("Bootstrap of",exp.titles[i+1],"Data\nMean:", round(mean(bootstrap_rad),3),"\u00B1", round(sigm,3), "fm") , xlab="Radius (fm)", ylab=paste("Counts per", trials), breaks=30)
  rm(bootstrap_rad,x, y, dy, df, x_all, y_all, dy_all, data, con)
}
bootstrap_rad
