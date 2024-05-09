import httpService from "./httpService";

const API_ENDPOINT = `${process.env.REACT_APP_SERVER_URL}/smartcontracts`;

function getAllCollection(top: number = 10) {
    return httpService.get(
        `${API_ENDPOINT}/`
    );
}

const collectionService = {
    getAllCollection,
};

export default collectionService;
