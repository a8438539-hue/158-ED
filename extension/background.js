chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "NEW_MESSAGE") {
        fetch("https://你的railway專案名稱.railway.app/webhook", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: request.text })
        });
    }
});