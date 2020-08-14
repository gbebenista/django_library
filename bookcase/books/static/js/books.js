// add tooltip
$(document).ready(function(){
$('[data-toggle="tooltip"]').tooltip();
});

// disable borrow button if any book has been borrowed
$(document).ready(function(){
    if ( $('.warning').attr('data-loaned')){
    $('.borrow').addClass('disabled');
    }
});
// link to books' details on whole row of table
$(document).on("click", ".details", function(event){
    var bookId = $(this).attr('data-catid');
    window.location="detailbook/"+bookId;
    }
)

//delete from basket
$(document).on("click", ".deletefrombasket", function(event){
    event.stopImmediatePropagation();
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

// add to basket
$(document).on("click", ".basket", function(event){
    event.stopImmediatePropagation();
    var bookid = $(this).attr("data-catid");
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type:"POST",
        url: '/add_to_basket',
        data:{
            'csrfmiddlewaretoken': csrftoken,
            'book_id': bookid,
            },
        dataType: 'json',
        success: function(data){
            if (data.success){
                if ($('#basket'+bookid).hasClass('btn-success')){
                    $('#detail'+bookid).text("In basket");
                    $('#status'+bookid).text("In basket");
                    $('#status'+bookid).removeClass('text-success');
                    $('#status'+bookid).addClass('text-warning');
                    $('#basket'+bookid).addClass('btn-warning disabled');
                    $('#basket'+bookid).removeClass('btn-success');
                }
                else{
                    $('#detail'+bookid).text("Available");
                    $('#status'+bookid).text("Available");
                    $('#status'+bookid).removeClass('text-warning');
                    $('#status'+bookid).addClass('text-success');
                    $('#basket'+bookid).removeClass('btn-warning disabled');
                    $('#basket'+bookid).addClass('btn-success');
                }
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

//return book
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