대회 일자 (05-08 참여 시작 - 05.22 종료)

[log]
[2023-05-08]  
- baseline 코드 pytorch_lightning code로 변환  
- data imbalance를 위한 class weight 적용
[2023-05-09]
- 여러 차례, 학습이 진행함에 따라 val_loss와 val_score가 함께 증가하는 현상 발생  
    => 클래스별 데이터 수량에 반비례하는 class weight 때문일수도  

- val loss가 가장 작은 초기 체크포인트가 val_score를 기준으로 뽑은 체크포인트보다 test score가 높음  
    => validation data distribution과 test data distribution이 다르다.  