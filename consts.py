WORKING_DAYS = ["pon", "wt", "sr", "czw", "pt"]  # for employee: excluded days
OFF_DAYS = [5, 6, 12, 13, 19, 20, 26, 27, 33, 34]  # Saturdays & Sundays for create_calendar, counting from 0
HOLIDAYS = {1: [1, 6], 2: [], 3: [], 4: [1], 5: [1, 3, 30], 6: [], 7: [], 8: [15], 9: [], 10: [],
            11: [1, 11], 12: [25, 26]}  # Polish holidays for create_calendar, counting from 1
