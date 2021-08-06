
from re import split, sub
from main import db
from main.model.user_complete import UserComplete
from main.model.user import User
from main import cur

query_cols = 'subject_id, 과목명, 학과, 강의계획서, 학점, 요일, 시작시간, 종료시간, 강의실, 교수진, 수강대상, 과목_설명, 비고, 대면여부, 강의언어'
zip_cols = (
  'subject_id',
  '과목명',
  '학과',
  '강의계획서',
  '학점',
  '요일',
  '시작시간',
  '종료시간',
  '강의실',
  '교수진',
  '수강대상',
  '과목설명',
  '비고',
  '대면여부',
  '강의언어'
)
def get_subjects(user_email):
    # Join table에서 해당 유저의 모든 즐겨찾기 과목 검색
    user = UserComplete.query.filter_by(email=user_email).all()
    if user:
        # 배열로 먼저 가져온 다음 순차적으로 하나씩 뽑아서 response 완성하자
        res = []
        sub_code = []
        for i in user:
            
            # 어떤 table에서 뽑을 건지 결정
            splitdata = i.subject_id.split('-')
            sub_code.append(splitdata[2])
            target_table = 's' + splitdata[0] + '_' + splitdata[1]
            # 테이블에서 해당 id 조회
            cur.execute("SELECT {} FROM {} WHERE subject_id = '{}'".format(query_cols, target_table, i.subject_id))
            # 리턴 오브젝트에 추가 후 한번에 리턴
            for elem in cur:
                res.append(dict(zip(zip_cols, elem)))        
        response_object = {
            'status': 'success',
            'message': '해당 유저의 즐겨찾기 목록 조회 완료',
            'data':res,
            'subject_code': sub_code
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'success',
            'message': '즐겨찾기에 아직 아무것도 등록 안됨'
        }
        return response_object, 201

def add_subjects(user_email, data):
    # Join table에 해당 유저의 id + subject_id로 추가
    # 존재하는 유저인지 검증
    user = User.query.filter_by(email=user_email).first()
    
    if user:
        new_favorite = UserComplete(
            email = user_email,
            subject_id = data['sub_id']
        )
        save_changes(new_favorite)
        response_object = {
            'status': 'success',
            'message': '즐겨찾기에 추가, 혹은 업데이트 되었습니다.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': '등록된 사용자가 아닙니다.'
        }
        return response_object, 201

def del_subjects(user_email,data):
    # Join table에서 해당 유저의 해당 즐겨찾기 과목 전체 삭제
    #user = UserComplete.query.filter_by(email=user_email).all()
    user = db.session.query(UserComplete).filter(UserComplete.email == user_email,UserComplete.subject_id == data['sub_id']).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        db.session.close()
        response_object = {
            'status': 'success',
            'message': '해당 과목을 수강완료한 등록에서 삭제했습니다.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': '수강완료한 과목이 없습니다.'
        }
        return response_object

def save_changes(data):
    db.session.add(data)
    db.session.commit()
    db.session.close()