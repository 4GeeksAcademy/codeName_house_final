import React, { useState } from "react";
import { Link } from "react-router-dom";
import house from "../../img/house.png";
import limpieza from "../../img/limpieza.png";
import animales from "../../img/animales.png";
import jardineria from "../../img/jardineria.png";
import niños from "../../img/niños.png";
import chef from "../../img/chef.png";

export const Acceptedcontractprofesionaldcard = ({ contract }) => {
    const [isModalOpen6, setIsModalOpen6] = useState(false);

    const toggleModal6 = () => {
        setIsModalOpen6(!isModalOpen6);
    };

    const hideModal6 = () => {
        setIsModalOpen6(false);
    };

    return (
        <div className="w-full flex flex-col p-3 justify-center mt-10 mb-3">
        <h3 className="text-center font-black text-gray-800 md:text-3xl text-xl">Contratado por: {contract.cmr_profile_id.name}</h3>
        <div className="w-full relative flex flex-col md:flex-row md:space-x-5 space-y-3 md:space-y-0 rounded-xl shadow-lg p-3 mx-auto border border-white bg-white">
            <div className="w-full md:w-1/3 bg-white grid place-items-center">
                <img src={house} className="rounded-full" />
            </div>
            <div className="w-full md:w-2/3 bg-white dark:bg-gray-700 flex flex-col space-y-2 p-3">
                <div className="text-left px-3 py-1 rounded-full text-xl  text-gray-800 dark:text-white ">
                    <b>Lugar</b>: {contract.home_id.name}
                </div>
                <div className="text-left px-3 py-1 rounded-full text-xl  text-gray-800 dark:text-white ">
                    <b>Dirección</b>: {contract.home_id.address}
                </div>
                <div className="text-left px-3 py-1 rounded-full text-xl  text-gray-800 dark:text-white ">
                    <b>Teléfono</b>: {contract.cmr_profile_id.phone_number}
                </div>
                <div className="text-left px-3 py-1 rounded-full text-xl  text-gray-800 dark:text-white ">
                    <b>Inicio</b>: {contract.starting_time}
                </div>
                <div className="text-left px-3 py-1 rounded-full text-xl  text-gray-800 dark:text-white ">
                    <b>Fin</b>: {contract.finishing_time}
                </div>
                <div className="text-left px-3 py-1 rounded-full text-xl  text-gray-800 dark:text-white ">
                    <b>Horas</b>: {contract.time_difference}
                </div>
                <div className="text-left px-3 py-1 rounded-full text-xl  text-gray-800 dark:text-white ">
                    <b>Precio final</b>: {contract.total_price} €
                </div>
                <div className="text-left px-3 py-1 rounded-full text-xl  text-gray-800 dark:text-white ">
                    <b>Detalle del contrato</b>: {contract.comment}
                </div>


                    <div className="text-right">
                        {contract.job_status == "Pendiente" ? (
                            <p className="text-white bg-red-700 hover:bg-indigo-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-blue-800"
                            >PENDIENTE DE APROBACION DEL CLIENTE</p>
                        ) : (
                            <button
                                data-modal-target="authenticationModal6"
                                data-modal-toggle="authenticationModal6"
                                type="button"
                                className="text-white bg-indigo-700 hover:bg-indigo-800 focus:ring-4 focus:outline-none focus:ring-indigo-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                                onClick={toggleModal6}
                            >
                                SERVICIO ACEPTADO
                            </button>
                        )}
                    </div>
                </div>
            </div>

            {/* Main modal 6 */}
            {isModalOpen6 && (
                <div
                    tabIndex="-1"
                    aria-hidden="true"
                    className="fixed top-0 left-0 right-0 bottom-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
                >
                    <div className="py-3 sm:max-w-xl sm:mx-auto">
                        <div className="bg-white dark:bg-gray-800 min-w-1xl flex flex-col rounded-xl shadow-lg">
                            <div className="px-12 py-5">
                                <h2 className="text-gray-800 dark:text-white text-3xl font-semibold">Deja una reseña</h2>
                            </div>
                            <div className="text-center dark:bg-gray-800 w-full flex flex-col items-center">
                                <div className="flex flex-col items-center py-6 space-y-3">
                                    <span className="text-lg text-gray-800 dark:text-white">Servicio Contratado</span>
                                    <div className="flex space-x-3">
                                        <svg className="w-12 h-12 text-yellow-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                        </svg>
                                        <svg className="w-12 h-12 text-yellow-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                        </svg>
                                        <svg className="w-12 h-12 text-yellow-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                        </svg>
                                        <svg className="w-12 h-12 text-gray-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                        </svg>
                                        <svg className="w-12 h-12 text-gray-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                        </svg>
                                    </div>
                                </div>
                                <div className="w-3/4 flex flex-col">
                                    <textarea rows="3" className="p-4 text-gray-500 dark:bg-gray-800 dark:text-white rounded-xl resize-none">
                                        Deja un mensaje
                                    </textarea>
                                    <button
                                        className="py-3 my-8 text-lg bg-indigo-700 hover:bg-indigo-800 focus:ring-4 focus:outline-none focus:ring-indigo-300 rounded-xl text-white"
                                        onClick={hideModal6}
                                    >
                                        Valora
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};
