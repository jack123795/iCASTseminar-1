$(document).ready(function() {
  
  $(document).on('click', '#pull', function() {    // RWD: pull-down menu
    $('#menu li').slideToggle();
  });
  
  
  $(document).on('click', '#orderElement', function() { //menu order pull-down
    $('ul li a#order').slideToggle();
    
    var nowElement = $(this).children(); 
    if(!nowElement.attr('class')){
      nowElement.remove();
      $(this).append('<pre class="down">&#9650;</pre>');
    }
    else{
      nowElement.remove();
      $(this).append('<pre>&#9660;</pre>');
    }
    return false;
  });
  
  $(document).on('click', '#sysElement', function() { //menu sys pull-down
    $('ul li a#sys').slideToggle();
    
    var nowElement = $(this).children(); 
    if(!nowElement.attr('class')){
      nowElement.remove();
      $(this).append('<pre class="down">&#9650;</pre>');
    }
    else{
      nowElement.remove();
      $(this).append('<pre>&#9660;</pre>');
    }
    return false;
  });
 
  
  $(document).on('click', '#productElement', function() { //menu sys pull-down
    $('ul li a#product').slideToggle();
    
    var nowElement = $(this).children(); 
    if(!nowElement.attr('class')){
      nowElement.remove();
      $(this).append('<pre class="down">&#9650;</pre>');
    }
    else{
      nowElement.remove();
      $(this).append('<pre>&#9660;</pre>');
    }
    return false;
  });  
 
  $(document).on('click', '#invoiceElement', function() { //menu order pull-down
    $('ul li a#invoice').slideToggle();
    
    var nowElement = $(this).children(); 
    if(!nowElement.attr('class')){
      nowElement.remove();
      $(this).append('<pre class="down">&#9650;</pre>');
    }
    else{
      nowElement.remove();
      $(this).append('<pre>&#9660;</pre>');
    }
    return false;
  });  
  
  $(document).on('click', '#invoiceOutputElement', function() { //menu order pull-down
	    $('ul li a#invoiceOutput').slideToggle();
	    
	    var nowElement = $(this).children(); 
	    if(!nowElement.attr('class')){
	      nowElement.remove();
	      $(this).append('<pre class="down">&#9650;</pre>');
	    }
	    else{
	      nowElement.remove();
	      $(this).append('<pre>&#9660;</pre>');
	    }
	    return false;
	  });  
  
   $(document).on('click', '#dailyReminderElement', function() { //menu order pull-down
    $('ul li a#dailyReminder').slideToggle();
    
    var nowElement = $(this).children(); 
    if(!nowElement.attr('class')){
      nowElement.remove();
      $(this).append('<pre class="down">&#9650;</pre>');
    }
    else{
      nowElement.remove();
      $(this).append('<pre>&#9660;</pre>');
    }
    return false;
  });   
  
  
  $(function(){    /*保持hover*/
      $('li a').each(function(){
      if(this.href==window.location.href)
        $(this).addClass('jsHover');
      });
  });
  
  $('#floating-button').hide();
  $(window).scroll(function() {   /* floating-button */
    if ( $(this).scrollTop() > 300) {
      $('#floating-button').fadeIn("fast");
    }
    else {
      $('#floating-button').stop().fadeOut("fast");
    }
  });    
  
});
