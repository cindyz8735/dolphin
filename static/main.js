$(document).ready(function() {

    const num_colors = 5;

    $('#color-toggle').click(function() {
        if ($(this).text() === "Show All Colors") {
            $('.diff').removeClass('hide_colors');
        }
        else {
            $('.diff').addClass('hide_colors');
        }
        $(this).text(function(i, text){
          return text === "Show All Colors" ? "Hide All Colors" : "Show All Colors";
        })
    });

    $('.diff-button').click(function() {
        let diff_id = $(this).attr('diff');
        $('.diff' + diff_id).toggleClass('hide_colors');
        $()
        $(this).text(function(i, text){
          return text === "Show Difference " + diff_id ? "Hide Difference " + diff_id : "Show Difference " + diff_id;
        })
    })
});