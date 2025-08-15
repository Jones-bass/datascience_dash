import requests
import json
import os
from html.parser import HTMLParser

# Diretório base
base_dir = r"D:\Search\dashboard_python\04_Extraindo_dados\Asimov_News"
# Pasta "dados" dentro do base_dir
dados_dir = os.path.join(base_dir, "dados")
# Cria a pasta se não existir
os.makedirs(dados_dir, exist_ok=True)
# Caminho completo do arquivo JSON
new_path = os.path.join(dados_dir, "links_noticias.json")


class NewsParser(HTMLParser):
    def __init__(self, patterns):
        super().__init__()
        self.patterns = patterns
        self.news_links = []
        self.current_href = None
        self.capture_text = False
        self.expected_tag = None
        self.expected_class = None
        self.text_func = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        tag_class = attrs_dict.get("class", "")
        href = attrs_dict.get("href", None)

        if href:
            self.current_href = href

        for pattern_tag, class_name, text_func in self.patterns:
            if tag == pattern_tag and class_name in tag_class.split():
                self.capture_text = True
                self.expected_tag = tag
                self.expected_class = class_name
                self.text_func = text_func
                return

    def handle_data(self, data):
        if self.capture_text:
            text = data.strip()
            if text and self.current_href:
                if self.current_href not in self.news_links:
                    self.news_links.append(self.current_href)
                self.capture_text = False

    def handle_endtag(self, tag):
        if tag == self.expected_tag:
            self.capture_text = False
            self.expected_tag = None
            self.expected_class = None
            self.text_func = None


class Site:
    def __init__(self):
        self.sites_config = {
            "globo": {
                "url": "https://www.globo.com/",
                "patterns": [
                    ("h2", "post__title", lambda t: t.strip()),
                    ("h2", "post-multicontent__link--title__text", lambda t: t.strip()),
                ],
            },
            "veja": {
                "url": "https://veja.abril.com.br/",
                "patterns": [
                    ("a", "related-article", lambda t: t.strip()),
                    ("h2", "title", lambda t: t.strip()),
                    ("h3", "title", lambda t: t.strip()),
                    ("h4", "title", lambda t: t.strip()),
                ],
            },
            "totvs": {
                "url": "https://centraldeatendimento.totvs.com/hc/pt-br/sections/115002597048-Administrativo",
                "patterns": [
                    ("a", "article-list-link", lambda t: t.strip()),
                    ("a", "related-article", lambda t: t.strip()),
                    ("h2", "title", lambda t: t.strip()),
                    ("h3", "title", lambda t: t.strip()),
                    ("h4", "title", lambda t: t.strip()),
                ],
            },
        }

    def _fetch_news(self, url: str, patterns: list):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/86.0.4240.198 Safari/537.36"
        }
        page = requests.get(url, headers=headers, timeout=10)
        parser = NewsParser(patterns)
        parser.feed(page.text)
        return parser.news_links

    def update_all_news(self):
        all_news = {}
        for site_name, config in self.sites_config.items():
            print(f"🔍 Coletando links de {site_name}...")
            try:
                all_news[site_name] = self._fetch_news(
                    config["url"], config["patterns"]
                )
            except Exception as e:
                print(f"⚠ Erro ao coletar {site_name}: {e}")
                all_news[site_name] = []
        return all_news


if __name__ == "__main__":
    coletor = Site()
    links = coletor.update_all_news()

    with open(new_path, "w", encoding="utf-8") as f:
        json.dump(links, f, ensure_ascii=False, indent=4)

    print(f"✅ Apenas os links foram salvos em {new_path}")
