(() => {
  const button = document.getElementById("theme-toggle");
  const preference = window.matchMedia("(prefers-color-scheme: dark)");
  const isDark = () =>
    document.documentElement.dataset.theme
      ? document.documentElement.dataset.theme === "dark"
      : preference.matches;
  const sync = () => {
    button.setAttribute(
      "aria-label",
      `Switch to ${isDark() ? "light" : "dark"} theme`,
    );
    document.querySelector('meta[name="theme-color"]').content = isDark()
      ? "#101e26"
      : "#f5f5ef";
  };
  button.hidden = false;
  button.addEventListener("click", () => {
    const theme = isDark() ? "light" : "dark";
    document.documentElement.dataset.theme = theme;
    try {
      localStorage.setItem("portfolio-theme", theme);
    } catch {}
    sync();
  });
  preference.addEventListener("change", sync);
  sync();
})();
