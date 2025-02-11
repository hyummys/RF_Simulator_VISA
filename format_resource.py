STX = "0x02"
ETX = "0x03"
SUCCESS = "0x00"

#main commands
CMD_SEND = "0xe8"
CMD_RECEIVE = "0xe9"

#sub commands
SUB_CMD_ACT = "0xb1"
SUB_CMD_STOP = "0xc5"
SUB_CMD_RF_RESET = "0x31"
SUB_CMD_GET_VERSION = "0xca"
SUB_CMD_CLEAN = "0xc6"
SUB_CMD_RECEIVE = "0xc1"

#extra commands
CMD_CONFIG_DATA = "0xa2"
CMD_TRXN_DATA = "0xa1"

#response codes
RES_SUCCESS = "0x00"
RES_STOP = "0x01"

#datas
DATA_RF_RESET = []
DATA_STOP = []
DATA_CLEAN = ['0x01']
DATA_CLEAN_ALL = ['0x02']


def combine_hex(hex_list):
    #combine hex list to string
    return ' '.join([item[2:] for item in hex_list])

def hex_to_bitlist(hex_data):
    binary_str = bin(int(hex_data, 16))[2:]
    binary_str = binary_str.zfill(8)
    bitlist = [int(bit) for bit in binary_str]
    return bitlist

def data_object_df8115(data):
    L1 = data[0] #1
    L1_msg = ""

    L2 = data[1] #1
    L2_msg = ""

    L3 = data[2] #1
    L3_msg = ""

    SW12 = data[3:3+2] #2

    Msg_on_Error = data[5] #1
    Msg_on_Error_msg = ""

    if L1 == '0x00':            L1_msg = "OK"
    elif L1 == '0x01':          L1_msg = "TIME OUT ERROR"
    elif L1 == '0x02':          L1_msg = "TRANSMISSION ERROR"
    elif L1 == '0x03':          L1_msg = "PROTOCOL ERROR"
    else :                      L1_msg = "RFU"
        
    if L2 == '0x00':            L2_msg = "OK"
    elif L2 == '0x01':          L2_msg = "CARD DATA MISSING"
    elif L2 == '0x02':          L2_msg = "CAM FAILED"
    elif L2 == '0x03':          L2_msg = "STATUS BYTES"
    elif L2 == '0x04':          L2_msg = "PARSING ERROR"
    elif L2 == '0x05':          L2_msg = "MAX LIMIT EXCEEDED"
    elif L2 == '0x06':          L2_msg = "CARD DATA ERROR"
    elif L2 == '0x07':          L2_msg = "MAGSTRIPE NOT SUPPORTED"
    elif L2 == '0x08':          L2_msg = "NO PPSE"
    elif L2 == '0x09':          L2_msg = "PPSE FAULT"
    elif L2 == '0x0a':          L2_msg = "EMPTY CANDIDATE LIST"
    elif L2 == '0x0b':          L2_msg = "IDS READ ERROR"
    elif L2 == '0x0c':          L2_msg = "IDS WRITE ERROR"
    elif L2 == '0x0d':          L2_msg = "IDS DATA ERROR"
    elif L2 == '0x0e':          L2_msg = "IDS NO MATCHING AC"
    elif L2 == '0x0f':          L2_msg = "TERMINAL DATA ERROR"
    else :                      L2_msg = "RFU"

    if L3 == '0x00':            L3_msg = "OK"
    elif L3 == '0x01':          L3_msg = "TIME OUT"
    elif L3 == '0x02':          L3_msg = "STOP"
    elif L3 == '0x03':          L3_msg = "AMOUNT NOT PRESENT"
    else :                      L3_msg = "RFU"

    if (L1 == '0x00') and (L2 == '0x00') and (L3 == '0x00'):
        Value = combine_hex(data[0:3])

    if Msg_on_Error == '0x17':        Msg_on_Error_msg = "CARD READ OK"
    elif Msg_on_Error == '0x21':      Msg_on_Error_msg = "TRY AGAIN"
    elif Msg_on_Error == '0x03':      Msg_on_Error_msg = "APPROVED"
    elif Msg_on_Error == '0x1a':      Msg_on_Error_msg = "APPROVED-SIGN"
    elif Msg_on_Error == '0x07':      Msg_on_Error_msg = "DECLINED"
    elif Msg_on_Error == '0x1c':      Msg_on_Error_msg = "ERROR-OTHER CARD"
    elif Msg_on_Error == '0x1d':      Msg_on_Error_msg = "INSERT CARD"
    elif Msg_on_Error == '0x20':      Msg_on_Error_msg = "SEE PHONE"
    elif Msg_on_Error == '0x1b':      Msg_on_Error_msg = "AUTHORISING-PLEASE WAIT"
    elif Msg_on_Error == '0x1e':      Msg_on_Error_msg = "CLEAR DISPLAY"
    elif Msg_on_Error == '0xff':      Msg_on_Error_msg = "N/A"
    else:                             Msg_on_Error_msg = "RFU"

    result = {
        f"  L1 [{L1}]" : L1_msg,
        f'  L2 [{L2}]' : L2_msg,
        f'  L3 [{L3}]' : L3_msg,
        '  SW12' : combine_hex(SW12),
        f'  Message on Error [{Msg_on_Error}]' : Msg_on_Error_msg,
    }

    if (L1 == '0x00') and (L2 == '0x00') and (L3 == '0x00'):
        result[f'  Value [{Value}]'] = "OK"

    return result

def data_object_df8116(data):
    msg_id = data[0] #1
    msg_id_msg = ""

    status = data[1] #1
    status_msg = ""

    hold_time = data[2:2+3] #3
    language_preference = data[5:5+8]

    value_qualifier = data[13] #1
    value_qualifier_msg = ""

    value = data[14:14+6] #6

    currency_code = data[20:20+2] #2

    if msg_id == '0x17':        msg_id_msg = "CARD READ OK"
    elif msg_id == '0x21':      msg_id_msg = "TRY AGAIN"
    elif msg_id == '0x03':      msg_id_msg = "APPROVED"
    elif msg_id == '0x1a':      msg_id_msg = "APPROVED-SIGN"
    elif msg_id == '0x07':      msg_id_msg = "DECLINED"
    elif msg_id == '0x1c':      msg_id_msg = "ERROR-OTHER CARD"
    elif msg_id == '0x1d':      msg_id_msg = "INSERT CARD"
    elif msg_id == '0x20':      msg_id_msg = "SEE PHONE"
    elif msg_id == '0x1b':      msg_id_msg = "AUTHORISING-PLEASE WAIT"
    elif msg_id == '0x1e':      msg_id_msg = "CLEAR DISPLAY"
    elif msg_id == '0xff':      msg_id_msg = "N/A"
    else:                       msg_id_msg = "RFU"
        
    if status == '0x00':        status_msg = "NOT READY"
    elif status == '0x01':      status_msg = "IDLE"
    elif status == '0x02':      status_msg = "READY TO READ"
    elif status == '0x03':      status_msg = "PROCESSING"
    elif status == '0x04':      status_msg = "CARD READ SUCCESSFULLY"
    elif status == '0x05':      status_msg = "PROCESSING ERROR"
    elif status == '0xff':      status_msg = "N/A"
    else:                       status_msg = "RFU"

    return {
        '<b style="color: blue">User Interface Request Data :</b>' : combine_hex(data),
        f'Message Identifier : [{msg_id}]' : msg_id_msg,
        f'Status : [{status}]' : status_msg,
        'Hold Time : ' : combine_hex(hold_time),
        'Language Preference : ' : combine_hex(language_preference),
        f'Value Qualifier [{value_qualifier}]: ' : "None",
        'Value : ' : combine_hex(value),
        'Currency Code : ' : combine_hex(currency_code)
    }

def data_object_df8129(data):
    status_id = data[0] #1
    status_id_msg = ""

    start_id = data[1] #1
    start_id_msg = ""

    online_response_data = data[2] #1
    online_response_data_msg = ""

    cvm_id = data[3] #1
    cvm_id_msg = ""

    b5 = hex_to_bitlist(data[4]) #1
    
    alternate_interface_preference_id = data[5] #1
    alternate_interface_preference_id_msg = ""

    field_off_request_id = data[6] #1
    field_off_request_id_msg = ""

    removal_timeout = data[7] #1
    removal_timeout_msg = ""

    if status_id == '0x10':            status_id_msg = "APPROVED"
    elif status_id == '0x20':          status_id_msg = "DECLINED"
    elif status_id == '0x30':          status_id_msg = "ONLINE REQUEST"
    elif status_id == '0x40':          status_id_msg = "END APPLICATION"
    elif status_id == '0x50':          status_id_msg = "SELECT NEXT"
    elif status_id == '0x60':          status_id_msg = "TRY ANOTHER INTERFACE"
    elif status_id == '0x70':          status_id_msg = "TRY AGAIN"
    elif status_id == '0xf0':          status_id_msg = "N/A"
    else:                               status_id_msg = "RFU"  

    if start_id == '0x00':              start_id_msg = "A"
    elif start_id == '0x10':            start_id_msg = "B"
    elif start_id == '0x20':            start_id_msg = "C"
    elif start_id == '0x30':            start_id_msg = "D"
    elif start_id == '0xf0':            start_id_msg = "N/A"
    else:                               start_id_msg = "RFU"

    if online_response_data == '0xf0':  online_response_data_msg = "N/A"
    else:                               online_response_data_msg = "RFU"

    if cvm_id == '0x00':                cvm_id_msg = "NO CVM"
    elif cvm_id == '0x10':              cvm_id_msg = "OBTAIN SIGNATURE"
    elif cvm_id == '0x20':              cvm_id_msg = "ONLINE PIN"
    elif cvm_id == '0x30':              cvm_id_msg = "CONFIRMATION CODE VERIFIED"
    elif cvm_id == '0xf0':              cvm_id_msg = "N/A"
    else:                               cvm_id_msg = "RFU"

    if b5[0] == 1 : ui_out = "Set"
    else:           ui_out = "Not Set"
    if b5[1] == 1 : ui_restart = "Set"
    else:           ui_restart = "Not Set"
    if b5[2] == 1 : data_record_present = "Set"
    else:           data_record_present = "Not Set"
    if b5[3] == 1 : disc_data_present = "Set"
    else:           disc_data_present = "Not Set"
    if b5[4] == 1 : receipt = "YES"
    else:           receipt = "N/A"
    
    if alternate_interface_preference_id == '0xf0':  alternate_interface_preference_id_msg = "N/A"
    else:                                           alternate_interface_preference_id_msg = "RFU"

    if field_off_request_id == '0xff':              field_off_request_id_msg = "N/A"
    # else:                                           field_off_request_id_msg = str(int(field_off_request_id, 16))
    else:                                           field_off_request_id_msg = field_off_request_id[2:]

    removal_timeout_msg = str(int(removal_timeout, 16))

    return {
        '<b style="color: blue">Outcome Parameter Set :</b>' : combine_hex(data),
        f'Status [{status_id}]' : status_id_msg,
        f'Start [{start_id}]' : start_id_msg,
        f'Online Response Data [{online_response_data}]' : online_response_data_msg,
        f'CVM [{cvm_id}]' : cvm_id_msg,
        "UI Request on Outcome Present" : ui_out,
        "UI Request on Restart Present" : ui_restart,
        "Data Record Present" : data_record_present,
        "Discretionary Data Present" : disc_data_present,
        "Receipt" : receipt,
        f'Alternate Interface Preference [{alternate_interface_preference_id}]' : alternate_interface_preference_id_msg,
        f'Field Off Request [{field_off_request_id}]' : field_off_request_id_msg,
        f'Removal Timeout [{removal_timeout}]' : removal_timeout_msg
    }
def tag_title(tag):
    if tag[0] == '0x9f':
        if tag[1] == '0x01':    return 'Acquirer Identifier'
        elif tag[1] == '0x02':  return 'Amount, Authorised (Numeric)'
        elif tag[1] == '0x03':  return 'Amount, Other (Numeric)'
        elif tag[1] == '0x07':  return 'Application Usage Control'
        elif tag[1] == '0x08':  return 'Application Version Number (Card) '
        elif tag[1] == '0x09':  return 'Application Version Number (Reader) '
        elif tag[1] == '0x0d':  return 'Issuer Action Code-Default '
        elif tag[1] == '0x0e':  return 'Issuer Action Code-Denial'
        elif tag[1] == '0x0f':  return 'Issuer Action Code-Denial'
        elif tag[1] == '0x10':  return 'Issuer Application Data'
        elif tag[1] == '0x11':  return 'Issuer Code Table Index'
        elif tag[1] == '0x12':  return 'Application Preferred Name '
        elif tag[1] == '0x15':  return 'Merchant Category Code'
        elif tag[1] == '0x16':  return 'Merchant Identifier'
        elif tag[1] == '0x19':  return 'Token Requestor ID '
        elif tag[1] == '0x1a':  return 'Terminal Country Code'
        elif tag[1] == '0x1c':  return 'Terminal Identification'
        elif tag[1] == '0x1d':  return 'Terminal Risk Management Data'
        elif tag[1] == '0x1e':  return 'Interface Device Serial Number '
        elif tag[1] == '0x1f':  return 'Track 1 Discretionary Data'
        elif tag[1] == '0x20':  return 'Track 2 Discretionary Data '
        elif tag[1] == '0x21':  return 'Transaction Time'
        elif tag[1] == '0x24':  return 'Payment Account Reference'
        elif tag[1] == '0x26':  return 'Application Cryptogram'
        elif tag[1] == '0x27':  return 'Cryptogram Information Data '
        elif tag[1] == '0x32':  return 'Issuer Public Key Exponent'
        elif tag[1] == '0x33':  return 'Terminal Capabilities'
        elif tag[1] == '0x34':  return 'CVM Results'
        elif tag[1] == '0x35':  return 'Terminal Type'
        elif tag[1] == '0x36':  return 'Application Transaction Counter '
        elif tag[1] == '0x37':  return 'Unpredictable Number'
        elif tag[1] == '0x38':  return 'PDOL'
        elif tag[1] == '0x40':  return 'Additional Terminal Capabilities '
        elif tag[1] == '0x42':  return 'Application Currency Code'
        elif tag[1] == '0x44':  return 'Application Currency Exponent'
        elif tag[1] == '0x46':  return 'ICC Public Key Certificate '
        elif tag[1] == '0x47':  return 'ICC Public Key Exponent '
        elif tag[1] == '0x48':  return 'ICC Public Key Remainder'
        elif tag[1] == '0x4a':  return 'Static Data Authentication Tag List '
        elif tag[1] == '0x4b':  return 'Signed Dynamic Application Data'
        elif tag[1] == '0x4c':  return 'ICC Dynamic Number'
        elif tag[1] == '0x4d':  return 'Log Entry'
        elif tag[1] == '0x4e':  return 'Merchant Name and Location '
        elif tag[1] == '0x53':  return 'Transaction Category Code'
        elif tag[1] == '0x54':  return 'DS ODS Card'
        elif tag[1] == '0x5b':  return 'DSDOL'
        elif tag[1] == '0x5c':  return 'DS Requested Operator ID'
        elif tag[1] == '0x5d':  return 'Application Capabilities Information '
        elif tag[1] == '0x5e':  return 'DS ID'
        elif tag[1] == '0x5f':  return 'DS Slot Availability'
        elif tag[1] == '0x60':  return 'CVC3 (Track1)'
        elif tag[1] == '0x61':  return 'CVC3 (Track2)'
        elif tag[1] == '0x62':  return 'PCVC3(Track1) '
        elif tag[1] == '0x63':  return 'PUNATC(Track1)'
        elif tag[1] == '0x64':  return 'NATC(Track1)'
        elif tag[1] == '0x65':  return 'PCVC3(Track2)'
        elif tag[1] == '0x66':  return 'PUNATC(Track2)'
        elif tag[1] == '0x67':  return 'NATC(Track2)'
        elif tag[1] == '0x69':  return 'UDOL'
        elif tag[1] == '0x6a':  return 'Unpredictable Number (Numeric) '
        elif tag[1] == '0x6b':  return 'Track 2 Data'
        elif tag[1] == '0x6d':  return 'Mag-stripe Application Version Number (Reader)'
        elif tag[1] == '0x6e':  return 'Third Party Data'
        elif tag[1] == '0x6f':  return 'DS Slot Management Control '
        elif tag[1] == '0x70':  return 'Protected Data Envelope 1'
        elif tag[1] == '0x71':  return 'Protected Data Envelope 2'
        elif tag[1] == '0x72':  return 'Protected Data Envelope 3'
        elif tag[1] == '0x73':  return 'Protected Data Envelope 4'
        elif tag[1] == '0x74':  return 'Protected Data Envelope 5 '
        elif tag[1] == '0x75':  return 'Unprotected Data Envelope 1'
        elif tag[1] == '0x76':  return 'Unprotected Data Envelope 2'
        elif tag[1] == '0x77':  return 'Unprotected Data Envelope 3 '
        elif tag[1] == '0x78':  return 'Unprotected Data Envelope 4'
        elif tag[1] == '0x79':  return 'Unprotected Data Envelope 5 '
        elif tag[1] == '0x7c':  return 'Merchant Custom Data'
        elif tag[1] == '0x7d':  return 'DS Summary 1 '
        elif tag[1] == '0x7e':  return 'Mobile Support Indicator'
        elif tag[1] == '0x7f':  return 'DS Unpredictable Number'
    elif tag[0] == '0x5f':
        if tag[1] == '0x24':    return 'Application Expiration Date'
        elif tag[1] == '0x25':  return 'Application Effective Date'
        elif tag[1] == '0x28':  return 'Issuer Country Code'
        elif tag[1] == '0x2a':  return 'Transaction Currency Code'
        elif tag[1] == '0x2d':  return 'Language Preference '
        elif tag[1] == '0x30':  return 'Service Code'
        elif tag[1] == '0x34':  return 'Application PAN Sequence Number'
        elif tag[1] == '0x36':  return 'Transaction Currency Exponent'
        elif tag[1] == '0x57':  return 'Account Type '
    elif tag[0] == '0xbf':
        if tag[1] == '0x0c':    return 'FCI Issuer Discretionary Data' #'File Control Information (FCI) Issuer Discretionary Data'
    elif tag[0] == '0xdf':
        if tag[1] == '0x4b':    return 'POS Cardholder Interaction Information'
        elif tag[1] == '0x60':  return 'DS Input(Card)'
        elif tag[1] == '0x61':  return 'DS Digest H'
        elif tag[1] == '0x62':  return 'DS ODS Info'
        elif tag[1] == '0x63':  return 'DS ODS Term'
        elif tag[1] == '0x81':
            if tag[2] == '0x07':    return 'CDOL1 Related Data'
            #elif tag[2] == '0x0b':  return 'DS Summary Status'
            elif tag[2] == '0x0c':  return 'Kernel ID'
            elif tag[2] == '0x11':  return 'PDOL Related Data'
            elif tag[2] == '0x14':  return 'Reference Control Parameter'
            elif tag[2] == '0x15':  return 'Error Indication'
            elif tag[2] == '0x16':  return 'User Interface Request Data'
            elif tag[2] == '0x17':  return 'Card Data Input Capability'
            elif tag[2] == '0x18':  return 'CVM Capability-CVM Required'
            elif tag[2] == '0x19':  return 'CVM Capability-No CVM Required'
            elif tag[2] == '0x1b':  return 'Kernel Configuration'
            elif tag[2] == '0x1f':  return 'Security Capability '
            elif tag[2] == '0x20':  return 'Terminal Action Code-Default '
            elif tag[2] == '0x21':  return 'Terminal Action Code-Denial '
            elif tag[2] == '0x22':  return 'Terminal Action Code-Online '
            elif tag[2] == '0x23':  return 'Reader Contactless Floor Limit '
            elif tag[2] == '0x24':  return 'Reader Contactless Transaction Limit (No On-device CVM)'
            elif tag[2] == '0x25':  return 'Reader Contactless Transaction Limit (On-device CVM) '
            elif tag[2] == '0x26':  return 'Reader CVM Required Limit'
            elif tag[2] == '0x29':  return 'Outcome Parameter Set'
            elif tag[2] == '0x2d':  return 'Message Hold Time'
            elif tag[2] == '0x30':  return 'Hold Time Value '
            elif tag[2] == '0x31':  return 'Phone Message Table'
            elif tag[2] == '0x32':  return 'Minimum Relay Resistance Grace Period'
            elif tag[2] == '0x33':  return 'Maximum Relay Resistance Grace Period'
            elif tag[2] == '0x34':  return 'Terminal Expected Transmission Time For Relay Resistance C-APDU '
            elif tag[2] == '0x35':  return 'Terminal Expected Transmission Time For Relay Resistance R-APDU'
            elif tag[2] == '0x36':  return 'Relay Resistance Accuracy Threshold '
            elif tag[2] == '0x37':  return 'Relay Resistance Transmission Time Mismatch Threshold'
        elif tag[1] == '0x83':
            if tag[2] == '0x01':    return 'Terminal Relay Resistance Entropy'
            elif tag[2] == '0x02':  return 'Device Relay Resistance Entropy'
            elif tag[2] == '0x03':  return 'Min Time For Processing Relay Resistance APDU'
            elif tag[2] == '0x04':  return 'Max Time For Processing Relay Resistance APDU'
            elif tag[2] == '0x05':  return 'Device Estimated Transmission Time For Relay Resistance R-APDU'
            elif tag[2] == '0x06':  return 'Measured Relay Resistance Processing Time'
            elif tag[2] == '0x07':  return 'RRP Counter'
    elif tag[0] == '0xff':
        if tag[1] == '0x81':
            if tag[2] == '0x02':    return 'Tags To Write Before Gen AC'
            elif tag[2] == '0x03':  return 'Tags To Write After Gen AC'
            elif tag[2] == '0x04':  return 'Data To Send'
            elif tag[2] == '0x05':  return '<b style="color: blue">Data Record</b>'
            elif tag[2] == '0x06':  return '<b style="color: blue">Discretionary Data</b>'

    elif tag == '0x50':      return 'Application Label'
    elif tag == '0x56':      return 'Track 1 Data'
    elif tag == '0x57':      return 'Track 2 Equivalent Data'
    elif tag == '0x5a':      return 'Application PAN' #'Application Primary Account Number'
    elif tag == '0x6f':      return 'File Control Information Template'
    elif tag == '0x70':      return 'Read Record Template'
    elif tag == '0x77':      return 'Response Message Template Format 2 '
    elif tag == '0x80':      return 'Response Message Template Format 1'      
    elif tag == '0x82':      return 'Application Interchange Profile'
    elif tag == '0x84':      return 'DF Name'#'Dedicated File (DF) Name'
    elif tag == '0x87':      return 'Application Priority Indicator'
    elif tag == '0x8c':      return 'CDOL1'#Card Risk Management Data Object List 1'
    elif tag == '0x8e':      return 'CVM List'
    elif tag == '0x8f':      return 'CA Public Key Index'#'Certification Authority Public Key Index'
    elif tag == '0x90':      return 'Issuer Public Key Certificate'
    elif tag == '0x92':      return 'Issuer Public Key Remainder'
    elif tag == '0x94':      return 'Application File Locator'
    elif tag == '0x95':      return 'Terminal Verification Results' #TVR
    elif tag == '0x9a':      return 'Transaction Date'
    elif tag == '0x9c':      return 'Transaction Type'
    elif tag == '0xa5':      return 'FCI Proprietary Template' #File Control Information (FCI) Proprietary Template
    
    else:                    return f'TODO : {tag}'
        
def check_TVL_list(tag, data):

    cur_index = 0

    #initialize dictionary
    data_dict = dict()
    data_dict[tag_title(tag)] = f'[{len(data)}]'

    # print(data)
    while cur_index < len(data):
        if data[cur_index] == '0x9f' or data[cur_index] == '0x5f' or data[cur_index] == '0xbf':
            sub_tag = data[cur_index:cur_index+2]
            cur_index += 2
            length = int(data[cur_index],16)
            cur_index += 1
            value = data[cur_index : cur_index + length]
            cur_index += length
            if (tag_title(sub_tag) == None):
                continue
            else: 
                data_dict[tag_title(sub_tag)] = f'[{combine_hex(value)}]'

        elif data[cur_index] == '0xdf':
            if data[cur_index+1] == '0x81' or data[cur_index+1] == '0x83':
                sub_tag = data[cur_index:cur_index+3]
                cur_index += 3
            else:
                sub_tag = data[cur_index: cur_index+2]
                cur_index += 2
            length = int(data[cur_index],16)
            cur_index += 1
            value = data[cur_index : cur_index + length]
            cur_index += length
            
            if (tag_title(sub_tag) == None):
                continue
            elif (length == 0):
                data_dict[tag_title(sub_tag)] = f'[{combine_hex(value)}]'
            elif (tag_title(sub_tag) == 'Error Indication'): #df8115
                data_dict.update(data_object_df8115(value))
            elif (tag_title(sub_tag) == 'Measured Relay Resistance Processing Time' #df8306
                or tag_title(sub_tag) == 'Minimum Relay Resistance Grace Period' #df8132
                or tag_title(sub_tag) == 'Maximum Relay Resistance Grace Period' #df8133
                or tag_title(sub_tag) == 'Min Time For Processing Relay Resistance APDU' #df8303
                or tag_title(sub_tag) == 'Max Time For Processing Relay Resistance APDU'): #df8304
                result = [int(value[0], 16) << 8 | int(value[1], 16)]
                # data_dict[tag_title(sub_tag)] = f'[{result}]'
                data_dict[tag_title(sub_tag) + f' [{combine_hex(value)}]'] = f'{result}'
            else:
                data_dict[tag_title(sub_tag)] = f'[{combine_hex(value)}]'
                
        elif data[cur_index] == '0xff':
            sub_tag = data[cur_index : cur_index +3]
            cur_index += 3
            length = int(data[cur_index],16)
            cur_index += 1
            value = data[cur_index : cur_index + length]
            cur_index += length
            if (tag_title(sub_tag) == None):
                continue
            else: 
                data_dict[tag_title(sub_tag)] = f'[{combine_hex(value)}]' 
        else:
            sub_tag = data[cur_index]
            cur_index += 1
            length = int(data[cur_index],16)
            cur_index += 1
            value = data[cur_index : cur_index + length]
            cur_index += length
            if (tag_title(sub_tag) == None):
                continue
            else: 
                data_dict[tag_title(sub_tag)] = f'[{combine_hex(value)}]'

    return data_dict

def tag_to_object(tag, length, data):
    if tag == ['0xdf', '0x81', '0x16']:
        return data_object_df8116(data)
    elif tag == ['0xdf', '0x81', '0x29']:
        return data_object_df8129(data)
    else:
        return check_TVL_list(tag, data)

def ver_info_to_object(tag):
    if tag == 'A01':
        return "Marketing Name"
    elif tag == 'A02':
        return "Technical Name"
    elif tag == 'A03':
        return "PCD-ID"
    elif tag == 'A04':
        return "PCD HID"
    elif tag == 'A05':
        return "PCD SID"
    elif tag == 'A06':
        return "Application Select Mechanism"
    elif tag == 'A07':
        return "Mastercard Contactless Kernel"
    elif tag == 'A08':
        return "Mastercard Contactless Application"
    elif tag == 'A09':
        return "Operting System"
    elif tag == 'A10':
        return "Build/FirmWare"
    elif tag == 'A11':
        return "Test Application"
    elif tag == 'A12':
        return "Test Configuration Data Sets"
    elif tag == 'A13':
        return "Test Environment Interface"
    

    #generate sample function
    # elif tag == 'A14':
    #     return "Test Environment Interface"
    