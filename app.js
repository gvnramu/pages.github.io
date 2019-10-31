var nodemailer = require('nodemailer');
var mg = require('nodemailer-mailgun-transport');
 
// This is your API key that you retrieve from www.mailgun.com/cp (free up to 10K monthly emails)
var auth = {
  auth: {
    api_key: 'key-4938a332f5615d1c57e240986b0db40d',
    domain: 'sandboxa1338ea0d3b94288b97244cb3d59de94.mailgun.org'
  },
  // proxy: 'http://user:pass@localhost:8080' // optional proxy, default is false
}
 
var nodemailerMailgun = nodemailer.createTransport(mg(auth));
var t = "encoding muzzu"
var body = `<b>Wow Big powerful letters asdf ${t} </b>`
nodemailerMailgun.sendMail({
  from: 'bobby@sandboxa1338ea0d3b94288b97244cb3d59de94.mailgun.org',
  to: 'gvnramu@gmail.com', // An array if you have multiple recipients.
  // cc:'second@domain.com',
  // bcc:'secretagent@company.gov',
  subject: 'Hey you, awesome! test',
  'h:Reply-To': 'reply2this@company.com',
  //You can use "html:" to send HTML email content. It's magic!
  html: body,
  //You can use "text:" to send plain-text content. It's oldschool!
  text: 'Mailgun rocks, pow pow!'
}, function (err, info) {
  if (err) {
    console.log('Error: ' + err);
  }
  else {
    console.log('Response: ' + JSON.stringify( info));
  }
});

// var CronJob = require('cron').CronJob;
// new CronJob('* * * * * *', function() {
//   console.log('You will see this message every second');
// }, null, true, 'America/Los_Angeles');