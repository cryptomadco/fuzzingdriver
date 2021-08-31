  
import cpp 
from FunctionCall fucall, Expr size
where
    fucall.getTarget().hasName("strncmp")
select fucall.getArgument(_).getValueText()
