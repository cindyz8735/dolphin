$(document).ready(function() {

    const num_colors = 5;

    $('#color-toggle').click(function() {
        $('.diff').toggleClass('hide_colors');
    });

    $('.diff-button').click(function() {
        let diff_id = $(this).attr('diff');
        let color_category = parseInt(diff_id) % num_colors;
        $('.diff' + diff_id).toggleClass('color' + color_category);
    })
});