par(mfrow=c(4,4));
k=470;
l=0;
for(i in c(1:16))
{
  data = read.table(paste(i,".txt",sep=''));
  x=data[[1]]/180*pi; y=data[[2]]; dy=data[[3]];
  plot(x, y, main=i, xlab ="rad", ylab="f^2")
  arrows(x0=x, y0=y-dy, x1=x, y1=y+dy, code=3, lwd=1, angle=90, length=0.02)
  func = nls(y~(1/k*sin(d)*cos(x))**2, start = list(d=1))
  d=summary(func)$coefficients[[1]]
  curve(1/k*exp(d)*sin(d)*cos(x), add=TRUE)
}


