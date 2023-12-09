from django.shortcuts import render
from django.http import HttpResponse
from .completion_executor import CompletionExecutor
import json
import markdown
    
def diagnosis_detail(request):
    response_data = "안녕"
    user_input = "안녕"
 
    completion_executor = CompletionExecutor(
        host='https://clovastudio.stream.ntruss.com',
        api_key='NTA0MjU2MWZlZTcxNDJiY5QzHQ6hbf+RlqukhkrE6MKyQBBLMLCWc8Dw9GD3KZmZb9s7nF1fFxZ3cskKuLH1huEKzoyK1M82nxb0jZzfRvOQuhTN/JcyrWagDZn7QUTgYlZ0aFzlLnzpdpogGtOPy+BlOj3UHkqhipd6YKL3VRSgt+c07DYnStBs3zUGtpscJ7L3c7JIU1x96D8XEp30oonw9EsEfqtYLki1ylo6ptg=',
        api_key_primary_val='5DjAyKwmAOSewiiNVGRUTqPWtY5R9M9RMpvTCBJo',
        request_id='26b306daefad43b88b2a99c2369abc75'
    )
    
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        preset_text = [
            {"role": "system", "content": "너는 친절하고 똑똑한 의사야. 사용자가 증상을 입력하면 너는 증상과 관련되어 가장 자주 발생하는 질병 몇 가지를 설명해줘. 마지막으로는 관련 진료과도 알려줘."},
            {"role": "user", "content": user_input}
        ]

        request_data = {
            'messages': preset_text,
            'topP': 0.8,
            'topK': 0,
            'maxTokens': 500,
            'temperature': 0.5,
            'repeatPenalty': 5.0,
            'stopBefore': [],
            'includeAiFilters': True
        }

        response_data = json.loads(completion_executor.execute(request_data)[-4][5:])['message']['content']
        response_data = markdown.markdown(response_data)
 
    return render(request, 
                  "mainapp/diagnosis_detail.html",
                  {"response_data":response_data,
                   "user_input":user_input})
    
def diagnosis(request):

    return render(request, 
                  "mainapp/diagnosis.html",
                  {})

# 메인 페이지
def main(request):
    return render(request,
                  "mainapp/main.html",
                  {})