class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def dfs(current_expression):
            closing_brace_index = current_expression.find('}')
            if closing_brace_index == -1:
                result_set.add(current_expression)
                return
            opening_brace_index = current_expression.rfind('{', 0, closing_brace_index - 1)
            prefix = current_expression[:opening_brace_index]
            suffix = current_expression[closing_brace_index + 1:]
            brace_content = current_expression[opening_brace_index + 1:closing_brace_index]
            for option in brace_content.split(','):
                dfs(prefix + option + suffix)
        result_set = set()
        dfs(expression)
        return sorted(result_set)