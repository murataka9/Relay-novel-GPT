$(document).ready(function() {
        // ページ読み込み時に物語をロードする
        loadStory();

    $("#input-form").on("submit", function(event) {
        event.preventDefault();
    const userInput = $("#user-input").val();
    $.post("/submit", {text: userInput}, function (data) {
        addStoryElement(data.input_text, "user");
    addStoryElement(data.generated_text, "gpt");
    $("#user-input").val("");
    $("#user-input").focus();
        });
    });
});

    function addStoryElement(text, cssClass) {
    const newElement = $("<div></div>").text(text).addClass(cssClass);
    $("#story-container").append(newElement);
}

function loadStory() {
    $.get("/load_story", function (data) {
        $("#story-title").text(data.title);
        for (const el of data.story) {
            addStoryElement(el.text, el.type);
        }
    });
}