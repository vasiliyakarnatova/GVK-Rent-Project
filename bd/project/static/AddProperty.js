document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('propertyForm');
    const additionalFieldsContainer = document.getElementById('additionalFields');

    form.addEventListener('change', function (event) {
        if (event.target.name === 'property_type') {
            updateAdditionalFields(event.target.value);
        }
    });``   

    function updateAdditionalFields(propertyType) {
        additionalFieldsContainer.innerHTML = ''; // Изчистване на допълнителните полета

        if (propertyType === 'apartment') {
            additionalFieldsContainer.innerHTML = `
            <div class="input-box">
            <span class="details">Вид:</span>
            <input type="text" placeholder="едностаен/двустаен/тристаен/многостаен" required>
            </div>

            <div class="input-box">
            <span class="details">Етаж:</span>
            <input type="text" placeholder="въведи етаж" required>
            </div>

            <div class="input-box">
            <span class="details">Година:</span>
            <input type="text" placeholder="въведи година" required>
            </div>

            <div class="input-box">
            <span class="details">Гараж:</span>
            <input type="radio" id="garage_yes" name="garage" value="yes">
            <label for="garage_yes">Да</label>
            <input type="radio" id="garage_no" name="garage" value="no">
            <label for="garage_no">Не</label>
            </div>

            <div class="input-box">
            <span class="details">Състояние:</span>
            <input type="text" placeholder="въведи състояние" required>
            </div>

            <div class="input-box">
            <span class="details">Ремонт:</span>
            <input type="text" placeholder="въведи ремонт" required>
            </div>

            <div class="input-box">
            <span class="details">Строителство:</span>
            <input type="text" placeholder="въведи строителство" required>
            </div>

            <div class="input-box">
            <span class="details">Позволени ли са домашни любимци:</span>
            <input type="radio" id="pets_allowed_yes" name="pets_allowed" value="yes">
            <label for="pets_allowed_yes">Да</label>
            <input type="radio" id="pets_allowed_no" name="pets_allowed" value="no">
            <label for="pets_allowed_no">Не</label>
            </div>
            `;
        } else if (propertyType === 'house') {
            additionalFieldsContainer.innerHTML = `
            <div class="input-box">
            <span class="details">Ремонт:</span>
            <input type="text" placeholder="въведи ремонт" required>
            </div>

            <div class="input-box">
            <span class="details">Вид:</span>
            <input type="text" placeholder="въведи вид" required>
            </div>

            <div class="input-box">
            <span class="details">Година:</span>
            <input type="text" placeholder="въведи година" required>
            </div>

            <div class="input-box">
            <span class="details">Строителство:</span>
            <input type="text" placeholder="въведи строителство" required>
            </div>

            <div class="input-box">
            <span class="details">Гараж:</span>
            <input type="radio" id="garage_yes" name="garage" value="yes">
            <label for="garage_yes">Да</label>
            <input type="radio" id="garage_no" name="garage" value="no">
            <label for="garage_no">Не</label>
            </div>

            <div class="input-box">
            <span class="details">Двор:</span>
            <input type="radio" id="yard_yes" name="yard" value="yes">
            <label for="yard_yes">Да</label>
            <input type="radio" id="yard_no" name="yard" value="no">
            <label for="yard_no">Не</label>
            </div>

            <div class="input-box">
            <span class="details">Допълнителна земя:</span>
            <input type="radio" id="additional_land_yes" name="additional_land" value="yes">
            <label for="additional_land_yes">Да</label>
            <input type="radio" id="additional_land_no" name="additional_land" value="no">
            <label for="additional_land_no">Не</label>
            </div>

            <div class="input-box">
            <span class="details">Позволени ли са домашни любимци:</span>
            <input type="radio" id="pets_allowed_yes" name="pets_allowed" value="yes">
            <label for="pets_allowed_yes">Да</label>
            <input type="radio" id="pets_allowed_no" name="pets_allowed" value="no">
            <label for="pets_allowed_no">Не</label>
            </div>

            `;
        } else if (propertyType === 'others') {
            additionalFieldsContainer.innerHTML = `
            <div class="input-box">
            <span class="details">Вид:</span>
            <input type="text" placeholder="въведи вида на имота" required>
            </div>
            <div class="input-box">
            <span class="details">Етаж:</span>
            <input type="text" placeholder="въведи етаж" required>
            </div>
            `;
        }
    }
});
