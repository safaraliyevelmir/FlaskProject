/**
 * Theme: Metrica - Responsive Bootstrap 4 Admin Dashboard
 * Author: Mannatthemes
 * Editor Js
 */

$(document).ready(function () {
  if($("#elm1").length > 0){
      tinymce.init({
          selector: "textarea#elm1",
          theme: "modern",
          height:300,
          plugins: [
              "advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker",
              "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
              "save table contextmenu directionality emoticons template paste textcolor"
          ],
          toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | l      ink image | forecolor backcolor emoticons",
          style_formats: [
              {title: 'Bold text', inline: 'b'},
              {title: 'text', inline: 'span', styles: {color: '#000'}},
              {title: 'header', block: 'h1', styles: {color: '#000'}},
              {title: 'Example 1', inline: 'span', classes: 'example1'},
              {title: 'Example 2', inline: 'span', classes: 'example2'},
              {title: 'Table styles'},
              {title: 'Table row 1', selector: 'tr', classes: 'tablerow1'}
          ]
      });
  }
});