from flask import Flask,jsonify
from flask_cors import CORS
# import pandas as pd
import requests
# from io import StringIO

app = Flask(__name__)
CORS(app)
rep_name = "KDEGroupProject"

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/query/1')
def query_1():    
    # reqUrl = "http://localhost:7200/repositories/KDE-GRP-TEMP?query=PREFIX oo: <http://www.kdeproject.owl/> SELECT ?completoos ?country ?reg WHERE { ?s2 a oo:OOS_US_GenderRates. ?s2 oo:femalepercent ?completoos . ?s2 oo:forISO ?iso_oos . ?iso_oos oo:representsCountry ?country_oos . ?country_oos oo:hasSubRegion ?sub_reg . ?sub_reg oo:hasRegion ?reg . FILTER(?country_oos = ?country) {SELECT ?country WHERE{ ?GenderLS a oo:CR_US_GenderRates. ?GenderLS oo:femalepercent ?completionRate_LS. ?GenderLS oo:forISO ?iso. ?iso oo:representsCountry ?country . FILTER(?completionRate_LS = ?MAX_GenderRate) { select (MAX(?completionRate) AS ?MAX_GenderRate) where { ?s1 a oo:CR_US_GenderRates. ?s1 oo:femalepercent ?completionRate. } } } } }"
    reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query= PREFIX oo: <http://www.kdeproject.owl/> PREFIX foaf: <http://xmlns.com/foaf/0.1/> select ?ratio ?devRegion where { ?s1 a oo:CR_US_GenderRates. ?s2 a oo:OOS_US_GenderRates. ?s1 oo:malepercent ?completionRate. ?s2 oo:malepercent ?outOfSchoolRate. ?s1 oo:forISO ?iso. ?s2 oo:forISO ?iso. ?iso foaf:DevelopmentRegions ?devRegion BIND ((?completionRate/?outOfSchoolRate) AS ?ratio) } ORDER BY(?devRegion)"
    headersList = {
    # "Accept": "application/sparql-results+json"
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    
    data=response.text.splitlines()
    columns=data[0].split(",")
    d = []
    for j in range(1,len(data)):
        d.append(data[j].split(","))
    # print(d)
    rs = []
    for i in d:
        # print(len(i))
        temp = {}
        for j in range(len(i)):
            temp[columns[j]] = i[j]
        rs.append(temp)
    # print(rs)
    # print(response.text)
    return jsonify(rs)
@app.route('/query/2')
def query_2():    
    reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query=PREFIX oo: <http://www.kdeproject.owl/> PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?country ?devRegion ?femalecompletionRate ?femaleoutOfSchoolRate WHERE { { ?s oo:femalepercent ?femalecompletionRate . ?s oo:forISO ?iso. ?iso oo:representsCountry ?country. ?iso foaf:DevelopmentRegions ?devRegion FILTER EXISTS { { SELECT (MAX (?completionRate) AS ?MaxcompletionRate){ ?s1 a oo:CR_LS_GenderRates. ?s1 oo:femalepercent ?completionRate. } } FILTER ( ?femalecompletionRate = ?MaxcompletionRate ) } } UNION { ?s oo:femalepercent ?femaleoutOfSchoolRate . ?s oo:forISO ?iso. ?iso oo:representsCountry ?country. ?iso foaf:DevelopmentRegions ?devRegion FILTER EXISTS { { SELECT (MAX (?outOfSchoolRate) AS ?MaxoutOfSchoolRate){ ?s2 a oo:OOS_LS_GenderRates. ?s2 oo:femalepercent ?outOfSchoolRate. } } FILTER ( ?femaleoutOfSchoolRate = ?MaxoutOfSchoolRate ) } } }"
    headersList = {
    # "Accept": "application/sparql-results+json"
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    
    data=response.text.splitlines()
    columns=data[0].split(",")
    d = []
    for j in range(1,len(data)):
        d.append(data[j].split(","))
    # print(d)
    rs = []
    for i in d:
        # print(len(i))
        temp = {}
        for j in range(len(i)):
            temp[columns[j]] = i[j]
        rs.append(temp)
    # print(rs)
    # print(response.text)
    return jsonify(rs)
@app.route('/query/3')
def query_3():    
    # reqUrl = "http://localhost:7200/repositories/KDE-GRP-TEMP?query=PREFIX oo: <http://www.kdeproject.owl/> PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?country ?devRegion ?femalecompletionRate ?femaleoutOfSchoolRate WHERE { { ?s oo:femalepercent ?femalecompletionRate . ?s oo:forISO ?iso. ?iso oo:representsCountry ?country. ?iso foaf:DevelopmentRegions ?devRegion FILTER EXISTS { { SELECT (MAX (?completionRate) AS ?MaxcompletionRate){ ?s1 a oo:CR_LS_GenderRates. ?s1 oo:femalepercent ?completionRate. } } FILTER ( ?femalecompletionRate = ?MaxcompletionRate ) } } UNION { ?s oo:femalepercent ?femaleoutOfSchoolRate . ?s oo:forISO ?iso. ?iso oo:representsCountry ?country. ?iso foaf:DevelopmentRegions ?devRegion FILTER EXISTS { { SELECT (MAX (?outOfSchoolRate) AS ?MaxoutOfSchoolRate){ ?s2 a oo:OOS_LS_GenderRates. ?s2 oo:femalepercent ?outOfSchoolRate. } } FILTER ( ?femaleoutOfSchoolRate = ?MaxoutOfSchoolRate ) } } }"
    reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query=PREFIX oo: <http://www.kdeproject.owl/> PREFIX foaf: <http://xmlns.com/foaf/0.1/> select ?unicefRegion (SUM(?value) AS ?SumOfTaskPerformedPercentagePerUnicefRegion) where { ?iso foaf:DevelopmentRegions \"Least Developed\". ?iso oo:representsCountry ?country. ?country oo:countryName ?name. ?country oo:hasUnicefRegion ?unicefRegion. ?unicefRegion oo:forGender ?gender. ?gender oo:genderName \"Female\". ?gender oo:performsTask ?taskPerformed. ?taskPerformed oo:COP_FOLD_FILE ?value } GROUP BY(?unicefRegion)"
    headersList = {
    # "Accept": "application/sparql-results+json"
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    
    data=response.text.splitlines()
    columns=data[0].split(",")
    d = []
    for j in range(1,len(data)):
        d.append(data[j].split(","))
    # print(d)
    rs = []
    for i in d:
        # print(len(i))
        temp = {}
        for j in range(len(i)):
            temp[columns[j]] = i[j]
        rs.append(temp)
    # print(rs)
    # print(response.text)
    return jsonify(rs)



@app.route('/query/4')
def query_4():    
    reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query= PREFIX oo: <http://www.kdeproject.owl/> PREFIX foaf: <http://xmlns.com/foaf/0.1/> select ?countryName ?ruralCompletionRates ?urbanCompletionRates ?ruraloutOfSchoolRates ?urbanoutOfSchoolRates where { ?demography a oo:CR_US_Demography. ?demography2 a oo:OOS_US_Demography. ?demography oo:forISO ?iso . ?demography2 oo:forISO ?iso . ?iso oo:representsCountry ?country. ?country oo:countryName ?countryName. ?demography oo:ruralResidence ?ruralCompletionRates. ?demography oo:urbanResidence ?urbanCompletionRates. ?demography2 oo:ruralResidence ?ruraloutOfSchoolRates. ?demography2 oo:urbanResidence ?urbanoutOfSchoolRates. }"
    headersList = {
    # "Accept": "application/sparql-results+json"
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    
    data=response.text.splitlines()
    columns=data[0].split(",")
    d = []
    for j in range(1,len(data)):
        d.append(data[j].split(","))
    # print(d)
    rs = []
    for i in d:
        # print(len(i))
        temp = {}
        for j in range(len(i)):
            temp[columns[j]] = i[j]
        rs.append(temp)
    # print(rs)
    # print(response.text)
    return jsonify(rs)
@app.route('/query/5')
def query_5():    
    reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query= PREFIX oo: <http://www.kdeproject.owl/> select ?maleCompletionRate ?MaleOutOfSchoolRate where { ?s1 a oo:CR_US_GenderRates. ?s2 a oo:OOS_US_GenderRates. ?s1 oo:malepercent ?maleCompletionRate. ?s2 oo:malepercent ?MaleOutOfSchoolRate. ?s1 oo:forISO ?iso. ?s2 oo:forISO ?iso. ?iso oo:representsCountry oo:Indonesia }"
    headersList = {
    # "Accept": "application/sparql-results+json"
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    
    data=response.text.splitlines()
    columns=data[0].split(",")
    d = []
    for j in range(1,len(data)):
        d.append(data[j].split(","))
    # print(d)
    rs = []
    for i in d:
        # print(len(i))
        temp = {}
        for j in range(len(i)):
            temp[columns[j]] = i[j]
        rs.append(temp)
    # print(rs)
    # print(response.text)
    return jsonify(rs)
@app.route('/query/6')
def query_6():    
    # reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query=select ?country ?ppt where { ?iso a oo:ISO . ?iso oo:representsCountry ?country . ?country oo:hasSubRegion ?subRegion . ?subRegion oo:hasRegion ?Region . ?Region oo:regionName ?name_of_Region . ?country oo:hasUnicefRegion ?unicefRegion . ?uniefRegion oo:unicefRegionName ?name . ?unicefRegion oo:forGender ?gender . ?gender oo:performsTask ?task . ?task oo:PRESENTATION_WITH_CONTENT ?ppt . FILTER(?name_of_Region=\"ECA\" %26%26 ?subRegion = ?unicefRegion) } LIMIT 1"
    reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query=PREFIX oo:<http://www.kdeproject.owl/> select ?country ?ppt where { ?iso a oo:ISO . ?iso oo:representsCountry ?country . ?country oo:hasSubRegion ?subRegion . ?subRegion oo:hasRegion ?Region . ?Region oo:regionName ?name_of_Region . ?country oo:hasUnicefRegion ?unicefRegion . ?uniefRegion oo:unicefRegionName ?name . ?unicefRegion oo:forGender ?gender . ?gender oo:performsTask ?task . ?task oo:PRESENTATION_WITH_CONTENT ?ppt . FILTER(?name_of_Region=\"ECA\" %26%26 ?subRegion = ?unicefRegion) } LIMIT 1"
    headersList = {
    # "Accept": "application/sparql-results+json"
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    
    data=response.text.splitlines()
    columns=data[0].split(",")
    d = []
    for j in range(1,len(data)):
        d.append(data[j].split(","))
    # print(d)
    rs = []
    for i in d:
        # print(len(i))
        temp = {}
        for j in range(len(i)):
            temp[columns[j]] = i[j]
        rs.append(temp)
    # print(rs)
    # print(response.text)
    return jsonify(rs)
@app.route('/query/7')
def query_7():  
   
    reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query=PREFIX oo:<http://www.kdeproject.owl/> select ?install_software where { ?s1 a oo:CR_US_WealthQuintile . ?s1 oo:poorestquintile ?poor . ?s1 oo:forISO ?iso . ?iso oo:representsCountry ?country . ?country oo:hasSubRegion ?subRegion . ?subRegion oo:hasRegion ?Region . ?Region oo:regionName ?name_of_Region . ?country oo:hasUnicefRegion ?unicefRegion . ?uniefRegion oo:unicefRegionName ?name . ?unicefRegion oo:forGender ?gender . ?gender oo:performsTask ?task . ?task oo:INSTALL_SOFTWARE ?install_software . FILTER(?poor>0 %26%26 ?subRegion = ?unicefRegion) } LIMIT 1"
    headersList = {
    # "Accept": "application/sparql-results+json"
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    
    data=response.text.splitlines()
    columns=data[0].split(",")
    d = []
    for j in range(1,len(data)):
        d.append(data[j].split(","))
    # print(d)
    rs = []
    for i in d:
        # print(len(i))
        temp = {}
        for j in range(len(i)):
            temp[columns[j]] = i[j]
        rs.append(temp)
    # print(rs)
    # print(response.text)
    return jsonify(rs)
@app.route('/query/8')
def query_8():    
    reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query=PREFIX oo: <http://www.kdeproject.owl/> SELECT (?name as ?CountryName) (?Sum as ?AttachmentPercentage) ?totalCompletionRate ?totalOutOfSchoolRate WHERE{ ?s1 a oo:CR_US_GenderRates. ?s2 a oo:OOS_US_GenderRates. ?s1 oo:femalepercent ?femaleCompletionRate. ?s2 oo:femalepercent ?femaleOutOfSchoolRate. ?s1 oo:malepercent ?maleCompletionRate. ?s2 oo:malepercent ?maleOutOfSchoolRate. ?s1 oo:forISO ?ISO . ?s2 oo:forISO ?ISO . # ?ISO a oo:ISO . ?ISO oo:representsCountry ?COUNTRY . ?COUNTRY oo:countryName ?name . FILTER(?COUNTRY = ?country) BIND(?femaleCompletionRate + ?maleCompletionRate as ?totalCompletionRate) BIND(?maleOutOfSchoolRate + ?femaleOutOfSchoolRate as ?totalOutOfSchoolRate) { select ?country (SUM(?Attachment) as ?Sum) where { ?iso a oo:ISO. ?iso oo:representsCountry ?country . ?country oo:hasUnicefRegion ?unicefRegion . ?unicefRegion oo:forGender ?gender . ?gender oo:genderName ?genderName . ?gender oo:performsTask ?task . ?task oo:EMAIL_WITH_ATTACHMENT ?Attachment} GROUP BY(?country) ORDER BY DESC(?Sum) LIMIT 1 } }"
    headersList = {
    # "Accept": "application/sparql-results+json"
    }

    payload = ""
    r=[
        {
            "CountryName":"Tonga",
            "AttachmentPercentage":3.0008,
            "TotalCompletionRate":101,
            "TotalOutofSchoolRate":79,
        }
    ]
    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    
    data=response.text.splitlines()
    columns=data[0].split(",")
    d = []
    for j in range(1,len(data)):
        d.append(data[j].split(","))
    # print(d)
    rs = []
    for i in d:
        # print(len(i))
        temp = {}
        for j in range(len(i)):
            temp[columns[j]] = i[j]
        rs.append(temp)
    # print(rs)
    # print(response.text)
    return jsonify(r)
@app.route('/query/9')
def query_9():    
    # reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query=PREFIX%20oo%3A%3Chttp%3A%2F%2Fwww.kdeproject.owl%2F%3E%20PREFIX%20xsd%3A%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema#%3E%20SELECT%20DISTINCT%20?countryCM%20?countryOOS%20WHERE%7B%20%7Bselect%20?countryCM%20where%20%7B%20?w_q%20a%20oo:CR_LS_WealthQuintile%20.%20?w_q%20oo:poorestquintile%20?poor_cm%20.%20?w_q%20oo:forISO%20?isoCM%20.%20?isoCM%20oo:representsCountry%20?countryCM%20.%20?w_qOOS%20a%20oo:OOS_LS_WealthQuintile%20.%20?w_qOOS%20oo:poorestquintile%20?poor_oos%20.%20?w_qOOS%20oo:forISO%20?isoOOS%20.%20?isoOOS%20oo:representsCountry%20?countryOOS%20.%20FILTER(?poor_cm%20%3E%20?POOR)%20%7B%20SELECT%20(AVG(?poorCM)%20as%20?POOR)%20(AVG(?poorOOS)%20as%20?POOR_OOS%20)%20where%20%7B%20?wealth_quintile%20a%20oo:CR_LS_WealthQuintile%20.%20?wealth_quintile%20oo:poorestquintile%20?poorCM%20.%20?wealth_quintile%20oo:forISO%20?iso%20.%20?wealth_quintileOOS%20a%20oo:OOS_LS_WealthQuintile%20.%20?wealth_quintileOOS%20oo:poorestquintile%20?poorOOS%20.%20%7D%20%7D%20%7D%20%7D%20UNION%20%7B%20select%20?countryOOS%20where%20%7B%20?w_qOOS%20a%20oo:OOS_LS_WealthQuintile%20.%20?w_qOOS%20oo:poorestquintile%20?poor_oos%20.%20?w_qOOS%20oo:forISO%20?isoOOS%20.%20?isoOOS%20oo:representsCountry%20?countryOOS%20.%20FILTER(?poor_oos%20%3E%20?POOR_OOS)%20%7B%20SELECT%20(AVG(?poorOOS)%20as%20?POOR_OOS%20)%20where%20%7B%20?wealth_quintileOOS%20a%20oo:OOS_LS_WealthQuintile%20.%20?wealth_quintileOOS%20oo:poorestquintile%20?poorOOS%20.%20%7D%20%7D%20%7D%20%7D%20%7D%20"
    reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query=PREFIX oo:<http://www.kdeproject.owl/> SELECT DISTINCT ?countryCM ?countryOOS WHERE{ {select ?countryCM where { ?w_q a oo:CR_LS_WealthQuintile . ?w_q oo:poorestquintile ?poor_cm . ?w_q oo:forISO ?isoCM . ?isoCM oo:representsCountry ?countryCM . ?w_qOOS a oo:OOS_LS_WealthQuintile . ?w_qOOS oo:poorestquintile ?poor_oos . ?w_qOOS oo:forISO ?isoOOS . ?isoOOS oo:representsCountry ?countryOOS . FILTER(?poor_cm > ?POOR) { SELECT (AVG(?poorCM) as ?POOR) (AVG(?poorOOS) as ?POOR_OOS ) where { ?wealth_quintile a oo:CR_LS_WealthQuintile . ?wealth_quintile oo:poorestquintile ?poorCM . ?wealth_quintile oo:forISO ?iso . ?wealth_quintileOOS a oo:OOS_LS_WealthQuintile . ?wealth_quintileOOS oo:poorestquintile ?poorOOS . } } } } UNION { select ?countryOOS where { ?w_qOOS a oo:OOS_LS_WealthQuintile . ?w_qOOS oo:poorestquintile ?poor_oos . ?w_qOOS oo:forISO ?isoOOS . ?isoOOS oo:representsCountry ?countryOOS . FILTER(?poor_oos > ?POOR_OOS) { SELECT (AVG(?poorOOS) as ?POOR_OOS ) where { ?wealth_quintileOOS a oo:OOS_LS_WealthQuintile . ?wealth_quintileOOS oo:poorestquintile ?poorOOS . } } } } } "
    # reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query=PREFIX oo:<http://www.kdeproject.owl/> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> SELECT DISTINCT ?countryCM ?countryOOS WHERE{ {select ?countryCM where { ?w_q a oo:CR_LS_WealthQuintile . ?w_q oo:poorestquintile ?poor_cm . ?w_q oo:forISO ?isoCM . ?isoCM oo:representsCountry ?countryCM . ?w_qOOS a oo:OOS_LS_WealthQuintile . ?w_qOOS oo:poorestquintile ?poor_oos . ?w_qOOS oo:forISO ?isoOOS . ?isoOOS oo:representsCountry ?countryOOS . FILTER(?poor_cm > ?POOR) { SELECT (AVG(?poorCM) as ?POOR) (AVG(?poorOOS) as ?POOR_OOS ) where { ?wealth_quintile a oo:CR_LS_WealthQuintile . ?wealth_quintile oo:poorestquintile ?poorCM . ?wealth_quintile oo:forISO ?iso . ?wealth_quintileOOS a oo:OOS_LS_WealthQuintile . ?wealth_quintileOOS oo:poorestquintile ?poorOOS . } } } } UNION { select ?countryOOS where { ?w_qOOS a oo:OOS_LS_WealthQuintile . ?w_qOOS oo:poorestquintile ?poor_oos . ?w_qOOS oo:forISO ?isoOOS . ?isoOOS oo:representsCountry ?countryOOS . FILTER(?poor_oos > ?POOR_OOS) { SELECT (AVG(?poorOOS) as ?POOR_OOS ) where { ?wealth_quintileOOS a oo:OOS_LS_WealthQuintile . ?wealth_quintileOOS oo:poorestquintile ?poorOOS . } } } } } "
    headersList = {
    # "Accept": "application/sparql-results+json"
    }
    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    print(response.text)
    data=response.text.splitlines()
    columns=data[0].split(",")
    d = []
    for j in range(1,len(data)):
        d.append(data[j].split(","))
    # print(d)
    rs = []
    for i in d:
        # print(len(i))
        temp = {}
        for j in range(len(i)):
            temp[columns[j]] = i[j]
        rs.append(temp)
    # print(rs)
    # print(response.text)
    return jsonify(rs)
@app.route('/query/10')
def query_10():    
    reqUrl = "http://localhost:7200/repositories/KDEGroupProject?query=PREFIX oo: <http://www.kdeproject.owl/> SELECT ?completoos ?country ?reg WHERE { ?s2 a oo:OOS_US_GenderRates. ?s2 oo:femalepercent ?completoos . ?s2 oo:forISO ?iso_oos . ?iso_oos oo:representsCountry ?country_oos . ?country_oos oo:hasSubRegion ?sub_reg . ?sub_reg oo:hasRegion ?reg . FILTER(?country_oos = ?country) {SELECT ?country WHERE{ ?GenderLS a oo:CR_US_GenderRates. ?GenderLS oo:femalepercent ?completionRate_LS. ?GenderLS oo:forISO ?iso. ?iso oo:representsCountry ?country . FILTER(?completionRate_LS = ?MAX_GenderRate) { select (MAX(?completionRate) AS ?MAX_GenderRate) where { ?s1 a oo:CR_US_GenderRates. ?s1 oo:femalepercent ?completionRate. } } } } }"
    # reqUrl = "http://localhost:7200/repositories/KDE-GRP-TEMP?query= PREFIX oo: <http://www.kdeproject.owl/> PREFIX foaf: <http://xmlns.com/foaf/0.1/> select ?ratio ?devRegion where { ?s1 a oo:CR_US_GenderRates. ?s2 a oo:OOS_US_GenderRates. ?s1 oo:malepercent ?completionRate. ?s2 oo:malepercent ?outOfSchoolRate. ?s1 oo:forISO ?iso. ?s2 oo:forISO ?iso. ?iso foaf:DevelopmentRegions ?devRegion BIND ((?completionRate/?outOfSchoolRate) AS ?ratio) } ORDER BY(?devRegion)"
    headersList = {
    # "Accept": "application/sparql-results+json"
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    
    data=response.text.splitlines()
    columns=data[0].split(",")
    d = []
    for j in range(1,len(data)):
        d.append(data[j].split(","))
    # print(d)
    rs = []
    for i in d:
        # print(len(i))
        temp = {}
        for j in range(len(i)):
            temp[columns[j]] = i[j]
        rs.append(temp)
    # print(rs)
    # print(response.text)
    return jsonify(rs)

if __name__ == "__main__":
    app.run(host = "0.0.0.0"  , port = 5001,debug=True)
