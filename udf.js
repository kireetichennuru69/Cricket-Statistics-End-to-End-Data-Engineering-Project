function transform(line) {
    var values = line.split(",");
    var obj = new Object();
    obj.id = values[0];
    obj.rank = values[1];
    obj.name = values[2];
    obj.country = values[3];
    obj.career_span = values[4];
    obj.innings = values[5];
    obj.matches = values[6];
    obj.runs = values[7];
    obj.avg = values[8];
    obj.sr = values[9];
    obj.highestScore = values[10];
    obj.hundreds = values[11];
    obj.fifties = values[12];
    var jsonString = JSON.stringify(obj);
    return jsonString;
}