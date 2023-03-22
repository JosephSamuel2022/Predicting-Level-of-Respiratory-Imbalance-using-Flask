function validateForm()
{
    var numbers = /^[0-9]+$/;
    if(!document.forms["form1"]["Dehydration"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.Dehydration.focus();
        return false;        
    }
    else if(!document.forms["form1"]["Medicine_Overdose"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.Medicine_Overdose.focus();
        return false;
    }
    else if(!document.forms["form1"]["Acidious"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.Acidious.focus();
        return false;
    }
    else if(!document.forms["form1"]["Cold"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.Cold.focus();
        return false;
    }
    else if(!document.forms["form1"]["Cough"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.Cough.focus();
        return false;
    }
    else if(!document.forms["form1"]["Type"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.Type.focus();
        return false;
    }
    else if(!document.forms["form1"]["Temperature"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.Temperature.focus();
        return false;
    }
    else if(!document.forms["form1"]["Heart_Rate"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.Heart_Rate.focus();
        return false;
    }
    else if(!document.forms["form1"]["Pulse"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.Pulse.focus();
        return false;
    }
    else if(!document.forms["form1"]["BPSYS"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.BPSYS.focus();
        return false;
    }
    else if(!document.forms["form1"]["BPDIA"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.BPDIA.focus();
        return false;
    }
    else if(!document.forms["form1"]["Respiratory_Rate"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.Respiratory_Rate.focus();
        return false;
    }
    else if(!document.forms["form1"]["Oxygen_Saturation"].value.match(/^[-+]?[0-9]+\.[0-9]+$/))
    {
        alert('Please input numeric values only!');
        document.form1.Oxygen_Saturation.focus();
        return false;
    }
    else if(!document.forms["form1"]["PH"].value.match(numbers))
    {
        alert('Please input numeric values only!');
        document.form1.PH.focus();
        return false;
    }
    else
    {
        return true;
    }
}
