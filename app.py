# 나만의 프롬프트 관리기

# 기본 프롬프트 데이터 (이전 미션에서 작성한 프롬프트)
prompts = [
    {
        "title": "학습 MBTI 영상 씬 구성",
        "content": (
            "학습 MBTI로 5분 만에 아이의 학습 성향을 찾는 과정을 영상으로 구성한다. "
            "민준이는 감각형-순차형으로, 구체적이고 사실적인 내용을 단계적으로 학습할 때 이해가 빠르며 "
            "이리저리 넘나드는 수업 진행은 피해야 한다. "
            "민준이 동생은 직관형-총체형으로, 전체 흐름을 먼저 파악하고 개념을 연결·확장하며 학습하는 방식을 선호한다. "
            "각자 같은 성향의 코치를 만나 공부하는 모습을 보여주고, "
            "학습 결과가 2배 이상 좋아지는 변화를 돋보기 연출로 강조하는 씬을 넣는다."
        ),
        "category": "영상 생성",
        "favorite": False
    },
    {
        "title": "상담 접수 자동화 설계 (n8n·Make)",
        "content": (
            "n8n과 Make로 상담 접수 자동화를 두 개 구성한다. "
            "1부: 랜딩페이지에서 상담을 요청하면 이름, 학교, 학년, 이메일, 전화번호를 입력받아 "
            "구글 시트에 저장하고 Slack 알림으로 전달한다. "
            "2부: 알림을 확인한 뒤 트리거를 실행하면 학습스타일 검사 URL을 안내 문자로 발송하고, "
            "검사 완료 후 결과가 도착하면 결과지를 자동 발송한다."
        ),
        "category": "자동화",
        "favorite": False
    },
    {
        "title": "코치 강의형 앱 MVP 기획 + JTBD",
        "content": (
            "기존 앱과 달리 메인 화면이 '코치가 강의하는 화면'인 것이 핵심 차별점인 앱의 MVP를 기획한다. "
            "아직 덜 잡힌 세부 항목을 단계별로 어떻게 구체화할지 검토한다. "
            "또한 학부모, 학생, 코치 각 사용자가 앱에서 이루려는 목적을 고객 관점의 JTBD로 그려, "
            "가장 자연스러운 사용자 동선을 도출한다."
        ),
        "category": "페르소나",
        "favorite": False
    }
]
# 카테고리 목록 (여러 기능에서 공통으로 사용)
categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def add_prompt():
    """새 프롬프트를 입력받아 리스트에 추가한다."""
    print("\n=== 프롬프트 추가 ===")

    # 제목 입력 (비어 있으면 다시 요청)
    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목은 비워둘 수 없습니다. 다시 입력해주세요.")

    # 내용 입력 (비어 있으면 다시 요청)
    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용은 비워둘 수 없습니다. 다시 입력해주세요.")

    # 카테고리 선택
    print("\n카테고리 선택:")
    for i, name in enumerate(categories, start=1):
        print(f"{i}) {name}")

    while True:
        sel = input("선택: ").strip()
        if sel.isdigit() and 1 <= int(sel) <= len(categories):
            category = categories[int(sel) - 1]
            break
        print("목록에 있는 번호를 입력해주세요.")

    # 새 프롬프트를 딕셔너리로 만들어 리스트에 추가
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")


def show_list():
    """저장된 모든 프롬프트를 번호와 함께 출력한다."""
    print("\n=== 프롬프트 목록 ===")

    # 프롬프트가 하나도 없을 때
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 번호를 매겨 하나씩 출력
    for i, p in enumerate(prompts, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")

    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    """카테고리를 선택하면 해당 카테고리의 프롬프트만 출력한다."""
    print("\n=== 카테고리별 조회 ===")

    # 카테고리 목록을 번호와 함께 보여주기
    for i, name in enumerate(categories, start=1):
        print(f"{i}) {name}")

    # 카테고리 선택 받기
    while True:
        sel = input("선택: ").strip()
        if sel.isdigit() and 1 <= int(sel) <= len(categories):
            chosen = categories[int(sel) - 1]
            break
        print("목록에 있는 번호를 입력해주세요.")

    # 선택한 카테고리에 속한 프롬프트만 골라내기
    matched = [p for p in prompts if p["category"] == chosen]

    print(f"\n[{chosen}] 카테고리 프롬프트:")

    if not matched:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(matched, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star}")

    print(f"\n총 {len(matched)}개의 프롬프트")


def search_prompt():
    """키워드를 입력받아 제목 또는 내용에 포함된 프롬프트를 찾는다."""
    print("\n=== 프롬프트 검색 ===")

    # 검색어 입력 (비어 있으면 다시 요청)
    while True:
        keyword = input("검색어: ").strip()
        if keyword:
            break
        print("검색어를 입력해주세요.")

    # 제목 또는 내용에 검색어가 들어간 프롬프트만 골라내기
    matched = [
        p for p in prompts
        if keyword.lower() in p["title"].lower() or keyword.lower() in p["content"].lower()
    ]

    print("\n검색 결과:")

    if not matched:
        print(f"'{keyword}'에 해당하는 프롬프트가 없습니다.")
        return

    for i, p in enumerate(matched, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")

    print(f"\n{len(matched)}개의 프롬프트를 찾았습니다.")


def show_detail():
    """번호를 입력받아 해당 프롬프트의 전체 내용을 보여준다."""
    print("\n=== 프롬프트 상세 보기 ===")

    # 프롬프트가 없을 때
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 어떤 번호를 고를지 참고하도록 목록을 먼저 간단히 보여주기
    for i, p in enumerate(prompts, start=1):
        print(f"{i}. {p['title']}")

    # 번호 입력 받기
    sel = input("\n번호 입력: ").strip()

    # 올바른 번호인지 검사
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    # 선택한 프롬프트 꺼내기 (사람이 세는 번호는 1부터, 리스트는 0부터라 -1)
    p = prompts[int(sel) - 1]
    star = "⭐" if p["favorite"] else "없음"

    # 상세 정보 출력
    print("\n────────────────────────────")
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print("────────────────────────────")
    print("내용:")
    print(p["content"])
    print("────────────────────────────")


def show_menu():
    """메뉴를 화면에 출력한다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def main():
    """프로그램의 전체 흐름을 담당한다."""
    while True:
        show_menu()
        choice = input("선택: ")

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            print("[즐겨찾기 관리] 기능은 다음 단계에서 만듭니다.")
        elif choice == "7":
            print("[즐겨찾기 목록] 기능은 다음 단계에서 만듭니다.")
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


# 프로그램 시작점
if __name__ == "__main__":
    main()