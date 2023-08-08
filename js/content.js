document.addEventListener("click", () => {
    chrome.runtime.sendMessage({
        type: "click_event"
    });
})
chrome.action.onClicked.addListener(() => {
    console.log('hhh');
})