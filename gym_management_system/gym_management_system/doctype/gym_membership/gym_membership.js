frappe.ui.form.on('Gym Membership', {
    onload: function(frm) {
        console.log("Membership Tenure:", frm.doc.membership_tenure);
        calculateAndSetPayableAmount(frm);
    },
    
    membership_tenure: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    total_payable_amount: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    body_building: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    weight_loss: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    locker: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    personal_trainer: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    suppliments: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    diet_chart: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    steam_bath: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    cardio: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    zoomba: function(frm) {
        calculateAndSetPayableAmount(frm);
    },
    crossfit: function(frm) {
        calculateAndSetPayableAmount(frm);
    }
});

function calculateAndSetPayableAmount(frm) {
    var base_tenure_charges = 0;
    var membership_tenure = frm.doc.membership_tenure;
    var additional_charges = 0;
    var total_payable_amount = 0;

    var checkbox_charges = {
        body_building: 1500,
        weight_loss: 800,
        locker: 300,
        personal_trainer: 2000,
        suppliments: 5000,
        diet_chart: 250,
        steam_bath: 150,
        cardio: 250,
        zoomba: 700,
        crossfit: 900
    };

    for (var checkbox in checkbox_charges) {
        if (frm.doc[checkbox] === 1 || frm.doc[checkbox] === true) { 
            additional_charges += checkbox_charges[checkbox];
        }
    }

  
    if (membership_tenure === 'Monthly') {
        frm.set_value('membership_plan',"30 Days")
        base_tenure_charges = 2000;
        total_payable_amount = base_tenure_charges + additional_charges;
    } else if (membership_tenure === 'Yearly') {
        base_tenure_charges = 20000;
        frm.set_value('membership_plan',"365 Days")
        total_payable_amount = base_tenure_charges+ (additional_charges * 12);
    } else if (membership_tenure === 'Quarterly') {
        base_tenure_charges = 7500;
        frm.set_value('membership_plan',"120 Days")
        total_payable_amount = base_tenure_charges + (additional_charges * 4);
    } else if (membership_tenure === 'Half Yearly') {
        frm.set_value('membership_plan',"180 Days")
        base_tenure_charges = 11000;
        total_payable_amount = base_tenure_charges + (additional_charges * 6);
    }

    
    frm.set_value('base_tenure_charges', base_tenure_charges);
    frm.set_value('additional_charges', additional_charges);
    frm.set_value('total_payable_amount', total_payable_amount);
}
