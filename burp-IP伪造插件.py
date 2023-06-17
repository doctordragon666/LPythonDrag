# # -*- coding: utf-8 -*-
# """
# -------------------------------------------------
#    File Name：     fakeIP
#    Description :
#    Author :       CoolCat
#    date：          2019-06-05
# -------------------------------------------------
#    Change Activity:
#                    2019-06-05:
# -------------------------------------------------
# """
# __author__ = 'CoolCat'
#
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import random
# from burp import ITab
# from javax.swing import JMenu
# from javax.swing import JMenuItem
# from burp import IBurpExtender
# # from burp import IHttpListener
# from java.io import PrintWriter
# from burp import IContextMenuFactory
# from burp import IIntruderPayloadGeneratorFactory
# from burp import IIntruderPayloadGenerator
# from java.awt import GridBagLayout, GridBagConstraints
# from javax.swing import JLabel, JTextField, JOptionPane, JTabbedPane, JPanel, JButton
#
#
# class BurpExtender(IBurpExtender, IHttpListener, IContextMenuFactory, IIntruderPayloadGeneratorFactory):
#     def registerExtenderCallbacks(self, callbacks):
#
#         print
#         "[+] #####################################"
#         print
#         "[+]    fakeIp for burp V1.0"
#         print
#         "[+]    anthor: CoolCat"
#         print
#         "[+]    email: CoolCat@gzsec.org"
#         print
#         "[+]    gayhub:https://github.com/TheKingOfDuck"
#         print
#         "[+] #####################################"
#
#         print
#         "\n[-]fakeIp loading..."
#
#         self._callbacks = callbacks
#         self._helpers = callbacks.getHelpers()
#         callbacks.setExtensionName("fakeIp")
#         callbacks.registerHttpListener(self)
#         callbacks.registerContextMenuFactory(self)
#         self.stdout = PrintWriter(callbacks.getStdout(), True)
#         self.stderr = PrintWriter(callbacks.getStderr(), True)
#         callbacks.issueAlert("Loaded Successfull.")
#
#         # obtain an extension helpers object
#         self._helpers = callbacks.getHelpers()
#
#         # register ourselves as an Intruder payload generator
#         callbacks.registerIntruderPayloadGeneratorFactory(self)
#
#         print
#         "[*]Successfull..."
#
#     def createMenuItems(self, invocation):
#         self.menus = []
#         self.mainMenu = JMenu("fakeIp")
#         self.menus.append(self.mainMenu)
#         self.invocation = invocation
#         # print invocation.getSelectedMessages()[0].getRequest()
#         menuItem = ['inputIP', '127.0.0.1', 'randomIP']
#         for tool in menuItem:
#             # self.mainMenu.add(JMenuItem(tool))
#             if tool == 'inputIP':
#                 menu = JMenuItem(tool, None, actionPerformed=lambda x: self.modifyHeader(x))
#                 self.mainMenu.add(menu)
#             elif tool == '127.0.0.1':
#                 menu = JMenuItem(tool, None, actionPerformed=lambda x: self.modifyHeader(x))
#                 self.mainMenu.add(menu)
#             elif tool == 'randomIP':
#                 menu = JMenuItem(tool, None, actionPerformed=lambda x: self.modifyHeader(x))
#                 self.mainMenu.add(menu)
#
#         return self.menus if self.menus else None
#
#     def addIPs(self, ip):
#
#         currentRequest = self.invocation.getSelectedMessages()[0]  # getSelectedMessages()方法返回的是一个数组，判断时为1即可，否则为2。
#         requestInfo = self._helpers.analyzeRequest(currentRequest)  # 这个方法获取到的是完整的Http请求的相关信息
#         self.headers = list(requestInfo.getHeaders())
#
#         self.headers.append(u'X-Forwarded-For:' + ip)
#         self.headers.append(u'X-Forwarded:' + ip)
#         self.headers.append(u'Forwarded-For:' + ip)
#         self.headers.append(u'Forwarded:' + ip)
#         self.headers.append(u'X-Forwarded-Host:' + ip)
#         self.headers.append(u'X-remote-IP:' + ip)
#         self.headers.append(u'X-remote-addr:' + ip)
#         self.headers.append(u'True-Client-IP:' + ip)
#         self.headers.append(u'X-Client-IP:' + ip)
#         self.headers.append(u'Client-IP:' + ip)
#         self.headers.append(u'X-Real-IP:' + ip)
#         self.headers.append(u'Ali-CDN-Real-IP:' + ip)
#         self.headers.append(u'Cdn-Src-Ip:' + ip)
#         self.headers.append(u'Cdn-Real-Ip:' + ip)
#         self.headers.append(u'CF-Connecting-IP:' + ip)
#         self.headers.append(u'X-Cluster-Client-IP:' + ip)
#         self.headers.append(u'WL-Proxy-Client-IP:' + ip)
#         self.headers.append(u'Proxy-Client-IP:' + ip)
#         self.headers.append(u'Fastly-Client-Ip:' + ip)
#         self.headers.append(u'True-Client-Ip:' + ip)
#
#         # print 'self.headers',self.headers
#         bodyBytes = currentRequest.getRequest()[requestInfo.getBodyOffset():]  # bytes[]类型
#         self.body = self._helpers.bytesToString(bodyBytes)  # bytes to string转换一下
#         # print 'self.body:',self.body
#         newMessage = self._helpers.buildHttpMessage(self.headers, self.body)
#         currentRequest.setRequest(newMessage)  # setRequest() 是动态方法
#
#     def modifyHeader(self, x):
#         if x.getSource().text == 'inputIP':  # 通过获取当前点击的菜单项 text 属性，确定当前需要执行的 command
#             ip = JOptionPane.showInputDialog("Pls input ur ip:");
#
#             self.addIPs(ip)
#         elif x.getSource().text == '127.0.0.1':
#             self.addIPs("127.0.0.1")
#
#         elif x.getSource().text == 'randomIP':
#
#             a = str(int(random.uniform(1, 255)))
#             b = str(int(random.uniform(1, 255)))
#             c = str(int(random.uniform(1, 255)))
#             d = str(int(random.uniform(1, 255)))
#             ip = a + "." + b + "." + c + "." + d
#
#             self.addIPs(ip)
#
#     def getGeneratorName(self):
#         return "fakeIpPayloads"
#
#     def createNewInstance(self, attack):
#         return fakeIpGenerator(self, attack)
#
#
# # 实现 fakeIpGenerator，继承 IIntruderPayloadGenerator。这里定义了 max_payload（最大负载）和 num_iterations（迭代次数）这两个参数，用于模拟攻击时的情况。
# class fakeIpGenerator(IIntruderPayloadGenerator):
#     def __init__(self, extender, attack):
#         self._extender = extender
#         self._helpers = extender._helpers
#         self._attack = attack
#         self.max_payload = 1
#         self.num_iterations = 0
#         return
#
#     # 通过比较判断是否达到最大负载
#     def hasMorePayloads(self):
#         if self.num_iterations == self.max_payload:
#             return False
#         else:
#             return True
#
#     # 返回原始的HTTP请求以及当前负载，这里不作任何修改，直接返回随机生成的IP地址
#     def getNextPayload(self, current_payload):
#         a = str(int(random.uniform(1, 255)))
#         b = str(int(random.uniform(1, 255)))
#         c = str(int(random.uniform(1, 255)))
#         d = str(int(random.uniform(1, 255)))
#
#         payload = a + "." + b + "." + c + "." + d
#
#         return payload
