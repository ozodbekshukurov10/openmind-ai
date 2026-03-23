import './style.css'

const slides = [
  {
    eyebrow: 'Investor Pitch Deck',
    title: 'Marketly',
    subtitle: 'Savdo oson, mijoz yaqin',
    body:
      'A modern digital marketplace helping Uzbekistan\'s small businesses reach nearby customers, advertise affordably, and turn price transparency into growth.',
    badges: ['B2B2C Marketplace', 'Uzbekistan Focus', 'SMB Growth Engine'],
    accent: 'hero',
  },
  {
    eyebrow: 'Problem',
    title: 'The local commerce journey is still fragmented',
    bullets: [
      'Local entrepreneurs struggle to consistently find new customers beyond word-of-mouth and scattered messaging groups.',
      'Small businesses lack affordable, effective advertising tools tailored to neighborhood-level demand.',
      'Customers waste time comparing product prices across multiple channels with no standardized view.',
    ],
    stat: { label: 'Pain point', value: '3-sided inefficiency across discovery, promotion, and pricing' },
  },
  {
    eyebrow: 'Solution',
    title: 'Marketly connects supply and demand in one trusted platform',
    bullets: [
      'Entrepreneurs create professional storefronts and reach ready-to-buy local audiences.',
      'Affordable advertising tools help small businesses promote offers, launches, and seasonal campaigns.',
      'Built-in comparison features let customers evaluate prices quickly and confidently.',
    ],
    stat: { label: 'Value proposition', value: 'Simple discovery, smarter promotion, transparent pricing' },
  },
  {
    eyebrow: 'Target Audience',
    title: 'Designed for high-frequency local commerce',
    bullets: [
      'Small business owners who need better digital visibility.',
      'Local entrepreneurs selling products and services across neighborhoods and cities.',
      'Customers searching for the best prices and fastest buying decisions.',
    ],
    stat: { label: 'Market opportunity', value: 'Hundreds of thousands of businesses and millions of customers in Uzbekistan' },
    callout: 'Large underserved SMB base + digitally active consumers = strong adoption potential.',
  },
  {
    eyebrow: 'Alternatives & Differentiation',
    title: 'From scattered listings to structured commerce intelligence',
    columns: [
      {
        heading: 'Current alternatives',
        items: ['Telegram groups', 'OLX-style listing platforms', 'Social media pages and stories'],
      },
      {
        heading: 'Why Marketly wins',
        items: [
          'Professional price comparison instead of manual searching',
          'Dedicated advertising built specifically for small businesses',
          'A focused local-commerce experience rather than general social browsing',
        ],
      },
    ],
    stat: { label: 'Differentiator', value: 'Structured discovery + performance marketing for SMBs' },
  },
  {
    eyebrow: 'Monetization',
    title: 'Multiple revenue streams with scalable upside',
    monetization: [
      { name: 'Premium accounts', description: 'Advanced storefront features, analytics, and visibility boosts.' },
      { name: 'Advertising slots', description: 'Paid placements for promotions, featured listings, and category highlights.' },
      { name: 'Transaction commission', description: 'A percentage from completed transactions as marketplace activity grows.' },
    ],
    stat: { label: 'Business model', value: 'Subscription + ads + transaction-based monetization' },
  },
  {
    eyebrow: 'International Opportunities',
    title: 'Built in Uzbekistan, expandable across Central Asia and beyond',
    bullets: [
      'Expand into neighboring Central Asian markets with similar SMB digitization gaps.',
      'Localize language, categories, and payment flows to accelerate regional adoption.',
      'Evolve into a global platform that empowers small businesses with accessible digital commerce tools.',
    ],
    stat: { label: 'Expansion thesis', value: 'Repeatable SMB playbook for emerging commerce ecosystems' },
  },
  {
    eyebrow: 'Conclusion',
    title: 'Marketly: Big opportunities for small businesses',
    body:
      'Marketly is positioned to become the trusted bridge between entrepreneurs and price-conscious customers—unlocking growth, transparency, and scalable regional expansion.',
    badges: ['Clear pain point', 'Practical monetization', 'Regional growth potential'],
    accent: 'closing',
  },
]

const renderBullets = (bullets = []) =>
  bullets
    .map(
      (bullet) => `
        <li>
          <span class="bullet-mark"></span>
          <span>${bullet}</span>
        </li>`,
    )
    .join('')

const renderSlides = () =>
  slides
    .map((slide, index) => {
      const badges = slide.badges
        ? `<div class="badge-row">${slide.badges.map((badge) => `<span class="badge">${badge}</span>`).join('')}</div>`
        : ''

      const subtitle = slide.subtitle ? `<p class="slide-subtitle">${slide.subtitle}</p>` : ''
      const body = slide.body ? `<p class="slide-body">${slide.body}</p>` : ''
      const stat = slide.stat
        ? `
          <div class="stat-card">
            <span>${slide.stat.label}</span>
            <strong>${slide.stat.value}</strong>
          </div>`
        : ''

      const bulletList = slide.bullets
        ? `<ul class="bullet-list">${renderBullets(slide.bullets)}</ul>`
        : ''

      const columns = slide.columns
        ? `
          <div class="comparison-grid">
            ${slide.columns
              .map(
                (column) => `
                  <div class="comparison-card">
                    <h3>${column.heading}</h3>
                    <ul class="mini-list">${column.items.map((item) => `<li>${item}</li>`).join('')}</ul>
                  </div>`,
              )
              .join('')}
          </div>`
        : ''

      const monetization = slide.monetization
        ? `
          <div class="revenue-grid">
            ${slide.monetization
              .map(
                (item) => `
                  <article class="revenue-card">
                    <h3>${item.name}</h3>
                    <p>${item.description}</p>
                  </article>`,
              )
              .join('')}
          </div>`
        : ''

      const callout = slide.callout ? `<p class="callout">${slide.callout}</p>` : ''

      return `
        <section class="slide ${slide.accent || ''}" id="slide-${index + 1}">
          <div class="slide-header">
            <span class="eyebrow">${String(index + 1).padStart(2, '0')} · ${slide.eyebrow}</span>
            <h2>${slide.title}</h2>
          </div>
          ${subtitle}
          ${body}
          ${badges}
          ${bulletList}
          ${columns}
          ${monetization}
          ${callout}
          ${stat}
        </section>`
    })
    .join('')

const agenda = slides
  .map(
    (slide, index) => `
      <a href="#slide-${index + 1}">
        <span>${String(index + 1).padStart(2, '0')}</span>
        <strong>${slide.eyebrow}</strong>
      </a>`,
  )
  .join('')

document.querySelector('#app').innerHTML = `
  <div class="deck-shell">
    <aside class="sidebar">
      <div>
        <p class="sidebar-label">Startup deck</p>
        <h1>Marketly</h1>
        <p class="sidebar-copy">Creative investor presentation crafted to showcase the platform, market need, and scale potential.</p>
      </div>
      <nav class="agenda">
        ${agenda}
      </nav>
    </aside>

    <main class="deck-content">
      <section class="hero-banner">
        <div>
          <p class="hero-label">Investor-ready narrative</p>
          <h2>Connecting small businesses with nearby customers through smarter discovery and pricing.</h2>
        </div>
        <div class="hero-metrics">
          <div>
            <span>Audience</span>
            <strong>SMBs + Consumers</strong>
          </div>
          <div>
            <span>Region</span>
            <strong>Uzbekistan first</strong>
          </div>
          <div>
            <span>Growth</span>
            <strong>Central Asia next</strong>
          </div>
        </div>
      </section>

      <div class="slides-grid">
        ${renderSlides()}
      </div>
    </main>
  </div>
`
