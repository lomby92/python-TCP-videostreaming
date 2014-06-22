import socket, cv2, numpy

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('192.168.1.31',5000))

while True:
    data=client_socket.recv(4096000)
    #print data
    a1D = numpy.fromstring(data,dtype=numpy.uint8)
    try:
        img = numpy.reshape(a1D,(480,640,3))
    except Exception as detail:
        img= numpy.zeros((480,640,3))
        print "Error:",detail
    print img
    print "Tipo img: ",type(img)
    print "Grandezza img",img.shape
    print "Tipo di dato img: ",img.dtype
    print "Numero di elementi: ",img.size
    cv2.imshow("It works?",img)
    key=cv2.waitKey(33)
    if key==27:
        client_socket.send("end")
        break
    else:
        client_socket.send("continue")
    data = None
cv2.destroyAllWindows()
