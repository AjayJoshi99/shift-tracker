function updateClock() {
  const now = new Date();
  const ist = new Date(now.toLocaleString("en-US", { timeZone: "Asia/Kolkata" }));

  document.getElementById("clock").innerText =
    ist.toLocaleTimeString("en-US", {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
      hour12: true
    });
}

setInterval(updateClock, 1000);
updateClock();
