logs = [ ["panther_candidate","login"],
 ["panther_candidate","session_extended"],
 ["panther_candidate","login"],
 ["panther_curtis","logout"],
 ["panther_candidate","logout"],
 ["panther_candidate","logout"],
 ["panther_curtis","logout"]]

def print_name(logs):
    user_lastaction_dict = {}
    for log_line in logs:
        user = log_line[0]
        action = log_line[1]
        if action != "login" and action != "logout":
            continue
        
        if user in user_lastaction_dict.keys():
            if user_lastaction_dict[user] == action:
                print(user)
        user_lastaction_dict[user] = action


print_name(logs)

# import csv
# log_file = csv.DictReader(open(“log.csv”))
# def print_suspicious_users(infile):
#     user_lastaction_dict = {}
#     for log_line in infile:
#         #added new variables here
#         user = log_line["user"]
#         action = log_line["action"]
	
#         #added a condition here
#         if action != "login" and action != "logout": 
#             continue
            
#         if user in user_lastaction_dict.keys():
#             if user_lastaction_dict[user] == action:
#                 print(user)
#         user_lastaction_dict[user] = action
