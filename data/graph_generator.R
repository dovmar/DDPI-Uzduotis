library(tidygraph)
library(igraph)
library(tidyverse)


#### Small

y <- play_erdos_renyi(5, 0.8, directed = FALSE, loops = FALSE)
yy<- to_components(y)

ind <- which.max(map(yy,gsize))

yyy <- yy[[ind]]

yyy <- activate(yyy,"edges")

write_csv(as_tibble(yyy),"small.csv",col_names = FALSE)


#### Medium

y <- play_erdos_renyi(15, 0.3, directed = FALSE, loops = FALSE)
yy<- to_components(y)

ind <- which.max(map(yy,gsize))

yyy <- yy[[ind]]

yyy <- activate(yyy,"edges")

write_csv(as_tibble(yyy),"medium.csv",col_names = FALSE)



#### Large

y <- play_erdos_renyi(40, 0.06, directed = FALSE, loops = FALSE)
yy<- to_components(y)

ind <- which.max(map(yy,gsize))

yyy <- yy[[ind]]

yyy <- activate(y,"edges")

write_csv(as_tibble(yyy),"large.csv",col_names = FALSE)
