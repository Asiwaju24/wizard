document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    toggle.addEventListener('click', function() {
        navLinks.classList.toggle('open');
        toggle.classList.toggle('active');
    });
});

document.getElementById('jobForm').addEventListener('submit', function(e) {
    e.preventDefault();
    document.getElementById('successMsg').style.display = 'block';
    this.reset();
});


const animatedElements = document.querySelectorAll(
  '.fade-in, .ease-out, .slide-in-left, .slide-in-right'
);

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('scroll-show');
    } else {
      entry.target.classList.remove('scroll-show');
    }
  });
}, {
  threshold: 0.2,
});

animatedElements.forEach(el => observer.observe(el));
