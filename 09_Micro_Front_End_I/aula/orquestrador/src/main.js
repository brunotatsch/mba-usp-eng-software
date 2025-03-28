import './style.css';

const rotas = [
  {
    path: '/',
    source: 'http://localhost:8002',
    nome: 'Home'
  },
  {
    path: '/produtos',
    source: 'http://localhost:8003',
    nome: 'Produtos'
  },
  {
    path: '/clientes',
    source: 'http://localhost:8001',
    nome: 'Clientes'
  }
]

const navIframe = document.querySelector('#mf-nav');
const containerIframe = document.querySelector('#container');

const pathAtual = window.location.pathname;

const mfInicial = rotas.find(rota => rota.path == pathAtual);

if (mfInicial) {
  containerIframe.setAttribute('src', mfInicial.source);
}

navIframe.onload = () => {
  navIframe.contentWindow.postMessage({ type: 'INICIAR', rotas }, 'http://localhost:8000');
}

window.addEventListener('message', (event) => {
  if (event.data.type == 'NAVEGACAO') {
    console.log('event.data', event.data);
    const mfAlvoNavegacao = rotas.find(rota => rota.path == event.data.destino.path);

    if (mfAlvoNavegacao) {
      containerIframe.setAttribute('src', mfAlvoNavegacao.source);
      window.history.pushState({}, '', mfAlvoNavegacao.path);
    }
  }
});
 
window.addEventListener('popstate', () => {
  const path = window.location.pathname;
  const mfAlvoPop = rotas.find(rota => rota.path == path);

  if (mfAlvoPop) {
    containerIframe.setAttribute('src', mfAlvoPop.source);
    window.history.pushState({}, '', mfAlvoPop.path);
  }
});