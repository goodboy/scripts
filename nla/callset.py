# interface for a call set
import time
import datetime
import csv

class CallSet(object):
    def __init__(self, csv_buffer, callset_id):
        self._id = callset_id
        self.length = 0

        # try to open csv file and return a reader/iterator
        try:
            print("opening csv file: '" + csv_buffer + "'")
            print("assigning callset id: '" + str(callset_id) + "'")
            csv_file = open(csv_buffer, 'rb')
            self.reader = csv.reader(csv_file) # default delimiter=','

            # first line should be the title
            # self._title = self._reader.next()

            # second line should be the field names
            # self._fields = self._reader.next()

            # DictReader takes a list of field keys
            # self._dict_reader = csv.DictReader(csv_file, self._fields)

            #TODO: 
                # check for logs for each entry
                # report errors if logs not found etc.

        except csv.Error as err:
            print('file %s, line %d: %s' % (csv_buffer, self._reader.line_num, err))
            print("Error:", exc)
            sys.exit(1)

    def _buildset(reader, fields):
        """csv.reader, list of fields -> list of dicts = csv rows"""
    # consider changing this to use lists (for speed) of fields and then
    # map to a dict for field access?
        # if self.line_num == 0:

        # each row contains a dictionary of fields
        row = []
        # iterate through the iterable
        for entry in self._reader:
            # self.line_num = self._reader.line_num
            self.length += 1

            d = dict(zip(self.fields, entry))
            lf = len(self.fields)
            le = len(entry)
            if lf < le:
                d[self.restkey] = entry[lf:]
            elif lf > le:
                for key in self.fields[le:]:
                    d[key] = None
        return row.append(d)

    # read-only properties
    # @property
    # def reader(self):
    #     """Access to the csv reader"""
    #     return self._reader

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

    def write(self):
        """Access to the csv writer"""
        #ex. cs.write("dirname/here")
        print("this would write your new logs package")
        return None

    # filter closure
    def filter(filterfunction):
# should work where you call filter(remove(key="result"))
        return None


    # if not cpaVersionManager.isSupported(self.__cpaVersion):
      # raise cpaVersionManager.VersionNotSupported(self.__cpaVersion)

     #if the version is different of 1.x, skip the second line of the csv
    # if(self.__cpaVersion != cpaVersionManager.SUPPORTED_VERSION[0]):
      # self.__listRows.pop(0)

    def get_call(self, pos):
        row = self.row[pos]
        return self.__build_call(row)

    def getCpaVersion(self):
        return self.__cpaVersion

    def numberofcalls(self):
        return len(self.__listRows)

    # build a call from a csv row
      #@param csvRow: csv row that represent the call
    # def __build_call(self,csvRow):

    #       #parse csv
    #     try:
    #       paraxipCallid = csvRow[0]
    #       callDate = csvRow[1]
    #       referenceID = csvRow[2]
    #       campaignName = csvRow[3]
    #       phoneNumber = csvRow[4]
    #       cpaResult = csvRow[5]
    #       timeDialing = csvRow[6]
    #       timeConnected = csvRow[7]
    #       timeCpaCompleted = csvRow[8]
    #       timeQueued = csvRow[9]
    #       timeConnectedToAgent = csvRow[10]

    #       if(self.__cpaVersion == cpaVersionManager.SUPPORTED_VERSION[0]):
    #           detailedCpaResult = ""
    #       else:
    #           detailedCpaResult = csvRow[11]
    #     except IndexError:
    #         PyLoggingFunctions.log_error(fileLogger, "Unable to parse the csvRow: " + str(csvRow)+ " (IndexError)")
    #         raise Exception("Invalid row")

    #     #correction
    #     if cpaResult == 'Voice':
    #        cpaResult = 'Human'

    #     #get foreignKeys
    #     cpaResultKey = self.__callset.cpaResults[cpaResult]
    #     detailedCpaResultKey = self.__callset.detailedCpaResults[detailedCpaResult]

    #     #process 1 (string to timeObject)
    #     callDate = cpaOMExtended.processDate(callDate)
    #     timeDialing = cpaOMExtended.processTime(timeDialing)
    #     timeConnected = cpaOMExtended.processTime(timeConnected)
    #     timeCpaCompleted = cpaOMExtended.processTime(timeCpaCompleted)
    #     timeQueued = cpaOMExtended.processTime(timeQueued)
    #     timeConnectedToAgent = cpaOMExtended.processTime(timeConnectedToAgent)

    #     #process 2 (combine the calldate and the time)
    #     timeDialing = cpaOMExtended.processDateTimeFromDateObjects(callDate, timeDialing)
    #     timeConnected = \
    #             cpaOMExtended.processDateTimeFromDateObjects(callDate, timeConnected)
    #     timeCpaCompleted = \
    #             cpaOMExtended.processDateTimeFromDateObjects(callDate, timeCpaCompleted)
    #     timeQueued = cpaOMExtended.processDateTimeFromDateObjects(callDate, timeQueued)
    #     timeConnectedToAgent = \
    #             cpaOMExtended.processDateTimeFromDateObjects(callDate, timeConnectedToAgent)

    #     #intantiate
    #     return Call(paraxipCallid,
    #             callDate,
    #             referenceID,
    #             campaignName,
    #             phoneNumber,
    #             cpaResultKey,
    #             detailedCpaResultKey,
    #             timeDialing,
    #             timeConnected,
    #             timeCpaCompleted,
    #             timeQueued,
    #             timeConnectedToAgent)

