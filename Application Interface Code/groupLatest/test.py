# import requests

# reqUrl = "http://localhost:7200/repositories/KDE-GRP-TEMP?query=PREFIX oo:<http://www.kdeproject.owl/> select ?country ?ppt where { ?iso a oo:ISO . ?iso oo:representsCountry ?country . ?country oo:hasSubRegion ?subRegion . ?subRegion oo:hasRegion ?Region . ?Region oo:regionName ?name_of_Region . ?country oo:hasUnicefRegion ?unicefRegion . ?uniefRegion oo:unicefRegionName ?name . ?unicefRegion oo:forGender ?gender . ?gender oo:performsTask ?task . ?task oo:PRESENTATION_WITH_CONTENT ?ppt . FILTER(?name_of_Region=\"ECA\" %26%26 ?subRegion = ?unicefRegion) } LIMIT 1"

# headersList = {
 
# }

# payload = ""

# response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

# print(response.text)


# import requests

# reqUrl = "http://localhost:7200/repositories/KDE-GRP-TEMP?query=PREFIX oo: <http://www.kdeproject.owl/> SELECT ?completoos ?country ?reg WHERE { ?s2 a oo:OOS_US_GenderRates. ?s2 oo:femalepercent ?completoos . ?s2 oo:forISO ?iso_oos . ?iso_oos oo:representsCountry ?country_oos . ?country_oos oo:hasSubRegion ?sub_reg . ?sub_reg oo:hasRegion ?reg . FILTER(?country_oos = ?country) {SELECT ?country WHERE{ ?GenderLS a oo:CR_US_GenderRates. ?GenderLS oo:femalepercent ?completionRate_LS. ?GenderLS oo:forISO ?iso. ?iso oo:representsCountry ?country . FILTER(?completionRate_LS = ?MAX_GenderRate) { select (MAX(?completionRate) AS ?MAX_GenderRate) where { ?s1 a oo:CR_US_GenderRates. ?s1 oo:femalepercent ?completionRate. } } } } }"

# headersList = {
 
# }

# payload = ""

# response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

# print(response.text)