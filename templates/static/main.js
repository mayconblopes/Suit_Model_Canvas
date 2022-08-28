const btn = document.getElementById("list-btn");
const smc_list = document.getElementById("smc-list");
btn.addEventListener("click", () => {
    smc_list.classList.toggle("inactive");
})