import os
import grpc
from concurrent import futures
from dataclasses import fields
import logging
from solidpy_domain.common.dataclass.person import Person, Organization
from dotenv import load_dotenv

en = load_dotenv()
logging.getLogger().setLevel(logging.INFO)
if __name__ == "__main__":
    logging.info(f"Starting GRPC server(s)...")

    external_ip = os.environ.get("GRPC_EXTERNAL_HOST_IP", "0.0.0.0")
    external_port = int(os.environ.get("GRPC_EXTERNAL_HOST_PORT", 10000))

    internal_ip = os.environ.get("GRPC_EXTERNAL_HOST_IP", "0.0.0.0")
    internal_port = int(os.environ.get("GRPC_INTERNAL_HOST_PORT", 10001))
        
    server_external = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_external.add_insecure_port(f"{external_ip}:{external_port}")
    
    server_internal = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_internal.add_insecure_port(f"{internal_ip}:{internal_port}")
    
    logging.info("Starting external server on %s:%s", external_ip, external_port)
    server_external.start()
    logging.info("External server started; Waiting for termination...")

    logging.info("Starting internal server on %s:%s", internal_ip, internal_port)
    server_internal.start()
    logging.info("Internal server started; Waiting for termination...")

    server_external.wait_for_termination()
    server_internal.wait_for_termination()

    
    
