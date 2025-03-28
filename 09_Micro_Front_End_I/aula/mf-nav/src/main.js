const listaDeLinks = document.querySelector('#lista-de-links');

window.addEventListener('message', (event) => {
  if (event.data.type == 'INICIAR') {
    //console.log('event.data', event.data);
    event.data.rotas.forEach(rota => {
      //console.log('rota', rota);
      const li = document.createElement('li');
      const ancora = document.createElement('a');
      ancora.innerText = rota.nome;
      ancora.setAttribute('href', rota.path);
      
      ancora.addEventListener('click', (evt) => {
          evt.preventDefault();
          window.parent.postMessage({type: 'NAVEGACAO', destino: rota}, '*');
      })
      
      li.appendChild(ancora);
      listaDeLinks.appendChild(li);
    })    
  }
})