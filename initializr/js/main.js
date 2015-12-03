    var template1 = Handlebars.templates['nav_list'];

    //var searchTemplate = $('#dvd-search-template').html();
    var template2 = Handlebars.templates['dvd_search'];

    //var listTemplate = $('#dvd-list-template').html();
    var template3 = Handlebars.templates['dvd_list'];

    //var paginationSearchTemplate = $('#pagination-search-template').html();
    var template4 = Handlebars.templates['pagination_search'];

    //var paginationListTemplate = $('#pagination-list-template').html();
    var template5 = Handlebars.templates['pagination_list'];

    var template6 = Handlebars.templates['dvd_detail'];

var setUp = function() {
      $('.search_bar').show();
      $('#pagination-search').show();
      
      console.log('dvd search');

      $.ajax({
          type:'GET',
          url:'http://127.0.0.1:8000/dvd_search/',
          data:{},
          success: function(data){
              nav_template = template1(data);
              navList.html(nav_template);

              search_template = template2(data);
              dvdSearch.html(search_template);

              pagination_search_template = template4(data);
              paginationSearch.html(pagination_search_template);

              
          }
      });
}


var paginate_search = function() {
$('#pagination-search').on('click', '.page-button', function(e) {
              console.log(e.target.id);
              $('.search_bar').show();
              $('#pagination-search').show();
              $('#pagination-list').css('display', 'none');
              $('#dvd-list').css('display', 'none');
              $('#dvd-search').show();
              $.ajax({
                  type:'GET',
                  url:'http://127.0.0.1:8000/dvd_search/',
                  data:{'page': e.target.id, 'search_term': search_term},
                  success: function(data) {

                      nav_template = template1(data);
                      navList.html(nav_template);

                      search_template = template2(data)
                      dvdSearch.html(search_template);

                      pagination_search_template = template4(data);
                      paginationSearch.html(pagination_search_template);

                  }
              })
      });
}

var paginate_list = function() {
$('#pagination-list').on('click', '.page-button', function(e) {
              console.log(e.target.id);
              $('.search_bar').css('display', 'none');
              $('#pagination-search').css('display', 'none');
              $('#pagination-list').show();
              $('#dvd-search').css('display', 'none');
              $('#dvd-list').show();
              $.ajax({
                  type:'GET',
                  url:'http://127.0.0.1:8000/dvd_list/',
                  data:{'page': e.target.id, 'letter': page_letter},
                  success: function(data) {

                      nav_template = template1(data);
                      navList.html(nav_template);


                      list_template = template3(data)
                      dvdList.html(list_template);

                      pagination_list_template = template5(data);
                      paginationList.html(pagination_list_template);

                      

                  }
              })
      });
}

var nav_list_search = function() {
$('#nav-list').on('click', '#search-dvds', function(e){

          console.log('dvd search icon');

          $('.search_bar').show();
          $('#pagination-search').show();
          $('#pagination-list').css('display', 'none');
          $('#dvd-list').css('display', 'none');
          $('#dvd-search').show();

          $.ajax({
              type:'GET',
              url:'http://127.0.0.1:8000/dvd_search/',
              data:{},
              success: function(data){
                  html_template = template2(data)
                  dvdSearch.html(html_template)

                  pagination_search_template = template4(data);
                  paginationSearch.html(pagination_search_template);

              }
            })
          });
}

var nav_list_letter = function() {
    $('#nav-list').on('click', '.letter', function(e) {
          $('.search_bar').css('display', 'none');
          $('#pagination-search').css('display', 'none');
          $('#pagination-list').show();
          $('#dvd-search').css('display', 'none');
          $('#dvd-list').show();
          console.log('letter');
          console.log(e.target.id);

          page_letter = e.target.id

          $.ajax({
          type:'GET',
          url:'http://127.0.0.1:8000/dvd_list/',
          data:{'letter': e.target.id},
          success: function(data) {

              nav_template = template1(data);
              navList.html(nav_template);

              list_template = template3(data);
              dvdList.html(list_template);

              pagination_list_template = template5(data);
              paginationList.html(pagination_list_template);

          }
        });
      })
  }

var search_detail = function() {
$('#dvd-search').on('click', '.dvd', function(e){
        $('.search_bar').css('display', 'none');
        $('#pagination-search').css('display', 'none');
        $('#pagination-list').css('display', 'none');
        $('#dvd-search').show();
        $('#dvd-list').css('display', 'none');
      console.log('dvd detail');

        

        $.ajax({
            type:'GET',
            url:'http://127.0.0.1:8000/dvd_detail/' + e.target.id,
            data:{},
            success: function(data){

                detail_template = template6(data);
                dvdSearch.html(detail_template);


            }
        });
    });
}

var list_detail = function() {
$('#dvd-list').on('click', '.dvd', function(e){
        $('.search_bar').css('display', 'none');
        $('#pagination-search').css('display', 'none');
        $('#pagination-list').css('display', 'none');
        $('#dvd-search').css('display', 'none');
        $('#dvd-list').show();
      console.log('dvd detail');

        $.ajax({
            type:'GET',
            url:'http://127.0.0.1:8000/dvd_detail/' + e.target.id,
            data:{},
            success: function(data){
                detail_template = template6(data)
                dvdList.html(detail_template)
                

            }
        });
    });
}

var search_result = function() {
$('#search').on('keyup', function(){

        $('#searchsubmit').on('click', function(){
          
          search_term = $('#search').val();
          console.log(search_term);

          $.ajax({
          type:'GET',
          url:'http://127.0.0.1:8000/dvd_search/',
          data:{'search_term': search_term},
          success: function(data) {

              nav_template = template1(data);
              navList.html(nav_template);

              search_template = template2(data);
              dvdSearch.html(search_template);

              pagination_search_template = template4(data);
              paginationSearch.html(pagination_search_template);

          }
        });

    });
});

}
