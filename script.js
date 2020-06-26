let input = document.querySelector('input');
let feed = document.getElementById('content-list');
 
input.addEventListener('change', () => {
    let files = input.files;
 
    if(files.length == 0) return;
 
    const file = files[0];
 
    let reader = new FileReader();
 
    reader.onload = (e) => {
        const file = e.target.result;
        const lines = file.split(/\r\n|\n/);
        // lines.sort(() => Math.random() - 0.5);
        for(line of lines) {
            if (!line.startsWith("Highlight") && !line.startsWith("   ")) {
                let sentence = '<li>' + line + '</li>';
                feed.innerHTML += sentence;
            }
            
        }
        console.log(lines);
    };
 
    reader.onerror = (e) => alert(e.target.error.name);
 
    reader.readAsText(file); 
    
});