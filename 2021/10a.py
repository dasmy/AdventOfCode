from collections import deque

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def parse_brackets(input):
    total = 0

    for line in input.split('\n'):
        line = line.strip()
        if len(line) == 0:
            continue

        stack = deque()
        for char in line:
            if char == '(':
                stack.append(')')
            elif char == '<':
                stack.append('>')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            else:
                expected = stack.pop()
                if char != expected:
                    total += POINTS[char]

    print(f'Total points: {total}')


parse_brackets(
'''
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''
)

parse_brackets(
'''
<<{<[<<<{<<(<({}())({}[]))[[{}[]]<{}[]>])[<[{}[]]{()()}>{((){})<<><>>}]>>[<(<<{}>>[<()()><<><>>]
{[[[{<[(([[{(({}))([<>[]]((){}))}<<<[][]>[{}{}]>[{()[]}(()())]>][[[{<>()}[{}[]]]]]]<{{{{()[]}}}[[{[][]}{{
([((<(<(<<([{{[][]}([]<>)}({<>{}}[[]()])]<[[()()](()[])]([[][]](<><>))>>{{<(<><>)[<>()]>([[]()])}<<[[]()]<[][
{{{([((([({[{{()()}{<>[]}}({{}{}}([]{}))]{([{}<>])<(<><>){[]<>}}}})({{{(()())[[][]]}{<{}{}>
{{([[((({(({({<><>}([]{}))([()()]{[]{}})}[[({}{})<(){}>]<<()<>>>]){[[[()()][<>[]]}<[{}()]{{}<>}
{([<[[<<({[<(<()<>>(()())){<<>[]><()[]>}>[({{}<>})]][[(<()<>>{(){}})[{[]<>}[[]{}])][[(()()){[][]}]<{{}{}}<[
[<{[((<([[([<<{}()>{{}()}>{(()[])[<>{}]}]<{[<><>]{<>{}}}>)]{[{{{()<>}[{}<>]}<<()>{{}{}}>}]({{<
[<((<<({[{<{[[<><>](<>{})]{<()()><[]{}>}}<<[{}()]<[][]>><({}<>)>>>{<[[()<>]<{}[]>]<(<>()){<>{}}>>[{(()[])[{
([(<<{{<[<(<<[[]{}]({}{})><[()[]]{<><>}>>[[{[]<>}[{}()]][({}{})({}())]>){(<{(){}}[{}[]]>[{[][]}<<
([<{<<<[[<{[{({}{})[{}[]]}])[[(({}{}){()<>})<[()[]]<[][]>>]<(<()()>{()()}){(<><>)([]())}>]>]]<<{
[{((<<{[{[<<<(()[])[[][]]>>><{<{<>[]>{[]{}}>{<<>()>[<><>]}}[{{<>{}}([]())}{({}[])[<><>]}]>][(<({<>()}[[]{}])[
<(<[[<{(<[(<[([]())]({<>()}({}()))>[({(){}})[[[][]][<>{}]]]){{[[<><>]{{}[]}]<[(){}]<{}()>>}(<(<>{
{{{([[(<<<{[{(<><>){<>[]}}<<[][]><()<>>>]<[[(){}][<>[]]]{{()<>}[{}()]}>}[{{({}<>)}[[{}{}]{{}[]}]}[([()()]
{(<[{[{([({[[{<>}]{[<>{}]([][])}]{[(<>[])({}())]<{<><>}({}<>)>}}<[[(<>()){()[]}][<()()>{[]{}}]]<{[[]][[]()]
<{(({({(<{{<{{()()}<()[]>}{[[]()](<>[])}>}<<({{}()}<[]{}>)[{[]()}]><<<<><>>[<>[]]>>>}([<[{()[]}(()()
[[[{<({{[[<[{[(){}]<[]<>>}[[<>[]]{()<>}]]({<{}[]>[<>[]]}{({}{})<{}[]>})>{[[{[]{}}{<><>}]{(
<([<[(([[[[([<[][]>]<([]()){<>()}>){[{[]()}([][])]<{[]<>}({}<>)>}]<[[[[]<>][<>{}]]{{{}()]{<>(
<({{<<<{<<[[[<()<>>[()[]]]](<[{}<>]{[][]}>[{<>()}<()()>])]><{<[<()<>>[[]()]]<<[][]><()()>>>
[[{{(([[<{[[(<[][]><<><>>}[{{}()}]]{(<<><>>({}<>))[[[][]]<[]{}>]}]<[{({}<>)[[]]}({()()}[<><>
([<[([[<{<((<<{}()>[<>()]>)(<{{}()}>(<[]<>>{()()})))>({<<{(){}}{{}}><[<>{}]<<>{}>>>{([(){}](<>)){{()<>}({
[{[[<((({[{[<[[]()]<{}[]>>{<{}<>>(<>[])}]<{({}{}){{}[]}}{[[]<>]([][])}>}(<{(<>)[()<>]>>(({{}()})[[{}[]]{[]}
[{[[({<<{([{{({}())[()[]]}<[<>()]({}{})>}({[{}<>]<<><>>}{{[]<>}{()]})][<([<>()]({}[])){[{}{}](<>[])}>[((()
{{((<[{{[[(<{({}()){()<>}}[{{}<>)({}{})]>({<(){}>[[]{}]}[[[]()]<{}>]))<<{[[]{}]({}[])}{<()>({}
<{<({[[({<(<<<[][]>[<>[]]><(()[])>>{([[]<>]({}{}>)})((<[{}][{}<>]>{(()<>)})<<<<>[]>[(){}]>[(<>{})<<>[]>]>)>}
[[[{[[{<{({<({{}<>}({}<>))>{[({}())]}})[<[[([][])][<{}<>><()<>>]]([[<><>]<[]()>]<({}{})(<><>
[<({{[(<{(<<((<>)<{}[]>){{<>[]}<{}{}>}>(<(<><>)<{}<>>><{{}()}[{}()]>)>([([[]{}][{}[]])]))}>((({{
<<{({{(<([[(<[<>()]<<><>>>(<[]()>{{}<>})){{<{}[]>[()()]}<(<>[])<()[]>]}]{({<(){}>{[]()}}[(<>
(({<[({{[[{{[[()[]]([][])]{(<>[])<(){}>}}<<({}{})([]())><({}[])>>}<<<<{}[]>{[]{}}>(<[][]>[{}{}])>(({()<>
{[[([<[{[{<[[({}[])<{}[]>]([<>[]]({}{}))][({()[]}(()()))]>{<<({})([]{})>{[[]()](()()]}>[(((){})(()[]))<[[]<>
({[(<[(<({<[[[{}()]][<()()>[()[]]]]<{{<>[]}}[[[]{}]([]<>)]>>})<<{[<[()[]](()()}><(()())[<><>]>
((<[{([[{(([([<>()][[][]])]))}]])<{(<<{{<<[]{}>({}())>}}>>[{([[{{}()}{(){}}]](((()[])[(){}])<[<><
{(<{[{<<(<<[<<{}{}>><[[][]}{(){}}>]{{{[]<>}[[]<>]}}>{({<{}<>>({}<>)}<<[]<>>>)[(<{}<>>(<>))<[
[<({<<({[{[<[([]<>)]{[(){}]({})}>{{((){})}[<[][]>]}]({(<{}<>>(<>())){{[]()}(()())}}(((<>{}){()()}){{[]()}<<>
[[{{[<<[[[<<[{{}[]}<(){}>][{(){}}<{}[]>]>>(({({}{}}{<>{}}}([<>[]](()[]))))]{[[{((){})<<>()>}{{()[]}{<>()}}]<
{(([([<({[[{{[<>[]][<>[]]}[([][])[{}()]]}[([()()][{}()])([<>{}])]]][[{[([]{}){[]()}][<(){}
<{{[{<(((({[{<[]()>({}{})}]}))<[((<([]<>)[{}[]]>{<(){}>[[][]]}))[{<[()()][{}()]>(({}[])<<>[]>)}[((<>()){{}
[(<[{[[<{[([{{[]()}<()>}(([]())<(){}>)][(({}{})<{}<>>)])(<({{}()}({}))<[()[]]{<>[]}>><(<{}<>><{}<>>)<({}<>
{([({<<((({[({[][]})<{{}{}}<{}()>>]}<(<<[]()><()<>>>{{[]<>}([][])})(<{[]<>}[[]<>]>)>){([{<[]()>[<>[]]}[{<><
[{{<<[<<<<{<({[]}[()[]]){{{}<>}[(){}]}>({([]())({}[])>)}><[[{[()<>]({}{})}<<<>{}>{()[]}>]{{[[][]]}(<<>()><
(({({[{({[{[{([][])[[][]]}]{{{[]()}({}[])}({<>[]}(<>))}}[<<([]<>)>(<{}{}>{()})>[{[<><>][<>{}]}]]]}([{
(({{<[{[([({([{}{}][{}<>])<<{}{}><<>()>>})]([((<[]()>[{}()])<<{}<>>((){})>)]<{[[{}<>]<[][]>]<(()[]
{<[({<[[<[(<<({}[])[[]()]>([<>{}]{{}<>})>[<<{}[]>{<>()}><[<>{}]({}[])>])]{{{({{}{}}<[]()>)
{<(({<[({<<[[[()[]]<{}<>>]]>><[{<{<><>}(<><>)>[[()[]]{<><>}]}[[{<><>}{{}<>}]({{}{}}[[][]])]]<<[{{}{}}<<>[]>]
[<{({{(({([{(<{}[]>(<>{}))<[[]{}](()[])>}<{(<>{})(<>{})}>])<<<<({}<>){<>{}}>[(()()>(()())]>
({((({[(<{{({({}())[[]<>]}([<>[]]{{}()}))<({{}()}<{}{}>)[{[]{}}({}[])]>}[([{{}<>}<{}>])[{{()[]}{{}()}}[([]{
[<[{<{([<({<[[{}<>]{[][]}]{<<>{}><<><>>}>({[[]{}]<{}<>>}{{{}<>}(()[])})}){{{[<[]()><[][]>]
<<{<{[[{([{<[<{}[]>{[]<>}]<<{}{}>[{}[]]>>}([([{}{}]{<><>})[{<>{}})])]){{([[<{}[]>({}[])][[<><>]
([[(<([[[<[((([]{}){[]<>}))<{<[][]>[[]()]}[(()<>)<[]{}>]>]{[([[][]][()[]]){{(){}}[{}<>]}]}><
<[{{<{<({{([[[[]{}]<{}()>><([]()){[]{}}>]<{<()[]>([]())}>)}<<{{((){}){[][]}}(({}<>)(()()))}([{[
({{({[[{<({[({<>{}}[<>()])(([][]){{}{}])][({{}<>}(()[]))[<[]()><[]{}>]]}[{(<()[]><[]()>)[<{}()>{()[]}]}
<<<{<{[([[[[(<()[]>){<[]()><[]()>}]<<([])<[]<>>><[[]<>][<>[]]>>]<<[[()()](<><>)]({()()}[<>[]])>([<[]
((([{([({({<(<{}()>[()<>])<[{}<>]<{}[]>>>][{<[[][]]{{}()}>[({}()){[]<>}]}([{{}{}}[[]()]])])<[(({<>()}
([<<[(<{<<[<[{()[]}{()[]}](({}[]){{}[]})>]{([{()[]}])({{<>()}(()())})}>((({{()()}(()<>)}][[(<>()){()}
({[{[((<[<{<([[][]]{{}()})[{<>()}(<>{})]>{{{{}}}{{()}({}[])}}}>]<(<{<(<>())(()())>}>[<{[{}<>]{{
{({[<{<[[[[<({<>{}}{()[]}){<[]()><[]()>}>([(<>())[[]()]](({}{})[()<>]))]]({([[<>{}]<{}[]>](<()()><()<>>))
([<[<{<<<<((({<>}[<>{}])<({}())<()<>>>)[[[[]()][{}{}]]<(()<>)[<>]>]){{[({}())][([][])<()[]>]}{
[{[({{<[{[<<[[<>()]]<([]())>><<<[][]>>{[()<>]{{}}}>>]}]{<{{{{[<>{}]({}[])}<{{}}{<>{}}>}{<({}){<>
{<<{{({([{[([{[]<>}{<>[]}](<()[]>))[([{}]<()<>>)<<<>[]>[()<>]>]]}{[{<[()[]][{}{}]>{[[]()][{}[]]}}({[[]{
((<(<{{<([{[{{()[]}{<><>}}{{<>}({}{})})[([(){}][[][]])[<()[]><(){}>]]}<([(<>()){[][]}][([]())([]())])[
<<{[{{<{<[[[<<()<>>[()[]]>([()]{{}[]})]](<[(()<>)[()[]]]>{<[{}{}]>[<<><>><<><>>]})][{((<{}{}>[()
<<<[[<[[([{[(<()><[]{}>)[(()[])[[]{}]]]{[{{}<>}[{}<>]]}}[(<<<>()><()[]>>[({}())<(){}>])[[[[][]][<
[[<(({[(([{{<([][])[[][]]>[{{}{}}{<>[]}]}<[(<><>)](<[][]>[<>{}])>}]{{{([(){}]([]))<[{}<>](())>}([[(
[<{[([<{({([((()>[{}[]])[(<><>){[][]}]])([{([]<>){[][]}}<(()[]){[]()}>]<((<>{}){[][]})({{}()}<()[
((((<<<({([<{[{}()]{[]{}}}{({}[]){(){}}}>[[{()[]}[<>()]]<(()<>){(){}}>]]{[<(()())[{}[]]>(<<>()>({}
(<({((((<{{{[{{}{}}[(){}]][{<>{}}{(){}}]}([[{}[]]{<><>}]<[[]{}]<[][]>>)}({[[{}<>]<(){}>]}<{{<>[]}}<<<>[]>
{(<{(<{({(([{{()()}}][(({}{})<{}>)])<<(<()<>>{{}<>})(((){})[[]{}])><[[<>{})[<><>]][{()()}]>
<{[(<[[{(<({[<{}()>{{}{}}]{(()){[]{}}}}[{{[]<>}[{}{}]}])({({[][]}{[]()})})>(<{{(()[])<<>>>[<<>[]><[]<
([<[<[[{<[<(([<>{}]){[(){}]<()()>})<{([]{}}<{}<>>}{<{}{}><[]()>}>>(<<{<><>}(<>())>({<>}[{}{}])>(<(<><>)
([{[[(<[(([{[{<>[]}{<>()}]<[(){}](<>{})>]<<<<>[]>>{(<><>)<[]{}>}>])){{{{<([]<>)([]{})><{{}{
[<{({{(({<[([[()<>]{[][]}]({<>[]}(()[])))](<<({}())([][])>[{()<>}(()())]><{[<>{}]<<>()>}[[{}()]{<><>}]>)>{
{({{{{[{{[<{{<[][]>([])}<[[]{}][{}()]>}>]{{[[<<>[]>[[][]>]<<{}<>>(()<>)>]{[[<>{}]{{}[]}]}}<[[[<><>]<<
<({{({(({{<{{([]{}){<><>}}<(<>())({}{}]>}[{((){})(<>())}]>(({<[]()>([]{})}({{}{}}<<>()>)))}[[([<{}<>>
[[<{<{<((<<({(<>())(<>())}{{(){}}[{}()]})<(<{}<>>{(){}})>>{{({[][]}{{}[]})<<{}<>>(()<>)>}<<<<>()>>{({}{}){()
{[(<<<{(<{<<({<>{}}{()[]}>({<>[]}({}()))>>}>)<{(<(<({}[]){()[]}>)>((({()[]}[[][]]){<[][]><<>()>})[(([]<>)<
<[<[{<[{[[<([<{}()>[<>]]{[[][]]<{}()>}}>({{{<>[]}{()[]}}{{()}<<><>>}}<<([])([][])>{[{}<>]((
{[<<[[(<<{[<[[[]]({}())]([{}()][[]<>])>]}<({{(()[])<[][]>}{({})<()<>>}})([((()[])<[]<>>)<{(){}}([]())
<{{<[[[(((<[{({}()){()()}}(<{}()>{()<>})]{{{()()}}{[[]{}]({}())}}>))<{<(((()<>)[{}[]])){[<[]<>>{{}()
<([((<<(((({{[{}<>]<[]<>>}(<[]{}><[]{}>)}[{{<>[]}}{(<>{}){[]<>}}])<<{(()())<<>{}>}[[{}[]][{}()]]>[<[[]()
{({{({[[({[<[<<><>)<{}{}>][<(){}>{[]{}}]>({(<>{})(<>())}<({})({})>)]})]<({[[({[]<>}{()()}){({}()
((([[(<(<[([({{}()})[{{}()}({}{})]]{({[]()}{{}()})(<()[]><<>[]>)}){{([{}()])}}]<[(<(<><>)[()[]}>[{{}<>}])]>>[
{(([(<[[[[<<([(){}][<>[]]){({}())[[]{}]}>>[[<{()[]}{(){}}>(<{}{}><{}{}>)]<([()[]]<{}>)(<()[]>{
{({([(<{<[[<<[<><>]<<><>>>>[<<{}<>>[{}<>]>{[[]{}][{}<>]}]]][{{<[{}[]]({})><[()()]>}}<[<{[]<>}[[]()]>]{[
(((<{([<[(<[{([][])<[][]>}({{}<>}[{}{}])]>[[({[]<>}{<>{}})]})[{({(()[])([][])}{<()()>[[][]
<(<{{<([<(<{<{{}}{<>{}}>}([([]{}){(){}>]{<()<>>([])})>)<<({<[]<>>})({[()[]]}<[(){}]{{}()}>)>{[<<[][]>>({[]{
({{(<(([[{((<<()[]><{}<>>>])}][<({<[{}[]][{}{}]><(()())([]())>})>{<(<{[]{}}{{}<>}>{{[]<>}{<><>}})>}]]{<[{[[
{<[<([(((<[{[(())]}[(<{}()>)([[]][{}])]]{({<[]{}><()[]>}{{[]()}<{}<>>})}>){(({{<(){}>{<>[]}}(<(){}>(
([[{<{{{({{<[<[][]><()()>>><<[<>()]>>}{[[(())]<{[]<>}<()<>>>]}})(<({[([]<>)<<>[]>]({<>()}[
{<[<<[((<<{<{([]<>)(<><>)}([()<>][{}[]])>}<<{{[]()}(<>{})}([<><>]({}[]))>{<[()<>]<{}()>>{<()(
{<{(<[[[<[{<[({}())<()<>>]>[{([]{})([]<>)}[<[][]>]>}][<([[()<>]{[][]}]){<[[]()](()())>({()}(()()))}>({<[()<
[{({<<<({{<[(({}[]){{}()})[{[]{}}{<><>}]]<{<[][]>(<>())}([<>{}])>>}[(<{{<>}([][])}>{{[[]()][[][]]}{<<>()><
<<([{{[(<[([<{[]()}<<><>>><(()())<()[]>>][{<[]()><{}()>}{<<><>>[()<>]}])(<<<<>{}][{}[]]>[{<>}({}
((<<<<[{<[[<[{()()}<[][]>]{(()<>)}><{[[]{}]<{}{}>}>]<<{{[]<>}([])}{({}())([]{})]><[(<>())(<>{})]>>]><([<(([]
{[[<(<[({[[[{{<>()}<()()>}]]]}[({(<[[][]]>(<{}<>>))}[<{<[]{}>(()<>)}{<{}{}>[()<>]}>])(<{([[]<>]){
{{<<{([<{[[[(<{}{}>[[]<>])({<><>}{{}[]})]]][([([()[]])[(()<>)<[]{}>]]<{{()<>}{[]()}}<<[]{}>{
<(([[<(({{(<{{()<>}[<>()]}[({}())[[][]]]>{{[{}<>]((){})][<<>{}><[]{}>]})<<({{}()}<<>{}>){(<>())[<>{}]}>(
(<[(<<(((([<[<{}[]>][[()()]<<>()>]><[<{}{}>{()<>}](<()()])>][{{[{}<>]{<>()}}[<()()><{}>]}<(<{}{
({{({[(<[{[<[((){})({}{})]([<>[]][[]()])>](<(<(){}><()()>)({<>{}}<{}()>)><{{<>()}(())}<{()()}<[]()>>
{<([(<<{([[[[(()<>)(()())]][[([]{})({}())]<[[]<>]{()[]}>)]([[<(){}>{<>{}}]((()())[()()])])]
(<<(((<[[{[{<[()<>]{<>{}}>([[]()][()()])}]{([<[]<>>{<>[]}]<<[][]>[{}()]>){<{[][]}[<>{}]><[<>[]]({}{}
<([[[(<[([{((<<>()>{()[]}){(<>())([])})[{<{}[]>([][])}[({}[])[<>()]]]}[(<<<>{}><()<>>><<<>[]>{(
[[{<[[(<<<(([(<><>)([][])](([]{}){[]{}}))[<[[]{}]>([[]()]{[][]})])>{{{[<()[]>[[]{}]][{()<>}[<>[]]]}}
([(<{<<(<{{{[[<>[]]<(){}>]([()[]][()[]])}{((<>()))}}{<[<{}<>>(<><>)](([][])<<>()>)}}}(<<[<{}[]
<[{{({{<[<[{(<<>[]>(<>()))<([]<>)[{}<>]>}]>{<<{<[]{}>(<>())}>([<(){}><(){}>]{[<>()]([]())})>}]>}})}}{(((
[<(((<{<<[(<{(<>[])}>){(<<{}<>>([]<>)>{<{}()>}}[[<{}{}>{[][]}](<<>[]>{{}[]})]}]><<([<[(){}]<()>><[(){}]
({[[(<[{(<((<[()[]]{[]<>}>){<(<>){()<>}>})(({<(){}>[{}[]]})[[(()[]){[]<>})<{[]()}>])>)<<<(<({}())(<>[])
[{([<<<[{{([<<{}{}>>[{{}[]]]])}<<[<{{}}{<><>}>(({}{})[<>[]])]({[<><>]([][])}{(()<>)<<><>>})
[[<(<<[{([[[[<[]{}><[]()>]][{[[][]]<()<>>}]]]{{{(<[]{}>(()<>))<(<>[])<<><>>>}]({{(()[]){{}()}}
({<<<{[<[[[{([{}<>]{<>()})(<<><>>)}(<(<>[])<{}>))][({<{}[]>[[][]]}(([]())(()[])))<<[[]()]{<><>}>>
[{<[[{{[<<([([<><>]([]<>))]({[()[]][{}{}]}{{()()}[[]<>]})){(<(()[])<[]()>><[[]()]<()<>>>)(<<()(
{<({((<([<(({{[]<>}[{}<>]}[<()[]><[]{}>]){<{[][]}{<><>]>})(({({}())[()()]}{[{}()][[]<>]}))>])<(<{(<{
'''
)