from stackapi import StackAPI
import csv
import threading

def consultar_stackoverflow(issue):
    nameWithOwner = issue[0]
    numeroIssue = issue[1]
    state = issue[2]

    print(nameWithOwner)
    print(numeroIssue)
    print(state)

    stack_api = StackAPI("stackoverflow")
    result = stack_api.fetch("search/advanced",
        title=numeroIssue,
        order="desc",
        sort="votes",
        pagesize=100,
        page=1
    )

    print(str(result))


def main():

    listaDeRespostas = []
    issues = list()

    with open('issues.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            issues.append(row)

    i = 0
    total_issues = len(issues)
    rerun = list()
    maximo_threads = 5

    while i < total_issues:
        threads = list()
        print(str(len(threads)))

        while len(threads) < maximo_threads:
            issue = issues[i]

            try:
                print(str(i) + '/' + str(total_issues))
                x = threading.Thread(target=consultar_stackoverflow, args=(issue,))
                threads.append(x)
                x.start()
                i += 1

            except Exception as e:
                rerun.append(issues[i])
                #print(str(e))


    for issue in rerun:
        consultar_stackoverflow(issue)


if __name__ == "__main__":
    main()