import json
# Remove these fields from profile.settings:
#
# disclaimer
# report_css
# report_excluded_sections
# report_num_sections_per_page
# report_section_max_rows
# report_template
# report_uri
# report_url_title
#
remove_list = ['disclaimer', 'report_css', 'report_excluded_sections',
    'report_num_sections_per_page', 'report_section_max_rows', 'report_template',
    'report_uri', 'report_uri_title', 'report_show_pagenumbers']

# remove_list = 'disclaimer'

profile = '/Users/juliaguimiot/practicespace/p/profile_Blade_Repair_[1.0.5].json'

def delete_sections(profile):
    f = open(profile, 'r')
    data = json.loads(f.read())
    print('data before')
    print json.dumps(data, indent=4)
    settings_keys = data['settings'].keys()
    for i in settings_keys:
        print("this is the item: {}".format(i))
        if i in remove_list:
            print("item deleted: {}".format(i))
            del(data['settings'][i])
    with open(profile, 'w') as out:
        out.write(json.dumps(data, indent=4, separators=(',', ': ')))

    print('data after')
    print json.dumps(data, indent=4)


    print("in delete sections")
    # lines_removed = []
    # data = open(profile, 'r')
    # data = open(json.loads(open_file.read()))
    # f = open(profile, 'r')
    # data = json.loads(f.read())
    # # profile_data = json.loads(data.read())
    # for line in data['settings']:
    #     print(line)
    #     # for l in data['settings'][line]:
    #     if line in remove_list:
    #         print("this is the line item {}".format(line))
    #         # lines_removed.append(line)
    #         # del(data['settings'][line])
    #         del(data)
    #
    # with open(profile, 'w') as open_file:
    #     open_file.write(json.dumps(data, indent=4, separators=(',', ': ')))

    # json_lines = []
    # with open("times.json", 'r') as open_file:
    #     for line in open_file.readlines():
    #         j = json.loads(line)
    #         if not j['Timestamp'] == '1234':
    #             json_lines.append(line)
    #
    # with open("times.json", 'w') as open_file:
    #     open_file.writelines('\n'.join(json_lines))


def main():
    delete_sections(profile)


if __name__ == '__main__':
    main()
