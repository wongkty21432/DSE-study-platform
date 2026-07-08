#!/usr/bin/env python3
"""Add refined programming questions for Topics 6 & 7"""
import json

path = "questions-ict.json"
with open(path, 'r', encoding='utf-8') as f:
    questions = json.load(f)

t6 = [q for q in questions if q['topic'] == 6]
t7 = [q for q in questions if q['topic'] == 7]
print(f"Topic 6: {len(t6)} | Topic 7: {len(t7)} | Total: {len(questions)}")

new_qs = [
    # ===== TOPIC 6: 計算思維與程式編寫 (一) =====
    {
        "qid": "ICT-067", "topic": 6, "year": 2023, "qnum": 28, "sourceType": "mc", "sourcePaper": "卷一", "difficulty": "medium",
        "question": "以下偽代碼執行後，變量result的值是多少？\nresult = 1\nfor i = 1 to 4\n  result = result * i\nnext i",
        "options": ["A. 10", "B. 24", "C. 120", "D. 4"], "answer": 1,
        "explanation": "追蹤偽代碼：i=1: result=1x1=1; i=2: result=1x2=2; i=3: result=2x3=6; i=4: result=6x4=24。這計算的是4的階乘(4! = 4x3x2x1 = 24)。注意result初始值為1（不是0，否則乘法結果永遠為0）。",
        "markingNotes": "1分：B (24)。偽代碼計算4的階乘：1x1x2x3x4=24。需正確追蹤變量變化。",
        "question_en": "After executing the following pseudocode, what is the value of result?\nresult = 1\nfor i = 1 to 4\n  result = result * i\nnext i",
        "options_en": ["A. 10", "B. 24", "C. 120", "D. 4"],
        "explanation_en": "Trace: i=1: result=1; i=2: result=2; i=3: result=6; i=4: result=24. This calculates 4! = 24. Note result starts at 1 (if 0, product always 0).",
        "markingNotes_en": "1 mark: B (24). Computes 4! = 1x1x2x3x4 = 24."
    },
    {
        "qid": "ICT-068", "topic": 6, "year": 2022, "qnum": 22, "sourceType": "mc", "sourcePaper": "卷一", "difficulty": "hard",
        "question": "以下偽代碼中，若輸入n=5，輸出是什麼？\n輸入 n\na = 0\nb = 1\nFOR i = 1 TO n\n  輸出 a\n  temp = a + b\n  a = b\n  b = temp\nNEXT i",
        "options": ["A. 1, 2, 3, 5, 8", "B. 0, 1, 1, 2, 3", "C. 1, 1, 2, 3, 5", "D. 0, 1, 2, 3, 5"], "answer": 1,
        "explanation": "這是費波那契數列(Fibonacci)的生成程式。追蹤：i=1: 輸出a=0, temp=0+1=1, a=1, b=1; i=2: 輸出a=1, temp=1+1=2, a=1, b=2; i=3: 輸出a=1, temp=1+2=3, a=2, b=3; i=4: 輸出a=2, temp=2+3=5, a=3, b=5; i=5: 輸出a=3。序列：0, 1, 1, 2, 3。注意先輸出a再更新值。",
        "markingNotes": "1分：B (0,1,1,2,3)。Fibonacci數列前5項，a=0,b=1起始。需逐行追蹤變量。",
        "question_en": "In the pseudocode, if n=5, what is output?\nINPUT n\na = 0\nb = 1\nFOR i = 1 TO n\n  OUTPUT a\n  temp = a + b\n  a = b\n  b = temp\nNEXT i",
        "options_en": ["A. 1, 2, 3, 5, 8", "B. 0, 1, 1, 2, 3", "C. 1, 1, 2, 3, 5", "D. 0, 1, 2, 3, 5"],
        "explanation_en": "Fibonacci generator. Trace: outputs 0, 1, 1, 2, 3. Outputs a BEFORE updating values each iteration.",
        "markingNotes_en": "1 mark: B. First 5 Fibonacci numbers with a=0, b=1."
    },
    {
        "qid": "ICT-069", "topic": 6, "year": 2021, "qnum": 16, "sourceType": "mc", "sourcePaper": "卷一", "difficulty": "medium",
        "question": "在Python中，range(2, 8, 2) 會產生哪些數字？",
        "options": ["A. 2, 4, 6, 8", "B. 2, 3, 4, 5, 6, 7", "C. 2, 4, 6", "D. 2, 3, 4, 5, 6, 7, 8"], "answer": 2,
        "explanation": "range(start, stop, step)：從start開始（包含），每次增加step，在stop之前結束（不包含stop）。range(2,8,2) → 2,4,6。8不包含。等價偽代碼：FOR i=2 TO 7 STEP 2。",
        "markingNotes": "1分：C (2,4,6)。range(2,8,2)=2,4,6。stop值(8)不包含。",
        "question_en": "In Python, what numbers does range(2, 8, 2) produce?",
        "options_en": ["A. 2, 4, 6, 8", "B. 2, 3, 4, 5, 6, 7", "C. 2, 4, 6", "D. 2, 3, 4, 5, 6, 7, 8"],
        "explanation_en": "range(start, stop, step): starts at start (inclusive), increments by step, stops before stop (exclusive). range(2,8,2) produces 2,4,6.",
        "markingNotes_en": "1 mark: C (2,4,6). stop value (8) is exclusive."
    },
    {
        "qid": "ICT-070", "topic": 6, "year": 2020, "qnum": 23, "sourceType": "mc", "sourcePaper": "卷一", "difficulty": "hard",
        "question": "以下偽代碼是要計算1到N之間所有奇數的和。哪一行有邏輯錯誤？\n1. 輸入 N\n2. sum = 0\n3. FOR i = 1 TO N\n4.   IF i % 2 = 1 THEN\n5.     sum = sum + i\n6.   ENDIF\n7. NEXT i\n8. 輸出 sum",
        "options": ["A. 第2行", "B. 第3行", "C. 第4行", "D. 沒有錯誤"], "answer": 3,
        "explanation": "此偽代碼沒有邏輯錯誤。i%2=1正確判斷奇數（除以2餘1）。sum初始化為0，遍歷1到N，累加所有滿足i%2=1的i值。常見陷阱：誤認i%2==0為奇數——但i%2==0是偶數。%是取餘數(mod)運算符。",
        "markingNotes": "1分：D。程式無錯誤。i%2=1正確識別奇數。理解%為取餘數運算。",
        "question_en": "The pseudocode sums odd numbers 1 to N. Which line has a logic error?\n1. INPUT N\n2. sum = 0\n3. FOR i = 1 TO N\n4.   IF i % 2 = 1 THEN\n5.     sum = sum + i\n6.   ENDIF\n7. NEXT i\n8. OUTPUT sum",
        "options_en": ["A. Line 2", "B. Line 3", "C. Line 4", "D. No error"],
        "explanation_en": "No logic error. i%2=1 correctly identifies odd numbers. % is the modulo operator.",
        "markingNotes_en": "1 mark: D. No error. i%2=1 correctly tests for odd numbers."
    },
    {
        "qid": "ICT-071", "topic": 6, "year": 2019, "qnum": 10, "sourceType": "mc", "sourcePaper": "卷一", "difficulty": "easy",
        "question": "在Python中，表達式 17 % 5 的結果是什麼？",
        "options": ["A. 3", "B. 2", "C. 3.4", "D. 5"], "answer": 1,
        "explanation": "% 是取餘數運算符(modulo)。17 / 5 = 3 餘 2，所以 17 % 5 = 2。區分：/ 返回浮點(17/5=3.4)，// 返回整數商(17//5=3)，% 返回餘數(17%5=2)。",
        "markingNotes": "1分：B (2)。17%5=2。%為取餘數(mod)運算。",
        "question_en": "In Python, what is 17 % 5?",
        "options_en": ["A. 3", "B. 2", "C. 3.4", "D. 5"],
        "explanation_en": "% is modulo. 17/5 = 3 remainder 2. / returns float (3.4), // returns integer quotient (3), % returns remainder (2).",
        "markingNotes_en": "1 mark: B (2). 17%5 = 2."
    },
    # ===== TOPIC 7: 計算思維與程式編寫 (二) =====
    {
        "qid": "ICT-072", "topic": 7, "year": 2023, "qnum": 33, "sourceType": "mc", "sourcePaper": "卷一", "difficulty": "medium",
        "question": "以下Python函數的功能是什麼？\ndef mystery(a, b):\n    if b == 0:\n        return a\n    else:\n        return mystery(b, a % b)",
        "options": ["A. 計算 a 的 b 次方", "B. 計算 a 和 b 的最大公因數 (GCD/HCF)", "C. 計算 a 和 b 的最小公倍數 (LCM)", "D. 比較 a 和 b 的大小"], "answer": 1,
        "explanation": "這是遞歸實現的歐幾里得算法(Euclidean Algorithm)，用於計算最大公因數(GCD/HCF)。原理：GCD(a,b) = GCD(b, a mod b)，當b=0時GCD為a。例：mystery(48,18)→mystery(18,12)→mystery(12,6)→mystery(6,0)→返回6（48和18的GCD=6）。",
        "markingNotes": "1分：B。歐幾里得算法的遞歸實現，計算最大公因數(HCF/GCD)。",
        "question_en": "What does this Python function do?\ndef mystery(a, b):\n    if b == 0:\n        return a\n    else:\n        return mystery(b, a % b)",
        "options_en": ["A. Calculates a to power b", "B. Calculates GCD/HCF of a and b", "C. Calculates LCM of a and b", "D. Compares a and b"],
        "explanation_en": "Recursive Euclidean Algorithm for GCD. Principle: GCD(a,b) = GCD(b, a mod b). When b=0, GCD = a. Example: mystery(48,18) returns 6.",
        "markingNotes_en": "1 mark: B. Recursive Euclidean Algorithm for HCF/GCD."
    },
    {
        "qid": "ICT-073", "topic": 7, "year": 2022, "qnum": 34, "sourceType": "mc", "sourcePaper": "卷一", "difficulty": "hard",
        "question": "以下程式對陣列 arr=[8,3,5,1,9,2] 執行後，arr的值是什麼？\nn = len(arr)\nfor i in range(n-1):\n  min_idx = i\n  for j in range(i+1, n):\n    if arr[j] < arr[min_idx]:\n      min_idx = j\n  arr[i], arr[min_idx] = arr[min_idx], arr[i]",
        "options": ["A. [9,8,5,3,2,1]", "B. [8,3,5,1,9,2]", "C. [1,2,3,5,8,9]", "D. [1,8,3,5,9,2]"], "answer": 2,
        "explanation": "這是選擇排序(Selection Sort)。每輪在未排序部分找最小值，與未排序的第一個元素交換。第1輪：找[8,3,5,1,9,2]最小=1(idx3)，交換arr[0]↔arr[3]→[1,3,5,8,9,2]；第2輪：找[3,5,8,9,2]最小=2(idx5)，交換→[1,2,5,8,9,3]；繼續→最終[1,2,3,5,8,9]。與冒泡排序不同，選擇排序每輪只交換一次。",
        "markingNotes": "1分：C [1,2,3,5,8,9]。選擇排序升序排列。需理解每輪找最小值並交換的過程。",
        "question_en": "After executing this code on arr=[8,3,5,1,9,2], what is arr?\nn = len(arr)\nfor i in range(n-1):\n  min_idx = i\n  for j in range(i+1, n):\n    if arr[j] < arr[min_idx]:\n      min_idx = j\n  arr[i], arr[min_idx] = arr[min_idx], arr[i]",
        "options_en": ["A. [9,8,5,3,2,1]", "B. [8,3,5,1,9,2]", "C. [1,2,3,5,8,9]", "D. [1,8,3,5,9,2]"],
        "explanation_en": "Selection Sort. Each round finds minimum in unsorted portion and swaps with first unsorted element. Final result: [1,2,3,5,8,9] (ascending).",
        "markingNotes_en": "1 mark: C. Selection Sort produces ascending order [1,2,3,5,8,9]."
    },
    {
        "qid": "ICT-074", "topic": 7, "year": 2021, "qnum": 35, "sourceType": "mc", "sourcePaper": "卷一", "difficulty": "hard",
        "question": "以下Python程式碼執行後會發生什麼？\ndef divide(a, b):\n    return a / b\n\ntry:\n    result = divide(10, 0)\n    print(result)\nexcept ZeroDivisionError:\n    print(\"錯誤：不能除以零\")",
        "options": ["A. 輸出 0", "B. 輸出 \"錯誤：不能除以零\"", "C. 程式崩潰並顯示錯誤", "D. 輸出 None"], "answer": 1,
        "explanation": "try-except用於異常處理。divide(10,0)引發ZeroDivisionError，except區塊捕獲異常，程式不崩潰。執行流程：divide(10,0)拋出異常→跳轉至except→輸出錯誤訊息。print(result)不會執行（異常發生在前）。",
        "markingNotes": "1分：B。try-except捕獲ZeroDivisionError，輸出錯誤訊息而不崩潰。理解異常處理概念。",
        "question_en": "What happens after executing this code?\ndef divide(a, b):\n    return a / b\ntry:\n    result = divide(10, 0)\n    print(result)\nexcept ZeroDivisionError:\n    print(\"Error: Cannot divide by zero\")",
        "options_en": ["A. Output 0", "B. Output error message", "C. Program crashes", "D. Output None"],
        "explanation_en": "try-except handles exceptions. divide(10,0) raises ZeroDivisionError, caught by except block. Program does not crash. Error message is printed.",
        "markingNotes_en": "1 mark: B. try-except catches ZeroDivisionError gracefully."
    },
    {
        "qid": "ICT-075", "topic": 7, "year": 2020, "qnum": 31, "sourceType": "mc", "sourcePaper": "卷一", "difficulty": "medium",
        "question": "以下關於程式測試中「邊界值分析」的描述，哪項是正確的？",
        "options": ["A. 隨機選擇測試數據", "B. 測試輸入範圍的邊界值（如最小值、最大值、剛超出範圍的值）", "C. 測試所有可能的輸入值", "D. 只測試正常值"], "answer": 1,
        "explanation": "邊界值分析(Boundary Value Analysis)是黑盒測試技術，重點測試輸入範圍邊界。例如程式接受1-100：測試0（低於下限）、1（下限）、100（上限）、101（高於上限）。錯誤常發生在邊界處。全面測試(C)不實際，隨機測試(A)無系統性。",
        "markingNotes": "1分：B。邊界值分析測試輸入範圍邊界，因錯誤常集中於此。",
        "question_en": "Which describes Boundary Value Analysis in testing?",
        "options_en": ["A. Randomly select test data", "B. Test boundary values of input ranges", "C. Test all possible input values", "D. Test only normal values"],
        "explanation_en": "Boundary Value Analysis tests edges of input ranges where errors commonly occur. Example for range 1-100: test 0, 1, 100, 101.",
        "markingNotes_en": "1 mark: B. Boundary testing focuses on edges of input ranges."
    },
    {
        "qid": "ICT-076", "topic": 7, "year": 2019, "qnum": 29, "sourceType": "mc", "sourcePaper": "卷一", "difficulty": "medium",
        "question": "在Python中，以下哪項關於 list (陣列) 的描述是正確的？",
        "options": ["A. list 中所有元素必須是同一數據類型", "B. list 的索引從 1 開始", "C. list 是可變的 (mutable)，可以修改其中的元素", "D. list 的長度在創建後不可改變"], "answer": 2,
        "explanation": "Python list是可變的(mutable)——可修改、添加、刪除元素（如arr[0]=10, arr.append(5), arr.pop()）。list可含不同類型(A錯——[1,'hello',True]合法），索引從0開始(B錯)，長度可動態改變(D錯——可用append/extend/pop）。",
        "markingNotes": "1分：C。Python list可變(mutable)，可修改元素、增刪項目。索引從0開始。",
        "question_en": "In Python, which statement about lists is correct?",
        "options_en": ["A. All elements must be same type", "B. Indices start from 1", "C. Lists are mutable", "D. Length fixed after creation"],
        "explanation_en": "Python lists are mutable — elements can be modified, added (append), removed (pop). Mixed types allowed, indices start at 0, length is dynamic.",
        "markingNotes_en": "1 mark: C. Python lists are mutable."
    },
]

# Add new questions
existing_ids = {q['qid'] for q in questions}
added = 0
for nq in new_qs:
    if nq['qid'] not in existing_ids:
        questions.append(nq)
        added += 1

with open(path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

t6_after = len([q for q in questions if q['topic'] == 6])
t7_after = len([q for q in questions if q['topic'] == 7])
print(f"Added {added} new questions")
print(f"Topic 6: {len(t6)} -> {t6_after}")
print(f"Topic 7: {len(t7)} -> {t7_after}")
print(f"Total: {len(questions)} questions")
