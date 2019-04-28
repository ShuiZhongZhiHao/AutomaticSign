from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.http import FileResponse  

# import commands
 # Create your views here.
CODE_SIGN_IDENTITY = 'CODE_SIGN_IDENTITY = "iPhone Distribution: Li Tongming (K25843MQW5)"'
@csrf_exempt
def checkoutUDID(request):
   if request.method == "POST":
         UDID = request.POST.get('UDID')
         arg1 = 'ipone1'
         arg2 = '71eb7f3e802cd713cc91e2e83bbdb453bcafa99d'
         os.system('chmod +x /Users/haoli/Desktop/AutomaticSign/sign/test.sh')
         os.system('/Users/haoli/Desktop/AutomaticSign/sign/test.sh' + ' ' + arg1 + ' ' + arg2)
    # os.system('fastlane fastlane-credentials add --username l8ijmm@yeah.net')
   # # os.system("fastlane run register_devices devices:'158e3ef5d604852efe77682a1512b295d3a374c0' username:'l8ijmm@yeah.net'")
         
   return JsonResponse({"returnCode":'0000','Message':'请求方式成功'})
def file_down(request):  
    file=open('/Users/haoli/Desktop/fastlane_ipa/Lottery/Lottery.ipa','rb')  
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="Lottery.ipa"'  
    return response 

def mobileconfigFile_down(request):  
   file=open('/Users/haoli/Desktop/4.mobileconfig','rb')  
   response =FileResponse(file)  
   response['Content-Type']='application/octet-stream'  
   response['Content-Disposition']='attachment;filename="4.mobileconfig"'  
   return response 

def mobileconfigFile_d(request):  
   file=open('/Users/haoli/Desktop/2.mobileconfig','rb')  
   response =FileResponse(file)  
   response['Content-Type']='application/octet-stream'  
   response['Content-Disposition']='attachment;filename="2.mobileconfig"'  
   return response 

def receive(request):
    print(123)
	#   response.setContentType("text/html;charset=UTF-8");
	#   request.setCharacterEncoding("UTF-8");

	#   //获取HTTP请求的输入流
	#   InputStream is = request.getInputStream();
	#   //已HTTP请求输入流建立一个BufferedReader对象
	#   BufferedReader br = new BufferedReader(new InputStreamReader(is,"UTF-8"));
	#   StringBuilder sb = new StringBuilder();

	#   //读取HTTP请求内容
	#   String buffer = null;
	#   while ((buffer = br.readLine()) != null) {
	#    sb.append(buffer);
	#   }
	#   String content = sb.toString().substring(sb.toString().indexOf("<?xml"), sb.toString().indexOf("</plist>")+8);
	#   System.out.println(content);


	#      // 创建xml解析对象
	#      SAXReader reader = new SAXReader();
	#      // 定义一个文档
	#      Document document = null;
	#      //将字符串转换为
	#      try {
	#          document = reader.read(new ByteArrayInputStream(content.getBytes("GBK")));
	#      } catch (DocumentException e) {
	#          e.printStackTrace();
	#      }
	# response.setHeader("Location", "http://192.168.203.123:8080/UDID/udid.jsp?UDID=2123");
    return JsonResponse({"returnCode":'0000','Message':'请求方式成功'})



  




