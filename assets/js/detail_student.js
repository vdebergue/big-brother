$(document).ready( function() {

    var mock = {
        fbProfile : {
            school   : "Telecoms",
            majors   : "IA, Security, Hacking",
            from     : "05/01/2012",
            to       : "09/30/2012",
            keywords : "IA, Security, Hacking"
        }
    };

    function showSaveButton() {
        $('#save_button').parent().show();
    }

    function showMainForm() {
        $('#main_form').show();
        showSaveButton();
    }

    function newDates() {
        $clones = $('#internship').children().clone();
        $clones.find('input').val("");
        $('#internship').parent().append($clones);
        $('.datepicker').datepicker();
        $('.internship_plus').unbind('click');
        $('.internship_plus').on('click', newDates);
    }

    function bindAddButtons() {
        $editProject = $('#edit_project_section');
        $editOrga = $('#edit_orga_section');
        $editSkill = $('#edit_skill_section');
        $editInternship = $('#edit_internship_section');
        $editReferences = $('#edit_references_section');

        $('#add_project_button').on('click', function() {
            $editProject.slideDown('fast');

            $editReferences.slideUp('fast');
            $editOrga.slideUp('fast');
            $editSkill.slideUp('fast');
            $editInternship.slideUp('fast');
        });

        $('#add_orga_button').on('click', function() {
            $editOrga.slideDown('fast');

            $editReferences.slideUp('fast');
            $editProject.slideUp('fast');
            $editInternship.slideUp('fast');
            $editSkill.slideUp('fast');
        });

        $('#add_skill_button').on('click', function() {
            $editSkill.slideDown('fast');

            $editReferences.slideUp('fast');
            $editProject.slideUp('fast');
            $editInternship.slideUp('fast');
            $editOrga.slideUp('fast');
        });

        $('#add_internship_button').on('click', function() {
            $editInternship.slideDown('fast');

            $editReferences.slideUp('fast');
            $editProject.slideUp('fast');
            $editOrga.slideUp('fast');
            $editSkill.slideUp('fast');
        });
        
        $('#add_references_button').on('click', function() {
            $editReferences.slideDown('fast');

            $editInternship.slideUp('fast');
            $editProject.slideUp('fast');
            $editOrga.slideUp('fast');
            $editSkill.slideUp('fast');
        });
    }

    function bindSaveButtons() {
        $inputProject = $('#edited-inputProject');
        $inputOrga = $('#edited-inputSorority');
        $inputSkill = $('#edited-inputSkill');
        $inputInternship = $('#edited-inputInternship');

        $inputProject.on('keyup keydown keypress change paste', function() {
            if($(this).val() == '') {
                $('#save_project_button').addClass('disabled');            
            } else {
                $('#save_project_button').removeClass('disabled'); 
            }
        });

        $inputOrga.on('keyup keydown keypress change paste', function() {
            if($(this).val() == '') {
                $('#save_orga_button').addClass('disabled');            
            } else {
                $('#save_orga_button').removeClass('disabled'); 
            }
        });
      
        $inputSkill.on('keyup keydown keypress change paste', function() {
            if($(this).val() == '') {
                $('#save_skill_button').addClass('disabled');            
            } else {
                $('#save_skill_button').removeClass('disabled'); 
            }
        });
        $inputInternship.on('keyup keydown keypress change paste', function() {
            if($(this).val() == '') {
                $('#save_internship_button').addClass('disabled');            
            } else {
                $('#save_internship_button').removeClass('disabled'); 
            }
        });
        $inputInternship.on('keyup keydown keypress change paste', function() {
            if($(this).val() == '') {
                $('#save_references_button').addClass('disabled');            
            } else {
                $('#save_references_button').removeClass('disabled'); 
            }
        });
    }

    function init2() {
        var $container = $('#main_container');
        $container.delay('300').fadeIn('slow');

        $('#second_page_majors').html(mock.fbProfile.majors);
        $('#intern_from').html(mock.fbProfile.from);
        $('#intern_to').html(mock.fbProfile.to);

        bindAddButtons();
        bindSaveButtons();

        $("#truand").on("click", function(){
          $("#truand2").show();
        });

        $('#friend_list').on('click',friendsAutocomplete);
    }

    function friendsAutocomplete(){
        var makeItems = function(fbresponse) {
          return $.map(fbresponse, function(item) {
            return {
              label: item.name,
              value: item.id,
            }
          });
        };

        var setAutoComplete = function(parsed_items) {
         console.log(parsed_items);
          $("#input_13").autocomplete({
            source : parsed_items,
            select : function(event, ui){
              $("#input_13").val(ui.item.label);
              return false;
            }
          }).data( "autocomplete" )._renderItem = function( ul, item ) {
            return $( "<li>" )
                .data( "item.autocomplete", item )
                .append( "<div><img src='http://graph.facebook.com/"+ item.value +"/picture?type=square' ><a style='float:right'>" + item.label + "</a></div>" )
                .appendTo( ul );
            };
        };

        FB.api('/me/friends', function(fbresponse) {
          setAutoComplete(makeItems(fbresponse.data));
        });
        $('#input_13').show();
    }

    init2();
});