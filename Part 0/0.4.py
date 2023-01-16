'''
sequenceDiagram
    participant browser
    participant server

    browser->>server: POST https://fullstack-exampleapp.herokuapp.com/new_note
    activate server
    server->>browser: HTTP code 302
    deactivate server

    browser->>server: GET https://fullstack-exampleapp.com/main.css
    activate server
    server->>browser: the css file
    deactivate server

    browser->>server: GET https://fullstack-exampleapp.com/main.js
    activate server
    server->>browser: the JS file
    deactivate server

    browser->>server: GET https://fullstack-exampleapp.com/data.json
    activate server
    server->>browser: json for notes 
    deactivate server



'''