from pysnmp.hlapi import *

def snmp_get(ip, community, oid):
    """
    Wykonuje zapytanie SNMP GET do urządzenia.
    :param ip: Adres IP urządzenia
    :param community: Społeczność SNMP (community string)
    :param oid: OID (Object Identifier) do pobrania
    :return: Wartość OID
    """
    error_indication, error_status, error_index, var_binds = next(
        getCmd(SnmpEngine(),
               CommunityData(community, mpModel=0),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if error_indication:
        print(f"Błąd: {error_indication}")
    elif error_status:
        print(f"Błąd: {error_status.prettyPrint()}")
    else:
        for var_bind in var_binds:
            return var_bind.prettyPrint().split('=')[1].strip()

def discover_devices(ips, community):
    """
    Wykrywa urządzenia w podanej sieci SNMP.
    :param ips: Lista adresów IP do przeszukania
    :param community: Społeczność SNMP (community string)
    :return: Lista wykrytych urządzeń
    """
    devices = []
    for ip in ips:
        try:
            sys_descr = snmp_get(ip, community, '1.3.6.1.2.1.1.1.0')  # OID dla system description
            if sys_descr:
                devices.append({'ip': ip, 'description': sys_descr})
        except Exception as e:
            print(f"Błąd podczas próby połączenia z {ip}: {e}")
    return devices

def run_snmp_discovery():
    # Lista IP do przeszukania
    ips = ['192.168.88.1', '192.168.1.2', '192.168.1.3']

    # Społeczność SNMP
    community = 'public'

    # Wykrywanie urządzeń
    devices = discover_devices(ips, community)

    # Wyświetlanie wykrytych urządzeń
    for device in devices:
        print(f"IP: {device['ip']}, Opis: {device['description']}")

