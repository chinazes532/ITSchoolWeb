import axios from 'axios';

const apiUrl = import.meta.env.VITE_BASE_URL; 

export default class UserService {
    static async register(full_name, phone) {
        const params = {full_name, phone};

        try {
            const response = await axios.post(
                `http://72.56.244.152:8000/users`,
                params,
                {withCredentials: true}
            )
            console.log(response);
            
        } catch (error) {
            console.log(error);     
        }
    }
}