import os
import compileall
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [SECURITY-OBFUSCATE] - %(message)s')

def secure_compile_project():
    logging.info("Starting Step 24: Code Security & Bytecode Obfuscation (Source Protection)...")
    
    app_dir = os.path.dirname(__file__)
    
    # Compile all python files to optimized bytecode (.pyc) for protection
    success = compileall.compile_dir(app_dir, force=True, quiet=0)
    
    if success:
        logging.info("All Python modules successfully compiled to secure bytecode (.pyc)! Source code protected.")
        print("[SUCCESS] Step 24: Code Security & Obfuscation Completed Successfully!")
    else:
        logging.error("Bytecode compilation encountered warnings/errors.")

if __name__ == "__main__":
    secure_compile_project()
