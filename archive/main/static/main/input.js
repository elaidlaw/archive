$(document).ready(function() {
  var tags = JSON.parse($('#tags').text());
  var locations = JSON.parse($('#locations').text());
  var people = JSON.parse($('#people').text());
  var start_date_element = $('#id_start_date');
  var end_date_element = $('#id_end_date');
  var timeframe_element = $('#id_timeframe');
  var description_element = $('#id_description');
  var tags_element = $('#id_tags');
  var location_element = $('#id_location');
  var people_element = $('#id_people');
  tags_element.before('<div id="tags_list"></div>');
  var tags_list_element = $('#tags_list');
  people_element.before('<div id="people_list"></div>');
  var people_list_element = $('#people_list');
  var tag_template = $('.tag');
  start_date_element.attr('autocomplete', 'off');
  end_date_element.attr('autocomplete', 'off');
  tags_element.attr('autocomplete','off');
  location_element.attr('autocomplete','off');
  people_element.attr('autocomplete','off');

  var tags_list = []
  var people_list = []

  $('input[value="Submit"]').click(function(event) {
    if (start_date_element.val() == '' && timeframe_element.val() == '') {
      alert('Enter a date into either the start/end date or timeframe fields');
      return false;
    }
    if (description_element.val() == '') {
      alert('Enter a description');
      return false;
    }
    if (tags_list.length == 0 || people_list.length == 0) {
      r = confirm('Are you sure you want to submit with no tags/people?');
      if (!r) {
        return false;
      }
    }
    tags_element.val(JSON.stringify(tags_list))
    people_element.val(JSON.stringify(people_list))
  })

  start_date_element.datepicker();
  end_date_element.datepicker();

  function add_tag(value) {
    if (!tags_list.includes(value)) {
      tags_list.push(value);
      var new_tag = tag_template.clone();
      new_tag.find('p').text(value);
      if (!tags.includes(value)) {
        new_tag.css('background-color', 'orange');
        // new_tag.css('color', 'white');
      }
      new_tag.css('display', 'inline-block');
      new_tag.find('.x').click(function (e) {
        tags_list = tags_list.filter(function (x) { return x != value });
        new_tag.remove()
      });
      tags_list_element.append(new_tag);
    }
    tags_element.val('')
  }

  function add_person(value) {
    if (!people_list.includes(value)) {
      if (!people.includes(value)) {
        r = confirm('Are you sure you want to add ' + value + ' as a new person?')
        if (!r) {
          people_element.val('')
          return;
        }
      }
      people_list.push(value);
      var new_tag = tag_template.clone();
      new_tag.find('p').text(value);
      if (!people.includes(value)) {
        new_tag.css('background-color', 'orange');
        // new_tag.css('color', 'white');
      }
      new_tag.css('display', 'inline-block');
      new_tag.find('.x').click(function (e) {
        people_list = people_list.filter(function (x) { return x != value; });
        new_tag.remove()
      });
      people_list_element.append(new_tag);
    }
    people_element.val('')
  }

  tags_element.autocomplete({
    autoFocus: true,
    select: function( event, ui ) {
      add_tag(ui.item.value);
      event.preventDefault();
  },
    source: tags,
  });
  people_element.autocomplete({
    autoFocus: true,
    select: function( event, ui ) {
      add_person(ui.item.value);
      event.preventDefault();
  },
    source: people,
  });
  location_element.autocomplete({
    autoFocus: true,
    source: locations,
  });
  location_element.keyup(function(event) {
    if (locations.includes(location_element.val())) {
      location_element.css('color', 'green');
    } else {
      location_element.css('color', 'orange');
    }
  });
  // $('#id_location').autocomplete({
  //   source: locations,
  // });
  // $('#id_people').autocomplete({
  //   source: people,
  // });
  // $('#id_tags').before('<div id="tags_list"></div>');
  tags_element.keypress(function(event) {
    if (event.keyCode == 13) {
      if (tags_element.val() == '') {
        return true;
      }
      add_tag(tags_element.val())
      event.preventDefault();
    }
  });

  people_element.keypress(function(event) {
    if (event.keyCode == 13) {
      if (people_element.val() == '') {
        return true;
      }
      add_person(people_element.val())
      event.preventDefault();
    }
  });
});
