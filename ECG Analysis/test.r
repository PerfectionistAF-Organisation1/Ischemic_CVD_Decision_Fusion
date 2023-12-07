load(system.file("ecgRDA", "ecg.Rda", package = "heartBeat"))
str(ecg)
library(ggplot2)
ggplot(data = ecg, aes(x = time, y = ecg)) + geom_line()