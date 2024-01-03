let currentStep = 1;
let steps = document.getElementsByClassName('step');
let prevBtn = document.getElementById('prevBtn');
let nextBtn = document.getElementById('nextBtn');
let listItems = document.querySelectorAll('#side-list .list-group-item');

const showStep = (step) => {
    for (let i = 0; i < steps.length; i++) {
        steps[i].style.display = 'none';
    }
    steps[step - 1].style.display = 'block';

    for (let j = 0; j < listItems.length; j++) {
        listItems[j].classList.remove('active');
    }
    listItems[step - 1].classList.add('active');
}

const prevStep=() => {
    if (currentStep === 1) return;
    currentStep--;
    showStep(currentStep);
    updateButtons();
}

const nextStep=() => {
    if (currentStep === steps.length) return;
    currentStep++;
    showStep(currentStep);
    updateButtons();
}

const updateButtons=() => {
    if (currentStep === 1) {
        prevBtn.style.display = 'inline-block';
    } else {
        prevBtn.style.display = 'inline-block';
    }

    if (currentStep === steps.length) {
        nextBtn.style.display = 'none';
    } else {
        nextBtn.style.display = 'inline-block';
    }
}