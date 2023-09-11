# test_name = 'Mary_Ann'
# test_obj = ["Anna", "Rita", "Mary_Ann", "John", "Rita_1", "Mary_Ann_1"]

test_name = 'reference_image'
test_obj = ['reference_image', 'item', 'reference_image_1', 'display_text']

def check_recursive(item_name, section_obj, name_count=1):
    """check the section of the checklist for the display_text.  if the display_text
    is already in that section, iterate the name_count and append to display_slug.
    recursively call the function so that all entries in the section are unique"""
    if not item_name in section_obj:
        print("didn't find the base_name in the obj. returning it {}".format(item_name))
        return item_name
    else:
        base_name = ''.join(c for c in item_name if not c.isdigit()).rstrip('_')
        print("base name: {}".format(base_name))
        item_name = '{}_{}'.format(base_name, name_count)
        print("count: {} ////// item_name: {}".format(name_count, item_name))
        name_count += 1
        check_recursive(item_name, section_obj, name_count)


#
# def set_display_slug(item_name, section_obj, name_count=1):
#     """check the section of the checklist for the display_text.  if the display_text
#     is already in that section, iterate the name_count and append to display_slug.
#     recursively call the function so that all entries in the section are unique"""
#
#     if not item_name in section_obj:
#         print("this is the name {}".format(item_name))
#         return item_name
#     else:
#         base_name = ''.join(c for c in item_name if not c.isdigit()).rstrip('_')
#         print("base_name {}".format(base_name))
#         item_name = '{}_{}'.format(base_name, name_count)
#         print("this should be the correct item_name: {}, name_count {}".format(item_name, name_count))
#         name_count += 1
#
#         set_display_slug(item_name, section_obj)

def main():
    check_recursive(test_name, test_obj)
    # set_display_slug(test_name, test_obj)

if __name__ == "__main__":
    main()
