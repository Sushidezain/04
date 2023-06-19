import streamlit as st
import locale

st.markdown('<h2 style="font-size: 24px;">Inflační doložka</h3>', unsafe_allow_html=True)
def calculate_EP(IP1, PM1, EP0):
    IP0 = st.number_input('IP0', value=140.0, format="%.0f", step=1000.0)
    PM0 = st.number_input('PM0', value=42000.0, format="%.0f", step=1000.0)
    
    if IP0 == 0 or PM0 == 0:
        return EP0
    
    EP = 0.8 * EP0 * (0.5 * (IP1 / IP0) + 0.5 * (PM1 / PM0)) + 0.2 * EP0
    return EP

def main():
    # Set the locale for formatting thousands separator
    locale.setlocale(locale.LC_ALL, '')

    EP0 = st.number_input('EP0', value=10000000.0, format="%.0f", step=1000.0)
    IP1 = st.slider('IP1', min_value=120.0, max_value=150.0, step=0.1, value=120.0)
    PM1 = st.slider('PM1', min_value=39000, max_value=50000, step=1000, value=40000)

    EP = calculate_EP(IP1, PM1, EP0)
    difference = EP - EP0

    st.write('EP0: {:,}'.format(EP0).replace(',', ' '))
    st.write('EP: {:,}'.format(EP).replace(',', ' '))
    st.markdown('<h2 style="font-size: 24px;">Porovnání  mezi EP a EP0:</h2>', unsafe_allow_html=True)
    if EP > EP0:
        st.markdown('<p style="font-size: 18px; color: green; font-weight: bold;">EP je větší než EP0 o {:,}</p>'.format(int(difference)).replace(',', ' '), unsafe_allow_html=True)
    elif EP < EP0:
        st.markdown('<p style="font-size: 18px; color: red; font-weight: bold;">EP je menší než EP0 o {:,}</p>'.format(int(abs(difference))).replace(',', ' '), unsafe_allow_html=True)
    else:
        st.markdown('<p style="font-size: 18px; font-weight: bold;">EP je rovno EP0</p>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()


