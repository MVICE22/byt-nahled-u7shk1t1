#!/usr/bin/env python3
"""Generuje index.html (galerie je statická kvůli rychlosti a SEO). Spuštění: python3 tools/build.py"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# slug, šířka, výška originálu, kategorie, popisek
P = [
 ("obyvak",           2946,1964,"interier","Obývací pokoj"),
 ("obyvak-jidelna",   3000,2000,"interier","Obývací pokoj"),
 ("obyvak-tv",        3000,2000,"interier","Obývací pokoj"),
 ("obyvak-sedacka",   3000,2000,"interier","Obývací pokoj"),
 ("kuchyn",           3000,2000,"interier","Kuchyň"),
 ("loznice",          3000,2000,"interier","Ložnice"),
 ("loznice-skrine",   3000,2000,"interier","Ložnice"),
 ("terasa",           3000,2000,"terasa","Terasa"),
 ("aerial-les",       3240,2160,"rezidence","Rezidence"),
 ("koupelna-zelena",  3000,2000,"interier","Koupelna"),
 ("detsky-pokoj",     3000,2000,"interier","Dětský pokoj"),
 ("terasa-shora",     2667,2000,"terasa","Terasa"),
 ("wellness",         3000,2000,"rezidence","Wellness"),
 ("predsin",          3000,2000,"interier","Předsíň"),
 ("sauna",            3554,2000,"rezidence","Sauna"),
 ("koupelna-vana",    3000,2000,"interier","Koupelna"),
 ("les-slunce",       3000,2000,"rezidence","Soukromý lesopark"),
 ("pradelna",         3000,2000,"interier","Prádelna"),
 ("fitness",          3000,2000,"rezidence","Fitness"),
 ("detsky-pokoj-mapa",3000,2000,"interier","Dětský pokoj"),
 ("hriste",           3000,2000,"rezidence","Venkovní fitness"),
 ("terasa-fasada",    2667,2000,"terasa","Terasa"),
 ("les-stezka",       3000,2000,"rezidence","Soukromý lesopark"),
 ("aerial-rezidence", 2837,1892,"rezidence","Rezidence"),
 ("garaz",            3000,2000,"rezidence","Garážové stání"),
 ("sklep",            3000,2000,"rezidence","Sklep"),
 ("nadvori",          3000,2000,"rezidence","Nádvoří"),
 ("parkovani",        3000,2000,"rezidence","Venkovní stání"),
 ("aerial-brana",     2667,2000,"rezidence","Rezidence"),
]

ORDER = ['obyvak-jidelna', 'obyvak-tv', 'obyvak-sedacka', 'obyvak', 'kuchyn', 'loznice', 'loznice-skrine', 'detsky-pokoj', 'detsky-pokoj-mapa', 'predsin', 'koupelna-zelena', 'koupelna-vana', 'pradelna', 'terasa', 'terasa-shora', 'terasa-fasada', 'aerial-les', 'aerial-areal', 'aerial-rezidence', 'aerial-brana', 'nadvori', 'parkovani', 'garaz', 'sklep', 'wellness', 'sauna', 'fitness', 'hriste', 'les-slunce', 'les-stezka']
P.sort(key=lambda p: ORDER.index(p[0]))

def widths(W):
    return sorted(set([x for x in (900,1600,2400) if x<W]+[W]))

def img(slug, w, h, alt, sizes, lazy=True, cls=""):
    ss=", ".join(f"img/{slug}-{x}.webp {x}w" for x in widths(w))
    l=' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c=f' class="{cls}"' if cls else ""
    return f'<img{c} src="img/{slug}-1600.webp" srcset="{ss}" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}"{l}>'

dims={s:(w,h) for s,w,h,_,_ in P}
def im(slug, alt, sizes="(max-width:1024px) 100vw, 50vw", cls=""):
    w,h=dims[slug]; return img(slug,w,h,alt,sizes,True,cls)

tiles="\n".join(
 f'''      <figure class="tile reveal" style="--ar:{w/h:.4f}" tabindex="0" role="button" data-c="{c}" data-full="img/{s}-{w}.webp" data-cap="{cap}" aria-label="Zvětšit fotku: {cap}">
        {img(s,w,h,cap,"(max-width:640px) 56vw, (max-width:1024px) 56vw, 38vw")}
        <figcaption>{cap}</figcaption>
      </figure>''' for s,w,h,c,cap in P)

HTML = f'''<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Prodej bytu 3+kk s terasou – rezidence Harmonia, Praha 9</title>
<meta name="description" content="Prodej bytu 3+kk, 78,1 m² plus terasa 14,8 m², v nejvyšším patře rezidence Harmonia v Praze 9 – Hrdlořezích. Přímo od majitele, bez provize. Garážové stání, venkovní stání a sklep v ceně.">
<meta name="theme-color" content="#F4EFE8">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="img/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<meta name="robots" content="noindex,nofollow">
<meta property="og:type" content="website">
<meta property="og:title" content="Byt, který má vše – uprostřed zeleně, kousek od centra Prahy">
<meta property="og:description" content="78,1 m² + terasa 14,8 m², nejvyšší patro, garáž, venkovní stání a sklep v ceně. Prodej přímo od majitele, bez provize.">
<meta property="og:image" content="img/obyvak-tv-1600.webp">
<meta property="og:locale" content="cs_CZ">
<link rel="preload" href="fonts/fraunces_vf_latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/inter_vf_latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="#top">Úvod</a>
    <nav class="nav-links" aria-label="Hlavní menu">
      <a href="#galerie">Galerie</a>
      <a href="#pudorys">Půdorys</a>
      <a href="#popis">Popis</a>
      <a href="#cena">Cena</a>
      <a href="#kontakt">Kontakt</a>
    </nav>
    <a class="nav-cta" href="tel:+420737509539">Zavolat</a>
    <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
  </div>
</header>

<main id="top">

<!-- HERO -->
<section class="hero">
  <div class="hero-media">
    <img src="img/obyvak-tv-2400.webp" srcset="img/obyvak-tv-900.webp 900w, img/obyvak-tv-1600.webp 1600w, img/obyvak-tv-2400.webp 2400w, img/obyvak-tv-3000.webp 3000w" sizes="(max-width:640px) 150vh, 100vw" width="3000" height="2000" alt="Obývací pokoj s TV stěnou, knihovnou, sedačkou a dřevěným obložením" fetchpriority="high">
  </div>
  <div class="wrap hero-content">
    <h1><span class="ln">Byt, </span><span class="ln">který </span><span class="ln">má&nbsp;vše</span><em>uprostřed zeleně, kousek od centra Prahy</em></h1>
    <p class="sub">Byt 3+kk, 78,1&nbsp;m² + terasa 14,8&nbsp;m² v Praze. Kompletně vybavený, připravený k okamžitému nastěhování. Prodej přímo od majitele, bez realitní kanceláře a provize.</p>
    <div class="hero-actions">
      <a class="btn btn-light" href="#kontakt">Domluvit si prohlídku</a>
      <a class="btn btn-ghost" href="#galerie">Galerie</a>
    </div>
  </div>
  <div class="hero-price"><small>Celková cena</small><strong>16&nbsp;890&nbsp;000&nbsp;Kč</strong></div>
  <div class="scroll-cue" aria-hidden="true"></div>
</section>

<!-- FAKTA -->
<section class="facts">
  <div class="wrap">
    <div class="facts-grid">
      <div class="fact reveal"><b>78,1<i>m²</i></b><span>plocha bytu, dispozice 3+kk</span></div>
      <div class="fact reveal" style="--d:.08s"><b>14,8<i>m²</i></b><span>jihozápadní terasa</span></div>
      <div class="fact reveal" style="--d:.16s"><b>3. NP</b><span>nejvyšší patro budovy</span></div>
      <div class="fact fact-price reveal"><b>16 890 000<i>Kč</i></b><span>celková cena</span></div>
    </div>
  </div>
</section>

<!-- ÚVOD -->
<section class="intro">
  <div class="wrap intro-grid">
    <div>
      <h2 class="reveal">Ráno lesopark, odpoledne terasa, <em>večer fitness a sauna</em></h2>
      <p class="lead reveal">Byt 3+kk v nejvyšším patře novostavby rezidence Harmonia (dokončena v 1Q 2026), uprostřed zeleně, ale jen kousek od centra Prahy.</p>
      <p class="reveal">Byt je kompletně vybavený, a to včetně chytré domácnosti Loxone. Je připravený k okamžitému nastěhování. Součástí je garážové stání, venkovní stání s přípravou pro nabíjení elektromobilu i sklep, vše v ceně.</p>
    </div>
    <div class="photo reveal">{im("terasa-fasada","Terasa v nejvyšším patře rezidence","(max-width:1024px) 100vw, 64vw")}</div>
  </div>
</section>

<!-- GALERIE -->
<section class="gallery" id="galerie">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <div class="eyebrow reveal">Galerie</div>
        <h2 class="reveal">Projděte si byt <em>i rezidenci</em></h2>
      </div>
      <div class="tabs reveal" role="group" aria-label="Filtr fotek">
        <button class="tab" data-f="all" aria-pressed="true">Vše</button>
        <button class="tab" data-f="interier" aria-pressed="false">Byt</button>
        <button class="tab" data-f="terasa" aria-pressed="false">Terasa</button>
        <button class="tab" data-f="rezidence" aria-pressed="false">Rezidence</button>
        <button class="tab" data-f="video" aria-pressed="false">Video</button>
      </div>
    </div>
    <div class="grid">
{tiles}
    </div>
    <div class="video-panel" hidden>
      <div class="video-empty">
        <span class="play" aria-hidden="true"><svg viewBox="0 0 24 24" width="28" height="28"><path d="M8 5v14l11-7z" fill="currentColor"/></svg></span>
        <strong>Video z bytu</strong>
        <span>Připravujeme</span>
      </div>
    </div>
  </div>
</section>

<!-- PŮDORYS -->
<section class="plan" id="pudorys">
  <div class="wrap">
    <div class="eyebrow reveal">Půdorys</div>
    <h2 class="reveal">Dispozice <em>3+kk</em></h2>
    <div class="plan-grid">
      <div class="plan-fig reveal"><img src="img/pudorys-tv.jpg" width="2240" height="2080" alt="Půdorys bytu 3+kk se zakresleným nábytkem a světovými stranami" loading="lazy"></div>
      <div class="reveal">
        <ol class="legend">
          <li><span>1</span>Předsíň</li>
          <li><span>2</span>Koupelna</li>
          <li><span>3</span>Prádelna</li>
          <li><span>4</span>Dětský pokoj</li>
          <li><span>5</span>Obývací pokoj s kuchyňským koutem</li>
          <li><span>6</span>Ložnice</li>
          <li><span>7</span>Terasa 14,8 m²</li>
        </ol>
        <div class="orient"><strong>Orientace:</strong> okna a terasa na jihozápad a severozápad.</div>
      </div>
    </div>
  </div>
</section>

<!-- POPIS -->
<section class="desc" id="popis">
  <div class="wrap">
    <div class="eyebrow reveal">Popis</div>
    <h2 class="reveal">Promyšlený byt, <em>vybavený do detailu</em></h2>
    <div class="cols">
      <div class="reveal dcard">
        <h3>Vybavení bytu</h3>
        <ul class="ul">
          <li><b>chytrá domácnost Loxone</b> (vytápění, chlazení, ventilace, stínění, osvětlení, alarm, regulace vlhkosti, přístup do všech prostor domu)</li>
          <li>klimatizace a rekuperace v každé místnosti</li>
          <li>podlahové vytápění, masivní dřevěné podlahy</li>
          <li>designové osvětlení s nastavitelnou intenzitou a teplotou světla v každé místnosti, pohybová čidla</li>
          <li>plastová okna s hliníkovým opláštěním a trojskly, předokenní žaluzie</li>
          <li>vestavěné skříně a kuchyň na míru od truhláře</li>
          <li>dřevěné obložení na stěnách v obývacím pokoji</li>
        </ul>
      </div>
      <div class="reveal dcard" style="--d:.1s">
        <h3>Dispozice</h3>
        <ul class="ul">
          <li>obývací pokoj s kuchyňským koutem, ložnice, dětský pokoj</li>
          <li>koupelna a samostatná prádelna s úložným prostorem</li>
          <li>okna na jihozápad a severozápad, terasa 14,8 m² na jihozápad</li>
          <li>byt v nejvyšším patře budovy</li>
          <li>1× garážové stání, 1× venkovní stání s přípravou pro nabíjení elektromobilu a sklep (vše v ceně)</li>
        </ul>
      </div>
    </div>

    <div class="dcard wide reveal" style="margin-top:20px"><p class="energy"><b>Energetická náročnost budovy: třída B</b>, centrální tepelné čerpadlo s plynovou kotelnou, teplá voda dohřívaná z fotovoltaiky.</p></div>

    <div class="potential light reveal">
      <b>5,85<i> m</i></b>
      <div>
        <h3>Potenciál prostoru</h3>
        <p>Strop vysoký 5,85 m v obýváku skýtá potenciální možnost vestavby patra.</p>
      </div>
    </div>

    <div class="eyebrow reveal" style="margin-top:96px">Rezidence Harmonia a její služby</div>
    <div class="feature-row">
      <a class="feature reveal" href="#galerie">{im("les-slunce","Lesopark přímo u rezidence","(max-width:640px) 100vw, 50vw")}<div><h3>1 ha privátního lesoparku</h3><p>místa k posezení a pikniku, hřiště na pétanque</p></div></a>
      <a class="feature reveal" style="--d:.08s" href="#galerie">{im("wellness","Wellness v rezidenci","(max-width:640px) 100vw, 50vw")}<div><h3>Privátní wellness</h3><p>se saunou</p></div></a>
      <a class="feature reveal" style="--d:.16s" href="#galerie">{im("fitness","Fitness v rezidenci","(max-width:640px) 100vw, 50vw")}<div><h3>Privátní fitness</h3><p>vnitřní i venkovní</p></div></a>
      <div class="feature reveal" style="--d:.24s"><img src="img/skolka-1600.webp" srcset="img/skolka-900.webp 900w, img/skolka-1600.webp 1600w, img/skolka-2400.webp 2400w, img/skolka-3000.webp 3000w" sizes="(max-width:640px) 100vw, 50vw" width="3000" height="2003" alt="Ilustrační foto: děti si hrají ve školce" loading="lazy"><span class="tag">Ilustrační foto</span><div><h3>Soukromá školka</h3><p>přímo v areálu rezidence</p></div></div>
      <a class="feature pos-l reveal" href="#galerie">{im("aerial-brana","Rezidence z výšky, 66 bytů","(max-width:640px) 100vw, 50vw")}<div><h3>Pouze 66 bytů</h3><p>v celé rezidenci</p></div></a>
      <div class="feature reveal" style="--d:.08s"><img src="img/kolarna-1125.webp" srcset="img/kolarna-600.webp 600w, img/kolarna-1125.webp 1125w" width="1125" height="1500" sizes="(max-width:640px) 100vw, 50vw" alt="Ilustrační foto: kolárna s koly na stojanech" loading="lazy"><span class="tag">Ilustrační foto</span><div><h3>Kolárna a umývárna kol</h3></div></div>
      <a class="feature wide zoom reveal" style="--d:.16s" href="#galerie">{im("aerial-les","Rezidence z výšky uprostřed lesů","(max-width:640px) 150vw, 72vw")}<div><h3>Oplocený areál</h3><p>přístupný jen obyvatelům, kamerový systém v celé rezidenci</p></div></a>
    </div>
  </div>
</section>

<!-- OKOLÍ -->
<section class="area">
  <div class="area-bg">{img("aerial-les",3240,2160,"Rezidence z výšky uprostřed podzimního lesa","100vw")}</div>
  <div class="wrap">
    <div class="eyebrow reveal">Okolí a dostupnost</div>
    <h2 class="reveal">Les <em>za dveřmi</em>, centrum na dosah</h2>
    <p class="reveal">Rezidence stojí uprostřed lesů a parků, ale na dosah centra Prahy a běžného aktivního života. Byt se nachází v Praze 9 – Hrdlořezích, na hranici Prahy 3, 9 a 10.</p>
    <p class="reveal">Cyklostezka, meandry Rokytky, Hořejší rybník, přírodní park Smetanka a dětské hřiště jsou přímo u rezidence.</p>
    <div class="trans">
      <div class="reveal"><b>18 min</b><span>autem na Václavské náměstí</span></div>
      <div class="reveal" style="--d:.08s"><b>9 min</b><span>autem do OC Harfa a O2 areny</span></div>
      <div class="reveal" style="--d:.16s"><b>13 min</b><span>autem do OC Černý Most</span></div>
    </div>
    <ul class="area-list reveal">
      <li>zastávka autobusu (146) 200 m, 2 min pěšky</li>
      <li>zastávka tramvaje (8, 37, 94) 10 min pěšky</li>
      <li>Lidl 700 m, 15 min pěšky</li>
    </ul>
  </div>
</section>

<!-- CENA -->
<section class="price light" id="cena">
  <div class="wrap">
    <div class="price-top">
      <div>
        <div class="eyebrow reveal">Cena a forma vlastnictví</div>
        <div class="price-big reveal">16&nbsp;890&nbsp;000<small>Kč</small></div>
      </div>
      <p class="price-note reveal">Jde o družstevní vlastnictví v Bytovém družstvu Hrdlořezy. Prodává se družstevní podíl, tedy převod členských práv a povinností.</p>
    </div>
    <div class="pgrid">
      <div class="pcell reveal"><small>Vlastní zdroje<br>(cena za družstevní podíl)</small><b>8&nbsp;865&nbsp;533 Kč</b><p>platí se prodávajícímu</p></div>
      <div class="pcell reveal" style="--d:.08s"><small>Podíl na úvěru družstva<br>(k 1. 12. 2026)</small><b>8&nbsp;024&nbsp;467 Kč</b><p>sazba 5,60 % p.a., fixace do 20. 4. 2029; splácí se jako hypotéka v měsíčních splátkách po dobu 35 let</p></div>
      <div class="pcell reveal" style="--d:.16s"><small>Měsíční splátka družstvu za byt</small><b>43&nbsp;883 Kč</b><p>splátka podílu na úvěru družstva</p></div>
      <div class="pcell reveal" style="--d:.24s"><small>Zálohy na energie a služby</small><b>7&nbsp;511 Kč</b><p>měsíčně</p></div>
    </div>
    <div class="own">
      <div class="reveal">
        <h3>Jak prodej probíhá</h3>
        <p>Prodej probíhá přímo od majitele, bez realitní kanceláře a provize. Garážové stání, venkovní stání i sklep jsou v ceně.</p>
      </div>
      <div class="reveal" style="--d:.1s">
        <h3>Družstevní podíl</h3>
        <ul class="ul">
          <li>byt lze převést do osobního vlastnictví</li>
          <li>převod podílu na nové majitele nepodléhá souhlasu orgánů družstva a nikdo neschvaluje bonitu a schopnost splácet měsíční splátky nových majitelů</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="faq">
  <div class="wrap">
    <div class="eyebrow reveal">Časté otázky</div>
    <h2 class="reveal">Co se nejčastěji <em>ptáte</em></h2>
    <div class="faq-list reveal">
      <details><summary>Prodáváte přes realitní kancelář?</summary><p>Ne. Prodej probíhá přímo od majitele, bez realitní kanceláře a bez provize.</p></details>
      <details><summary>Je byt vybavený?</summary><p>Ano, byt je kompletně vybavený. Je možné jej přebrat jak s vybavením, tak bez vybavení.</p></details>
      <details><summary>Kdy se lze nastěhovat?</summary><p>Byt je připravený k okamžitému nastěhování.</p></details>
      <details><summary>Co všechno je v ceně?</summary><p>Garážové stání, venkovní stání s přípravou pro nabíjení elektromobilu a sklep jsou v ceně bytu.</p></details>
      <details><summary>Je to družstevní byt. Dá se převést do osobního vlastnictví?</summary><p>Ano, byt lze převést do osobního vlastnictví.</p></details>
      <details><summary>Schvaluje převod družstvo?</summary><p>Převod podílu na nové majitele nepodléhá souhlasu orgánů družstva a nikdo neschvaluje bonitu a schopnost splácet měsíční splátky nových majitelů.</p></details>
    </div>
  </div>
</section>

<!-- KONTAKT -->
<section class="contact" id="kontakt">
  <div class="wrap contact-grid">
    <div>
      <div class="eyebrow reveal">Kontakt</div>
      <h2 class="reveal">Přijďte se <em>podívat</em></h2>
      <p class="lead reveal">Zavolejte mi nebo pošlete e-mail. Rád vám byt ukážu a odpovím na všechny otázky.</p>
    </div>
    <div class="card light reveal">
      <div class="who">Matěj Vais</div>
      <div class="role">majitel a prodávající</div>
      <a class="row" href="tel:+420737509539"><div><small>Telefon</small><strong>737 509 539</strong></div><span class="ic">→</span></a>
      <a class="row" href="mailto:matejvais@seznam.cz?subject=Prohl%C3%ADdka%20bytu%20Harmonia"><div><small>E-mail</small><strong>matejvais@seznam.cz</strong></div><span class="ic">→</span></a>
      <a class="row" href="https://www.google.com/maps/search/?api=1&amp;query=Mezitra%C5%A5ov%C3%A1%20343%2F26%2C%20Praha%209" target="_blank" rel="noopener"><div><small>Adresa</small><strong>Mezitraťová 343/26, Praha 9 – Hrdlořezy</strong></div><span class="ic">↗</span></a>
      <div class="btns">
        <a class="btn btn-green" href="tel:+420737509539">Zavolat</a>
        <a class="btn btn-line" href="mailto:matejvais@seznam.cz?subject=Prohl%C3%ADdka%20bytu%20Harmonia">Napsat e-mail</a>
      </div>
    </div>
  </div>
</section>

</main>

<footer>
  <div class="wrap">
    <p>Informace na těchto stránkách mají informativní charakter a nejsou návrhem na uzavření smlouvy.</p>
    <p>© 2026 Matěj Vais. Fotografie bytu a rezidence, video, texty a grafika na těchto stránkách jsou chráněny autorským právem. Jejich stahování, kopírování a další použití nebo šíření bez předchozího souhlasu vlastníka není povoleno. Fotografie označené jako ilustrační pocházejí z fotobanky Pexels.</p>
  </div>
</footer>

<div class="mbar" aria-label="Rychlý kontakt"><a class="a" href="tel:+420737509539">Zavolat</a><a class="b" href="mailto:matejvais@seznam.cz?subject=Prohl%C3%ADdka%20bytu%20Harmonia">Napsat</a></div>

<div class="lb" role="dialog" aria-modal="true" aria-label="Galerie">
  <div class="count"></div>
  <button class="x" aria-label="Zavřít">✕</button>
  <button class="p" aria-label="Předchozí">←</button>
  <button class="n" aria-label="Další">→</button>
  <figure><img alt=""><figcaption></figcaption></figure>
</div>

<script src="js/main.js" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(HTML)
print("index.html", len(HTML))
