import json, pathlib
root = pathlib.Path(__file__).parent
page = (root/'src/page.html').read_text()
head_part, body_part = page.split('<!--HEAD_END-->')
head_part = head_part.replace('<title>Claude · Boutique du Menuisier Tignieu</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n', '')
title = "Fenêtres, portes et volets sur mesure à Tignieu-Jameyzieu | La Boutique du Menuisier"
desc = "Menuiserie sur mesure à Tignieu-Jameyzieu : fenêtres, volets, portes d'entrée, portails, pergolas. Devis gratuit, rappel dans la journée par votre conseiller Claude. Certifié RGE Qualibat."
biz = {
 "@context":"https://schema.org","@type":"HomeAndConstructionBusiness",
 "name":"TPM - La Boutique du Menuisier Tignieu-Jameyzieu",
 "description":desc,"telephone":"+33478322749","email":"contact@tpm38.fr",
 "url":"https://www.laboutiquedumenuisier-lyon.fr/boutique/tignieu-jameyzieu/",
 "address":{"@type":"PostalAddress","streetAddress":"65 route de Crémieu","postalCode":"38230","addressLocality":"Tignieu-Jameyzieu","addressRegion":"Isère","addressCountry":"FR"},
 "geo":{"@type":"GeoCoordinates","latitude":45.7518997,"longitude":5.1934605},
 "openingHoursSpecification":[
   {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:45","closes":"12:30"},
   {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"13:30","closes":"17:00"}],
 "areaServed":["Tignieu-Jameyzieu","Pont-de-Chéruy","Charvieu-Chavagneux","Chavanoz","Crémieu","Saint-Romain-de-Jalionas","Villette-d'Anthon","Janneyrias","Meyzieu","Jonage"],
 "priceRange":"Devis gratuit"
}
faq_q = [("Le devis est-il vraiment gratuit ?","Oui. La visite, la prise de mesures et le devis sont gratuits et ne vous engagent à rien."),
 ("Sous quel délai suis-je rappelé ?","Votre conseiller vous rappelle dans la journée (du lundi au vendredi), sur le créneau indiqué. Le devis détaillé suit généralement sous 72 h après la visite."),
 ("Intervenez-vous en rénovation comme en neuf ?","Oui. Nous remplaçons des menuiseries existantes avec dépose soignée, et nous équipons aussi les constructions neuves."),
 ("Puis-je bénéficier d'aides financières ?","Nos poseurs sont certifiés RGE Qualibat, ce qui permet d'accéder à certaines aides à la rénovation énergétique selon votre logement et vos revenus.")]
faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_q]}
seo = f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#062B49">
<meta name="format-detection" content="telephone=yes">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="La Boutique du Menuisier">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://www.laboutiquedumenuisier-lyon.fr/wp-content/uploads/2026/09/bpi-menuisier-lyon.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="https://www.laboutiquedumenuisier-lyon.fr/wp-content/uploads/2026/02/favicon.svg" type="image/svg+xml">
<link rel="preload" as="image" href="claude.jpg">
<script type="application/ld+json">{json.dumps(biz, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq, ensure_ascii=False)}</script>
'''
out = '<!doctype html>\n<html lang="fr">\n<head>\n' + seo + head_part.strip() + '\n</head>\n<body>\n' + body_part.strip() + '\n</body>\n</html>\n'
(root/'index.html').write_text(out)
print(len(out))
