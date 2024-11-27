# hw13
- 카테고리와 태그 구현
- 부트스트랩 최신 버전에 맞게 코드를 수정
- tag와 category는 Post모델과 달리 절대 경로를 get_absolute_url 로 하면 구현이 안되서
{% url 'blog:category_page' category.slug %} 같은 형태로 구현함 
