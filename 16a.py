from bitarray import bitarray, util


HEX2BIN = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1],
}


def decode(msg):

    sum_version = 0
    msg = util.hex2ba(msg)

    def get_int(bits, pos, num_bits):
        value = util.ba2int(bits[pos:pos+num_bits])
        return value, pos+num_bits

    def get_bit(bits, pos):
        return bits[pos], pos+1

    def unpackage(bits, max_packages=None):
        nonlocal sum_version

        pos = 0
        num_packages = 0

        while pos < len(bits) - 7:
            packet_version, pos = get_int(bits, pos, 3)
            packet_type, pos = get_int(bits, pos, 3)
            sum_version += packet_version
            num_packages += 1

            if packet_type == 4:
                # literal packet
                literal = bitarray()
                while True:
                    another_nibble, pos = get_bit(bits, pos)
                    literal.extend(bits[pos:pos+4])
                    pos += 4
                    if not another_nibble:
                        break

                literal = util.ba2int(literal)
                print(literal, end=' ')
            else:
                # operator packet
                print(f'op{packet_type}(', end=' ')

                length_type_id, pos = get_bit(bits, pos)
                length, pos = get_int(bits, pos, 11 if length_type_id else 15)

                if not length_type_id:
                    sub_length = unpackage(bits[pos:pos+length])
                    assert sub_length == length
                else:
                    sub_length = unpackage(bits[pos:], max_packages=length)
                pos += sub_length
                print(')', end=' ')

            if max_packages is not None and num_packages == max_packages:
                break

        assert max_packages is None or num_packages == max_packages
        return pos

    unpackage(msg)
    print(f'\tSum Version {sum_version}\n')


decode('D2FE28')
decode('38006F45291200')
decode('EE00D40C823060')
decode('8A004A801A8002F478')
decode('620080001611562C8802118E34')
decode('C0015000016115A2E0802F182340')
decode('A0016C880162017C3686B18A3D4780')
decode('005173980232D7F50C740109F3B9F3F0005425D36565F202012CAC0170004262EC658B0200FC3A8AB0EA5FF331201507003710004262243F8F600086C378B7152529CB4981400B202D04C00C0028048095070038C00B50028C00C50030805D3700240049210021C00810038400A400688C00C3003E605A4A19A62D3E741480261B00464C9E6A5DF3A455999C2430E0054FCBE7260084F4B37B2D60034325DE114B66A3A4012E4FFC62801069839983820061A60EE7526781E513C8050D00042E34C24898000844608F70E840198DD152262801D382460164D9BCE14CC20C179F17200812785261CE484E5D85801A59FDA64976DB504008665EB65E97C52DCAA82803B1264604D342040109E802B09E13CBC22B040154CBE53F8015796D8A4B6C50C01787B800974B413A5990400B8CA6008CE22D003992F9A2BCD421F2C9CA889802506B40159FEE0065C8A6FCF66004C695008E6F7D1693BDAEAD2993A9FEE790B62872001F54A0AC7F9B2C959535EFD4426E98CC864801029F0D935B3005E64CA8012F9AD9ACB84CC67BDBF7DF4A70086739D648BF396BFF603377389587C62211006470B68021895FCFBC249BCDF2C8200C1803D1F21DC273007E3A4148CA4008746F8630D840219B9B7C9DFFD2C9A8478CD3F9A4974401A99D65BA0BC716007FA7BFE8B6C933C8BD4A139005B1E00AC9760A73BA229A87520C017E007C679824EDC95B732C9FB04B007873BCCC94E789A18C8E399841627F6CF3C50A0174A6676199ABDA5F4F92E752E63C911ACC01793A6FB2B84D0020526FD26F6402334F935802200087C3D8DD0E0401A8CF0A23A100A0B294CCF671E00A0002110823D4231007A0D4198EC40181E802924D3272BE70BD3D4C8A100A613B6AFB7481668024200D4188C108C401D89716A080')
