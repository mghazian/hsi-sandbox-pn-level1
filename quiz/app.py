import json
import os
import random

class Choice(object):
    def __init__(self, content):
        self.content = content

    def __hash__(self):
        return hash(self.content)

    def __eq__(self, __o):
        return self.__hash__() == __o.__hash__()

    def format(self, id, is_chosen = False, is_correct = False):
        marker = ""
        if is_chosen and is_correct:
            marker = "(Jawaban anda benar)"
        elif is_chosen and not is_correct:
            marker = "(Jawaban anda)"
        elif is_correct:
            marker = "(Jawaban benar)"
        else:
            marker = ""
        
        return (
            (">> " if is_chosen else "   ") +
            f"[{id}] {self.content} " +
            marker)

class Question(object):
    def __init__(self, query, choices, correct_index):
        self.query = query
        self.choices = list(map(lambda query: Choice(query), choices))
        self.choices_count = len(choices)
        self._correct_answer = self.choices[correct_index]

    def check(self, selected_choice):
        return self._correct_answer == selected_choice

    def shuffle_choice(self):
        random.shuffle(self.choices)

    def present(self):
        print(f"{self.query}")
        for i in range(self.choices_count):
            choice = self.choices[i]
            print(choice.format(i + 1))
        print("")

    def explain(self, answer):
        print(f"{self.query}")
        for i in range(self.choices_count):
            choice = self.choices[i]
            print(choice.format(i + 1, choice == answer, self.check(choice)))
        print("")

class QuizApp(object):
    def __init__(self, filename = None):
        self._questions = []
        self.title = ""
        self.chapter = ""
        self.no = 0

        if filename != None:
            self.load(filename)

    def load(self, filename):
        with open(filename, 'r') as exam:
            exam_json = json.load(exam)

            self.title = exam_json['title']
            self.chapter = exam_json['chapter']
            self.no = exam_json['no']

            self._questions = list(map(lambda entry: Question(entry['query'], entry['choices'], entry['answer']), exam_json['questions']))

    def _select_question(self, quantity):
        return list(map(lambda question: { 'question': question, 'idx_answer': None }, random.sample(self._questions, quantity)))

    def _receive_answer(self):
        try:
            return int(input("Jawaban anda >>> "))
        except ValueError:
            return -1

    def _ask(self, question):
        question.shuffle_choice()
        question.present()

        answer = self._receive_answer()
        # We use 1-based index here to make it human readable
        while answer - 1 < 0 or answer > question.choices_count:
            print(f"Jawaban harus ada di rentang [1-{question.choices_count}]")
            answer = self._receive_answer()
            
        return answer - 1

    def start(self, quantity):
        current_attempt = self._select_question(quantity)

        print(f"Evaluasi Harian #{self.no} {self.chapter} - {self.title}")
        input("Tekan [ENTER] apabila anda siap untuk mengerjakan ujian dengan jujur >>> ")

        score = 0
        for i in range(len(current_attempt)):
            entry = current_attempt[i]
            print("")
            print(f"[Soal {i + 1}]")
            entry['idx_answer'] = self._ask(entry['question'])
            score += int(entry['question'].check(entry['question'].choices[entry['idx_answer']]))

        print("")
        print("-------------------------------------------------")
        print("Pengerjaan evaluasi telah berakhir")
        print(f"Anda menjawab benar sebanyak {score} dari {len(current_attempt)} pertanyaan")

        print("")
        print("+--------------+")
        print("|  PEMBAHASAN  |")
        print("+--------------+")

        for i in range(len(current_attempt)):
            entry = current_attempt[i]
            print(f"[Soal {i + 1}]")
            entry['question'].explain(entry['question'].choices[entry['idx_answer']])

QuizApp(os.path.dirname(__file__) + '/questions.json').start(2)