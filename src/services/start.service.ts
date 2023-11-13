const fs = require('fs'),
  // nano = require('../couch-db/couch'),
  spawn = require('child_process').spawn

class StartService {
  getStart() {
    return new Promise((res, rej) => {

      const pyProg = spawn('C:\\Users\\vaant\\AppData\\Local\\Programs\\Python\\Python311\\python.exe', ['D:\\sum.py']);
      pyProg.stdout.on('data', function(data) {
        res(data);
      });
      pyProg.stderr.on('data', (data) => {
        console.log('stderr:', data.toString().length, 'chars');
        rej(data.toString());
      });
    })
  }

  createHost(data) {
    return new Promise((res, rej) => {
      fs.writeFile(
        'data.json',
        JSON.stringify(data),
        (err, response) => {
          if (err) return res(false)

          return res({ message: 'User created.' })
        }
      )
    })
  }

  updateHost(data) {
    return new Promise((res, rej) => {
      fs.writeFile(
        'data.json',
        JSON.stringify(data),
        (err, response) => {
          if (err) return res(false)

          return res({ message: 'User updated.' })
        }
      )
    })
  }

  deleteHost(data) {
    return new Promise((res, rej) => {
      fs.writeFile(
        'data.json',
        JSON.stringify(data),
        (err, response) => {
          if (err) return res(false)
          return res({ message: 'User deleted.' })
        }
      )
    })
  }
}

export = new StartService()