import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import "../styles/Form.css";
import UserService from '../API/userService';

function Form() {
    const [user, setUser] = useState({full_name: "", phone: "+79", isChecked: false});

    const newUser = async (e) => {
        e.preventDefault();
        const re = /^(\+7|8)\d{10}$/;

        if (!user.full_name || !user.phone) {
            alert("Пожалуйста, заполните все поля корректно");
            return;
        }    

        if (!re.test(user.phone)) {
            alert("Пожалуйста, введите корректный номер телефона в формате +7XXXXXXXXXX или 8XXXXXXXXXX");
            return;
        }
    

        if (!user.isChecked) {
            alert("Для отправки данных вы должны подтвердить согласие!");
            return;
        }

        const response = await UserService.register(user.full_name, user.phone);

        setUser({full_name: "", phone: "+79", isChecked: false});

        alert("Ваша заявка была успешно отправлена! Ожидайте обратной связи!");

        return response;
    }

    return (
        <div className='form'>
            <form onSubmit={newUser}>
                <div className="form-input">
                    <label>Ваше фамилия и имя: </label>
                    <input 
                        type="text" 
                        placeholder='Иванов Иван' 
                        required
                        value={user.full_name}
                        onChange={(e) => setUser({ ...user, full_name: e.target.value })}
                    />
                </div>

                <div className="form-input">
                    <label>Ваш номер телефона: </label>
                    <input 
                        type="tel" 
                        placeholder='+79999999999' 
                        required
                        value={user.phone}
                        onChange={(e) => setUser({...user, phone: e.target.value })}
                    />
                </div>

                <div className="form-check-box">
                    <input 
                        type="checkbox" 
                        required
                        checked={user.isChecked}
                        onChange={(e) => setUser({...user, isChecked: e.target.checked})} 
                    />
                    <label>
                        Нажимая кнопку "Отправить", я даю согласие на обработку моих персональных 
                        данных в соответствии с Федеральным законом от 27.07.2006 № 152 ФЗ "О персональных данных", 
                        на условиях и для целей, определенных в <Link to="/politika_obrabotki">политике в отношении обработки персональных данных.</Link>
                    </label>
                </div>

                <div className="form-button">
                    <button 
                        type='submit' 
                        className='btn'
                    >
                        Отправить заявку
                    </button>
                </div>
                
            </form>
        </div>
    )
}

export default Form;