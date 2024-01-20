from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel

class GDSC(BaseModel):
    num: int  # 기수
    part: str  # 파트
    height: Union[int, float]  # 키, Union -> int와 float 둘다 가능
    birth_date: Optional[datetime] = None  # 생일, 디폴트는 None
    interest_list: List[str] = []  # 관심 있는 것, 리스트 요소 속성은 문자열, 디폴트는 []

gdsc_member_data = {
    'num': 2,  # Corrected to integer
    'part': 'AI/ML',
    'height': 178.0,  # Corrected to float
    'birth_date': None,
    'interest_list': [3, 'server/cloud', 'web/mobile']  
}

gdsc_member = GDSC(**gdsc_member_data)
print(gdsc_member)


