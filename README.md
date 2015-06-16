Login process :

1. Get token in http://cas.upc.edu.cn/cas/login
2. POST data to http://cas.upc.edu.cn/cas/login?service=http://i.upc.edu.cn/dcp/index.jsp
3. Get a 302 redirect to http://i.upc.edu.cn/dcp/index.jsp?ticket=Another_TOKEN , and set your session in this page
4. Redirect again to Home Page http://i.upc.edu.cn/dcp/forward.action?path=/portal/portal&p=wkHomePage