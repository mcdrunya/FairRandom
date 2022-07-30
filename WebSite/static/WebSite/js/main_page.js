function Random() {
    min = Math.ceil(document.getElementById("min").value);
    max = Math.floor(document.getElementById("max").value);

    if (min != "" && max != "")
      document.getElementById('result').value = Math.floor(Math.random() * (max - min + 1)) + min;
    else
      alert('You have to enter a range!');
      console.log("No");
}

  function Clear() {
    var min_input = document.getElementById("min"),
    max_input = document.getElementById("max"),
    result = document.getElementById("result");
    min_input.value = min_input.defaultValue;
    max_input.value = max_input.defaultValue;
    result.value = result.defaultValue;
  }

  function ClientTime() {
    var dt = new Date(new Date().toString().split('GMT')[0]+' UTC').toISOString();
    document.getElementById('date-time').value=dt;
  }