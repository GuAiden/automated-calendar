def readSheetRange(sheetService, sheetId, range):
    try:
        return sheetService.spreadsheets().values().get(
            spreadsheetId=sheetId, range=range
        ).execute()
    except Exception as e:
        print(f"Read sheet range failed with exception {e}")
    
def processSheetRange(data):
    result = []
    for e in data:
        for i in e:
            result.append(i)
    return result