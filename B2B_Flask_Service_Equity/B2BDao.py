import json
from dbHandeling import validateHeader,validateCustomer,postTransaction
from utility import readPropertyFile,writeLog

def validateInputAccountValidation(jsonstring):
    writeLog('validateInputAccountValidation-1',str(jsonstring))
    bool = False
    messageID=''
    connectionID=''
    connectionPassword=''
    errpoint='.00'
    returnjson={}
    try:
        paramdict={}
        paramdict=json.loads(jsonstring)
        errpoint='.01'
        billNumber=paramdict['billNumber']
        errpoint='.02'

        username=paramdict['username']
        errpoint='.03'

        password=paramdict['password']
        errpoint='.04'
        bool =True
    except Exception as er:
        print("The parameters are not valid or they are missing.")
        #retstr= {'header':{'statusCode':'400','statusDescription':'The parameters are not valid or they are missing.'+str(errpoint)}}
    if bool==True :
        try:
            errpoint='.081111'
            vd=validateHeader(username,password)
            writeLog('validateInputAccountValidation-2',vd['RESPDESC'])
            errpoint=vd['RESPCODE']
            if vd['RESPCODE']==0:
                conn=vd['CONNECTION']
            else:
                conn=None
            if conn!=None:
                #print(str(paramdict))
                print(conn)
                DBparamdict={}
                DBparamdict['VALIDATIONSTR']=billNumber
                defaultDict=readPropertyFile('defaultvalues.properties')
                propertyDict=readPropertyFile('b2b.properties')
                DBparamdict['VENDORID']=propertyDict['VENDORID']
                #DBparamdict['VENDORREQSTR']=jsonstring
                print(str(DBparamdict))
                retstr= validateCustomer(conn,str(DBparamdict))
                print(retstr)
                retstrjson={}
                retstrjson=json.loads(retstr)
                respcode=retstrjson['RESPCODE']
                errpoint='.02'

                if respcode==0:
                    respdesc={}
                    respdesc=retstrjson['RESPDESC']
                    custname=respdesc['CUSTNAME']
                    accno=respdesc['ACCNO']
                    CUSTOMERREFNUMBER=respdesc['CUSTOMERREFNUMBER']
                    createdOn=respdesc['CREATEDON']
                    returnjson['amount']=0
                    returnjson['billName']=custname
                    returnjson['billNumber']=billNumber
                    returnjson['billerCode']=defaultDict['billerCode']
                    returnjson['createdOn']=createdOn
                    returnjson['currencyCode']=defaultDict['currencyCode']
                    returnjson['customerName']=custname
                    returnjson['customerRefNumber']=str(CUSTOMERREFNUMBER)
                    returnjson['description']=''
                    returnjson['dueDate']=''
                    returnjson['expiryDate']=''
                    returnjson['Remarks']='Fees'
                    returnjson['type']='1'
                else:
                    returnjson['amount']=0
                    returnjson['billName']=None
                    returnjson['billNumber']=None
                    returnjson['description']='bill number not found'
                    returnjson['type']='1'
                    writeLog('validateInputAccountValidation-2',str(retstr));
            else:
                print('The caller is not authorized for this request.')
                returnjson['amount']=0
                returnjson['billName']=None
                returnjson['billNumber']=None
                returnjson['description']='The caller is not authorized for this request.'
                returnjson['type']='1'
            #retstr= {'header':{'messageID':messageID,'statusCode':'200','statusDescription':'Successfully validated student'},'response': { 'TransactionReferenceCode': 'EDA/1140/13', 'TransactionDate': '2018-07-23T18:24:00.195+03:00', 'TotalAmount': 0.0,'Currency': '', 'AdditionalInfo': 'Wanyama Jostine Anyango', 'AccountNumber': 'EDA/1140/13', 'AccountName': 'Wanyama Jostine Anyango', 'InstitutionCode': '2100082', 'InstitutionName': 'Eldoret University '}}
        except Exception as e:
            print("A severe problem has occurred.",e)
            returnjson['amount']=0
            returnjson['billName']=None
            returnjson['billNumber']=None
            returnjson['description']='A severe problem has occurred.'+str(errpoint)+str(e)
            returnjson['type']='1'
    else:
        print("A severe problem has occurred."+str(errpoint))
        returnjson['amount']=0
        returnjson['billName']=None
        returnjson['billNumber']=None
        returnjson['description']='The parameters are not valid or they are missing.'#+str(errpoint)+str(e)
        returnjson['type']='1'
    writeLog('validateInputAccountValidation-3',str(returnjson))
    return returnjson


def postTran(jsonstring):
    writeLog('postTran-1',str(jsonstring))
    bool = False
    messageID=''
    connectionID=''
    connectionPassword=''
    errpoint='.00'
    defaultDict=readPropertyFile('defaultvalues.properties')
    jsonkeyvalidationstr=""
    try:
        paramdict={}
        paramdict=json.loads(jsonstring)
        errpoint='.01'
        headerdict={}
        jsonkeyvalidationstr="username not found"
        username=paramdict['username']
        errpoint='.02'
        jsonkeyvalidationstr="password not found"
        password=paramdict['password']
        errpoint='.03'
        jsonkeyvalidationstr="billNumber not found"
        billNumber=paramdict['billNumber']
        errpoint='.04'
        jsonkeyvalidationstr="billAmount not found"
        billAmount=paramdict['billAmount']
        errpoint='.05'
        jsonkeyvalidationstr="CustomerRefNumber not found"
        CUSTOMERREFNUMBER=paramdict['CustomerRefNumber']
        errpoint='.06'
        jsonkeyvalidationstr="bankreference not found"
        bankreference=paramdict['bankreference']
        errpoint='.07'
        jsonkeyvalidationstr="tranParticular not found"
        tranParticular=paramdict['tranParticular']
        errpoint='.09'
        jsonkeyvalidationstr="paymentMode not found"
        paymentMode=paramdict['paymentMode']
        errpoint='.10'
        jsonkeyvalidationstr="transactionDate not found"
        transactionDate=paramdict['transactionDate']
        errpoint='.11'
        jsonkeyvalidationstr="phonenumber not found"
        phonenumber=paramdict['phonenumber']
        errpoint='.12'
        jsonkeyvalidationstr="debitaccount not found"
        debitaccount=paramdict['debitaccount']
        errpoint='.13'
        jsonkeyvalidationstr="debitcustname not found"
        debitcustname=paramdict['debitcustname']
        errpoint='.14'
        bool =True
    except Exception as er:
        print("The parameters are not valid or they are missing.")
        return {'responseCode':'400','responseMessage':'The parameters are not valid or they are missing.'+jsonkeyvalidationstr}
    jsonkeyvalidationstr=""
    if bool==True :
        try:
            vd=validateHeader(username,password)
            if vd['RESPCODE']==0:
                conn=vd['CONNECTION']
            else:
                conn=None
            errpoint='.25'
            if conn!=None:
                DBparamdict={}
                DBparamdict['VALIDATIONSTR']=billNumber
                DBparamdict['TRANREFNO']=bankreference
                defaultDict=readPropertyFile('b2b.properties')
                DBparamdict['VENDORID']=defaultDict['VENDORID']
                DBparamdict['TRANAMOUNT']=billAmount
                #DBparamdict['VENDORREQSTR']=jsonstring
                DBparamdict['CUSTOMERREFNUMBER']=CUSTOMERREFNUMBER
                print(DBparamdict)
                retstr= postTransaction(conn,str(DBparamdict))
                print(retstr)
                writeLog('postTran-2',str(retstr));
                retstrjson={}
                retstrjson=json.loads(retstr)
                respcode=retstrjson['RESPCODE']
                errpoint='.02'
                if respcode==0:
                    respdesc={}
                    respdesc=retstrjson['RESPDESC']
                    returnjson={}
                    returnjson={'responseCode':'OK','responseMessage':'SUCCESSFUL'}
                #if retstr.find("ERROR")>-1:
                elif respcode==3:
                    returnjson={'responseCode':'OK','responseMessage':'DUPLICATE TRANSACTION'}
                else:
                    returnjson= {'responseCode':respcode,'responseMessage':'ERROR OCCURRED'}
            else:
                print('The caller is not authorized for this request.')
                returnjson= {'responseCode':'1','responseMessage':'401'+errpoint,'statusDescription':'The caller is not authorized for this request.'}
            #retstr= {'header':{'messageID':messageID,'statusCode':'200','statusDescription':'Successfully validated student'},'response': { 'TransactionReferenceCode': 'EDA/1140/13', 'TransactionDate': '2018-07-23T18:24:00.195+03:00', 'TotalAmount': 0.0,'Currency': '', 'AdditionalInfo': 'Wanyama Jostine Anyango', 'AccountNumber': 'EDA/1140/13', 'AccountName': 'Wanyama Jostine Anyango', 'InstitutionCode': '2100082', 'InstitutionName': 'Eldoret University '}}
        except Exception as e:
            print("A severe problem has occurred.",e)
            returnjson= {'responseCode':'1','responseMessage':'405'+errpoint,'statusDescription':'A severe problem has occurred.'}

    else:
        print("A severe problem has occurred.")
        returnjson= {'responseCode':'1','responseMessage':'405'+errpoint,'statusDescription':'A severe problem has occurred.'}

    writeLog('postTran-3',str(returnjson));
    return returnjson
