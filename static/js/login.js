function HideShowPassword() {
    var mot_passe = document.getElementById("password");
    if (mot_passe.type === "password") {
        mot_passe.type = "text";
    } else {
        mot_passe.type = "password";
    }
} 