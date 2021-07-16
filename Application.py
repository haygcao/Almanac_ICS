# Almanac
# By Clok Much
# Target json:
#       忌/宜: http://www.51wnl.com/YJData/2022.json
#       其他命理: http://www.51wnl.com/moreLumarData/2015.json
# Ref: icalics, By hxgz : https://github.com/hxgz/icalics

import config
import methods

with open(file="黄历.ics", encoding="utf8", mode="w") as file_object:
    start_string = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:" \
                   + config.Default.name + "\nX-WR-TIMEZONE:Asia/Shanghai\n" \
                   + "X-WR-CALDESC:黄历\n"
    file_object.write(start_string)
    body = methods.get_details()
    body_string = ("BEGIN:VEVENT\nDTSTAMP:20190912T184136Z\nUID:",
                   "END:VEVENT\n")
    for item in body:
        body0 = body_string[0]
        body1 = "UID:" + item[0] + 'almanac_in_' + config.Default.year + "\n"
        body2 = "DTSTART;VALUE=DATE:" + item[0] + "\nDTEND;VALUE=DATE:" + item[0] + "\n"
        body3 = "SUMMARY:" + item[1] + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + body3 + body4
        file_object.write(full_body)
    end_string = "END:VCALENDAR"
    file_object.write(end_string)


