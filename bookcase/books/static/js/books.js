$(document).ready(function(){
$('[data-toggle="tooltip"]').tooltip();
});
$(document).ready(function(){
    var isAnyBookLoaned = $('.warning').attr('data-loaned');
    if (isAnyBookLoaned == "true"){
    $('.borrow').addClass('disabled');
    }
});
$(document).on("click", ".details", function(event){
    var bookId = $(this).attr('data-catid');
    window.location="detailbook/"+bookId;
    }
)

$(document).on("click", ".deletefrombasket", function(){
    var bookId = $(this).attr('data-catid');
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type:"POST",
        url: "/delete_from_basket",
        data:{
            'csrfmiddlewaretoken': csrftoken,
            'book_id': bookId,
        },
        dataType: 'json',
        success: function(data){
        if (data.success){
            setTimeout(function(){
            location.reload();
                }, 100);
            }
        else{
            alert("There is an error occurred");
            }
        }
    });
});
$(document).on("click", ".basket", function(event){
    event.stopImmediatePropagation();
    var bookid = $(this).attr("data-catid");
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type:"POST",
        url: "add_to_basket",
        data:{
            'csrfmiddlewaretoken': csrftoken,
            'book_id': bookid,
            },
        dataType: 'json',
        success: function(data){
            if (data.success){
                $('#status'+bookid).text("In basket");
                $('#status'+bookid).removeClass('text-success');
                $('#status'+bookid).addClass('text-warning');
                $('#basket'+bookid).addClass('btn btn-warning disabled');
                if($('#userbasket').hasClass('disabled')){
                $('#userbasket').removeClass('disabled');
                }
            }
            else{
            alert("There is an error occurred");
            }
        }
    });
});
$(document).on("click", ".giveback", function(event){
    event.stopImmediatePropagation();
    var bookid = $(this).attr('data-catid');
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
      type:"POST",
      url: "/usergivebackbook",
      data:{
      'csrfmiddlewaretoken': csrftoken,
      'book_id': bookid,
      },
      dataType: 'json',
      success: function(data){
        if (data.success){
            setTimeout(function(){
                location.reload();
            }, 100);
            }
        else {
            alert("There is an error occurred");
            }
        }
    });
});