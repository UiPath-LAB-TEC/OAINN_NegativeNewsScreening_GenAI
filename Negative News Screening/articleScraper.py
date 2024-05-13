from newspaper import Article
import nltk

nltk.download('punkt')


def GetArticleBody(input_url):
	newsArticle = Article(input_url)
	newsArticle.download()
	newsArticle.parse()
	newsArticle.nlp()
	return(newsArticle.text)
print(GetArticleBody("https://finance.yahoo.com/news/elon-musk-shock-firing-supercharger-140311253.html?fr=sycsrp_catchall"))


