'''https://leetcode.com/problems/create-a-dataframe-from-list/submissions/1386035811/'''
#Try 1
import pandas as pd
from typing import List  # <- missing import

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=["student_id", "age"])
    return df  # <- fixed typo
