// Fade-in cards as they enter the viewport, and keep the pill nav
// state in sync with scroll position. Progressive enhancement only —
// the page is fully usable with this script disabled.

(function () {
  var cards = document.querySelectorAll("[data-reveal]");

  if ("IntersectionObserver" in window && cards.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -40px 0px" }
    );
    cards.forEach(function (card) { io.observe(card); });
  } else {
    cards.forEach(function (card) { card.classList.add("is-visible"); });
  }

  // Smooth scroll for in-page pill nav links
  document.querySelectorAll('.pill-nav a[href^="#"]').forEach(function (link) {
    link.addEventListener("click", function (e) {
      var id = link.getAttribute("href");
      if (id.length > 1) {
        var target = document.querySelector(id);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }
    });
  });

  // Briefly highlight the element a search result (or any #anchor link)
  // lands on, so it's obvious what got navigated to.
  if (location.hash) {
    var landed = document.querySelector(location.hash);
    if (landed) {
      requestAnimationFrame(function () {
        landed.scrollIntoView({ behavior: "smooth", block: "center" });
        landed.classList.add("search-highlight");
        setTimeout(function () { landed.classList.remove("search-highlight"); }, 1600);
      });
    }
  }

  // ---------- Overlay search ----------
  var searchTrigger = document.querySelector("[data-search-trigger]");
  var searchOverlay = document.getElementById("searchOverlay");

  if (searchTrigger && searchOverlay) {
    var searchInput = document.getElementById("searchInput");
    var searchResults = document.getElementById("searchResults");
    var searchScrim = searchOverlay.querySelector(".search-scrim");
    var data = window.SEARCH_DATA || [];

    var CLOSE_DURATION = 220;
    var closeTimer = null;
    var lockedScrollY = 0;

    // overflow:hidden on body alone doesn't stop touch scrolling on iOS
    // Safari, so pin the body in place with position:fixed and restore
    // the scroll position afterwards.
    var lockScroll = function () {
      lockedScrollY = window.scrollY || window.pageYOffset || 0;
      document.body.style.position = "fixed";
      document.body.style.top = -lockedScrollY + "px";
      document.body.style.left = "0";
      document.body.style.right = "0";
      document.body.style.width = "100%";
      document.body.style.overflow = "hidden";
    };

    var unlockScroll = function () {
      document.body.style.position = "";
      document.body.style.top = "";
      document.body.style.left = "";
      document.body.style.right = "";
      document.body.style.width = "";
      document.body.style.overflow = "";
      window.scrollTo(0, lockedScrollY);
    };

    var openSearch = function () {
      clearTimeout(closeTimer);
      searchOverlay.classList.remove("is-closing");
      searchOverlay.classList.add("is-open");
      lockScroll();
      searchInput.value = "";
      searchResults.hidden = true;
      searchResults.innerHTML = "";
      setTimeout(function () { searchInput.focus(); }, 10);
    };

    var closeSearch = function () {
      if (!searchOverlay.classList.contains("is-open")) return;
      searchOverlay.classList.remove("is-open");
      searchOverlay.classList.add("is-closing");
      unlockScroll();
      closeTimer = setTimeout(function () {
        searchOverlay.classList.remove("is-closing");
      }, CLOSE_DURATION);
    };

    var currentMatches = [];
    var activeIndex = -1;

    var setActive = function (index) {
      var rows = searchResults.querySelectorAll(".search-result");
      if (activeIndex >= 0 && rows[activeIndex]) rows[activeIndex].classList.remove("is-active");
      activeIndex = index;
      if (activeIndex >= 0 && rows[activeIndex]) {
        rows[activeIndex].classList.add("is-active");
        rows[activeIndex].scrollIntoView({ block: "nearest" });
      }
    };

    var renderResults = function (query) {
      var q = query.trim().toLowerCase();
      searchResults.innerHTML = "";
      currentMatches = [];
      activeIndex = -1;

      if (!q) {
        searchResults.hidden = true;
        return;
      }

      var matches = data.filter(function (item) {
        return (
          item.title.toLowerCase().indexOf(q) !== -1 ||
          (item.subtitle && item.subtitle.toLowerCase().indexOf(q) !== -1)
        );
      }).slice(0, 30);

      if (!matches.length) {
        var empty = document.createElement("li");
        empty.className = "search-empty";
        empty.textContent = "검색 결과가 없습니다.";
        searchResults.appendChild(empty);
      } else {
        currentMatches = matches;
        matches.forEach(function (item, i) {
          var li = document.createElement("li");
          li.className = "search-result";

          var a = document.createElement("a");
          a.href = item.url;

          var title = document.createElement("span");
          title.className = "search-result-title";
          title.textContent = item.title;

          var meta = document.createElement("span");
          meta.className = "search-result-meta";
          meta.textContent = item.url.replace(/\/$/, "");

          a.appendChild(title);
          a.appendChild(meta);
          li.appendChild(a);

          li.addEventListener("mouseenter", function () { setActive(i); });

          searchResults.appendChild(li);
        });
        setActive(0);
      }

      searchResults.hidden = false;
    };

    searchTrigger.addEventListener("click", function (e) {
      e.preventDefault();
      openSearch();
    });

    if (searchScrim) searchScrim.addEventListener("click", closeSearch);

    document.addEventListener("keydown", function (e) {
      if (!searchOverlay.classList.contains("is-open")) return;

      if (e.key === "Escape") {
        closeSearch();
      } else if (e.key === "ArrowDown" && currentMatches.length) {
        e.preventDefault();
        setActive(Math.min(activeIndex + 1, currentMatches.length - 1));
      } else if (e.key === "ArrowUp" && currentMatches.length) {
        e.preventDefault();
        setActive(Math.max(activeIndex - 1, 0));
      } else if (e.key === "Enter" && activeIndex >= 0 && currentMatches[activeIndex]) {
        e.preventDefault();
        window.location.href = currentMatches[activeIndex].url;
      }
    });

    searchInput.addEventListener("input", function () {
      renderResults(searchInput.value);
    });
  }
})();
