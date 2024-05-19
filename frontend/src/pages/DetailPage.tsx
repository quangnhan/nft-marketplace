import React, { useEffect, useState } from "react";
import {
  AiFillEnvironment,
  AiOutlineExport,
  AiFillHeart,
} from "react-icons/ai";
import "./pages.scss";

const DetailPage: React.FC = () => {
  return (
    <div className="flex justify-between flex-wrap flex-col md:flex-row mt-5">
      <div className="w-full md:w-[48%] lg:w-[49%]">
        <div className="flex justify-between h-10 w-full p-3 font-normal header-detail">
          <div className="flex items-center">
            <div className="flex items-center">
              <div className="flex mr-1">
                <AiFillEnvironment />
              </div>
            </div>
          </div>
          <div className="flex ml-auto mr-2 items-center">
            <AiOutlineExport />
          </div>
          <div className="flex items-center">
            <p className="text-xs leading-3 font-semibold text-secondary pr-2">
              <div className="flex flex-col justify-center ml-1 text-primary">
                0
              </div>
            </p>
            <div className="flex">
              <AiFillHeart />
            </div>
          </div>
        </div>
        <div
          data-radix-aspect-ratio-wrapper=""
          className="relative w-full pb-[100%]"
        >
          <div className="absolute inset-0">
            <div className="sc-beff130f-0 hksMfk absolute inset-0">
              <div className="sc-beff130f-0 ezLDzG h-full w-full">
                <div className="sc-8dd22570-0 dQCxJf item--media">
                  <div className="flex flex-col justify-center items-center relative h-full min-h-[inherit] w-full rounded-[inherit]">
                    <div className="AssetMedia--animation">
                      <div className="flex flex-col justify-center items-center AssetMedia--playback-wrapper">
                        <video
                          autoPlay
                          className="AssetMedia--video object-contain rounded-none"
                          controls
                          controlsList="nodownload"
                          loop
                          playsInline
                          poster="https://i.seadn.io/s/raw/files/aa334f2a379cf227f40970e3e476521d.gif?w=500&auto=format"
                          preload="metadata"
                          style={{
                            objectFit: "contain",
                            borderRadius: "initial",
                          }}
                        >
                          <source
                            data-testid="AssetMedia--video"
                            src="https://raw.seadn.io/files/6b3dd2bd86467c3845b78574af220fd6.mp4#t=0.001"
                            type="video/mp4"
                          />
                        </video>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="w-full md:w-[48%] lg:w-[49%]">Phần 2</div>
    </div>
  );
};

export default DetailPage;
