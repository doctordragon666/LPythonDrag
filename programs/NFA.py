# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
#

import time


# 表示一个状态
class State:
    def __init__(self, id, is_start=False, is_accept=False):
        self.id = id
        self.is_start = is_start
        self.is_accept = is_accept
        self.outgoing_edges = []

    def add_outgoing_edge(self, symbol, to_state):
        self.outgoing_edges.append((symbol, to_state))

    def get_outgoing_edges(self):
        return self.outgoing_edges

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    # 获取所有可到达的接受状态
    def get_all_accept_states(self):
        if self.is_accept:
            return {self}
        visited_states = {self}
        accept_states = set()
        stack = [self]
        while stack:
            state = stack.pop()
            for _, next_state in state.get_outgoing_edges():
                if next_state not in visited_states:
                    visited_states.add(next_state)
                    if next_state.is_accept:
                        accept_states.add(next_state)
                    stack.append(next_state)
        return accept_states


# 表示一条转移边
class Edge:
    def __init__(self, symbol, from_state, to_state):
        self.symbol = symbol
        self.from_state = from_state
        self.to_state = to_state


# 根据正则表达式构建NFA
def regex_to_nfa(regex):
    states = []
    edges = []
    start_state = State(len(states), is_start=True)
    accept_state = State(len(states) + 1, is_accept=True)
    states.extend([start_state, accept_state])
    state_stack = [start_state]
    for ch in regex:
        if ch == '(':
            new_state = State(len(states))
            edges.append(Edge('', state_stack[-1], new_state))
            states.append(new_state)
            state_stack.append(new_state)
        elif ch == ')':
            top_states = []
            while True:
                s = state_stack.pop()
                top_states.append(s)
                if s.is_start:
                    break
            new_state = State(len(states))
            edges.append(Edge('', new_state, None))
            states.append(new_state)
            for s in top_states:
                edges.append(Edge('', new_state, s))
            state_stack.append(new_state)
        elif ch == '|':
            nfa2 = state_stack.pop()
            nfa1 = state_stack.pop()
            new_state1 = State(len(states))
            new_state2 = State(len(states) + 1)
            states.extend([new_state1, new_state2])
            edges.extend([
                Edge('', new_state1, nfa1),
                Edge('', new_state1, nfa2),
                Edge('', nfa1.get_all_accept_states(), new_state2),
                Edge('', nfa2.get_all_accept_states(), new_state2),
            ])
            state_stack.append(new_state1)
        elif ch == '*':
            nfa = state_stack.pop()
            new_state1 = State(len(states))
            new_state2 = State(len(states) + 1)
            states.extend([new_state1, new_state2])
            edges.extend([
                Edge('', new_state1, nfa),
                Edge('', nfa.get_all_accept_states(), new_state2),
                Edge('', new_state1, new_state2),
                Edge('', nfa.get_all_accept_states(), nfa),
            ])
            state_stack.append(new_state1)
        else:
            new_state = State(len(states))
            states.append(new_state)
            edges.append(Edge(ch, state_stack[-1], new_state))
            state_stack.append(new_state)
    edges.append(Edge('', start_state, state_stack[0]))
    edges.append(Edge('', state_stack[-1].get_all_accept_states(), accept_state))
    return start_state, accept_state, states, edges


# 在NFA上模拟字符串匹配的过程，并返回匹配结果
def match_nfa(nfa, string):
    curr_states = {nfa}
    for i, ch in enumerate(string):
        next_states = set()
        for state in curr_states:
            for symbol, to_state in state.outgoing_edges:
                if symbol == ch or symbol == '':
                    next_states.add(to_state)
        if not next_states:
            return False
        curr_states = next_states
    return any(state.is_accept for state in curr_states)


# 绘制 NFA 图和字符串匹配过程的动画
def animate_nfa_match(nfa, string):
    print('NFA状态总数：', len(nfa[2]))
    print('输入字符串：', string)
    # 绘制 NFA 图，用字典保存每个节点的坐标
    node_positions = {}
    mermaid_code = 'graph LR\n'
    for state in nfa[2]:
        mermaid_code += f'    {state.id}{{ }}'
        if state.is_start:
            node_positions[state.id] = (0, 0)
            mermaid_code += ' -->|start|'
        if state.is_accept:
            mermaid_code += ' -->|accept|'
    for edge in nfa[3]:
        mermaid_code += f'\n    {edge.from_state.id}'
        if edge.symbol != '':
            mermaid_code += f' --{edge.symbol}-->'
        else:
            mermaid_code += ' -->'
        mermaid_code += f' {edge.to_state.id}'
    mermaid_code += '\n'
    print('NFA图形表示：')
    print(mermaid_code)
    # 绘制字符串匹配过程的动画
    curr_states = {nfa[0]}
    for i, ch in enumerate(string):
        print(f'当前字符为：{ch}')
        next_states = set()
        for state in curr_states:
            for symbol, to_state in state.outgoing_edges:
                if symbol == ch or symbol == '':
                    next_states.add(to_state)
        if not next_states:
            print('无法转移，匹配失败')
            return
        curr_states = next_states
        # 绘制匹配过程
        dot_code = 'digraph {\n'
        for state in nfa[2]:
            dot_code += f'    {state.id} [shape={("circle" if state in curr_states else "point")}]'
            if state.is_start:
                dot_code += ' [style=filled] [color=black]'
            if state.is_accept:
                dot_code += ' [peripheries=2]'
            dot_code += '\n'
        for edge in nfa[3]:
            dot_code += f'    {edge.from_state.id} -> {edge.to_state.id} [label="{edge.symbol}"]\n'
        dot_code += '}\n'
        print(dot_code)
        time.sleep(1)
    if any(state.is_accept for state in curr_states):
        print('匹配成功')
    else:
        print('匹配失败')


# 测试代码
if __name__ == '__main__':
    nfa = regex_to_nfa('c(a|b)*t')
    animate_nfa_match(nfa, 'cat')

# 运行结果
