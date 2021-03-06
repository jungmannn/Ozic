import numpy as np

#기업의 Label인 10x10 단위행렬 생성

D =np.eye(10)

#기업의 DATA

X = np.array(
    [
[
            [1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            #삼성전자
        ],
[
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 1, 1],
            [0, 1, 1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            #SK C&C
        ],
[
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            #대우중공업
        ],
[
            [0, 0, 1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0],
            # 유니클로
                ],
[
            [0, 0, 1, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 0, 0],
            [1, 1, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            #MBC
        ],
[
            [1, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 1],
            [0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            #에스체트
        ],
[
            [0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0],
            #한국전력공사
        ],
[
            [0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0],
            #루트토닉
        ],
[
            [0, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0],
            #투니버스
        ],
[
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 0, 0, 1, 0],
            #엑시콘
        ],

    ]
)
