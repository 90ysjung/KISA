import json
import csv
import os, re

#BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\data'
BASE_DIR = 'C:\ysjung\KISA\data' + '\\'
# file_name = 'COLLECT_C0001.json'
file_name = 'COLLECT_C8000_5.json'


def read_json_file(directory, file_name):
    """ 디렉토리 명과 파일 명을 입력 받아 해당 파일을 JSON 객체로 반환하는  함수 """
    with open(os.path.join(directory, file_name), 'r', encoding='UTF8') as data_file:
        data = json.load(data_file)    ## loads()...?
    return data


def get_keys(file_name):
    data = read_json_file(BASE_DIR, file_name)

#    keys = [key for key in data[0]]
#    keys = data[0].keys()
    for key in data:
        if isinstance(key, dict):
            print(key.keys())
        else:
            print(key)
#    print(keys)


def print_all_items(file_name):
    """파라메터로 받은 파일명의 파일을 분석해서 해당 내용을 모두 출력"""
    data = read_json_file(BASE_DIR, file_name)  # JSON 파일 정보를 읽어온다.

    for i, values in enumerate(data):
        print('======================================= start =========================================')
        print('### row_num : ', i, ' ###')
        # _id {1}
        print('* _id : ')
        print('\t$oid : ', values['_id']['$oid'])

        # ctex:externals  {12}
        # ctex:externals 값을 읽어들이기 위해서 Instance 생성 후 Key 존재 유/무 체크
        externals = values.get('ctex:externals', 'N/A')
        if externals == 'N/A':  # Key 가 존재하지 않을 경우
            print('* ctex:externals : ', externals)
        else:                    # Key 가 존재할 경우
            print('* ctex:externals : ')
            print('\tctex:version : ', externals.get('ctex:version', 'N/A'))
            print('\tctex:title : ', externals.get('ctex:title', 'N/A'))

            # ctex:externals / ctex:when
            ctex_when = externals.get('ctex:when', 'N/A')
            if ctex_when == 'N/A':
                print('\tctex_when : ', ctex_when)
            else:
                print('\tctex_when : ')
                print('\t\tctex:date : ', ctex_when.get('ctex:date', 'N/A'))
                print('\t\tctex:time : ', ctex_when.get('ctex:time', 'N/A'))

            print('\tctex:method : ', externals.get('ctex:method', 'N/A'))
            print('\tctex:channel : ', externals.get('ctex:channel', 'N/A'))
            print('\tctex:source : ', externals.get('ctex:source', 'N/A'))

            # ctex:externals / ctex:report
            ctex_report = externals.get('ctex:report', 'N/A')
            if ctex_report == 'N/A':
                print('\tctex:report : ', ctex_report)
            else:
                print('\tctex:report : ')
                print('\t\tctex:path : ', ctex_report.get('ctex:path', 'N/A'))
                print('\t\tctex:item : ', ctex_report.get('ctex:item', 'N/A'))
                print('\t\tctex:caption : ', ctex_report.get('ctex:caption', 'N/A'))
                print('\t\t@compress : ', ctex_report.get('@compress', 'N/A'))

            print('\tctex:comment : ', externals.get('ctex:comment', 'N/A'))

            # ctex:externals / ctex:external
            ctex_external = externals.get('ctex:external', 'N/A')
            if ctex_external == 'N/A':
                print('\tctex:external : ', ctex_external)
            elif isinstance(ctex_external, list):  # external 가 List 인지 Dictionary 인지 체크 >> List 일 경우 반복처리
                for ctex_external_value in ctex_external:
                    print('\tctex:external : ')

                    # ctex:externals / ctex:external / ctex:when
                    ctex_when = ctex_external_value.get('ctex:when', 'N/A')
                    if ctex_when == 'N/A':
                        print('\t\tctex:when : ', 'N/A')
                    else:
                        print('\t\tctex:when : ')
                        print('\t\t\tctex:date : ', ctex_when.get('ctex:date', 'N/A'))
                        print('\t\t\tctex:time : ', ctex_when.get('ctex:time', 'N/A'))

                    print('\t\tctex:method : ', ctex_external_value.get('ctex:method', 'N/A'))
                    print('\t\tctex:channel : ', ctex_external_value.get('ctex:channel', 'N/A'))
                    print('\t\tctex:source : ', ctex_external_value.get('ctex:source', 'N/A'))

                    # ctex:externals / ctex:external / ctex:report
                    ctex_report = ctex_external_value.get('ctex:report', 'N/A')
                    if ctex_report == 'N/A':
                        print('\t\tctex:report : ', ctex_report)
                    else:
                        print('\t\tctex:report : ')
                        print('\t\t\tctex:path : ', ctex_report.get('ctex:path', 'N/A'))
                        print('\t\t\tctex:item : ', ctex_report.get('ctex:item', 'N/A'))
                        print('\t\t\tctex:caption : ', ctex_report.get('ctex:caption', 'N/A'))

                    print('\t\tctex:comment : ', ctex_external_value.get('ctex:comment', 'N/A'))

                    # ctex:externals / ctex:external / ctex:address
                    ctex_address = ctex_external_value.get('ctex:address', 'N/A')
                    if ctex_address == 'N/A':
                        print('\t\tctex:address : ', ctex_address)
                    elif isinstance(ctex_address, list):  # ctex:address 가 List 일경우 처리
                        for address_data in ctex_address:
                            print('\t\tctex:address : ')
                            print('\t\t\tctex:domain : ', address_data.get('ctex:domain', 'N/A'))
                            print('\t\t\tctex:dcountry : ', address_data.get('ctex:dcountry', 'N/A'))
                            print('\t\t\tctex:ip : ', address_data.get('ctex:ip', 'N/A'))
                            print('\t\t\tctex:icountry : ', address_data.get('ctex:icountry', 'N/A'))
                            print('\t\t\tctex:protocol : ', address_data.get('ctex:protocol', 'N/A'))
                            print('\t\t\tctex:port : ', address_data.get('ctex:port', 'N/A'))
                            print('\t\t\tctex:url : ', address_data.get('ctex:url', 'N/A'))
                            print('\t\t\tctex:type : ', address_data.get('ctex:type', 'N/A'))
                            print('\t\t\tctex:comment : ', address_data.get('ctex:comment', 'N/A'))
                    else:                                 # ctex:address 가 Dictionary 일 경우 처리
                        print('\t\tctex:address : ')
                        print('\t\t\tctex:domain : ', ctex_address.get('ctex:domain', 'N/A'))
                        print('\t\t\tctex:dcountry : ', ctex_address.get('ctex:dcountry', 'N/A'))
                        print('\t\t\tctex:ip : ', ctex_address.get('ctex:ip', 'N/A'))
                        print('\t\t\tctex:icountry : ', ctex_address.get('ctex:icountry', 'N/A'))
                        print('\t\t\tctex:protocol : ', ctex_address.get('ctex:protocol', 'N/A'))
                        print('\t\t\tctex:port : ', ctex_address.get('ctex:port', 'N/A'))
                        print('\t\t\tctex:url : ', ctex_address.get('ctex:url', 'N/A'))
                        print('\t\t\tctex:type : ', ctex_address.get('ctex:type', 'N/A'))
                        print('\t\t\tctex:comment : ', ctex_address.get('ctex:comment', 'N/A'))

                    # ctex:externals / ctex:external / ctex:sample
                    ctex_sample = ctex_external_value.get('ctex:sample', 'N/A')
                    if ctex_sample == 'N/A':
                        print('\t\tctex:sample : ', ctex_sample)
                    else:
                        print('\t\tctex:sample : ')
                        print('\t\t\tctex_md5 : ', ctex_sample.get('ctex:md5', 'N/A'))
                        print('\t\t\tctex_sha1 : ', ctex_sample.get('ctex:sha1', 'N/A'))
                        print('\t\t\tctex:ssdeep : ', ctex_sample.get('ctex:ssdeep', 'N/A'))

                        # ctex:externals / ctex:external / ctex_sample / ctex_report
                        ctex_report = ctex_sample.get('ctex_report', 'N/A')
                        if ctex_report == 'N/A':
                            print('\t\t\tctex:report : ', ctex_report)
                        else:
                            print('\t\t\tctex_report : ')
                            print('\t\t\t\tctex:path : ', ctex_report.get('ctex:path', 'N/A'))
                            print('\t\t\t\tctex:item : ', ctex_report.get('ctex:item', 'N/A'))
                            print('\t\t\t\tctex:caption : ', ctex_report.get('ctex:caption', 'N/A'))
                            print('\t\t\t\t@compress : ', ctex_report.get('@compress', 'N/A'))

                        print('\t\t\tctex:name : ', ctex_sample.get('ctex:name', 'N/A'))
                        print('\t\t\tctex:type : ', ctex_sample.get('ctex:type', 'N/A'))
                        print('\t\t\tctex:comment : ', ctex_sample.get('ctex:comment', 'N/A'))

                    # ctex:externals / ctex:external / ctex:message
                    ctex_message = ctex_external_value.get('ctex:message', 'N/A')
                    if ctex_message == 'N/A':
                        print('\t\tctex:message : ', ctex_message)
                    else:
                        print('\t\tctex:message : ')
                        print('\t\t\tctex:subject : ', ctex_message.get('ctex:subject', 'N/A'))
                        print('\t\t\tctex:from : ', ctex_message.get('ctex:from', 'N/A'))
                        print('\t\t\tctex:to : ', ctex_message.get('ctex:to', 'N/A'))

                        # ctex:externals / ctex:external / ctex:message / ctex:sent
                        ctex_sent = ctex_message.get('ctex:sent', 'N/A')
                        if ctex_sent == 'N/A':
                            print('\t\t\tctex:sent : ', ctex_sent)
                        else:
                            print('\t\t\tctex:sent : ')
                            print('\t\t\t\tctex:date : ', ctex_sent.get('ctex:date', 'N/A'))
                            print('\t\t\t\tctex:time : ', ctex_sent.get('ctex:time', 'N/A'))

                        # ctex:externals / ctex:external / ctex:message / ctex:sent
                        ctex_received = ctex_message.get('ctex:received', 'N/A')
                        if ctex_received == 'N/A':
                            print('\t\t\tctex:received : ', ctex_received)
                        else:
                            print('\t\t\tctex:received : ')
                            print('\t\t\t\tctex:date : ', ctex_received.get('ctex:date', 'N/A'))
                            print('\t\t\t\tctex:time : ', ctex_received.get('ctex:time', 'N/A'))

                        print('\t\t\tctex:content : ', ctex_message.get('ctex:content', 'N/A'))

                        # ctex:externals / ctex:external / ctex:message / ctex:attached
                        ctex_attached = ctex_message.get('ctex:attached', 'N/A')
                        if ctex_attached == 'N/A':
                            print('\t\t\tctex:attached : ', ctex_attached)
                        else:
                            print('\t\t\tctex:attached : ')
                            print('\t\t\t\tctex:md5 : ', ctex_attached.get('ctex:md5', 'N/A'))
                            print('\t\t\t\tctex:sh1 : ', ctex_attached.get('ctex:sh1', 'N/A'))
                            print('\t\t\t\tctex:ssdeep : ', ctex_attached.get('ctex:ssdeep', 'N/A'))

                            ctex_report = ctex_attached.get('ctex_report', 'N/A')
                            if ctex_report == 'N/A':
                                print('\t\t\t\tctex:report : ', ctex_report)
                            else:
                                print('\t\t\t\tctex_report : ')
                                print('\t\t\t\t\tctex:path : ', ctex_report.get('ctex:path', 'N/A'))
                                print('\t\t\t\t\tctex:item : ', ctex_report.get('ctex:item', 'N/A'))
                                print('\t\t\t\t\tctex:caption : ', ctex_report.get('ctex:caption', 'N/A'))

                        print('\t\t\tctex:comment : ', ctex_message.get('ctex:comment', 'N/A'))

            # ctex:externals
            print('\t@xmlns:ctex : ', externals.get('@xmlns:ctex', 'N/A'))
            print('\t@xmlns:xsi : ', externals.get('@xmlns:xsi', 'N/A'))
            print('\t@xsi:schemaLocation : ', externals.get('@xsi:schemaLocation', 'N/A'))

        # date {1}
        ctex_date = values.get('date', 'N/A')
        if ctex_date == 'N/A':
            print('* date : ', ctex_date)
        else:
            print('* date : ')
            print('\t$date : ', ctex_date.get('$date', 'N/A'))

        # offset ... {1}
        print('* offset : ', values.get('offset', 'N/A'))
        print('* path : ', values.get('path', 'N/A'))
        print('* channel : ', values.get('channel', 'N/A'))

        print('======================================== end ==========================================')

#################################################################


def print_one_level_keys(file_name):
    """ JSON 에서 Level 1 의 Key Name 출력 """
    data = read_json_file(BASE_DIR, file_name)

    for key in data[0].keys():
        print(key)


def json_to_cvs_all_data(file_name):
    """ JSON 파일 정보를 읽어서 필요한 정보를 CSV 파일로 저장하는 함수 
        예외처리를 위해서 JSON 구조에 맞춰 각각의 요소들을 분석해야 한다. 
    """
    
    # JSON 파일 정보 읽기
    json_data = read_json_file(BASE_DIR, file_name)

    result_list = []

    for item in json_data:
        # sub_result_list = []

        # sub_result_list.append(item['_id']['$oid'])   # id
        # sub_result_list.append(item['date']['$date'])    # date
        # sub_result_list.append(str(item['offset']))  # offset
        # sub_result_list.append(str(item['path']))  # path
        # sub_result_list.append(item['channel']) # channel

        # ID
        id_string = item['_id']['$oid']

        # Externals
        externals = item.get('ctex:externals', 'N/A')
        if externals == 'N/A':
            print('externals is not exist.')
        else:
            # Externals / External
            external = externals.get('ctex:external', 'N/A')
            if external == 'N/A':
                print('external is not exist.')
            elif isinstance(external, list):
                for external_values in external:
                    # Externals / External / Address
                    ctex_address = external_values.get('ctex:address', 'N/A')
                    if ctex_address == 'N/A':
                        print('ctex:address is not exist.')
                    elif isinstance(ctex_address, list):
                        for address_values in ctex_address:
                            sub_loop_list = []
                            sub_loop_list.append(id_string)
                            sub_loop_list.append(address_values.get('ctex:domain', 'N/A'))
                            sub_loop_list.append(address_values.get('ctex:dcountry', 'N/A'))
                            # ctex:ip 값 내용 중에 Escape 문자를 포함한 정보가 있어서 관련 부분을 정규식으로 처리
                            sub_loop_list.append(re.sub('[\r\n]', ' ', (address_values.get('ctex:ip', 'N/A'))))
                            sub_loop_list.append(address_values.get('ctex:icountry', 'N/A'))
                            sub_loop_list.append(address_values.get('ctex:protocol', 'N/A'))
                            sub_loop_list.append(address_values.get('ctex:port', 'N/A'))
                            sub_loop_list.append(address_values.get('ctex:url', 'N/A'))
                            sub_loop_list.append(address_values.get('ctex:type', 'N/A'))
                            result_list.append(sub_loop_list)
                    elif isinstance(ctex_address, dict):
                        sub_result_list = []
                        sub_result_list.append(id_string)
                        sub_result_list.append(ctex_address.get('ctex:domain', 'N/A'))
                        sub_result_list.append(ctex_address.get('ctex:dcountry', 'N/A'))
                        # ctex:ip 값 내용 중에 Escape 문자를 포함한 정보가 있어서 관련 부분을 정규식으로 처리
                        sub_result_list.append(re.sub('[\r\n]', ' ', (ctex_address.get('ctex:ip', 'N/A'))))
                        sub_result_list.append(ctex_address.get('ctex:icountry', 'N/A'))
                        sub_result_list.append(ctex_address.get('ctex:protocol', 'N/A'))
                        sub_result_list.append(ctex_address.get('ctex:port', 'N/A'))
                        sub_result_list.append(ctex_address.get('ctex:url', 'N/A'))
                        sub_result_list.append(ctex_address.get('ctex:type', 'N/A'))
                        result_list.append(sub_result_list)

                    else:
                        print('Exception Processing!')

    return result_list


def get_csv_file_name(json_file_name):
    """ CSV 파일명 생성 함수 """
    return json_file_name.split('.')[0] + '_csv_output.csv'


def create_csv_file(json_file_name):
    """ CSV 파일을 생성 하는 함수 """
    csv_header_list = ["id","external.ctex:domain", "external.ctex:dcountry", "external.ctex:ip",
                       "external.ctex:icountry", "external.ctex:protocol", "external.ctex:port",
                       "external.ctex:url", "external.ctex:type"]

    csv_file_name = get_csv_file_name(json_file_name)
    # JSON 파일정보 분석 후 List 반환
    output_csv_data = json_to_cvs_all_data(json_file_name)

    # print(type(output_csv_data))
    with open(os.path.join(BASE_DIR, csv_file_name), 'wb', newline='', encoding='utf8') as output_file:
        csv_file = csv.writer(output_file)

        for p_item in output_csv_data:
            csv_file.writerow(p_item)

# print_one_level_keys(file_name)
# print_all_items('COLLECT_C8000.json')
# get_keys('COLLECT_C8000.json')
# json_to_cvs_all_data('COLLECT_C8001.json')
create_csv_file('COLLECT_C8000.json')


