import binascii
import os
import random

# Utils to generate random hex values
def generate_random_hexdecimal(length, is_lower_case):
    random_value = binascii.hexlify(os.urandom(int(length/2)))
    str_value = random_value.decode('utf-8')
    return str_value if is_lower_case else str_value.upper()


# Utils to generate random number values
def generate_random_number(length):
    start = '1' + ''.join('0' for i in range(length-1))
    end = '9' + ''.join('9' for i in range(length-1))
    return '{}'.format(random.randint(int(start), int(end)))


# Utils to generate random names in lowercase
def generate_random_user():
    names = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7']
    return random.choice(names)


def doc_id(length=0):
    r1 = generate_random_hexdecimal(12, False)
    r2 = generate_random_number(10)
    r3 = generate_random_number(5)
    return '{}-{}-{}'.format(r1, r2, r3)


def agent(length=0):
    r1 = generate_random_hexdecimal(8, False)
    return '{}.acme.net'.format(r1)


def assetid(length=0):
    letters = ['A', 'B', 'C', 'X', 'Y', 'Z']
    r1 = ''.join(random.choice(letters) for i in range(2))
    r2 = generate_random_number(9)
    return '{}{}'.format(r1, r2)


def cartid(length=0):
    letters = ['A', 'B', 'C', 'X', 'Y', 'Z']
    r1 = random.choice(letters)
    r2 = generate_random_number(8)
    return '{}-{}'.format(r1, r2)


def generate_random_string(length):
    letters = ['A', 'B', 'C', 'X', 'Y', 'Z', 'f', 'g', 'h', 'i', 'j', 'k', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return ''.join(random.choice(letters) for i in range(length))


def mac_no_colon(length=0):
    return generate_random_hexdecimal(length, True)


def generate_mac_addrress(sep="", is_lower_case=True):
    r1 = ''.join('{}{}'.format(generate_random_hexdecimal(2, is_lower_case), sep) for i in range(5))
    return '{}{}'.format(r1, generate_random_hexdecimal(2, is_lower_case))


def mac_address_dash(length=0):
    return generate_mac_addrress('-')


def mac_address_colon(length=0):
    return generate_mac_addrress(':')


def mac_address_colon_uppercase(length=0):
    return generate_mac_addrress(':', False)


def mac_cisco_asa(length=0):
    # MAC 0012.123a.89c1
    r1 = generate_random_hexdecimal(4, True)
    r2 = generate_random_hexdecimal(4, True)
    r3 = generate_random_hexdecimal(4, True)

    return 'MAC {}.{}.{}'.format(r1, r2, r3)


def hex(length=0, is_lower_case=True):
    return generate_random_hexdecimal(length, is_lower_case)


def hex_upper(length=0):
    return generate_random_hexdecimal(length, False)


def pos_neg_number(length=0):
    signal = random.choice(['-', ''])
    number = generate_random_number(length)
    return '{}{}'.format(signal, number)


def crazy_name(length=0):
    r1 = random.randint(1,15)
    r2 = random.randint(15,30)
    r3 = random.randint(1,30)
    return  'S-{}-{}-{}'.format(r1, r2, r3)


def windows_security_id(length=0):
    #S-1-2-12-823511234-1958361234-682001234-1234
    r1= generate_random_number(9)
    r2= generate_random_number(10)
    r3= generate_random_number(9)
    r4= generate_random_number(4)

    return 'S-1-2-3-{}-{}-{}-{}'.format(r1, r2, r3, r4)


def machine_name(length=0):
    letters = ['A', 'B', 'C', 'X', 'Y', 'Z']
    r1 = ''.join(random.choice(letters) for i in range(4))
    r2 = random.randint(100000,999999)
    r3 = ''.join(random.choice(letters) for i in range(3))
    return '{}{}-{}'.format(r1, r2, r3)


def machine_sep(length=0, is_lower_case=False):
    return generate_random_hexdecimal(length, is_lower_case)


def device_name(length=0):
    # J0093305W28774D
    return machine_sep(15, False)


def ipv4(length=0):
    r1 = random.randint(1,255)
    return '10.20.30.{}'.format(r1)


def ipv4_between_spaces(length=0):
    r1 = ipv4(length)
    return ' {} '.format(r1)


def ipv6(length=0):
    #1234:12:1234:abc:123a:12ab:ce7e:f585
    r1 = hex(4)
    r2 = hex(4)
    return '1234:12:1234:abc:123a:12ab:{}:{}'.format(r1, r2)


def guid(length=0, is_lower=False, is_separated=True):
    r1 = generate_random_hexdecimal(8, is_lower)
    r2 = generate_random_hexdecimal(4, is_lower)
    r3 = generate_random_hexdecimal(4, is_lower)
    r4 = generate_random_hexdecimal(4, is_lower)
    r5 = generate_random_hexdecimal(12, is_lower)
    if is_separated:
        return '{}-{}-{}-{}-{}'.format(r1, r2, r3, r4, r5)
    else:
        return '{}{}{}{}{}'.format(r1, r2, r3, r4, r5)

def guid_upper_without_separator(length=0):
    return guid(length, False, False)


def lower_guid(length=0, is_lower=False):
    return guid(length, True)


def ref_uid(length=0, is_lower=False):
    # 8040:abc28ed0-1234-12eb-abcd-000003c20c9f
    r1 = generate_random_number(4)
    r2 = lower_guid()

    return '{}:{}'.format(r1, r2)


def shost(length=0):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4']
    r1 = ''.join(random.choice(letters) for i in range(4))
    return 'www.{}.acme.com'.format(r1)


def collector_host(length=0):
    # hostname.cc.ad.cchs.net
    name = ['acme1', 'acme2', 'acme3', 'acme4']
    r1 = random.choice(name)
    r2 = generate_random_string(2)
    r3 = generate_random_string(2)
    r4 = generate_random_string(4)
    return '{}.{}.{}.{}.net'.format(r1, r2, r3, r4)


def external_id(length=0):
    r1 = random.randint(100000,999999)
    return str(r1)


def fqdn(length=0):
    #abcd07-v123321.abc.xy.acme.com
    r1 = generate_random_string(6)
    r2 = generate_random_string(6)
    r3 = generate_random_string(3)
    r4 = generate_random_string(2)
    domains = ['acme1', 'acme2', 'acme3', 'acme4']
    r5 = domains[random.randint(0, len(domains) - 1)]
    return '{}-v{}.{}.{}.{}.com'.format(r1, r2, r3, r4, r5)


def dt_machine_name(length=0):
    r1 = random.randint(1000,9999)
    r2 = random.randint(10,99)
    return 'dtools-dt-{}-{}'.format(r1, r2)


def syslog_id_host(length=0):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5']
    r1 = random.randint(1000,999999)
    r2 = ''.join(random.choice(letters) for i in range(11))
    r3 = ''.join(random.choice(letters) for i in range(4))
    r4 = ''.join(random.choice(letters) for i in range(4))
    return '{}: {}_{}_{}:'.format(r1, r2, r3, r4)


def host_numbers_letters(length=0):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '7', '8']
    r1 = ''.join(random.choice(letters) for i in range(4))
    r2 = ''.join(random.choice(letters) for i in range(4))
    r3 = ''.join(random.choice(letters) for i in range(4))
    return 'Host {}.{}.{} '.format(r1, r2, r3)


def domain_plus_user(length=0):
    domains = ['acme1', 'acme2', 'acme3', 'acme4']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    r1 = domains[random.randint(0, len(domains) - 1)]
    r2 = ''.join(random.choice(letters) for i in range(8))
    return '{}\\\\\\\\\\\\\\\\{}'.format(r1, r2)


def user_name_dot_surname(length=0):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    r1 = ''.join(random.choice(letters) for i in range(8))
    r2 = ''.join(random.choice(letters) for i in range(8))
    return '{}.{}'.format(r1, r2)


def user_name_surname(length=0):
    firstname = ['tony', 'viuva', 'jonh', 'bruce', 'clark', 'saga']
    secondname = ['stark', 'spider', 'doe', 'wayne', 'kent']
    r1 = random.choice(firstname)
    r2 = random.choice(secondname)
    return '{}{}'.format(r1, r2)


def surname_comma_name(length=0, complement=False, is_complement_brackets=False):
    firstname = ['tony', 'viuva', 'jonh', 'bruce', 'clark', 'saga']
    secondname = ['stark', 'spider', 'doe', 'wayne', 'kent']
    r1 = random.choice(firstname)
    r2 = random.choice(secondname)

    if complement:
        r3 = generate_random_string(7)
        if is_complement_brackets:
            return '{}, {}   [{}]'.format(r2, r1, r3)
        else:
            return '{}, {}   ({})'.format(r2, r1, r3)
    else:
        return '{}, {}'.format(r2, r1)


def name_surname(length=0, try_complement=True):
    firstname = ['tony', 'viuva', 'jonh', 'bruce', 'clark', 'saga']
    secondname = ['stark', 'spider', 'doe', 'wayne', 'kent']
    r1 = random.choice(firstname)
    r2 = random.choice(secondname)
    complement = random.randint(0, 10) % 2
    if try_complement and complement:
        r3 = generate_random_string(7)
        return '{} {}   ({})'.format(r1, r2, r3)
    else:
        return '{} {}'.format(r1, r2)


def host_plus_domain(length=0):
    domains = ['ACME1', 'ACME2', 'ACME3', 'ACME4']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    letters_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '1', '2', '3', '4', '5', '6']
    r1 = ''.join(random.choice(letters) for i in range(4))
    r2 = ''.join(random.choice(letters_up) for i in range(5))
    r3 = ''.join(random.choice(letters_up) for i in range(3))
    r4 = domains[random.randint(0, len(domains) - 1)]
    return '{}/{}-{}.{}.COM'.format(r1, r2, r3, r4)


def domain_email_user(length=0):
    domains = ['acme1', 'acme2', 'acme3', 'acme4']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    r1 = domains[random.randint(0, len(domains) - 1)]
    r2 = ''.join(random.choice(letters) for i in range(8))
    r3 = ''.join(random.choice(letters) for i in range(5))
    r4 = ''.join(random.choice(letters) for i in range(3))
    return '{}@{}.{}.{}'.format(r1, r2, r3, r4)


def hashed_email(length=0):
    domains = ['acme1', 'acme2', 'acme3', 'acme4']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']

    r1 = hex(32)
    r2 = domains[random.randint(0, len(domains) - 1)]
    r3 = ''.join(random.choice(letters) for i in range(8))
    r4 = ''.join(random.choice(letters) for i in range(5))
    return '{}@{}.{}.{}'.format(r1, r2, r3, r4)


def email_user(length=0):
    firstname = ['tony', 'viuva', 'jonh', 'bruce', 'clark', 'saga']
    secondname = ['stark', 'spider', 'doe', 'wayne', 'kent']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    r1 = random.choice(firstname)
    r2 = random.choice(secondname)
    r3 = ''.join(random.choice(letters) for i in range(5))
    r4 = ''.join(random.choice(letters) for i in range(3))
    return '{}.{}@{}.{}.com'.format(r1, r2, r3, r4)


def email_simple(length=0):
    domains = ['acme1.com', 'acme2.com', 'acme3.com', 'acme4.com']
    domain = domains[random.randint(0, len(domains) - 1)]
    user = generate_random_user()
    return '{}@{}'.format(user, domain)


def email_entry(length=0):
    cia_names = ['', 'acme1', 'acme2', 'acme3',
                 'acme4', 'acme5', 'acme6', 'acme7']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    r1 = random.choice(cia_names)
    r2 = ''.join(random.choice(letters) for i in range(5))
    r3 = ''.join(random.choice(letters) for i in range(3))
    return '{}@{}.{}.com'.format(r1, r2, r3)


def phone(length=0):
    r1 = generate_random_number(3)
    r2 = generate_random_number(3)
    r3 = generate_random_number(4)
    return '({}) {}-{}'.format(r1, r2, r3)


def ad_domain(length=0):
    letters = ['acme1', 'acme2', 'acme3',
               'acme4', 'acme5', 'acme6', 'acme7']
    domains = ['prd', 'hom', 'test', 'local']
    r1 = letters[random.randint(0, len(letters) - 1)]
    r2 = domains[random.randint(0, len(domains) - 1)]
    return '{}.{}.com'.format(r1, r2)


def host(length=0):
    name = ['acme1', 'acme2', 'acme3',
               'acme4', 'acme5', 'acme6', 'acme7']
    domains = ['prd', 'hom', 'test', 'local']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    r1 = name[random.randint(0, len(name) - 1)]
    r2 = domains[random.randint(0, len(domains) - 1)]
    r3 = letters[random.randint(0, len(letters) - 1)]
    return '{}-{}.{}.com'.format(r1, r2, r3)


def link(length=0):
    name = ['acme1', 'acme2', 'acme3',
               'acme4', 'acme5', 'acme6', 'acme7']
    domains = ['prd', 'hom', 'test', 'local']
    path = ['agent', 'local', 'level', 'test']

    r1 = name[random.randint(0, len(name) - 1)]
    r2 = domains[random.randint(0, len(domains) - 1)]
    r3 = path[random.randint(0, len(path) - 1)]
    return 'http://{}.{}.com/{}'.format(r1, r2, r3)


def link_or_mailto(length=0):
    is_link = random.randint(0, 10) % 2
    if is_link:
        return link(length)
    else:
        e = email_user()
        return 'mailto:{}'.format(e)


def url(length=0):
    is_link_file = random.randint(0, 10) % 2
    if is_link_file:
        l = link()
        return '{}/file.ext'.format(l)
    else:
        e = email_user()
        return 'mailto:{}'.format(e)


def ad_log_id(length=0):
    r1 = random.randint(1000000000,9999999999)
    r2 = random.randint(1000000000,9999999999)
    return '{}/{}'.format(r1, r2)


def id_number(length=0):
    return generate_random_number(length)


def random_company_name(length=0):
    names = ['Acme1', 'Acme2', 'Acme3', 'Acme4', 'Acme5', 'Acme6']
    r1 = names[random.randint(0, len(names) - 1)]
    return '{}'.format(r1)


def sid(length=0):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    r1 = ''.join(random.choice(letters) for i in range(7))
    r2 = random.choice(letters)

    return 'sid_{}_{}'.format(r1, r2)


def simple_domain(length=0):
    domains = ['ACME', 'CORP', 'COMP', 'STARK', 'DOMA']
    r1 = random.choice(domains)

    return r1


def mysql_user(length=0):
    user = generate_random_user()
    return 'user: \'{}\''.format(user)


def big_id(length=0):
    return generate_random_string(length)


def windows_path(length=0):
    # "C:\\\\Users\\\\cra3\\\\AppData\\\\Local\\\\Microsoft\\\\SquirrelTemp
    root = ['Users', 'ProgramData']
    user_or_program = generate_random_string(8)
    folder = generate_random_string(8)
    leaf = ['TEST', 'UAT', 'DummyFiles']

    r1 = root[random.randint(0, len(root) - 1)]
    r2 = leaf[random.randint(0, len(leaf) - 1)]

    return 'C:\\\\\\\\{}\\\\\\\\{}\\\\\\\\{}\\\\\\\\{}'.format(r1, user_or_program, folder, r2)


def windows_acc_name(length=0):
    #CB669
    r1 = generate_random_string(2)
    r2 = generate_random_number(3)

    return '{}{}'.format(r1, r2)


def windows_user_principal_name(length=0):
    #cb699@acme.com
    acc_name = windows_acc_name(length)
    domains = ['acme', 'corp', 'comp', 'stark', 'doma']
    r1 = random.choice(domains)

    return '{}@{}.com'.format(acc_name, r1)


def json_array_email_proofpoint(length=0):
    # num = random.randint(0, 12)
    num = 5

    if num < 3: #[\"Felipe Castro <FCastro@test.org>,        Cacilda Clark\\t<CClark@test.org>\"]
        name1 = name_surname(length, False)
        email1 = email_user()
        name2 = name_surname(length, False)
        email2 = email_user()
        return '[\\"{} <{}>,        {}\\\\t<{}>\\"]'.format(name1, email1, name2, email2)
    elif num >= 3 and num < 7: #[\"FCrazy@test.org\",\"CAtos@test.org\",\"RTest@test.org\"]
        email1 = email_user()
        email2 = email_user()
        email3 = email_user()
        return '[\\"{}\\",\\"{}\\",\\"{}\\"]'.format(email1, email2, email3)
    elif num >=7 and num <10: # [\"\\\"Stark, Tony [BLAH]\\\" <Tony.Stark@blah.test.gov>, \\\"Kent, Clark [BLAH]\\\" <Clark.Kent@blah.test.gov>\"]
        name1 = surname_comma_name(length, True, True)
        email1 = email_user()
        name2 = surname_comma_name(length, True, True)
        email2 = email_user()
        return '[\\"\\\\\\\"{}\\\\\\\" <{}>,        \\\\\\\"{}\\\\\\\" <{}>\\"]'.format(name1, email1, name2, email2)
    else: # [\"\\\"Aloyo, Anna M.   (CHRMAMA)\\\" <AAloyo@njtransit.com>,        \\\"Phelps, Adam K.   (COCRAKP)\\\" <APhelps@njtransit.com>\"]
        name1 = surname_comma_name(length, True, False)
        email1 = email_user()
        name2 = surname_comma_name(length, True, False)
        email2 = email_user()
        return '[\\"\\\\\\\"{}\\\\\\\" <{}>,        \\\\\\\"{}\\\\\\\" <{}>\\"]'.format(name1, email1, name2, email2)


def json_array_hashed_emails(length=0):
    email1 = hashed_email()
    email2 = hashed_email()
    email3 = hashed_email()
    return '[\\"{}\\",\\"{}\\",\\"{}\\"]'.format(email1, email2, email3)


def content_type_id(length=0):
    hex = generate_random_hexdecimal(38, False)
    return '0x{}'.format(hex)


def data_base_64(length=0):
    hex = generate_random_hexdecimal(30, False)
    return '\\"{}==\\\\n\\"'.format(hex)


def delivery_id(length=0):
    del_id = generate_random_number(8)
    return '{}del'.format(del_id)


def name_surname_upper(length=0):
    director = name_surname(length, False)
    return director.upper()


def document_user_name(length=0):
    return name_surname(length, False)


def json_array_surname_name(length=0):
    try_compl = random.randint(0, 10) % 2
    name = name_surname(length, try_compl)
    return '[\\"{}\\"]'.format(name)


def json_array_hashed_email(length=0):
    email = hashed_email()
    return '[\\"{}\\"]'.format(email)


def json_array_single_email(length=0):
    email = email_user()
    return '[\\"{}\\"]'.format(email)


def json_array_single_domain_email(length=0):
    email = domain_email_user()
    return '[\\"{}\\"]'.format(email)


def guid_no_dash(length=0):
    return guid(length, True, False)


def azure_family(length=0):
    # dd8541c-de6d-40c7-40b1-08d8e032e6ef-15217734666834694554-1
    g = guid(length, True)
    r1 = generate_random_number(20)

    return '{}-{}-1'.format(g, r1)


def links(length=0):
    link1 = link_or_mailto(length)
    link2 = link_or_mailto(length)
    return '{}, {}'.format(link1, link2)


def md5(length=0):
    return hex(32)


def md5_upper(length=0):
    return hex(32, False)


def sha1(length=0):
    return hex(40)


def sha256(length=0):
    return hex(64)


def sha256_upper(length=0):
    return hex(64, False)


def net_bios_name(length=0):
    #abcd-l123321
    r1 = generate_random_string(4)
    r2 = generate_random_string(7)

    return '{}-{}'.format(r1, r2)


def message_id_array(length=0):
    msg_id_type = random.randint(0, 10) % 2
    message_id = ''
    if msg_id_type:
        message_id = hashed_email()
    else:
        message_id = '<{}>'.format(hashed_email())

    return '[\\"{}\\"]'.format(message_id)


def message_id(length=0):
    return '<{}>'.format(hashed_email())


def double_phone_number(length=0):
    phone1 = phone(length)
    phone2 = phone(length)
    return '{} TDD {}'.format(phone1, phone2)


def query_domain(length=0):
    return '_{}'.format(ad_domain(length))


def host_and_ip(length=0):
    h = host(length)
    i = ipv4(length)
    return '{}. [{}]'.format(h, i)


def json_array_diff_repr_email_proofpoint(length=0):
    num = random.randint(0, 12)

    if num < 3: #[\"Felipe Castro <FCastro@test.org>\"]
        name1 = name_surname(length, False)
        email1 = email_user()
        return '[\\"{} <{}>\\"]'.format(name1, email1)
    elif num >= 3 and num < 7: #[\"FCrazy@test.org\"]
        email1 = email_user()
        return '[\\"{}\\"]'.format(email1)
    elif num >=7 and num <10: # [\"\\\"Stark, Tony\\\" <Tony.Stark@blah.test.gov>\"]
        name1 = name_surname(length, False)
        email1 = email_user()
        return '[\\"\\\\\\\"{}\\\\\\\" <{}>\\"]'.format(name1, email1)
    else: # [\"<test-email@inbound.mailchimpapp.net>\"]
        email1 = domain_email_user()
        return '[\\"<{}>\\"]'.format(email1)


def email_between_angle_brackets(length=0):
    email1 = domain_email_user()
    return '<{}>'.format(email1)


def sent_email_stat(length=0):
    r1 = guid(length)
    r2 = generate_random_number(14)
    r3 = host(length)
    r4 = generate_random_number(5)

    sent_fmt = 'Sent (<{}@test.com> [InternalId={}, Hostname={}] {} ' \
               'bytes in 1.366, 19.772 KB/sec Queued mail for delivery)'

    return sent_fmt.format(r1, r2, r3, r4)


def user_config_id(length=0):
    r1 = generate_random_number(8)
    return 'UC{}'.format(r1)


def user_perm_id(length=0):
    r1 = generate_random_number(8)
    return 'urn:user:PA{}'.format(r1)


def user_cisco_asa(length=0):
    r1 = generate_random_user()

    return 'User \'{}\''.format(r1)


def username_cisco_asa(length=0):
    # Username = acme001
    r1 = generate_random_user()

    return 'Username = {}'.format(r1)


def user_angle_brackets_cisco_asa(length=0):
    # User <pgime012>
    name = ['stark', 'spider', 'doe', 'wayne', 'kent']
    r1 = random.choice(name)
    r2 = generate_random_string(2)

    return 'User <{}{}>'.format(r1, r2)


def single_ip_inside_string_array(length=0):
    is_ipv4 = random.randint(0, 10) % 2
    ip = ipv4() if is_ipv4 else ipv6()

    return '[\\"[{}]\\"]'.format(ip)


def src_host(length=0):
    pre = ['ABC', 'XYZ', 'Test', 'Prd']
    middle = ['Stark', 'Spider', 'Doe', 'Wayne', 'Kent']
    last = ['Acme1', 'Acme2', 'Acme3', 'Acme4', 'Acme5', 'Acme6']
    r1 = pre[random.randint(0, len(pre) - 1)]
    r2 = middle[random.randint(0, len(middle) - 1)]
    r3 = last[random.randint(0, len(last) - 1)]

    return '{}-{}-{}'.format(r1, r2, r3)


def json_windows_path(length=0):
    path = windows_path(length)
    return '\\"{}\\"'.format(path)


def json_email_entry(length=0):
    email = email_entry(length)
    return '\\"{}\\"'.format(email)


def json_array_guid(length=0):
    guid_1 = guid(length, True)
    guid_2 = guid(length, True)

    return '[\\"{}\\", \\"{}\\"]'.format(guid_1, guid_2)


def symantec_authorization(length=0):
    # \\\"Authorization\\\":\\\"token 00abcde0132547f7a9603a4d9f912345\\\"
    r1 = generate_random_hexdecimal(32, True)
    return '\\\\\\"Authorization\\\\\\":\\\\\\"token {}\\\\\\"'.format(r1)


def symantec_client_id(length=0):
    # \\\"client_id\\\":\\\"__FGL__1213131313131\\\"
    r1 = generate_random_hexdecimal(180, True)
    return '\\\\\\"client_id\\\\\\":\\\\\\"__FGL__{}\\\\\\"'.format(r1)


def symantec_mstr_auth_token(length=0):
    # \\\"X-MSTR-AuthToken\\\":\\\"123402ho2n9g1umkek6dlkabcd\\\"
    r1 = generate_random_hexdecimal(27, True)
    return '\\\\\\"X-MSTR-AuthToken\\\\\\":\\\\\\"{}\\\\\\"'.format(r1)


def symantec_mstr_projectid(length=0):
    # \\\"X-MSTR-ProjectID\\\":\\\"ABCDC24711E9AD2AFCF60080EF951234\\\"
    r1 = generate_random_hexdecimal(32, False)
    return '\\\\\\"X-MSTR-ProjectID\\\\\\":\\\\\\"{}\\\\\\"'.format(r1)


def json_array_email_workspace(length=0):
    r1 = email_user()
    r2 = email_user()
    r3 = email_user()
    r4 = email_user()
    return '[\\"{}\\",\\"{}\\",\\"{}\\",\\"{}\\"]'.format(r1, r2, r3, r4)


def etag(length=0):
    # \"etag\":\"\\\"123ABCDjmaexiWf6erlw41vzbKis3GAHwFKPo-K4ddk/sOv_TuW6giLMJP6jpcqqiGS99Lw\\\"\"
    r1 = generate_random_string(71)
    return '\\\"etag\\\":\\\"\\\\\\\"{}\\\\\\\"\\\"'.format(r1)


def pan_fw_user(length=0):
    #acme\\felipecastro
    r1 = user_name_surname(length)
    return 'acme\\\\{}'.format(r1)


def pan_fw_devicename(length=0):
    #ACME101MD01FW03
    r1 = generate_random_number(3)
    r2 = generate_random_string(2).upper()

    return 'ACME{}{}01FW01'.format(r1, r2)


def airwatch_domain_user(length=0):
    domains = ['acme1', 'acme2', 'acme3', 'acme4']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    r1 = domains[random.randint(0, len(domains) - 1)]
    r2 = ''.join(random.choice(letters) for i in range(7))
    return '{}\{}'.format(r1, r2)


def airwatch_asset_number(length=0):
    r1 = generate_random_number(8)
    r2 = hex_upper(16)
    return '{}-{}'.format(r1, r2)


def airwatch_device(length=0):
    r1 = generate_random_string(7)
    r2 = generate_random_string(7)
    return '{}.{}'.format(r1, r2)


def airwatch_friendly_name(length=0):
    r1 = hex_upper(6)
    r2 = generate_random_string(6)
    return '{}.{}'.format(r1, r2)


def random_string_between_escaped_quote(length=0):
    r1 = generate_random_string(length)
    return '\\"{}\\"'.format(r1)


def ip_between_escaped_quote(length=0):
    r1 = ipv4()
    return '\\"{}\\"'.format(r1)


def bro_json_hostname(length=0):
    # abcd50778-A1
    r1 = generate_random_string(9)
    r2 = generate_random_string(2)
    return '{}-{}'.format(r1, r2)
