import pymysql
import streamlit as st

# 세션 상태를 가져오는 함수 정의
def get_session_state():
    return st.session_state

# 세션 상태를 저장하는 함수 정의
def set_session_state(session_state):
    st.session_state = session_state

# 초기 세션 상태 설정
if "a_counter" not in get_session_state():
    set_session_state({"a_counter": 1})

# Design
# 버튼 클릭

st.title('유비온 최종프로젝트 설문조사(title)')
st.header('유비온 최종프로젝트 설문조사(header)')
st.subheader('유비온 최종프로젝트 설문조사(subheader)')

col1, col2, col3 = st.sidebar.columns([1,8,1])
with col1:
    st.write("")
with col2:
    st.image('/오뚜기CI.png',  use_column_width=True)
with col3:
    st.write("")

st.sidebar.markdown(" ## About Research")
st.sidebar.markdown("안녕하세요. 귀중한 시간을 내어 연구에 참여해주신 것을 감사드립니다."  )              
st.sidebar.markdown("본 설문은 오뚜기 '헬로베지' 신제품 개발을 위한 설문으로 수집된 자료는 연구의 자료로만 사용되며 그 외의 목적으로 사용되지 않을 것입니다.")
st.sidebar.markdown("설문은 평소 비건 간편식에 관한 질문으로 각 문항의 답은 맞고 틀리는 것이 없으며, 모든 설문지는 개별적으로 공개되는 일이 없이 참여자의 정보는 코드화하여 기록됩니다.")
st.sidebar.markdown("  소요시간은 약 5분으로 귀하께서 응답하신 의견은 본 연구의 귀중한 자료로서 활용된다는 점을 생각하시어 아래의 문항에 빠짐없이 진지하고 솔직하게 응답하여 주시기 부탁드립니다.")
st.sidebar.markdown(" 설문 참여를 원하시는 경우에만 설문을 시작해주시기 바라며, 본 연구에 참여해주신 귀하께 다시 한 번 진심으로 감사드립니다. 유빅마 2기 2조.")
st.sidebar.info("설문참여를 원하지 않는 분들은 설문을 종료해주세요.", icon="ℹ️")


name = st.text_input("**귀하의 이름을 입력해주세요.**")

no_1 = st.radio(
    '**귀하는 비건 간편식을 1주일에 몇번 섭취하십니까?**',
    ('주1회', '주2회', '주3회 이상', '먹지않는다'))

button = st.button('설문 제출')

if button:
    conn = pymysql.connect(host='localhost', user='root', password='1111', db='research', charset='utf8')
    cur = conn.cursor()
    
    st.write(name)

    # 'a_counter' 값을 가져옵니다.
    # a_counter = get_session_state().get("a_counter", 1)

    #cur.execute("INSERT INTO test VALUES(1, {0})".format(name))
    cur.execute("SELECT count(*) FROM test")
    row = cur.fetchone()
    cur.execute(f"INSERT INTO test VALUES({row[0]+1}, '{name}', '{no_1}')")
    
    conn.commit()
    conn.close()

    # 'a_counter'를 1 증가시킵니다.
    # set_session_state({"a_counter": a_counter + 1})

    st.write('참여해주셔서 감사합니다. 설문이 :blue[정상적으로]저장되었습니다.:white_check_mark:')
