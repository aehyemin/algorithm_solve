/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function(paths) {
    let start = new Set()
    let end = new Set()

    for(i=0; i<paths.length; i++) {
        start.add(paths[i][0])
        end.add(paths[i][1])
    }
  
    for (let city of end) {
        if(!start.has(city)) {
            return city
        }
    }

};