import streamlit as st
import yaml
import os
from pathlib import Path

class SimpleAuth:
    """Simple authentication system for Streamlit app"""
    
    def __init__(self, credentials_file="credentials.yaml"):
        self.credentials_file = credentials_file
        self._ensure_credentials_file()
    
    def _ensure_credentials_file(self):
        """Create default credentials file if it doesn't exist"""
        if not os.path.exists(self.credentials_file):
            default_credentials = {
                'usernames': {
                    'doctor': {
                        'password': 'doctor123',
                        'name': 'Dr. Heart',
                        'role': 'Doctor'
                    },
                    'patient': {
                        'password': 'patient123',
                        'name': 'John Patient',
                        'role': 'Patient'
                    },
                    'admin': {
                        'password': 'admin123',
                        'name': 'Admin User',
                        'role': 'Administrator'
                    }
                }
            }
            
            with open(self.credentials_file, 'w') as f:
                yaml.dump(default_credentials, f)
    
    def load_credentials(self):
        """Load credentials from YAML file"""
        try:
            with open(self.credentials_file, 'r') as f:
                credentials = yaml.safe_load(f)
            return credentials
        except Exception as e:
            st.error(f"Error loading credentials: {e}")
            return None
    
    def authenticate(self, username, password):
        """Authenticate user credentials"""
        credentials = self.load_credentials()
        
        if credentials and 'usernames' in credentials:
            if username in credentials['usernames']:
                user = credentials['usernames'][username]
                if user.get('password') == password:
                    return True, user
        
        return False, None
    
    def login_widget(self):
        """Display login widget"""
        st.set_page_config(page_title="Heart Disease Prediction - Login", layout="wide")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("<h1 style='text-align: center; color: #E74C3C;'>❤️ Heart Disease Prediction</h1>", 
                       unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center;'>Login to Continue</h3>", 
                       unsafe_allow_html=True)
            
            st.markdown("---")
            
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")
            
            col_a, col_b = st.columns(2)
            with col_a:
                login_button = st.button("🔓 Login", use_container_width=True)
            
            with col_b:
                demo_button = st.button("👁️ Demo Mode", use_container_width=True)
            
            st.markdown("---")
            
            with st.expander("📋 Demo Credentials"):
                st.info("""
                **Doctor Account:**
                - Username: `doctor`
                - Password: `doctor123`
                
                **Patient Account:**
                - Username: `patient`
                - Password: `patient123`
                
                **Admin Account:**
                - Username: `admin`
                - Password: `admin123`
                """)
            
            return login_button, demo_button, username, password
    
    def is_logged_in(self):
        """Check if user is logged in"""
        return 'user_logged_in' in st.session_state and st.session_state.user_logged_in
    
    def logout(self):
        """Logout user"""
        st.session_state.user_logged_in = False
        st.session_state.current_user = None
        st.session_state.user_role = None
        st.rerun()

# Global auth instance
auth = SimpleAuth()
