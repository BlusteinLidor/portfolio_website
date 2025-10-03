// const res = fetch('view-source:https://www.youtube.com/@TechWithTim');
// const html = res.body.innerHTML
// console.log(html)

fetch('https://api.codetabs.com/v1/proxy?quest=google.com').then((response) => response.text()).then((text) => console.log(text));

