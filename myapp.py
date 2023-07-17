import streamlit as st
import locale

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

def calculate_EP(IP1, PM1, EP0):
    IP0 = 144.9
    PM0 = 41446
    
    st.markdown('<h2 style="font-size: 30px;">Vstupní data</h2>', unsafe_allow_html=True)
    
    st.write('IP0 = {:,}'.format(IP0).replace(',', ' '))
    st.write('PM0 = {:,}'.format(PM0).replace(',', ' '))
    
    if IP0 == 0 or PM0 == 0:
        return IP0, PM0, EP0
    
    EP = 0.8 * EP0 * (0.5 * (IP1 / IP0) + 0.5 * (PM1 / PM0)) + 0.2 * EP0
    return IP0, PM0, EP

def main():
    # Set the locale for formatting thousands separator
    locale.setlocale(locale.LC_ALL, '')

    if check_password():
        st.markdown('<h2 style="font-size: 30px;">Inflační doložka</h2>', unsafe_allow_html=True)

        EP0 = st.number_input('EP0', value=10_000_000, step=1_000, format="%d")
        IP1 = st.slider('IP1', min_value=100.0, max_value=160.0, step=0.1, value=144.9)
        PM1 = st.slider('PM1', min_value=39000, max_value=52000, step=1, value=41446)

        IP0, PM0, EP = calculate_EP(IP1, PM1, EP0)
        difference = EP - EP0
        percentage_change = ((EP - EP0) / EP0) * 100

        st.markdown('<h2 style="font-size: 24px;">Porovnání mezi EP a EP0:</h2>', unsafe_allow_html=True)

        st.write('EP0 = {:,}'.format(EP0).replace(',', ' '))
        st.write('EP = {:,}'.format(int(EP)).replace(',', ' '))

        if EP > EP0:
            st.markdown('<p style="font-size: 18px; color: green; font-weight: bold;">EP je větší než EP0 o {:,}</p>'.format(int(difference)).replace(',', ' '), unsafe_allow_html=True)
        elif EP < EP0:
            st.markdown('<p style="font-size: 18px; color: red; font-weight: bold;">EP je menší než EP0 o {:,}</p>'.format(int(abs(difference))).replace(',', ' '), unsafe_allow_html=True)
        else:
            st.markdown('<p style="font-size: 18px; font-weight: bold;">EP je rovno EP0</p>', unsafe_allow_html=True)

        st.write('Procentuální změna mezi EP a EP0: {:.2f}%'.format(percentage_change))

        st.markdown('<br>' * 1 + '<p style="font-size: 10px; color: grey;">Made by: <a href="https://sushidezain.000webhostapp.com/" target="_blank">https://sushidezain.000webhostapp.com/</a></p>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
