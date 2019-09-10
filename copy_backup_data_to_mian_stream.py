if __name__ == "__main__":
    try:
        remove_duplicate().connect_to_database()
        remove_duplicate().find_duplicate()

        remove_duplicate().extra_data()
        remove_duplicate().backup_data()
        remove_duplicate().remove_data()

    except Exception as e:
        print("Exception captured: " + e)