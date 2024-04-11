import React, { useState, useEffect } from "react";
import collectionService from "../services/collectionService";
import { ICollection } from "../models/ICollection";

const CollectionsPage: React.FC = () => {
    const [collections, setCollections] = useState([])

    const getAllCollection = async () => {
        try {
            const { data } = await collectionService.getAllCollection()
            const formattedDataCollection = data.map((account: ICollection) => {
                return {
                    key: account.id,
                    id: account.id,
                    name: account.name,
                };
            });
            setCollections(formattedDataCollection);
            console.log(formattedDataCollection)
        } catch (error) {
            console.log(error);
        }
    }

    useEffect(() => {
        getAllCollection()
    }, []);

    return <div>
        CollectionListPage
    </div>;
}

export default CollectionsPage;