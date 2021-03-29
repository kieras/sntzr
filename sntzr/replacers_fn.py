import binascii
import os
import random

# Utils to generate random hex values
def generate_random_hexdecimal(length, is_lower_case):
    random_value = binascii.hexlify(os.urandom(int(length/2)))
    str_value = random_value.decode('utf-8')
    return str_value if is_lower_case else str_value.lower()


# Utils to generate random number values
def generate_random_number(length):
    start = '1' + ''.join('0' for i in range(length-1))
    end = '9' + ''.join('9' for i in range(length-1))
    return '{}'.format(random.randint(int(start), int(end)))


# Utils to generate random names in lowercase
def generate_random_user():
    names = ['jonhdoe', 'stark', 'marry', 'max', 'jonh', 'wayne', 'creed']
    return random.choice(names)


def mac_no_colon(length=0):
    return generate_random_hexdecimal(length, True)


def generate_mac_addrress(sep=""):
    r1 = ''.join('{}{}'.format(generate_random_hexdecimal(2, True), sep) for i in range(5))
    return '{}{}'.format(r1, generate_random_hexdecimal(2, True))


def mac_address_dash(length=0):
    return generate_mac_addrress('-')


def mac_address_colon(length=0):
    return generate_mac_addrress(':')


def hex(length=0):
    return generate_random_hexdecimal(length, True)


def crazy_name(length=0):
    r1 = random.randint(1,15)
    r2 = random.randint(15,30)
    r3 = random.randint(1,30)
    return  'S-{}-{}-{}'.format(r1, r2, r3)


def machine_name(length=0):
    letters = ['A', 'B', 'C', 'X', 'Y', 'Z']
    r1 = ''.join(random.choice(letters) for i in range(4))
    r2 = random.randint(100000,999999)
    r3 = ''.join(random.choice(letters) for i in range(3))
    return '{}{}-{}'.format(r1, r2, r3)


def ipv4(length=0):
    r1 = random.randint(1,255)
    return '10.20.30.{}'.format(r1)


def ipv4_between_spaces(length=0):
    r1 = ipv4(length)
    return ' {} '.format(r1)


def guid(length=0):
    r1 = generate_random_hexdecimal(8, False)
    r2 = generate_random_hexdecimal(4, False)
    r3 = generate_random_hexdecimal(4, False)
    r4 = generate_random_hexdecimal(4, False)
    r5 = generate_random_hexdecimal(12, False)
    return '{}-{}-{}-{}-{}'.format(r1, r2, r3, r4, r5)


def shost(length=0):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4']
    r1 = ''.join(random.choice(letters) for i in range(4))
    return 'www.{}.acme.com'.format(r1)


def external_id(length=0):
    r1 = random.randint(100000,999999)
    return str(r1)


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
    domains = ['acme', 'aloha', 'blaster', 'toster']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    r1 = domains[random.randint(0, len(domains) - 1)]
    r2 = ''.join(random.choice(letters) for i in range(8))
    return '{}\\\\\\\\\\\\\\\\{}'.format(r1, r2)


def user_name_dot_surname(length=0):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    r1 = ''.join(random.choice(letters) for i in range(8))
    r2 = ''.join(random.choice(letters) for i in range(8))
    return '{}.{}'.format(r1, r2)


def host_plus_domain(length=0):
    domains = ['ACME', 'ALOHA', 'BLASTER', 'TOSTER']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    letters_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '1', '2', '3', '4', '5', '6']
    r1 = ''.join(random.choice(letters) for i in range(4))
    r2 = ''.join(random.choice(letters_up) for i in range(5))
    r3 = ''.join(random.choice(letters_up) for i in range(3))
    r4 = domains[random.randint(0, len(domains) - 1)]
    return '{}/{}-{}.{}.COM'.format(r1, r2, r3, r4)


def domain_email_user(length=0):
    domains = ['acme', 'aloha', 'blaster', 'toster']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6']
    r1 = domains[random.randint(0, len(domains) - 1)]
    r2 = ''.join(random.choice(letters) for i in range(8))
    r3 = ''.join(random.choice(letters) for i in range(5))
    r4 = ''.join(random.choice(letters) for i in range(3))
    return '{}@{}.{}.{}'.format(r1, r2, r3, r4)


def email_simple(length=0):
    domains = ['acme.com', 'aloha.org', 'blaster.com', 'toster.org']
    domain = domains[random.randint(0, len(domains) - 1)]
    user = generate_random_user()
    return '{}@{}'.format(user, domain)


def ad_domain(length=0):
    letters = ['seabh', 'sealossan', 'earthbh', 'earthlossan', 'firelos', 'firevice', 'firecero']
    domains = ['prd', 'hom', 'test', 'local']
    r1 = letters[random.randint(0, len(letters) - 1)]
    r2 = domains[random.randint(0, len(domains) - 1)]
    return '{}.{}'.format(r1, r2)


def ad_log_id(length=0):
    r1 = random.randint(1000000000,9999999999)
    r2 = random.randint(1000000000,9999999999)
    return '{}/{}'.format(r1, r2)


def id_number(length=0):
    return generate_random_number(length)


def random_company_name(length=0):
    names = ['Acme', 'aloha', 'blaster', 'toster', 'Sa_Uap', 'Stark']
    r1 = names[random.randint(0, len(names) - 1)]
    return '{}'.format(r1)


def sid(length=0):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    r1 = ''.join(random.choice(letters) for i in range(7))
    r2 = random.choice(letters)

    return 'sid_{}_{}'.format(r1, r2)


def mysql_user(length=0):
    user = generate_random_user()

    return 'user: \'{}\''.format(user)
