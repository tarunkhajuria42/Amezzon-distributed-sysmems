"""
Helper file to generate html log 
"""
filename = "i.log"
htmlfilename = filename.split(".")[0] + ".html"


class LogServiceHelper(object):
    def __init__(self):
        try:
            self.__fh = open(filename, 'r')

        except:
            print " "

    def readNewLog(self):
        self.__data = []
        lines = self.__fh.readlines()
        # print lines
        writeHtml = []
        updateFile = {}

        for i in range(len(lines)):

            if "placed_html" in lines[i]:
                updateFile[lines[i]] = lines[i]

            else:
                newline = lines[i] + "    placed_html"
                writeHtml.append(lines[i])
                updateFile[newline] = newline

        self.__fh.close()

        self.htmlGenerator(writeHtml)
        # everything success now update existing log file
        self.updateLogFile(list(updateFile))

    def updateLogFile(self, data):
        self.__updateFile = data
        with open(filename, 'w') as f:
            for item in self.__updateFile:
                print item
                f.write("%s" % item)
            f.close()

    def htmlGenerator(self, data):

        self.__writeHtml = data
        self.__htmlLog = open(htmlfilename, 'a')
        self.__htmlLog.write("<table border=1 width=100%>")
        self.__i = 1
        for line in self.__writeHtml:
            self.__htmlLog.write("<tr><td>" + str(self.__i) + "</td><td>" + line + "</td></tr>")
            self.__i = self.__i + 1
        self.__htmlLog.write("</table>")
        self.__htmlLog.close()


a = LogServiceHelper()
a.readNewLog()
