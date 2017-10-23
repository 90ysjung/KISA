import csv
import json
import os

BASE_DIR = 'C:\ysjung\KISA\data' + '\\'
file_name = 'COLLECT_C8000.json'

with open(os.path.join(BASE_DIR, file_name), 'r', encoding='UTF8') as data_file:
    data = json.load(data_file)    ## loads() or load() ...?

rr = []
n = 'N/A'
for x in data:
    r = []

    r.append(x["date"]["$date"])
    r.append(x["offset"])
    r.append(x["path"])
    r.append(x["channel"])
    externals = x.get("ctex:externals", n)  ## 필드가 존재하지 않을 때
    if externals == n:
        r.append(n)   ## 하위 필드 개수..?
    else:
        title = externals.get("ctex:title", n)        # ctex:externals/ctex:title
        if title == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["ctex:title"])
        method = externals.get("ctex:method", n)          # ctex:externals/ctex:method
        if method == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["ctex:method"])
        channel = externals.get("ctex:method", n)         # ctex:externals/ctex:channel
        if channel == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["ctex:channel"])
        source = externals.get("ctex:method", n)          # ctex:externals/ctex:source
        if source == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["ctex:source"])
    r.append(x["_id"]["$oid"])    ## 상위 level인 id 필드를 중간에 찍어 줌
    if externals == n:
        r.append(n)   ## 하위 필드 개수..?
    else:
        version = externals.get("ctex:version", n)      # ctex:externals/ctex:version
        if version == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["ctex:version"])
        title = externals.get("ctex:title", n)          # ctex:externals/ctex:title
        if title == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["ctex:title"])
        method = externals.get("ctex:method", n)          # ctex:externals/ctex:method
        if method == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["ctex:method"])
        channel = externals.get("ctex:method", n)         # ctex:externals/ctex:channel
        if channel == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["ctex:channel"])
        source = externals.get("ctex:method", n)          # ctex:externals/ctex:source
        if source == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["ctex:source"])
        comment = externals.get("ctex:comment", n)       #  ctex:externals/ctex:comment
        if comment == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["ctex:comment"])
        xmlns = externals.get("@xmlns:ctex", n)        #  ctex:externals/@xmlns:ctex
        if xmlns == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["@xmlns:ctex"])
        xsi = externals.get("@xmlns:xsi", n)      # ctex:externals/@xmlns:xsi
        if xsi == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["@xmlns:xsi"])
        schemaLocation = externals.get("@xsi:schemaLocation", n)   # ctex:externals/@xsi:schemaLocation
        if schemaLocation == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["@xsi:schemaLocation"])
        schemaLocation = externals.get("@xmlns:schemaLocation", n)   # ctex:externals/@xmlns:schemaLocation
        if schemaLocation == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["@xmlns:schemaLocation"])
        noNamespaceSchemaLocation = externals.get("@xsi:noNamespaceSchemaLocation", n)     # ctex:externals/@xsi:noNamespaceSchemaLocation
        if noNamespaceSchemaLocation == n:
            r.append(n)
        else:
            r.append(x["ctex:externals"]["@xsi:noNamespaceSchemaLocation"])

        when = externals.get("ctex:when", n)
        if when == n:
            r.append(n)
        else:
            date = when.get("ctex:date", n)      # ctex:externals/ctex:when/ctex:date
            if date == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:when"]["ctex:date"])
            time = when.get("ctex:time", n)      # ctex:externals/ctex:when/ctex:time
            if time == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:when"]["ctex:time"])
        report = externals.get("ctex:report", n)
        if report == n:
            r.append(n)
        else:
            path = report.get("ctex:path", n)  # ctex:externals/ctex:report/ctex:path
            if path == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:report"]["ctex:path"])
            item = report.get("ctex:item", n)  # ctex:externals/ctex:report/ctex:item
            if item == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:report"]["ctex:item"])
            caption = report.get("ctex:caption", n)   # ctex:externals/ctex:report/ctex:caption
            if caption  == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:report"]["ctex:caption"])
            compress = report.get("compress", n)     # ctex:externals/ctex:report/ctex:@compress
            if compress  == n:
                r.append (n)
            else:
                r.append(x["ctex:externals"]["ctex:report"]["ctex:compress"])
        address = externals.get("ctex:address", n)
        if address == n:
            r.append(n)
        else:
            ip = address.get("ctex:ip", n)      # ctex:externals/ctex:address/ctex:ip
            if ip == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:address"]["ctex:ip"])
            icountry = address.get("ctex:icountry", n)    # ctex:externals/ctex:address/ctex:icountry
            if icountry == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:address"]["ctex:icountry"])
            domain = address.get("ctex:domain", n)     # ctex:externals/ctex:address/ctex:domain
            if domain == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:address"]["ctex:domain"])
            dcountry = address.get("ctex:dcountry", n)    # ctex:externals/ctex:address/ctex:dcountry
            if dcountry == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:address"]["ctex:dcountry"])
            port = address.get("ctex:port", n)    # ctex:externals.ctex:address.ctex:port
            if port == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:address"]["ctex:port"])
            url = address.get("ctex:url" , n)    # ctex:externals.ctex:address.ctex:url
            if url == n:
                r.append(n)
            else:
                r.append(x["ctex:externals"]["ctex:address"]["ctex:url"])
    export = x.get("ctex:export", n)
    if export == n:
        r.append(n)
    else:
        ctex = export.get("@xmlns:ctex", n)     # ctex:export/@xmlns:ctex
        if ctex == n:
            r.append(n)
        else:
            r.append(x["ctex:export"]["@xmlns:ctex"])
        xsi = export.get("@xmlns:xsi", n)        # ctex:export/@xmlns:xsi
        if xsi == n:
            r.append(n)
        else:
            r.append(x["ctex:export"]["@xmlns:xsi"])
        schemaLocation = export.get("@xsi:schemaLocation", n)     # ctex:export/@xsi:schemaLocation
        if  schemaLocation  == n:
            r.append(n)
        else:
            r.append(x["ctex:export"]["@xsi:schemaLocation"])
        when = export.get("ctex:when", n)
        if when == n:
            r.append(n)
        else:
            date = when.get("ctex:date", n)     # ctex:export/ctex:when/ctex:date
            if date == n:
                r.appen(n)
            else:
                r.append(x["ctex:export"]["ctex:when"]["ctex:date"])
            time = when.get("ctex:time", n)     # ctex:export/ctex:when/ctex:time
            if time == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:when"]["ctex:time"])
        sample = export.get("ctex:sample", n)
        if sample  == n:
            r.append(n)
        else:
            md5 = sample.get("ctex:md5", n)    # ctex:export/ctex:sample/ctex:md5
            if md5 ==n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:sample"]["ctex:md5"])
            sha1 = sample.get("ctex:sha1", n)    # ctex:export/ctex:sample/ctex:sha1
            if sha1  == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:sample"]["ctex:sha1"])
            ssdeep = sample.get("ctex:ssdeep", n)    # ctex:export/ctex:sample/ctex:ssdeep
            if ssdeep  == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:sample"]["ctex:ssdeep"])
            name = sample.get("ctex:name", n)    # ctex:export/ctex:sample/ctex:name
            if name == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:sample"]["ctex:name"])
            type = sample.get("ctex:type", n)    # ctex:export/ctex:sample/ctex:type
            if type == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:sample"]["ctex:type"])
            report = sample.get("ctex:report", n)
            if report  == n:
                r.append(n)
            else:
                path = report.get("ctex:path", n)  # ctex:export/ctex:sample/ctex:report/ctex:path
                if path == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:sample"]["ctex:report"]["ctex:path"])
                item = report.get("ctex:item", n)    # ctex:export/ctex:sample/ctex:report/ctex:item
                if item == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:sample"]["ctex:report"]["ctex:item"])
                caption = report.get("ctex:caption", n)    # ctex:export/ctex:sample/ctex:report/ctex:caption
                if caption  == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:sample"]["ctex:report"]["ctex:caption"])
                compress = report.get("ctex:@compress", n)  # ctex:export/ctex:sample/ctex:report/ctex:@compress
                if compress == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:sample"]["ctex:report"]["ctex:@compress"])
        address = export.get("ctex:address", n)
        if address  == n :
            r.append(n)
        else :
            domain = address.get("ctex:domain", n)           # ctex:export/ctex:address/ctex:domain
            if domain  == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:address"]["ctex:domain"])
            dcountry = address.get("ctex:dcountry", n)     # ctex:export/ctex:address/ctex:dcountry
            if dcountry  == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:address"]["ctex:dcountry"])
            ip = address.get("ctex:ip", n)                   # ctex:export/ctex:address/ctex:ip
            if ip == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:address"]["ctex:ip"])
            icountry = address.get("ctex:icountry", n)        # ctex:export/ctex:address/ctex:icountry
            if icountry  == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:address"]["ctex:icountry"])
            protocol = address.get("ctex:protocol", n)      # ctex:export/ctex:address/ctex:protocol
            if protocol  == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:address"]["ctex:protocol"])
            port = address.get("ctex:port", n)      # ctex:export/ctex:address/ctex:port
            if port  == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:address"]["ctex:port"])
            url = address.get("ctex:url", n)      # ctex:export/ctex:address/ctex:url
            if url  == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:address"]["ctex:url"])
            type = address.get("ctex:type", n)      # ctex:export/ctex:address/ctex:type
            if type  == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:address"]["ctex:type"])
        vulnerability = export .get("ctex:vulnerability", n)
        if vulnerability == (n):
            r.append(n)
        else:
            id = vulnerability.get("ctex:id")    # ctex:export/ctex:vulnerability/ctex:id
            if id == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:id"])
            cve = vulnerability.get("ctex:cve")    # ctex:export/ctex:vulnerability/ctex:cve
            if cve == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:cve"])
            kve = vulnerability.get("ctex:kve")    # ctex:export.ctex:vulnerability.ctex:kve
            if kve == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:kve"])
            company = vulnerability.get("ctex:company")    # ctex:export.ctex:vulnerability.ctex:company
            if company == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:company"])
            product = vulnerability.get("ctex:product")    # ctex:export.ctex:vulnerability.ctex:product
            if product == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:product"])
            effected = vulnerability.get("ctex:effected")   # ctex:export.ctex:vulnerability.ctex:effected
            if effected == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:effected"])
            type = vulnerability.get("ctex:type")   # ctex:export.ctex:vulnerability.ctex:type
            if type == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:type"])
            report = vulnerability.get("ctex:report")
            if report == n:
                r.append(n)
            else:
                path = report.get("ctex:path", n)       # ctex:export/ctex:vulnerability/ctex:report/ctex:path
                if path  == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:report"]["ctex:path"])
                item = report.get("ctex:item", n)       # ctex:export/ctex:vulnerability/ctex:report/ctex:item
                if item  == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:report"]["ctex:item"])
                caption = report.get("ctex:caption", n)       # ctex:export/ctex:vulnerability/ctex:report/ctex:caption
                if caption  == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:report"]["ctex:caption"])
                compress = report.get("ctex:@compress", n)       # ctex:export.ctex:vulnerability.ctex:report/ctex:@compress
                if compress  == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:report"]["ctex:@compress"])
            poc = vulnerability.get("ctex:poc", n)
            if poc == n:
                r.append(n)
            else:
                path = poc.get("ctex:path", n)          # ctex:export/ctex:vulnerability/ctex:poc/ctex:path
                if path == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:poc"]["ctex:path"])
                item = poc.get("ctex:item", n)          # ctex:export/ctex:vulnerability/ctex:poc/ctex:item
                if item == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:poc"]["ctex:item"])
                caption = poc.get("ctex:caption", n)          # ctex:export.ctex:vulnerability.ctex:poc.ctex:caption
                if caption == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:poc"]["ctex:caption"])
                compress = poc.get("ctex:@compress", n)          # ctex:export.ctex:vulnerability.ctex:poc.ctex:@compress
                if compress == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:vulnerability"]["ctex:poc"]["ctex:@compress"])
        message = export.get("ctex:message", n)
        if message == n:
            r.append(n)
        else:
            subject = message.get("ctex:subject", n)    # ctex:export/ctex:message/ctex:subject
            if subject == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:message"]["ctex:subject"])
            fron = message.get("ctex:from", n)       # ctex:export/ctex:message/ctex:from
            if fron  == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:message"]["ctex:from"])
            to = message.get("ctex:to", n)    # ctex:export/ctex:message/ctex:to
            if to == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:message"]["ctex:to"])
            content = message.get("ctex:content", n)    # ctex:export/ctex:message/ctex:content
            if content == n:
                r.append(n)
            else:
                r.append(x["ctex:export"]["ctex:message"]["ctex:content"])
            sent = message.get("ctex:sent", n)
            if sent == n:
                r.append(n)
            else:
                date = sent.get("ctex:date", n)   # ctex:export/ctex:message/ctex:sent/ctex:date
                if date == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:message"]["ctex:sent"]["ctex:date"])
                time = sent.get("ctex:time", n)   # ctex:export/ctex:message/ctex:sent/ctex:time
                if time == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:message"]["ctex:sent"]["ctex:time"])
            received = message.get("ctex:received", n)
            if received == n:
                r.append(n)
            else:
                date = received.get("ctex:date", n)     # ctex:export/ctex:message/ctex:received/ctex:date
                if date == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:message"]["ctex:received"]["ctex:date"])
                time = received.get("ctex:time", n)     # ctex:export/ctex:message/ctex:received/ctex:time
                if time == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:message"]["ctex:received"]["ctex:time"])
            attach = message.get("ctex:attach", n)
            if attach == n:
                r.append(n)
            else:
                md5 == attach.get("ctex:md5", n)     # ctex:export/ctex:message/ctex:attach/ctex:md5
                if md5 == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:message"]["ctex:attach"]["ctex:md5"])
                sha1 == attach.get("ctex:sha1", n)     # ctex:export/ctex:message/ctex:attach/ctex:sha1
                if sha1 == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:message"]["ctex:attach"]["ctex:sha1"])
                ssdeep == attach.get("ctex:ssdeep", n)     # ctex:export/ctex:message/ctex:attach/ctex:ssdeep
                if ssdeep == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:message"]["ctex:attach"]["ctex:ssdeep"])
                name == attach.get("ctex:name", n)     # ctex:export/ctex:message/ctex:attach/ctex:name
                if name == n:
                    r.append(n)
                else:
                    r.append(x["ctex:export"]["ctex:message"]["ctex:attach"]["ctex:name"])
                report == attach.get("ctex:report", n)     
                if report == n:
                    r.append(n)
                else:
                    path = report.get("ctex:path", n)    # ctex:export/ctex:message/ctex:attach/ctex:report/ctex:path
                    if path == n:
                        r.appned(n)
                    else:
                        r.append(x["ctex:export"]["ctex:message"]["ctex:attach"]["ctex:report"]["ctex:path"])
                    item = report.get("ctex:item", n)    # ctex:export/ctex:message/ctex:attach/ctex:report/ctex:item
                    if item == n:
                        r.appned(n)
                    else:
                        r.append(x["ctex:export"]["ctex:message"]["ctex:attach"]["ctex:report"]["ctex:item"])
                    caption = report.get("ctex:caption", n)    # ctex:export/ctex:message/ctex:attach/ctex:report/ctex:caption
                    if caption == n:
                        r.appned(n)
                    else:
                        r.append(x["ctex:export"]["ctex:message"]["ctex:attach"]["ctex:report"]["ctex:caption"])
               #     compress = report.get("ctex:@compress", n)    # ctex:export.ctex:message.ctex:attach.ctex:report.ctex:@compress
               #     if compress == n:
               #         r.appned(n)
               #     else:
               #         r.appned(n)  # r.append(x["ctex:export"]["ctex:message"]["ctex:attach"]["ctex:report"]["ctex:@compress"])
    when = x.get("ctex:when", n)
    if when == n:
        r.append(n) 
    else:
        date = when.get("ctex:date", n)   # ctex:when/ctex:date
        if date == n:
            r.append(n)
        else:
            r.append(x["ctex:when"]["ctex:date"])
        time = when.get("ctex:time", n)   # ctex:when/ctex:time
        if time == n:
            r.append(n)
        else:
            r.append(x["ctex:when"]["ctex:time"])
    #    ns2 = x.get("ns2:externals", n)
    #    if when == n:
    #        r.append(n) 
    #    else:
        #    title = ns2.get("ns2:title", n)  # ns2:externals.ns2:title
        #    if title == n:
        #        r.append(n)
        #    else:
        #         r.append(x["ns2:externals"]["ns2:title"])
        #    method = ns2.get("ns2:method", n)  # ns2:externals.ns2:method
        #    if method == n:
        #        r.append(n)
        #    else:
        #         r.append(x["ns2:externals"]["ns2:method"]) 
        #    channel = ns2.get("ns2:channel", n)  # ns2:externals.ns2:channel
        #    if channel == n:
        #        r.append(n)
        #    else:
        #         r.append(x["ns2:externals"]["ns2:channel"])
        #    source = ns2.get("ns2:source", n)  # ns2:externals.ns2:source
        #    if source == n:
        #        r.append(n)
        #    else:
        #         r.append(x["ns2:externals"]["ns2:source"])
        #     comment = ns2.get("ns2:comment", n)  # ns2:externals.ns2:comment
        #     if comment == n:
        #         r.append(n)
        #     else:
        #          r.append(x["ns2:externals"]["ns2:comment"])
        #     xmlns = ns2.get("ns2:@xmlns", n)  # ns2:externals.ns2:@xmlns
        #     if xmlns == n:
        #         r.append(n)
        #     else:
        #          r.append(x["ns2:externals"]["ns2:@xmlns"]) 
        #when = ns2.get("ns2:when", n)
        #if when == n:
        #    r.append(n)
        #else:
        #    date = when.get("ns2:date", n)      # ns2:externals.ns2:when.ns2:date 
        #    if date == n:
        #        r.append(n)
        #    else:
        #        r.append(x["ns2:externals"]["ns2:when"]["ns2:date"])
        #    time = when.get("ns2:time", n)      # ns2:externals.ns2:when.ns2:time
        #    if time == n:
        #        r.append(n)
        #    else:
        #        r.append(x["ns2:externals"]["ns2:when"]["ns2:time"])

    rr.append(r)
#print(rr)
print(len(rr), "rows")

f = csv.writer(open('C8000_level_1.csv', 'w', newline= ''))

# Write CSV Header , 총 87개..
f.writerow(["date", "offset", "path", "channel", "ctex:title", "ctex:method", "ctex:channel", "ctex:source", "_id.$oid", "ctex:externals.ctex:version", "ctex:externals.ctex:title", "ctex:externals.ctex:method", "ctex:externals.ctex:channel", "ctex:externals.ctex:source", "ctex:externals.ctex:comment", "ctex:externals.@xmlns:ctex", "ctex:externals.@xmlns:xsi", "ctex:externals.@xsi:schemaLocation", "ctex:externals.@xmlns:schemaLocation", "ctex:externals.@xsi:noNamespaceSchemaLocation", "ctex:externals.ctex:when.ctex:date", "ctex:externals.ctex:when.ctex:time", "ctex:externals.ctex:report.ctex:path", "ctex:externals.ctex:report.ctex:item", "ctex:externals.ctex:report.ctex:caption", "ctex:externals.ctex:report.ctex:@compress", "ctex:externals.ctex:address.ctex:ip", "ctex:externals.ctex:address.ctex:icountry", "ctex:externals.ctex:address.ctex:domain", "ctex:externals.ctex:address.ctex:dcountry", "ctex:externals.ctex:address.ctex:port", "ctex:externals.ctex:address.ctex:url", "ctex:externals.ctex:address.ctex:type", "ctex:export.@xmlns:ctex", "ctex:export.@xmlns:xsi", "ctex:export.@xsi:schemaLocation", "ctex:export.ctex:when.ctex:date", "ctex:export.ctex:when.ctex:time", "ctex:export.ctex:sample.ctex:md5", "ctex:export.ctex:sample.ctex:sha1", "ctex:export.ctex:sample.ctex:ssdeep", "ctex:export.ctex:sample.ctex:name", "ctex:export.ctex:sample.ctex:type", "ctex:export.ctex:sample.ctex:report.ctex:path", "ctex:export.ctex:sample.ctex:report.ctex:item", "ctex:export.ctex:sample.ctex:report.ctex:caption", "ctex:export.ctex:sample.ctex:report.ctex:@compress", "ctex:export.ctex:address.ctex:domain", "ctex:export.ctex:address.ctex:dcountry", "ctex:export.ctex:address.ctex:ip", "ctex:export.ctex:address.ctex:icountry", "ctex:export.ctex:address.ctex:protocol", "ctex:export.ctex:address.ctex:port", "ctex:export.ctex:address.ctex:url", "ctex:export.ctex:address.ctex:type", "ctex:export.ctex:vulnerability.ctex:id", "ctex:export.ctex:vulnerability.ctex:cve", "ctex:export.ctex:vulnerability.ctex:kve", "ctex:export.ctex:vulnerability.ctex:company", "ctex:export.ctex:vulnerability.ctex:product", "ctex:export.ctex:vulnerability.ctex:effected", "ctex:export.ctex:vulnerability.ctex:type", "ctex:export.ctex:vulnerability.ctex:report.ctex:path", "ctex:export.ctex:vulnerability.ctex:report.ctex:item", "ctex:export.ctex:vulnerability.ctex:report.ctex:caption", "ctex:export.ctex:vulnerability.ctex:report.ctex:@compress", "ctex:export.ctex:vulnerability.ctex:poc.ctex:path", "ctex:export.ctex:vulnerability.ctex:poc.ctex:item", "ctex:export.ctex:vulnerability.ctex:poc.ctex:caption", "ctex:export.ctex:vulnerability.ctex:poc.ctex:@compress", "ctex:export.ctex:message.ctex:subject", "ctex:export.ctex:message.ctex:from", "ctex:export.ctex:message.ctex:to", "ctex:export.ctex:message.ctex:content", "ctex:export.ctex:message.ctex:sent.ctex:date", "ctex:export.ctex:message.ctex:sent.ctex:time", "ctex:export.ctex:message.ctex:received.ctex:date", "ctex:export.ctex:message.ctex:received.ctex:time", "ctex:export.ctex:message.ctex:attach.ctex:md5", "ctex:export.ctex:message.ctex:attach.ctex:sha1", "ctex:export.ctex:message.ctex:attach.ctex:ssdeep", "ctex:export.ctex:message.ctex:attach.ctex:name", "ctex:export.ctex:message.ctex:attach.ctex:report.ctex:path", "ctex:export.ctex:message.ctex:attach.ctex:report.ctex:item", "ctex:export.ctex:message.ctex:attach.ctex:report.ctex:caption", "ctex:when.ctex:date", "ctex:when.ctex:time"])

for out in rr:
    f.writerow(out)
