#!/usr/bin/python3

import requests
import json

# just a separator to keep stuff organized (not really '-')
separator = "--------------------------------------------------------------------------------------------------------------------"

base_domain = "https://api.noopschallenge.com"

# this holds the answers to the questions
question_list = ['test', 'python', 'nums', 'nums', 'nums', 'nums', 'nums', 'fuk']

def next_question(inf):
    nx_ques = (base_domain + inf)
    return(nx_ques)

def send_answer(url_dest, answer):
    body = json.dumps({'answer': answer})
    print(body)
    response = requests.post(url_dest, data = body.encode('utf8'),headers = {'Content-Type': 'application/json'})
    return response

def fizz_num(rules, nums):
    ans = ""
    for num in nums:
        if (num%rules[0]["number"] == 0) & (num%rules[1]["number"] == 0):
            ans += (str(rules[0]["response"]) + str(rules[1]["response"]) + " ")
        elif num%rules[0]["number"] == 0:
            ans += (str(rules[0]["response"]) + " ")
        elif num%rules[1]["number"] == 0:
            ans += (str(rules[1]["response"]) + " ")
        else:
            ans += (str(num) + " ")
    return ans.rstrip()

def fizz_num_fuk(rules, nums):
    ans = ""
    for num in nums:
        if (num%rules[0]["number"] == 0) & (num%rules[1]["number"] == 0) & (num%rules[2]["number"] == 0):
            ans += (str(rules[0]["response"]) + str(rules[1]["response"]) + str(rules[2]["response"]) + " ")
        elif (num%rules[0]["number"] == 0) & (num%rules[1]["number"] == 0):
            ans += (str(rules[0]["response"]) + str(rules[1]["response"]) + " ")
        elif (num%rules[1]["number"] == 0) & (num%rules[2]["number"] == 0):
            ans += (str(rules[1]["response"]) + str(rules[2]["response"]) + " ")
        elif (num%rules[0]["number"] == 0) & (num%rules[2]["number"] == 0):
            ans += (str(rules[0]["response"]) + str(rules[2]["response"]) + " ")
        elif num%rules[0]["number"] == 0:
            ans += (str(rules[0]["response"]) + " ")
        elif num%rules[1]["number"] == 0:
            ans += (str(rules[1]["response"]) + " ")
        elif num%rules[2]["number"] == 0:
            ans += (str(rules[2]["response"]) + " ")
        else:
            ans += (str(num) + " ")
    return ans.rstrip()

def main():

    dict_inf = "/fizzbot"
    for indicator in question_list:
        try:
            if indicator == "test":
                url = next_question(dict_inf)
                question = requests.get(url).json()
                print(question["message"])
                print("first done")
                print(separator)
                dict_inf = question["nextQuestion"]

            elif indicator == "python":
                url = next_question(dict_inf)
                print(url)
                question = requests.get(url).json()
                print(question)
                print(separator)
                response = send_answer(url, indicator)
                if response.status_code == 200:
                    print(response.json()["message"])
                    dict_inf = (response.json()["nextQuestion"])
                    print(separator + "\n")
                else:
                    print(response.status_code)
                    print("lulz m8")

            elif indicator == "nums":
                url = next_question(dict_inf)
                print(url)
                question = requests.get(url).json()
                print(question)
                print(separator)
                ans = fizz_num(question["rules"], question["numbers"])
                print(ans)
                response = send_answer(url, ans)
                if response.status_code == 200:
                    print(response.json()["message"])
                    dict_inf = (response.json()["nextQuestion"])
                    print(separator + "\n")
                else:
                    print(response.status_code)
                    print("lulz m8")

            elif indicator == "fuk":
                url = next_question(dict_inf)
                print(url)
                question = requests.get(url).json()
                print(question)
                print(separator)
                ans = fizz_num_fuk(question["rules"], question["numbers"])
                print(ans)
                response = send_answer(url, ans)
                if response.status_code == 200:
                    print(response.json()["message"])
                    dict_inf = (response.json()["nextQuestion"])
                    print(separator + "\n")
                else:
                    print(response.status_code)
                    print("lulz m8")

        except Exception as e:
            print(e)
            break


if __name__ == "__main__": main()
