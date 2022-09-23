// --------------------- BUDGET ----------------------------------

if($('.add_new_income_btn')){
    $('.add_new_income_btn').on('click', function(){
        $('.budgetNewAddForm').css('max-height', '700px');
        setTimeout(function(){ $('.budgetNewAddForm').css('opacity', '1')}, 150)
    })
}


function openBudgetItem(evt, budgetItemName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(budgetItemName).style.display = "block";
    evt.currentTarget.className += " active";
}

// $('.tablinks').click();
// $('.tablinks').first().addClass('active');


if ($('.delete_budget_item')){
    $(document).ready(function(){
        $('.delete_budget_item').on('click', function(e){
            var parent = $(this).parent('.budget_item');
            var delete_budget_item_id = $(this).next('.delete_budget_item_id').val();

            $.ajax({
                method:'POST',
                url:'/add_budget_item/',
                headers: { "X-CSRFToken":$('input[name=csrfmiddlewaretoken]').val()},
                data:{
                    'budget_item_id':delete_budget_item_id,
                }, 
                success: function() {
                    parent.hide();
                },
            });

        });
    });
}