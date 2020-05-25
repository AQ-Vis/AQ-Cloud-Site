### Info on how Flask serves static files:
- Store only HTML files here
- .js and .css files can be stored in their respective subfolders in the static folder
- JavaScript files can be linked by the command  
`<script src="{{url_for('static', filename='js/filename.js')}}"></script>`  
- CSS files can be linked by the command  
`<link rel="stylesheet" href="{{url_for('static', filename='css/filename.css')}}">`  
