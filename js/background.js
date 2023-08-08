chrome.action.onClicked.addListener((tab) => {
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: test
    });
});
chrome.runtime.onInstalled.addListener(() => {
    console.log('onInstalled...');
});
chrome.runtime.onClicked.addListener(() => {
    console.log('hhh');
})
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.type == "click_event") {
        console.log("click event captured in current webpage");
        // Call the callback passed to chrome.action.onClicked
    }
});
function func() {
    console.log("test");
}