import React from 'react'
import { Link } from 'react-router-dom';
import "../styles/Form.css";

function Form() {
  return (
    <div className='form'>
       <form action="/consultaion" method='POST'>
            <div className="form-input">
                <label >Ваше имя: </label>
                <input type="text" placeholder='Иван' required/>
            </div>

            <div className="form-input">
                <label >Ваша фамилия: </label>
                <input type="text" placeholder='Иванов' required/>
            </div>

            <div className="form-input">
                <label >Ваш номер телефона: </label>
                <input type="tel" placeholder='+79999999999' required/>
            </div>

            <div className="form-check-box">
                <input type="checkbox" required/>
                <label>
                    Нажимая кнопку "Отправить", я даю согласие на обработку моих персональных 
                    данных в соответствии с Федеральным законом от 27.07.2006 № 152 ФЗ "О персональных данных", 
                    на условиях и для целей, определенных в <Link to="/politika_obrabotki">политике в отношении обработки персональных данных .</Link>
                </label>
            </div>

            <div className="form-button">
                <button type='submit' className='btn'>Отправить заявку</button>
            </div>
            
       </form>
    </div>
  )
}

export default Form;
