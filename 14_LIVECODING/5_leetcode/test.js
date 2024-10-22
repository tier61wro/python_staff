var API_KEY = 'CCf9Rd1e19HXtO';  // API-ключ из Gridly
var BASE_URL = 'https://eu-central-1.api.gridly.com/v1';  // Базовый URL для всех запросов в Gridly

// Массив с информацией о листах и View ID для синхронизации
var SHEETS = [
  { name: 'Static Texts', viewId: 'z4nlfu2lmvzli' },
  // { name: 'Game Text', viewId: '6y172mlyr9ip1' }
];

// Получение данных из Gridly для каждого View ID
function syncAllSheets() {
  SHEETS.forEach(function(sheetInfo) {
    Logger.log("Синхронизация для листа: " + sheetInfo.name);
    var data = getGridlyData(sheetInfo.viewId);
    Logger.log("Данные для листа " + sheetInfo.name + ": " + JSON.stringify(data, null, 2));
  });
}

// Получение данных из Gridly по View ID
function getGridlyData(viewId) {
  var url = BASE_URL + '/views/' + viewId + '/records';
  var options = {
    'method': 'get',
    'headers': {
      'Authorization': 'Bearer ' + API_KEY,
      'Content-Type': 'application/json'
    },
    'muteHttpExceptions': true
  };

  try {
    var response = UrlFetchApp.fetch(url, options);
    var responseCode = response.getResponseCode();
    Logger.log('HTTP код ответа: ' + responseCode);

    if (responseCode >= 200 && responseCode < 300) {
      var jsonData = JSON.parse(response.getContentText()); // Парсим JSON-ответ
      return jsonData; // Возвращаем данные
    } else {
      var errorMessage = 'Ошибка при запросе данных из Gridly. Код ответа: ' + responseCode + '. Тело ответа: ' + response.getContentText();
      Logger.log(errorMessage);
      throw new Error(errorMessage);
    }

  } catch (error) {
    Logger.log('Исключение при запросе данных из Gridly: ' + error.message);
    throw new Error('Не удалось получить данные из Gridly. Проверьте API-ключ или View ID.');
  }
}