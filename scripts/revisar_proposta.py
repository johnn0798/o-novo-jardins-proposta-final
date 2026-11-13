from pathlib import Path
from bs4 import BeautifulSoup
p=Path("index.html")
soup=BeautifulSoup(p.read_text(encoding="utf-8"),"html.parser")
intro=soup.select_one("main section.wrap > .intro")
if intro:
 lead=intro.select_one("p.lead")
 if lead: lead.string="Vocês já exploram vídeos dinâmicos. A proposta é ampliar esse repertório com formatos que chamam atenção nas redes sociais, trazendo mais visibilidade para o perfil e para os imóveis. Tudo a partir das fotos que vocês já têm."
 cols=intro.find_next_sibling("div",class_="columns")
 if cols: cols.decompose()
growth=soup.select_one(".growth-block")
if growth:
 h=growth.select_one("h2.h2")
 if h:h.string="O próximo conteúdo está no catálogo de vocês."
 l=growth.select_one("p.lead")
 if l:l.string="O portfólio da O Novo Jardins já reúne imóveis com grande potencial visual. Mas transformar esse catálogo em vídeos por meio de produções presenciais exige logística, contratação, captação e edição. Fazer isso em volume pode exigir um orçamento muito alto — e limitar a frequência de novas publicações."
 cost=growth.select_one(".production-note")
 if cost:
  st=cost.find("strong")
  if st:st.decompose()
  txt=cost.find("p")
  if txt:txt.string="Uma produção presencial pode facilmente chegar a R$ 5 mil, considerando captação, deslocamentos, equipe e edição. Para divulgar vários imóveis, esse investimento se multiplica."
 k=growth.select_one(".inventory .kicker")
 if k:k.string="Vocês já têm a matéria-prima."
 close=growth.select_one(".growth-close")
 if close:close.string="O acervo já existe. Agora, existe também uma forma de desbloquear esse potencial e transformar essas propriedades em conteúdo com escala e investimento acessível."
campaign=soup.select_one(".steps .step:last-child p")
if campaign:campaign.string="Vou disponibilizar também um gestor de tráfego especialista em vendas para colocar a campanha no ar no Meta Ads (Facebook e Instagram) e acompanhar seu desempenho durante sete dias. O serviço de gestão é por nossa conta no pacote completo."
feature=soup.select_one(".price.feature")
if feature:
 bonus=next((li for li in feature.select("li") if "Campanha de 7 dias" in li.get_text()),None)
 if bonus:bonus.string="Campanha de 7 dias no Meta Ads (Facebook e Instagram): gestor de tráfego especialista em vendas e acompanhamento incluídos como bônus"
 amount=feature.select_one(".amount")
 if amount:
  old=feature.select_one(".installments")
  if old:old.decompose()
  el=soup.new_tag("p");el["class"]="installments";el.string="Ou em até 5x no cartão, com acréscimo das taxas da maquineta.";amount.insert_after(el)
hero=soup.select_one("header.hero")
if hero:
 hero["class"]=list(dict.fromkeys(hero.get("class",[])+["hero-revised"]))
 brand=hero.select_one("img.brand")
 if brand:brand["alt"]="Identidade visual de O Novo Jardins Imóveis"
 if not soup.select_one(".jardins-desktop-preview"):
  preview=soup.new_tag("div");preview["class"]="jardins-desktop-preview"
  img=soup.new_tag("img",src="o-novo-jardins.gif",alt="Prévia de apresentação visual de imóvel");img["loading"]="lazy";preview.append(img)
  nxt=hero.find_next_sibling()
  if nxt and nxt.name!="main" and nxt.find(["video","iframe","img"]):nxt.append(preview)
  else:hero.insert_after(preview)
for old in soup.select("style[data-jardins-final-review]"):old.decompose()
css="""
.hero h1{font-size:clamp(2.7rem,5vw,4.8rem);line-height:1.04;letter-spacing:-.025em}
.h2{font-size:clamp(2rem,3.4vw,3.1rem);line-height:1.13;letter-spacing:-.018em}
.lead{font-size:clamp(1rem,1.35vw,1.11rem);line-height:1.66}
.intro{margin-bottom:32px}
.growth-block{margin-top:34px;margin-bottom:0;padding-top:30px;padding-bottom:16px;border-bottom:0}
.growth-block .h2{margin-bottom:14px}
.production-note{margin:22px 0 24px;padding:22px 28px}
.production-note p{font-size:1rem;line-height:1.65}
.inventory{margin-top:24px}
.growth-close{margin:22px 0 0;font-size:clamp(1.15rem,1.7vw,1.32rem);line-height:1.5}
.visual-examples{padding-top:14px}
.visual-examples .intro{margin-bottom:26px}
.installments{margin:7px 0 0;color:#e0ca9d;font-size:.93rem;line-height:1.5}
.closing{padding:66px 24px 70px}
.closing h2{font-family:Georgia,'Times New Roman',serif;font-size:clamp(1.65rem,3vw,2.65rem);font-weight:400;line-height:1.22;letter-spacing:-.018em;max-width:740px;margin:0 auto 18px}
.closing>p:not(.note){font-size:1rem;line-height:1.65}
.jardins-desktop-preview{display:none}
@media(min-width:701px){
 .hero.hero-revised{position:relative;min-height:72vh;background:#0b1b12!important;overflow:hidden;padding:42px 0 55px}
 .hero.hero-revised::before,.hero.hero-revised::after{background-image:none!important}
 .hero.hero-revised>div:first-child{width:auto;max-width:210px;position:absolute;top:20px;left:max(5vw,28px);z-index:2}
 .hero.hero-revised img.brand{height:auto!important;width:100%;max-width:210px;aspect-ratio:auto;object-fit:contain;object-position:center;border-radius:3px}
 .hero.hero-revised .hero-copy{margin:auto 0;padding-top:110px;padding-bottom:42px}
 .hero.hero-revised h1{max-width:780px}
 .jardins-desktop-preview{display:flex;justify-content:center;align-items:center;max-width:900px;margin:28px auto 38px;padding:0 24px}
 .jardins-desktop-preview img{display:block;width:min(100%,540px);max-height:290px;object-fit:contain;background:#10251a;border:1px solid #c4aa7860;box-shadow:0 14px 42px #09160c22;border-radius:12px}
}
@media(max-width:700px){
 .hero.hero-revised{background:#0b1b12}
 .hero.hero-revised .brand{width:100%;height:auto;max-width:none;aspect-ratio:16/9;object-fit:cover}
 .hero h1{font-size:clamp(2.1rem,9.6vw,2.75rem);line-height:1.04}
 .h2{font-size:clamp(1.8rem,7vw,2.1rem);line-height:1.14}
 .lead{font-size:1rem;line-height:1.58}
 .growth-block{margin:26px 0 0;padding:26px 0 12px}
 .visual-examples{padding-top:18px}
 .production-note{padding:20px}
 .growth-close{font-size:1.15rem;margin-top:20px}
 .closing{padding:52px 25px 56px}
 .closing h2{font-size:clamp(1.65rem,7.2vw,2rem);line-height:1.21}
 .installments{font-size:.89rem}
}
"""
st=soup.new_tag("style");st["data-jardins-final-review"]="true";st.string=css;soup.head.append(st)
p.write_text(str(soup),encoding="utf-8")
print("REVIEW_APPLIED",p.stat().st_size)
