document.getElementById("id_title").onkeyup = function() {
    const e = document.getElementById("id_slug");
    const d = document.getElementById("id_max_adorable_date");
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth() + 1; //January is 0!
    let yyyy = today.getFullYear();
    let minute = today.getMinutes();
    let hour = today.getHours();
    let ms = mm + 1;
    if (dd < 10) {
      dd = '0' + dd;
    }
    if (mm < 10) {
      mm = '0' + mm;
    }
    if (ms < 10) {
      ms = '0' + ms;
    }
    if (hour < 10) {
      hour = '0' + hour;
    }
    if (minute < 10) {
      minute = '0' + minute;
    }
    let today_v = dd + '.' + ms + '.' + yyyy;
    let today_slug = hour + '-' + minute + '_' + dd + '-' + mm;
    if (!e._changed) { e.value = URLify(document.getElementById("id_title").value, 50) + "_" + today_slug}
    if (!d._changed) { d.value = today_v}
};
