from LogicGame import *

def main() -> None:
    '''
    This function starts the Gui
    :return: None
    '''
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()