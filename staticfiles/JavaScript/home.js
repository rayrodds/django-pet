document.addEventListener('DOMContentLoaded', () => {

  // =================================
  // MENU HAMBURGUER – MOBILE ONLY
  // =================================
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link, .nav-btn');

  function isMobile() {
      return window.innerWidth <= 768;
  }

  // Abrir/Fechar menu ao clicar no botão
  hamburger.addEventListener('click', () => {
      if (isMobile()) {
          hamburger.classList.toggle('active');
          navMenu.classList.toggle('active');
      }
  });

  // Fecha o menu ao clicar em qualquer link (mobile)
  navLinks.forEach(link => {
      link.addEventListener('click', () => {
          if (isMobile()) {
              hamburger.classList.remove('active');
              navMenu.classList.remove('active');
          }
      });
  });

  // Fecha o menu ao clicar fora dele (mobile)
  document.addEventListener('click', (e) => {
      if (isMobile() && !hamburger.contains(e.target) && !navMenu.contains(e.target)) {
          hamburger.classList.remove('active');
          navMenu.classList.remove('active');
      }
  });

  // Fecha o menu se a tela for redimensionada para desktop
  window.addEventListener('resize', () => {
      if (!isMobile()) {
          hamburger.classList.remove('active');
          navMenu.classList.remove('active');
      }
  });

  // =================================
  // SCROLL AUTOMÁTICO DOS PARCEIROS
  // =================================
  const cardsContainer = document.querySelector('.cards');
  if (!cardsContainer) return;

  // Duplica os cards para efeito infinito
  cardsContainer.innerHTML += cardsContainer.innerHTML;

  let scrollSpeed = 1.0; // ajuste a velocidade
  let scrollPosition = 0;

  function scrollCards() {
    scrollPosition += scrollSpeed;

    // Quando chegar na metade (conteúdo original), reseta para 0
    if (scrollPosition >= cardsContainer.scrollWidth / 2) {
      scrollPosition = 0;
    }

    cardsContainer.scrollLeft = scrollPosition;
    requestAnimationFrame(scrollCards);
  }

  scrollCards();

  // Pausa ao passar o mouse
  cardsContainer.addEventListener('mouseenter', () => scrollSpeed = 0);
  cardsContainer.addEventListener('mouseleave', () => scrollSpeed = 0.8);

});

const accordionHeaders = document.querySelectorAll('.accordion-header');

accordionHeaders.forEach(header => {
  header.addEventListener('click', () => {
    const item = header.parentElement;

    // Fecha os outros e garante que eles voltem a ter a borda
    document.querySelectorAll('.accordion-item').forEach(i => {
      if (i !== item) {
        i.classList.remove('active');
        i.classList.remove('no-border'); // garante borda nos itens fechados
      }
    });

    // Alterna o atual
    item.classList.toggle('active');
    item.classList.toggle('no-border'); // remove ou coloca a borda
  });
});

