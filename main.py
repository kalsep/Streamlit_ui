from config import *

from PAGES import Page_1, Page_2


def main():
    st.set_page_config(
        page_title='AIRT',
        # page_icon=icon,
        layout='wide',
        initial_sidebar_state='collapsed',
    )

    # st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',
    #          unsafe_allow_html=True)  # convert radio buttons to horizontal
    # st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """,
    #             unsafe_allow_html=True)
    PAGES = {
        'Page_1': Page_1,
        'Page_2': Page_2,
    }

    options = list(PAGES.keys())
    active_tab = option_menu('Machine Learning App',
                             options, menu_icon='app-indicator', default_index=0, orientation='horizontal',
                             # icons=icons,
                             styles={
                                 'container': {'padding': '0!important', 'background-color': '#f5f5f5',
                                               'font-family': 'Permanent Marker'},
                                 'icon': {'color': 'orange', 'font-size': '25px'},
                                 # the icon next to each option 'menu-title': the <a> element containing the menu
                                 # title 'menu-icon': the icon next to the menu title 'nav': {'list-style-type':
                                 # 'none', 'margin': '0', 'padding': '0'}, # the <ul> containing 'nav-link'
                                 # 'nav-item': {'color': 'blue', 'font-size': '25px'}, #the <li> element containing
                                 # 'nav-link'
                                 'nav-link': {'font-size': '16px', 'text-align': 'left', 'margin': '0px',
                                              '--hover-color': '#eee'},
                                 # the <a> element containing the text of each option
                                 'nav-link-selected': {'background-color': '#1e90ff'},
                                 # the <a> element containing the text of the selected option
                                 # 'separator': '' # the <hr> element separating the options
                             })
    page = PAGES[active_tab]
    page.app()


if __name__ == '__main__':
    if runtime.exists():
        main()
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())
