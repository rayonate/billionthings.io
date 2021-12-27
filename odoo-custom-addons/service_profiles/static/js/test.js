function printConsole() {
    console.log();
    let url =  window.location.origin +'/check_method_get';
    fetch(url)
        .then(res => res.json())
        .then((out) => {
            console.log('Checkout this JSON! ', out);
        })
        .catch(err => {
            console.log(err);
            throw err
        });
    console.log('cool guy');
}