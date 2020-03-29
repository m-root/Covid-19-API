import requests


class Covid19():
    def __init__(self, base_url='https://covidapi.info/api/v1/'):
        self.base_url = base_url

    def public_request(self, api_url):
        '''Public Requests'''
        rURL = self.base_url + api_url
        try:
            data = requests.get(rURL)
            data.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        if data.status_code == 200:
            return data.json()

    def countryData(self, country):
        '''GET Country specific historic data'''
        return self.public_request('country/%s' % country)

    def countryCountGivenDate(self, country, date):
        '''GET Country specific data for a particular date'''
        return self.public_request('country/%s/%s' % (country, date))

    def latestGlobalCount(self):
        ''' GET Latest Global Count '''
        return self.public_request('global')

    def globalDate(self, date):
        '''GET Global count on a particular date'''
        return self.public_request('global/%s' % (date))

    def globalDataTimeRange(self, startDate, endDat):
        '''GET Global count in a date range'''
        return self.public_request('global/%s/%s' % (startDate, endDat))

    def globalTimeSeries(self, startDate, endDate):
        '''GET Global Timeseries data in date range'''
        return self.public_request('global/timeseries/%s/%s' % (startDate, endDate))

    def countryTimeSeries(self, country, startDate, endDate):
        '''GET Country specific time-series data'''
        return self.public_request('country/%s/timeseries/%s/%s' % (country, startDate, endDate))

    def latestDate(self):
        '''GET Date of last record entry for any country'''
        return self.public_request('latest-date')

    def countryLatestData(self, country):
        '''GET Latest record for a country'''
        return self.public_request('country/%s/latest' % country)

    def globalCount(self):
        '''GET Global date-wise count'''
        return self.public_request('global/count')

    def getDate(self):
        '''GET Latest count for all countries'''
        return self.public_request('global/latest')
