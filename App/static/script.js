document.addEventListener("DOMContentLoaded", function () {
    const listContainer = document.getElementById("list-container");
    const buttonNames = ['Rap', 'Pop', 'Reggae', 'Rock', 'Mix Aléatoire'];

    buttonNames.forEach(function (buttonName) {
        const button = document.getElementById(buttonName + "-button");
        button.addEventListener("click", function () {
            // Récupérer la liste correspondante en fonction du bouton cliqué
            const list = getListForButton(buttonName);
            // Afficher la liste dans le conteneur
            listContainer.innerHTML = list;
        });
    });

    function getListForButton(buttonName) {
        switch (buttonName) {
            case 'Rap':
                return L1.join(', ');
            case 'Pop':
                return L2.join(', ');
            case 'Reggae':
                return L3.join(', ');
            case 'Rock':
                return L4.join(', ');
            case 'Mix Aléatoire':
                return L5.join(', ');
            default:
                return '';
        }
    }
});
