# Almanac
# By Clok Much
# Target json:
#       忌/宜: http://www.51wnl.com/YJData/2022.json
#       其他命理: http://www.51wnl.com/moreLumarData/2015.json
# Ref: icalics, By hxgz : https://github.com/hxgz/icalics

import config
import methods

with open(file="黄历.ics", encoding="utf8", mode="w") as file_object:
    start_string = "BEGIN:VCALENDAR\n" + "VERSION:2.0\n" + "X-WR-CALNAME:" + config.Default.name + "\n" + \
                   "X-APPLE-CALENDAR-COLOR:" + config.Default.color + "\n" + "X-WR-TIMEZONE:" + config.Default.zone + \
                   "\n"
    file_object.write(start_string)
    body = methods.get_details()
    body_string = ("BEGIN:VEVENT\nUID:",
                   "SEQUENCE:0\nBEGIN:VALARM\nTRIGGER;VALUE=DATE-TIME:19760401T005545Z\nACTION:NONE\nEND:VALARM\n")
    for item in body:
        body0 = body_string[0]
        body1 = "UID:" + item[0] + 'almanac_in_' + config.Default.year + "\n"
        body2 = "DTSTART;VALUE=DATE:" + item[0] + "\n" + "DTEND;VALUE=DATE:" + item[0] + "\n"
        body3 = "SUMMARY:" + item[1] + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + body3 + body4
        file_object.write(full_body)
    end_string = "END:VCALENDAR"
    file_object.write(end_string)


