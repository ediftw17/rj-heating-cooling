const { copyFileSync, statSync } = require('fs');

const base = '/Users/edwardabramov/Documents/Antigravity/Dambl/projects/website-building-agency/clients/rj-heating-cooling-cleveland/assets/';

const copies = [
  ['hero-candidate-2.jpg', 'hero.jpg'],
  ['about-candidate.jpg', 'about.jpg'],
  ['service-candidate-1.jpg', 'service-1.jpg'],
  ['service-candidate-2.jpg', 'service-2.jpg'],
  ['service-candidate-3.jpg', 'service-3.jpg'],
  ['hero-candidate-3.jpg', 'service-4.jpg'],
];

module.exports = async (page) => {
  const results = [];
  for (const [src, dst] of copies) {
    try {
      copyFileSync(base + src, base + dst);
      const size = statSync(base + dst).size;
      results.push(`OK: ${dst} (${size} bytes)`);
    } catch(e) {
      results.push(`FAIL: ${dst} — ${e.message}`);
    }
  }
  return results.join('\n');
};
