## Stack
- Stack is a linear data structure that follows the Last In First Out (LIFO) principle. It means that the last element added to the stack will be the first one to be removed.
- The basic operations of a stack are:
  - **Push**: Add an element to the top of the stack.
  - **Pop**: Remove the top element from the stack.
  - **Peek/Top**: Retrieve the top element without removing it.
- Stacks can be implemented using arrays or linked lists.   


Session Overview
This session covered stacks from the ground up, starting with LIFO behavior and basic Python operations, then moving into classic stack problems such as valid parentheses, asteroid collision, next greater/smaller element patterns, daily temperatures, and stock span.
A recurring theme was that many interview questions are really the same monotonic stack idea with small changes in direction or comparison rule.
You also saw how to think about collisions, nested brackets, and “nearest” answers using the top of the stack as the key reference point.

Stack Basics
A stack is a linear data structure that follows LIFO:

Last In, First Out

That means the most recently added item is the first one removed. The mental model used was a pile of plates: you add to the top and remove from the top, and you can directly access only the top element.

For example, if you push 10, 20, 30, 40 in that order, the stack is:

bottom -> 10, 20, 30, 40 <- top
If you remove once, 40 comes out first; remove again, 30 comes out next.

In Python, a list can behave like a stack:

st = []
st.append(10)
st.append(20)
st.append(30)
st.append(40)
To inspect the top without removing it, use st[-1]. To remove and return the top, use pop(). To check the current size, use len(st).

print(st[-1])   # top element, e.g. 40
print(st.pop()) # removes and returns top, e.g. 40
print(len(st))
Key insight: st[-1] only reads the top element, while st.pop() removes it and shrinks the stack by one.

Think of a stack as “the most recent thing is the next thing you deal with.”

Key takeaway: A stack is a LIFO structure where push, peek, and pop all happen at the top.

Valid Parentheses / Bracket Matching
A classic stack problem is checking whether a bracket string is valid, such as strings made from (), {}, and []. A string is valid when every opening bracket is matched by the same type of closing bracket, in the correct nesting order.

The key rules are:

Every opening bracket must be closed by the same type.
Brackets must close in the correct order.
Every closing bracket must have a prior opening bracket.
Examples:

(] is invalid because the types do not match.
([)] is invalid because the order is wrong.
] is invalid because a closing bracket appears with nothing to match.
The closing bracket is the “problematic” one: an opening bracket is never rejected immediately, it only becomes a problem if the later closing bracket does not match.

The algorithm is straightforward:

If the current character is an opening bracket, push it.
If it is a closing bracket:
if the stack is empty, return false
compare it with the top of the stack
if they match, pop
otherwise return false
After the scan, return true only if the stack is empty
A small worked example:

() → push (, then see ) and pop → stack empty → valid
([]) → push (, push [, then ] pops [, then ) pops ( → valid
([)] → ) meets [ on top, so it fails immediately
Watch out: Do not return true just because the loop ended. Leftover opening brackets still make the string invalid.

Key insight: Validity depends on both type matching and proper nesting, which is exactly what the stack captures.

Key takeaway: Push openings, match closings against the stack top, and only accept if the stack is empty at the end.

Asteroid Collision
The asteroid collision problem uses numbers as moving objects:

positive = moving right
negative = moving left
A collision can only happen in the positive followed by negative case. Same-direction pairs do not collide, and negative followed by positive move away from each other.

Key insight: The only dangerous case is a right-moving object already on the stack, followed by a left-moving object arriving later.

The stack holds the survivors seen so far. For each new value:

If it is positive, push it.
If it is negative, compare it with the stack top while a collision is possible:
keep popping smaller positive values
if the stack becomes empty, push the negative value
if a larger positive remains, the negative is destroyed
if magnitudes are equal, both disappear
Equal magnitude means both are removed, not kept.

Worked examples:

[5, 10, -5] → 10 survives the encounter with -5, so the result keeps the surviving right movers.
[8, -8] → both are destroyed, leaving an empty array.
[3, 5, -6, 2, -1, 4] → the negative -6 can destroy multiple smaller positives before surviving or being destroyed; the final outcome discussed was [-6, 2, 4].
Key insight: A single incoming negative asteroid may trigger a whole chain of pops before the final decision is made.

Watch out: Collision logic only runs when the incoming asteroid is negative and the stack top is positive.

Key takeaway: Simulate collisions with a stack, repeatedly resolving the incoming negative asteroid against previous positive survivors.

Monotonic Stack for Nearest Greater/Smaller Problems
A major pattern in the session was the monotonic stack: keep popping elements that are no longer useful, then use the top of the stack as the answer for the current element, and finally push the current element for future queries.

This pattern appears in questions like:

Next Greater on Right (NGOR)
Next Smaller on Right (NSOR)
Next Greater on Left (NGOL)
Next Smaller on Left (NSOL)
Key insight: The stack stores potential answers for future elements, not just the current “best” value.

For NGOR, you typically traverse from right to left:

pop while the stack top is smaller than or equal to the current value
if the stack is empty, answer is -1
otherwise the stack top is the nearest greater element
push the current element
For NSOR, the comparison flips:

pop while the stack top is greater than or equal to the current value
then the top, if any, is the nearest smaller element
For the left-side variants:

traverse left to right
apply the same greater/smaller comparison logic, but now the answers come from what you have already seen on the left
A useful way to think about it is:

right-side queries are often easiest by scanning right to left
left-side queries are often easiest by scanning left to right
Choose the traversal direction so that the answer is already available when you process each element.

Watch out: Off-by-one errors in the loop bounds are common, especially when traversing from right to left.

Key takeaway: Most next-greater/smaller problems differ only by direction and by the comparison used in the pop condition.

Daily Temperatures
Daily Temperatures asks: for each day, how many days until a warmer temperature appears in the future? If no warmer day exists, the answer is 0.

The key is that this is really a Next Greater on Right problem, except you return the distance in indices rather than the value itself.

Example reasoning:

73 → next warmer is 74, so wait 1 day
74 → next warmer is 75, so wait 1 day
75 → next warmer is 76, so wait 4 days
76 → no warmer future day, so 0
The method:

Find the next greater index to the right for each day.
Subtract the current index to get the waiting time.
If none exists, store 0.
Key insight: Daily Temperatures is just NGOR with index differences.

Key takeaway: Use a monotonic stack to find the next warmer day, then convert that into days waited by subtracting indices.

Stock Span
Stock Span is the mirror-image style problem: for each day, count how many consecutive previous days including today have prices less than or equal to today’s price.

Unlike Daily Temperatures, this looks backward rather than forward. The span is not “all earlier smaller values”; it is the consecutive block immediately ending at today.

Examples discussed:

100 → span 1
80 → span 1
19 → span 2 if the immediate prior days are smaller and consecutive
10, 4, 5, 90, 120, 80 → the span grows when consecutive smaller prices continue, and stops as soon as a larger prior price blocks the chain
Key insight: Stock span stops at the first previous day with a higher price.

Watch out: Do not count non-consecutive smaller values across a blocking larger price; the span must be consecutive.

Key takeaway: Stock span is a backward-looking monotonic stack problem that counts consecutive smaller-or-equal prices until a larger value blocks you.

Quick Reference
Stack = LIFO

push/add: append()
peek top: st[-1]
pop top: pop()
size: len(st)
Valid Parentheses

push opening brackets
on closing bracket:
if stack empty → invalid
if top mismatch → invalid
else pop
valid only if stack empty at the end
Asteroid Collision

positive → push
negative → repeatedly compare with positive stack top
pop smaller positives
equal magnitudes → both removed
push negative only if it survives
Monotonic Stack Pattern

pop elements that cannot help the current answer
answer is usually the current stack top
push the current element afterward
NGOR / NSOR / NGOL / NSOL

change only:
traversal direction
pop comparison (greater vs smaller)
Daily Temperatures

NGOR + index difference
no warmer future day → 0
Stock Span

look left
count consecutive previous days with price <= current
stop at first previous higher price
