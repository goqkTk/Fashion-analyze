import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 데이터셋 불러오기
clothing_reviews = pd.read_csv(r'C:\Users\dbsxor\OneDrive\바탕 화면\fashion eojjeogo\a.csv')

# 데이터 전처리
clothing_reviews = clothing_reviews[['Review Text', 'Rating', 'Division Name', 'Department Name']]

# 리뷰 텍스트 및 평점에 결측값이 있을 경우 제거
clothing_reviews.dropna(subset=['Review Text', 'Rating'], inplace=True)

# 마케팅 전략별 리뷰 분석
# 제품 카테고리에 따른 평균 평점
division_avg_rating = clothing_reviews.groupby('Division Name')['Rating'].mean().sort_values(ascending=False)
division_avg_rating.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Average Rating by Division')
plt.ylabel('Average Rating')
plt.xlabel('Division Name')
plt.xticks(rotation=90)
plt.show()

# 부서명에 따른 평균 평점
department_avg_rating = clothing_reviews.groupby('Department Name')['Rating'].mean()
department_avg_rating.plot(kind='bar', figsize=(10, 6), color='lightcoral')
plt.title('Average Rating by Department')
plt.ylabel('Average Rating')
plt.xlabel('Department Name')
plt.xticks(rotation=90)
plt.show()

# 리뷰 텍스트 분석 (긍정적 부정적 리뷰 비교)
positive_reviews = clothing_reviews[clothing_reviews['Rating'] >= 4]
negative_reviews = clothing_reviews[clothing_reviews['Rating'] <= 2]

# 긍정적인 리뷰에서 가장 자주 등장하는 단어
positive_text = ' '.join(positive_reviews['Review Text'])
positive_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_text)

# 부정적인 리뷰에서 가장 자주 등장하는 단어
negative_text = ' '.join(negative_reviews['Review Text'])
negative_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(negative_text)

# 결과 출력
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.title('Word Cloud for Positive Reviews')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.title('Word Cloud for Negative Reviews')
plt.axis('off')

plt.tight_layout()
plt.show()