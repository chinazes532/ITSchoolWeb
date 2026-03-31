import axios from 'axios';

const apiUrl = proccess.env.BASE_URL;

export default class UserService {
    static async register(full_name, phone) {
        const params = {full_name, phone};

        try {
            const response = await axios.post(
                `${apiUrl}/users`,
                params,
                {withCredentials: true}
            )
            console.log(response);
            
        } catch (error) {
            console.log(error);     
        }
    }
}