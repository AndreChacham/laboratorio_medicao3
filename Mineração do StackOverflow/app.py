from stackapi import StackAPI
import csv
import threading

def consultar_stackoverflow(issue):
    nameWithOwner = issue[0]
    numeroIssue = issue[1]
    state = issue[2]

    stack_api = StackAPI("stackoverflow")
    result = stack_api.fetch("search/advanced",
        title=numeroIssue,
        order="desc",
        sort="votes",
        pagesize=100,
        page=1
    )

    pesquisaStack = open("pesquisa_stack.csv", 'a', newline='', encoding="utf-8")
    pesquisa = csv.writer(pesquisaStack)
    pesquisa.writerow(str(result.question(count++))+ ";" + str(result.answer(count++)) + ",\n")
        

def main():

    issues = list()

    with open('issues.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            issues.append(row)

    i = 0
    total_issues = len(issues)
    rerun = list()
    
    pesquisaStack = open("pesquisa_stack.csv", 'a', newline='', encoding="utf-8")
    pesquisa = csv.writer(pesquisaStack)
    pesquisa.writerow(('NameWithOwner', 'Questions', 'Answers'))

    while i < total_issues and i < 250:
        threads = list()
        print(str(len(threads)))

        issue = issues[i]

        try:
            print(str(i) + '/' + str(total_issues))
            consultar_stackoverflow(issue)
            i += 1

        except Exception as e:
            rerun.append(issues[i])
            #print(str(e))


if __name__ == "__main__":
    main()
