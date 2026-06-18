// 使用 MutationObserver 監測訊息視窗的 DOM 變化
const observer = new MutationObserver((mutations) => {
    const lastMessage = document.querySelector('.message-text:last-child');
    if (lastMessage) {
        const text = lastMessage.innerText;
        // 將訊息傳給 background.js
        chrome.runtime.sendMessage({ action: "NEW_MESSAGE", text: text });
    }
});
observer.observe(document.body, { childList: true, subtree: true });