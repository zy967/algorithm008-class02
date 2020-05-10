学习笔记
这周内容主要再于理解记忆递归, 分治, 回溯的代码模板, 并没有太多的知识点. 做题就完事儿了.

在有效修建无效分支的情况下, 递归方法并不会比迭代方法在时间上差多少

在构思递归代码的时候避免人肉推理, 尽快熟练直接写出递归框架

## 递归 & 回溯
``` Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed (回溯)
```
## 回溯
```
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```
