$(document).ready(function() {
        // ページ読み込み時に物語をロードする
        loadStory();
        console.log('ストーリーが読み込まれました。')

    $("#user-input").on("input", function () {
        const maxLength = 200;
        const charCount = $("#user-input").val().length;

        if (charCount > maxLength) {
            $("#error-message").show();
            $("#submit-button").prop("disabled", true);
        } else {
            $("#error-message").hide();
            $("#submit-button").prop("disabled", false);
        }

        $("#char-counter").text(charCount + " / " + maxLength);
    });

    $("#input-form").on("submit", function (event) {
        event.preventDefault();
        const userInput = $("#user-input").val();

        // 投稿ボタンを無効化し、待機メッセージを表示する
        $("#submit-button").prop("disabled", true).addClass("disabled");
        $("#submit-button").text("しばらくお待ちください...");

        $.post("/submit", { text: userInput }, function (data) {
            addStoryElement(data.input_text, "user");
            addStoryElement(data.generated_text, "gpt");
            $("#user-input").val("");
            $("#user-input").focus();

            // 投稿ボタンの無効化と待機メッセージを元に戻す
            setTimeout(function () {
                $("#submit-button").prop("disabled", false).removeClass("disabled");
                $("#submit-button").text("投稿");
            }, 5000);
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