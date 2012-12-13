# interface class for a call set
import time
import datetime
import csv

class CallSet(object):
    def __init__(self, csv_buffer, callset_id):
        self._id = callset_id
        self.line_num = 0

        # try to open csv file and return a reader/iterator
        try:
            csv_file = open(csv_buffer, 'rb')
            print("opening csv file: '" + csv_buffer + "'")
            print("assigning callset id: '" + str(callset_id) + "'")
            self._reader = csv.reader(csv_file) # default delimiter=','

            # first line will be the title
            self._title = self._reader.next()
            # second line will be the field names
            self._fields = self._reader.next()

            # DictReader takes a list of field keys
            # self._dict_reader = csv.DictReader(csv_file, self._fields)

        except csv.Error as err:
            print('file %s, line %d: %s' % (csv_buffer, self._reader.line_num, err))
            print("Error:", exc)
            sys.exit(1)

    def _buildset(reader, fields)

    # read-only properties
    @property
    def reader(self):
        """Access to the csv reader"""
        return self._reader
    @property
    def dict_reader(self):
        """Access to the csv reader"""
        return self._reader

    @property
    def id(self):
        """call id"""
        return self._id

    @property
    def title(self):
        # save the first row as the title
        return self._title

    @property
    def fields(self):
        # save the second row as the field names
        return self._fields

    @property
    def writer(self):
        """Access to the csv reader"""
        return None



    # if not cpaVersionManager.isSupported(self.__cpaVersion):
      # raise cpaVersionManager.VersionNotSupported(self.__cpaVersion)

     #if the version is different of 1.x, skip the second line of the csv
    # if(self.__cpaVersion != cpaVersionManager.SUPPORTED_VERSION[0]):
      # self.__listRows.pop(0)

    def get_title(self):
          print("this should get the first row")


    def get_call(self, pos):
        row = self.reader[pos]
        return self.__build_call(row)

    def getCpaVersion(self):
        return self.__cpaVersion

    def numberofcalls(self):
        return len(self.__listRows)

    # build a call from a csv row
      #@param csvRow: csv row that represent the call
    def __build_call(self,csvRow):

          #parse csv
        try:
          paraxipCallid = csvRow[0]
          callDate = csvRow[1]
          referenceID = csvRow[2]
          campaignName = csvRow[3]
          phoneNumber = csvRow[4]
          cpaResult = csvRow[5]
          timeDialing = csvRow[6]
          timeConnected = csvRow[7]
          timeCpaCompleted = csvRow[8]
          timeQueued = csvRow[9]
          timeConnectedToAgent = csvRow[10]

          if(self.__cpaVersion == cpaVersionManager.SUPPORTED_VERSION[0]):
              detailedCpaResult = ""
          else:
              detailedCpaResult = csvRow[11]
        except IndexError:
            PyLoggingFunctions.log_error(fileLogger, "Unable to parse the csvRow: " + str(csvRow)+ " (IndexError)")
            raise Exception("Invalid row")

        #correction
        if cpaResult == 'Voice':
           cpaResult = 'Human'

        #get foreignKeys
        cpaResultKey = self.__callset.cpaResults[cpaResult]
        detailedCpaResultKey = self.__callset.detailedCpaResults[detailedCpaResult]

        #process 1 (string to timeObject)
        callDate = cpaOMExtended.processDate(callDate)
        timeDialing = cpaOMExtended.processTime(timeDialing)
        timeConnected = cpaOMExtended.processTime(timeConnected)
        timeCpaCompleted = cpaOMExtended.processTime(timeCpaCompleted)
        timeQueued = cpaOMExtended.processTime(timeQueued)
        timeConnectedToAgent = cpaOMExtended.processTime(timeConnectedToAgent)

        #process 2 (combine the calldate and the time)
        timeDialing = cpaOMExtended.processDateTimeFromDateObjects(callDate, timeDialing)
        timeConnected = \
                cpaOMExtended.processDateTimeFromDateObjects(callDate, timeConnected)
        timeCpaCompleted = \
                cpaOMExtended.processDateTimeFromDateObjects(callDate, timeCpaCompleted)
        timeQueued = cpaOMExtended.processDateTimeFromDateObjects(callDate, timeQueued)
        timeConnectedToAgent = \
                cpaOMExtended.processDateTimeFromDateObjects(callDate, timeConnectedToAgent)

        #intantiate
        return Call(paraxipCallid,
                callDate,
                referenceID,
                campaignName,
                phoneNumber,
                cpaResultKey,
                detailedCpaResultKey,
                timeDialing,
                timeConnected,
                timeCpaCompleted,
                timeQueued,
                timeConnectedToAgent)

