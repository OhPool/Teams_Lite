import webview

if __name__ == '__main__':
    window = webview.create_window('Teams Lite', 'https://teams.microsoft.com/_#/school/teams-grid/General?ctx=teamsGrid', resizable=True, fullscreen=False, width=1280, height=720, on_top=True )
    webview.start(debug=False, http_server=False)
    