const sections = document.querySelectorAll('.section');

function revealSections() {
    sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top < window.innerHeight * 0.8) {
            section.classList.add('show');
        }
    });
}

window.addEventListener('scroll', revealSections);
revealSections();

document.addEventListener("DOMContentLoaded", function() {
    const sparkleContainer = document.createElement("div");
    sparkleContainer.classList.add("sparkles");
    document.body.appendChild(sparkleContainer);

    function createSparkle() {
        const sparkle = document.createElement("div");
        sparkle.classList.add("sparkle");
        sparkle.style.top = Math.random() * 100 + "vh";
        sparkle.style.left = Math.random() * 100 + "vw";
        sparkle.style.animationDuration = (Math.random() * 3 + 2) + "s";
        sparkleContainer.appendChild(sparkle);

        setTimeout(() => {
            sparkle.remove();
        }, 5000);
    }

    setInterval(createSparkle, 300);
});

