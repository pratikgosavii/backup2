$('select').each(function() {
    var $this = $(this),
        numberOfOptions = $(this).children('option').length;

    $this.addClass('select-hidden');
    $this.wrap('<div class="select"></div>');
    $this.after('<div class="select-styled"></div>');

    var $styledSelect = $this.next('div.select-styled');
    $styledSelect.text($this.children('option').eq(0).text());

    var $list = $('<ul />', {
        'class': 'select-options'
    }).insertAfter($styledSelect);

    for (var i = 0; i < numberOfOptions; i++) {
        $('<li />', {
            text: $this.children('option').eq(i).text(),
            rel: $this.children('option').eq(i).val()
        }).appendTo($list);
    }

    var $listItems = $list.children('li');

    $styledSelect.click(function(e) {
        e.stopPropagation();
        $('div.select-styled.active').not(this).each(function() {
            $(this).removeClass('active').next('ul.select-options').hide();
        });
        $(this).toggleClass('active').next('ul.select-options').toggle();
    });

    $listItems.click(function(e) {
        e.stopPropagation();
        $styledSelect.text($(this).text()).removeClass('active');
        $this.val($(this).attr('rel'));
        $list.hide();
        //console.log($this.val());
    });

    $(document).click(function() {
        $styledSelect.removeClass('active');
        $list.hide();
    });

});



var alert_items = document.querySelectorAll(".alert_item");
var btns = document.querySelectorAll(".btn");
var alert_wrapper = document.querySelector(".alert_wrapper");
var close_btns = document.querySelectorAll(".close");

btns.forEach(function(btn, btn_index) {
    btn.addEventListener("click", function() {
        alert_wrapper.classList.add("active");

        alert_items.forEach(function(alert_item, alert_index) {
            if (btn_index == alert_index) {
                alert_item.style.top = "50%";
            } else {
                alert_item.style.top = "-100%";
            }
        })
    })
})

close_btns.forEach(function(close, close_index) {
    close.addEventListener("click", function() {
        alert_wrapper.classList.remove("active");

        alert_items.forEach(function(alert_item, alert_index) {
            alert_item.style.top = "-100%";
        })
    })
})