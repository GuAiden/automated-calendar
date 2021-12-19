def sendCalendarInvites(calendarService, id, requestBody):
    try:
        result = calendarService.events().insert(calendarId=id,
                                        sendUpdates='all', body=requestBody).execute()
        return result;
    except Exception as e:
        print(f"Calendar Invite Failed With Error : {e}")
        
def createRequestBody(summary, description, startTime, endTime, attendees):
    # AEST GMT Offset
    GMT_OFF = '+11:00'
    requestBody = {}
    requestBody['summary'] = summary
    requestBody['description'] = description
    requestBody['startTime'] = f"{startTime}{GMT_OFF}"
    requestBody['endTime'] = f"{endTime}{GMT_OFF}"
    requestBody['attendees'] = attendees
    return requestBody