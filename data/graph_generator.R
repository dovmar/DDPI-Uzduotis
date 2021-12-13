library(tidygraph)
library(tidyverse)


#### Small

y <- play_erdos_renyi(5, 0.8, directed = FALSE, loops = FALSE)
yy <- activate(y,"edges")

write_csv(as_tibble(yy),"small.csv",col_names = FALSE)


#### Medium

y <- play_erdos_renyi(15, 0.3, directed = FALSE, loops = FALSE)
yy <- activate(y,"edges")

write_csv(as_tibble(yy),"medium.csv",col_names = FALSE)



#### Large

y <- play_erdos_renyi(20, 0.3, directed = FALSE, loops = FALSE)
yy <- activate(y,"edges")

write_csv(as_tibble(yy),"large.csv",col_names = FALSE)



#### Large no Hamiltonian paths

y <- play_erdos_renyi(40, 0.075, directed = FALSE, loops = FALSE)
yy <- activate(y,"edges")
if (to_components(yy) > 1) {
  write_csv(as_tibble(yy),"large_no_paths.csv",col_names = FALSE)
}