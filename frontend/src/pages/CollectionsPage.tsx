import React, { useState, useEffect } from "react";
import { Table } from "antd";
import collectionService from "../services/collectionService";
import { ICollection } from "../models/ICollection";

const CollectionsPage: React.FC = () => {
  const [collections, setCollections] = useState([]);

  const getAllCollection = async () => {
    try {
      const { data } = await collectionService.getAllCollection();
      const formattedDataCollection = data.map((collection: ICollection) => {
        return {
          key: collection.id,
          id: collection.id,
          blockchain: collection.blockchain,
          network: collection.network,
          name: collection.name,
          token_symbol: collection.token_symbol,
          address: collection.address,
          image_url: collection.image_url,
        };
      });
      setCollections(formattedDataCollection);
      console.log(formattedDataCollection);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    getAllCollection();
  }, []);

  const columns = [
    {
      title: "Blockhain",
      dataIndex: "blockchain",
    },
    {
      title: "Network",
      dataIndex: "network",
    },
    {
      title: "Name",
      dataIndex: "name",
    },
    {
      title: "Token Symbol",
      dataIndex: "token_symbol",
    },
    {
      title: "Address",
      dataIndex: "address",
    },
    {
      title: "Image",
      dataIndex: "image_url",
    },
  ];

  return (
    <div>
      <Table dataSource={collections} columns={columns} />
    </div>
  );
};

export default CollectionsPage;
