## Regular Expressions (Python RegEx)

https://www.programiz.com/python-programming/regex

### `^a...s$`

>  any five letter string starting with a and ending with s.

<br/><br/>
* MetaCharacters

### `[abc]`

> Square brackets specifies a set of characters you wish to match.

### `[a-e]`

> is the same as [abcde]

### `[^abc]`

> complement (invert) the character set by using caret ^ symbol at the start of a square-bracket.

### `.`

> A period matches any single character (except newline '\n').

### `^`

> The caret symbol ^ is used to check if a string starts with a certain character.

### `$`

> The dollar symbol $ is used to check if a string ends with a certain character.

### `*`

> The star symbol * matches zero or more occurrences of the pattern left to it.

### `+`

> The plus symbol + matches one or more occurrences of the pattern left to it.

### `?`

> The question mark symbol ? matches zero or one occurrence of the pattern left to it.

### `{}`

> Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.

### `|`

> Vertical bar | is used for alternation (or operator).

### `()`

> Parentheses () is used to group sub-patterns. For example, (a|b|c)xz match any string that matches either a or b or c followed by xz

### `\`

> Backlash \ is used to escape various characters including all metacharacters. For example, \\$a match if a string contains $ followed by a. Here, $ is not interpreted by a RegEx engine in a special way.

<br/><br/>
* Special Sequences

### `\A`

> Matches if the specified characters are at the start of a string.

### `\b`

> Matches if the specified characters are at the beginning or end of a word.

### `\B`

> Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.

### `\d`

> Matches any decimal digit. Equivalent to [0-9]

### `\D`

> Matches any non-decimal digit. Equivalent to [^0-9]

### `\s`

> Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v]

### `\S`

> Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v].

### `\w`

> Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also considered an alphanumeric character.

### `\W`

> Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_].

### `\Z`

>  Matches if the specified characters are at the end of a string.



---

<br/>

## Tags

| 태그 | 이름 | 설명 | 예시 |
| --- | --- | --- | --- |
|NNG|	일반 명사   | 일반 개념을 표시하는 명사.|
|NNP|	고유 명사   | 낱낱의 특정한 사물이나 사람을 다른 것들과 구별하여 부르기 위하여 고유의 기호를 붙인 이름. | (‘홍길동’)|
|NNB|	의존 명사   | 의미가 형식적이어서 다른 말 아래에 기대어 쓰이는 명사. | (‘것’, ‘따름’, ‘뿐’, ‘데’) |
|NNBC|  단위를 나타내는 명사 | |(‘미터’, ‘되’, ‘리터’)|
|NR|	수사        | 사물의 수량이나 순서를 나타내는 품사.| (‘하나’, ‘둘’)|
|NP|	대명사      |  사람이나 사물의 이름을 대신 나타내는 말.| (‘우리’, ‘너희’, ‘무엇’, ‘그것’)|
|VV|	동사        | 사물의 동작이나 작용을 나타내는 품사.||
|VA|	형용사      | 사물의 성질이나 상태를 나타내는 품사.||
|VX|	보조 용언   | 본용언과 연결되어 그것의 뜻을 보충하는 역할을 하는 용언. |(‘가지고 싶다’의 ‘싶다’, ‘먹어 보다’의 ‘보다’)|
|VCP|	긍정 지정사 | 무엇이 무엇이라고 지정하는 단어. |(긍정의 ‘이다’)|
|VCN|	부정 지정사 | 상동| (부정의 ‘아니다’)|
|MM|	관형사      | 체언 앞에 놓여서, 그 체언의 내용을 자세히 꾸며 주는 품사.| (‘순 살코기’의 ‘순’, ‘저 어린이’의 ‘저’)|
|MAG|	일반 부사   | 용언 또는 다른 말 앞에 놓여 그 뜻을 분명하게 하는 품사. |(‘매우’, ‘가장’, ‘과연’)|
|MAJ|	접속 부사   | 상동 |(‘그리고’)|
|IC|	감탄사      | 말하는 이의 본능적인 놀람이나 느낌, 부름, 응답 따위를 나타내는 말의 부류이다.||
|JKS|	주격 조사   | 문장 안에서, 체언이나 체언 구실을 하는 말 뒤에 붙어 주어의 자격을 가지게 하는 격 조사. |(‘이/가’, ‘께서’, ‘에서’)|
|JKC|	보격 조사   | 문장 안에서, 체언이나 체언 구실을 하는 말 뒤에 붙어 보어 자격을 가지게 하는 격 조사. |(‘철수는 위대한 학자가 되었다.’에서의 ‘가’)|
|JKG|	관형격 조사 | 문장 안에서, 앞에 오는 체언이나 체언 구실을 하는 말이 뒤에 오는 체언이나 체언 구실을 하는 말의 관형어임을 보이는 조사. |(‘의’)|
|JKO|	목적격 조사 | 문장 안에서, 체언이나 체언 구실을 하는 말 뒤에 붙어 목적어 자격을 가지게 하는 격 조사. |(‘을/를’)|
|JKB|	부사격 조사 | 문장 안에서, 체언이나 체언 구실을 하는 말 뒤에 붙어 부사어 자격을 가지게 하는 격 조사. |(‘에’, ‘에서’)|
|JKV|	호격 조사   | 문장 안에서, 체언이나 체언 구실을 하는 말 뒤에 붙어 독립어 자격을 가지게 하는 격 조사.| (‘영숙아’의 ‘아’, ‘철수야’의 ‘야’)|
|JKQ|	인용격 조사 | 앞의 말이 인용됨을 나타내는 조사.|(“‘언제 오겠니?’라고 물었다.”의 ‘라고’, ‘그는 내일 온다고 말했다.’의 ‘고’)|
|JX|	보조사      | 체언, 부사, 활용 어미 따위에 붙어서 어떤 특별한 의미를 더해 주는 조사. |(‘은’, ‘는’, ‘도’, ‘만’)|
|JC|	접속 조사   | 둘 이상의 단어나 구 따위를 같은 자격으로 이어 주는 구실을 하는 조사. |(‘와’, ‘과’, ‘하고’, ‘(이)나’)|
|EP|	선어말 어미 | 어말 어미 앞에 나타나는 어미. |(‘-시-’, ‘-옵-’, ‘-았-’, ‘-는-’)|
|EF|	종결 어미   | 한 문장을 종결되게 하는 어말 어미 |(‘-다’, ‘-네’)|
|EC|	연결 어미   | 어간에 붙어 다음 말에 연결하는 구실을 하는 어미. |(‘-게’, ‘-고’, ‘-(으)며’, ‘-(으)면’)|
|ETN|	명사형 전성 어미    | 용언의 어간에 붙어 다른 품사의 기능을 수행하게 하는 어미. |(‘-기’ㆍ‘-(으)ㅁ’, ‘-ㄴ’ㆍ‘-ㄹ’, ‘-게’ㆍ‘-도록’)|
|ETM|	관형형 전성 어미    | 상동 |(상동)|
|XPN|	체언 접두사 | 파생어를 만드는 접사로, 어근이나 단어의 앞에 붙어 새로운 단어가 되게 하는 말. |(‘맨손’의 ‘맨-’, ‘들볶다’의 ‘들-’)|
|XSN|	명사 파생 접미사    | 파생어를 만드는 접사로, 어근이나 단어의 뒤에 붙어 새로운 단어가 되게 하는 말. |(‘선생님’의 ‘-님’)|
|XSV|	동사 파생 접미사    | 상동 |(‘먹보’의 ‘-보’, ‘지우개’의 ‘-개’)|
|XSA|	형용사 파생 접미사  | 상동 |(‘먹히다’의 ‘-히-’)|
|XR|	어근 | 단어를 분석할 때, 실질적 의미를 나타내는 중심이 되는 부분. |(‘덮개’의 ‘덮-’, ‘어른스럽다’의 ‘어른’)|
|SF|	마침표, 물음표, 느낌표||. ? !|
|SE|	줄임표      ||…|
|SSO|	여는 괄호   ||( [|
|SSC|	닫는 괄호   ||) ]|
|SC|	구분자      ||, · / :|
|SY|	미정        |||
|SL|	외국어      ||
|SH|	한자        ||
|SN|	숫자        ||
