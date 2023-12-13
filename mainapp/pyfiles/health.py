### 라이브러리
import glob
import pickle
import pandas as pd

class Pred_Model :
    def __init__(self) :
        self.temp = 0
    def runModel(self, height, weight, sex, area, systolic, diastolic, ast, alt,
                             blood_sugar, total_cholesterol, triglycerides,
                             hemoglobin, proteinuria, serum_creatinine, gamma_gtp) :
        

        files = glob.glob('mainapp/pyfiles/*.pickle')

        i = 1
        for file in files:
            with open(file,'rb') as f:
                globals()['model{}'.format(i)] = pickle.load(f)
            i += 1
            
        with open('mainapp/pyfiles/model_scaler.pickle', 'rb') as f: 
            scaler2 = pickle.load(f)
            

        result_bmi = weight / ((height/100)**2)
        result_map = (2*diastolic+systolic)/3
        result_aaa = float(ast/alt)
        
        col = ['bmi', 'map', '식전혈당(공복혈당)', '총 콜레스테롤', '트리글리세라이드',
            '혈색소', '요단백', '혈청크레아티닌', '감마 지티피']

        df1 = pd.DataFrame([result_bmi, result_map, blood_sugar, total_cholesterol,
                            triglycerides, hemoglobin, proteinuria, serum_creatinine, gamma_gtp]).transpose()
        df1.columns = col

        df1 = pd.DataFrame(scaler2.transform(df1), columns=col)

        col2 = ['시도코드', '성별코드', 'ast_alt2']

        df2 = pd.DataFrame([area, sex, result_aaa]).transpose()

        df2.columns = col2
        df2['ast_alt2'] = pd.to_numeric(df2['ast_alt2'], errors='coerce')
        df2 = df2.replace({'성별코드':{'남자':1, '여자':2},
            '시도코드':{'서울':11, '부산':26, '대구':27, '인천':28, '광주':29, '대전':30, '울산':31,
                    '경기':41, '강원':42, '충북':43, '충남':44, '전북':45, '전남':46, '경북':47, '경남':48,
                    '제주':49, '전국':99}})
        
        df = pd.concat([df1, df2], axis=1)
        
        
        list_result = []
        for j, kcd in zip(range(1,6), ['당뇨병', '고혈압', '감기', '기관지염', '경추간판장애']):
            a = globals()['model{}'.format(j)].predict_proba(df)[0][1]
            '{}이(가) 발병할 확률은 {:.3f}%입니다 '.format(kcd, a*100)
            list_result.append('{}이(가) 발병할 확률은 {:.3f}%입니다 '.format(kcd, a*100))
            
        return list_result