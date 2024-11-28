import json
from dbHandeling import validateHeader,validateCustomer,postTransaction
from utility import readPropertyFile,writeLog

def validateInputAccountValidation(jsonstring):
    writeLog('validateInputAccountValidation',str(jsonstring))
    bool = False
    messageID=''
    connectionID=''
    connectionPassword=''
    errpoint='.00'
    try:
        paramdict={}
        paramdict=json.loads(jsonstring)
        errpoint='.01'
        headerdict={}
        headerdict=paramdict['header']
        errpoint='.02'

        requestdict={}
        requestdict=paramdict['request']
        errpoint='.03'

        serviceName=headerdict['serviceName']
        errpoint='.04'
        messageID=headerdict['messageID']
        errpoint='.05'
        connectionID=headerdict['connectionID']
        errpoint='.06'
        connectionPassword=headerdict['connectionPassword']
        errpoint='.07'
        TransactionReferenceCode=requestdict['TransactionReferenceCode']
        errpoint='.09'
        TransactionDate=requestdict['TransactionDate']
        errpoint='.10'
        InstitutionCode=requestdict['InstitutionCode']
        errpoint='.11'
        bool =True
    except Exception as er:
        print("The parameters are not valid or they are missing.")
        retstr= {'header':{'messageID':messageID,'statusCode':'400','statusDescription':'The parameters are not valid or they are missing.'+str(errpoint)}}
    if bool==True :
        try:
            errpoint='.081111'
            vd=validateHeader(connectionID,connectionPassword)
            errpoint=vd['RESPCODE']
            if vd['RESPCODE']==0:
                conn=vd['CONNECTION']
            else:
                conn=None
            if conn!=None:
                #print(str(paramdict))
                retstr= validateCustomer(conn,str(paramdict))
            else:
                print('The caller is not authorized for this request.')
                retstr= {'header':{'messageID':messageID,'statusCode':'401','statusDescription':'The caller is not authorized for this request.'+str(errpoint)+vd['RESPDESC']}}
            #retstr= {'header':{'messageID':messageID,'statusCode':'200','statusDescription':'Successfully validated student'},'response': { 'TransactionReferenceCode': 'EDA/1140/13', 'TransactionDate': '2018-07-23T18:24:00.195+03:00', 'TotalAmount': 0.0,'Currency': '', 'AdditionalInfo': 'Wanyama Jostine Anyango', 'AccountNumber': 'EDA/1140/13', 'AccountName': 'Wanyama Jostine Anyango', 'InstitutionCode': '2100082', 'InstitutionName': 'Eldoret University '}}
        except Exception as e:
            print("A severe problem has occurred.",e)
            retstr= {'header':{'messageID':messageID,'statusCode':'405','statusDescription':'A severe problem has occurred.'+str(errpoint)+str(e)}}

    else:
        print("A severe problem has occurred."+str(errpoint))
        retstr= {'header':{'messageID':messageID,'statusCode':'405','statusDescription':'A severe problem has occurred.'+str(errpoint)}}
    writeLog('validateInputAccountValidation',str(retstr))
    return retstr
    
    
def postTran(jsonstring):
    writeLog('validateInputAccountValidation',str(jsonstring))
    bool = False
    messageID=''
    connectionID=''
    connectionPassword=''
    errpoint='.00'
    defaultDict=readPropertyFile('defaultvalues.properties')
    try:
        paramdict={}
        paramdict=json.loads(jsonstring)
        #print(
        errpoint='.01'
        headerdict={}
        headerdict=paramdict['header']
        #print(
        errpoint='.02'

        requestdict={}
        requestdict=paramdict['request']
        #print(errpoint)
        errpoint='.03'

        serviceName=headerdict['serviceName']
        #print(errpoint)
        errpoint='.04'
        messageID=headerdict['messageID']
        #print(errpoint)
        errpoint='.05'
        connectionID=headerdict['connectionID']
        #print(errpoint)
        errpoint='.06'
        connectionPassword=headerdict['connectionPassword']
        #print(errpoint)
        errpoint='.07'
        TransactionReferenceCode=requestdict['TransactionReferenceCode']
        #print(errpoint)
        errpoint='.09'
        TransactionDate=requestdict['TransactionDate']
        #print(errpoint)
        errpoint='.10'
        InstitutionCode=requestdict['InstitutionCode']
        #print(errpoint)
        errpoint='.11'
        TotalAmount=requestdict['TotalAmount']
        #print(errpoint)
        errpoint='.12'
        requestdict['Currency']=''
        #print(errpoint)
        errpoint='.13'
        DocumentReferenceNumber=requestdict['DocumentReferenceNumber']
        #print(errpoint)
        errpoint='.14'
        try:
            BankCode=requestdict['BankCode']
            #print(errpoint)
            errpoint='.15'
        except Exception as ex:
            BankCode=defaultDict['BankCode']
            print(errpoint)
            errpoint='.15'
        try:
            BranchCode=requestdict['BranchCode']
            #print(errpoint)
            errpoint='.16'
        except Exception as ex:
            BranchCode=defaultDict['BranchCode']
            print(errpoint)
            errpoint='.16'
        PaymentDate=requestdict['PaymentDate']
        #print(errpoint)
        errpoint='.17'
        requestdict['PaymentReferenceCode']=''
        #print(errpoint)
        errpoint='.18'
        try:
            PaymentMode=requestdict['PaymentMode']
            #print(errpoint)
            errpoint='.19'
        except Exception as ex:
            PaymentMode=defaultDict['PaymentMode']
            print(errpoint)
            errpoint='.19'
        try:
            PaymentAmount=requestdict['PaymentAmount']
            #print(errpoint)
            errpoint='.20'
        except Exception as ex:
            requestdict['PaymentAmount']=TotalAmount
            print(errpoint)
            errpoint='.20'
        try:
            AdditionalInfo=requestdict['AdditionalInfo']
            #print(errpoint)
            errpoint='.21'
        except Exception as ex:
            requestdict['AdditionalInfo']=DocumentReferenceNumber
            print(errpoint)
            errpoint='.21'
        try:
            AccountNumber=requestdict['AccountNumber']
            #print(errpoint)
            errpoint='.22'
        except Exception as ex:
            requestdict['AccountNumber']=AdditionalInfo
            print(errpoint)
            errpoint='.22'
        requestdict['AccountName']=''
        #print(errpoint)
        errpoint='.23'
        requestdict['InstitutionName']=''
        #print(errpoint)
        errpoint='.24'
        print("header",str(headerdict))
        print("request",str(requestdict))
        paramdict={}
        paramdict['header']=headerdict
        paramdict['request']=requestdict
        bool =True
    except Exception as er:
        print("The parameters are not valid or they are missing.")
        retstr={'header':{'messageID':messageID,'statusCode':'400'+errpoint,'statusDescription':'The parameters are not valid or they are missing.'}}
        writeLog('postTran',str(retstr))
        
        #return {'header':{'messageID':messageID,'statusCode':'400'+errpoint,'statusDescription':'The parameters are not valid or they are missing.'}}
    if bool==True :
        try:
            vd=validateHeader(connectionID,connectionPassword)
            if vd['RESPCODE']==0:
                conn=vd['CONNECTION']
            else:
                conn=None
            errpoint='.25'
            if conn!=None:
                #print(str(paramdict))
                retstr= postTransaction(conn,str(paramdict))
            else:
                print('The caller is not authorized for this request.')
                retstr= {'header':{'messageID':messageID,'statusCode':'401'+errpoint,'statusDescription':'The caller is not authorized for this request.'}}
            #retstr= {'header':{'messageID':messageID,'statusCode':'200','statusDescription':'Successfully validated student'},'response': { 'TransactionReferenceCode': 'EDA/1140/13', 'TransactionDate': '2018-07-23T18:24:00.195+03:00', 'TotalAmount': 0.0,'Currency': '', 'AdditionalInfo': 'Wanyama Jostine Anyango', 'AccountNumber': 'EDA/1140/13', 'AccountName': 'Wanyama Jostine Anyango', 'InstitutionCode': '2100082', 'InstitutionName': 'Eldoret University '}}
        except Exception as e:
            print("A severe problem has occurred.",e)
            retstr= {'header':{'messageID':messageID,'statusCode':'405'+errpoint,'statusDescription':'A severe problem has occurred.'}}

    else:
        print("A severe problem has occurred.")
        retstr= {'header':{'messageID':messageID,'statusCode':'405'+errpoint,'statusDescription':'A severe problem has occurred.'}}

    writeLog('postTran',str(retstr))
    return retstr
