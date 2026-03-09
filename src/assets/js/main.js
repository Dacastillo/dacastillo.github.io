/**
 * Main JavaScript for dacastillo.github.io
 * Handles mobile navigation toggle and other interactive features
 */

(function() {
  'use strict';

  // Mobile Navigation Toggle
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (navToggle && navMenu) {
    navToggle.addEventListener('click', function() {
      const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', !isExpanded);
      navMenu.classList.toggle('active');
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
      if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
        navMenu.classList.remove('active');
        navToggle.setAttribute('aria-expanded', 'false');
      }
    });

    // Close menu when clicking on a nav link
    const navLinks = navMenu.querySelectorAll('.nav-link');
    navLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        navMenu.classList.remove('active');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // Add active class to current nav item
  const currentPage = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(function(link) {
    if (link.getAttribute('href') === currentPage) {
      link.classList.add('active');
    }
  });

  // Lazy loading images (fallback for browsers without native support)
  if ('loading' in HTMLImageElement.prototype === false) {
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(function(img) {
      img.src = img.dataset.src || img.src;
    });
  }

  // Set current year and last updated date
  const currentYearEl = document.getElementById('current-year');
  const lastUpdatedEl = document.getElementById('last-updated');
  
  if (currentYearEl) {
    currentYearEl.textContent = new Date().getFullYear();
  }
  
  if (lastUpdatedEl) {
    const today = new Date();
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    lastUpdatedEl.textContent = today.toLocaleDateString('en-US', options);
  }

  // Console welcome message
  console.log('%cWelcome to Daniel Castillo Castro\'s website!', 'color: #1e3a5f; font-size: 16px; font-weight: bold;');
  console.log('%cBuilt with 11ty (Eleventy) - Static Site Generator', 'color: #0d9488; font-size: 12px;');

})();
