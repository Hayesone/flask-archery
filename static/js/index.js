$(document).ready(() => {
  var selected_targets = [];

  $(".target__button").click(function (e) {
    e.preventDefault();
    var $el = $(this);
    var p = $el.parent();
    var date = $el.data("date");
    var target = $el.data("target");
    var time = $el.data("time");
    var i = $el.data("index");
    console.log(i);

    if (i === "none") {
      var index = selected_targets.length;
      console.log(`index: ${index}`);
      $el.data("index", index);
      var output = {
        date,
        target,
        time,
      };
      p.removeClass("target--free");
      p.addClass("target--active");
      selected_targets.push(output);
    } else {
      selected_targets.splice(i, 1);
      $el.data("index", "none");
      p.removeClass("target--active");
      p.addClass("target--free");
    }
    $("#id_booking_data").val(JSON.stringify(selected_targets));
    console.log(selected_targets);
  });
});
