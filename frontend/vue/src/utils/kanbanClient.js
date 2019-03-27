import axios from 'axios';
import {loadProgressBar} from 'axios-progress-bar';
import camelcaseKeys from 'camelcase-keys';


const _handleSuccess = response => {
    console.log(response.data);
    response.data = camelcaseKeys(response.data, {deep: true});
    return response;
};

class Client {
    constructor() {
        this.service = axios.create();
        this.service.interceptors.response.use(_handleSuccess);
        // TODO 进度条无效
        loadProgressBar({showSpinner: false}, this.service);
    }

    _get(path, payload) {
        return this.service.get(path, payload);
    }

    _patch(path, payload) {
        return this.service.patch(path, payload);
    }

    _post(path, payload, config = {}) {
        return this.service.post(path, payload, config);
    }

    _put(path, payload) {
        return this.service.put(path, payload);
    }

    _delete(path) {
        return this.service.delete(path);
    }
}


class KanbanClient extends Client {
    // KanbanClient是与http api交互的。而有些逻辑是与websocket交互(例如操作pipeLine部分)的，所以此Client不包括所有逻辑。
    constructor() {
        super();
        this.baseUrl = '/api';
    }

    async addBoard({boardName}) {
        await this._post(`${this.baseUrl}/boards/`, {
            "name": boardName,
        });
    }

    async getBoardList() {
        const response = await this._get(`${this.baseUrl}/boards/`);
        return response.data.boardList;
    }

    async getCardData({cardId}) {
        const response = await this._get(`${this.baseUrl}/cards/${cardId}/`);
        return response.data.cardData;
    }

    async updateCardData({cardId, content, title,}) {
        const response = await this._patch(`${this.baseUrl}/cards/${cardId}/`, {
            content,
            title,
        });
        return response.data.cardData;
    }

    async deleteCard({cardId}) {
        await this._delete(`${this.baseUrl}/cards/${cardId}/`);
    }

    async getAccountInfo() {
        const response = await this._get(`${this.baseUrl}/account/`);
        return response.data.accountInfo;
    }
}


export default new KanbanClient();
