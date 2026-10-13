(() => {
  let theme;
  try {
    theme = localStorage.getItem("portfolio-theme");
  } catch {}
  if (theme === "dark" || theme === "light")
    document.documentElement.dataset.theme = theme;
})();
