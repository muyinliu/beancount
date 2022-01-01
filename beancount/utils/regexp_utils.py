"""Regular expression helpers.
"""
__copyright__ = "Copyright (C) 2018  Martin Blais"
__license__ = "GNU GPLv2"


UNICODE_RANGES = {
    # Chinese
    'zh-CN': (r'\u4e00-\u9fa5'),
    # Letters.
    'L': (r'\u0041-\u005A'
          r'\u0061-\u007A'
          r'\u00AA'
          r'\u00B5'
          r'\u00BA'
          r'\u00C0-\u00D6'
          r'\u00D8-\u00F6'
          r'\u00F8-\u02C1'
          r'\u02C6-\u02D1'
          r'\u02E0-\u02E4'
          r'\u02EC'
          r'\u02EE'
          r'\u0370-\u0374'
          r'\u0376-\u0377'
          r'\u037A-\u037D'
          r'\u0386'
          r'\u0388-\u038A'
          r'\u038C'
          r'\u038E-\u03A1'
          r'\u03A3-\u03F5'
          r'\u03F7-\u0481'
          r'\u048A-\u0523'
          r'\u0531-\u0556'
          r'\u0559'
          r'\u0561-\u0587'
          r'\u05D0-\u05EA'
          r'\u05F0-\u05F2'
          r'\u0621-\u064A'
          r'\u066E-\u066F'
          r'\u0671-\u06D3'
          r'\u06D5'
          r'\u06E5-\u06E6'
          r'\u06EE-\u06EF'
          r'\u06FA-\u06FC'
          r'\u06FF'
          r'\u0710'
          r'\u0712-\u072F'
          r'\u074D-\u07A5'
          r'\u07B1'
          r'\u07CA-\u07EA'
          r'\u07F4-\u07F5'
          r'\u07FA'
          r'\u0904-\u0939'
          r'\u093D'
          r'\u0950'
          r'\u0958-\u0961'
          r'\u0971-\u0972'
          r'\u097B-\u097F'
          r'\u0985-\u098C'
          r'\u098F-\u0990'
          r'\u0993-\u09A8'
          r'\u09AA-\u09B0'
          r'\u09B2'
          r'\u09B6-\u09B9'
          r'\u09BD'
          r'\u09CE'
          r'\u09DC-\u09DD'
          r'\u09DF-\u09E1'
          r'\u09F0-\u09F1'
          r'\u0A05-\u0A0A'
          r'\u0A0F-\u0A10'
          r'\u0A13-\u0A28'
          r'\u0A2A-\u0A30'
          r'\u0A32-\u0A33'
          r'\u0A35-\u0A36'
          r'\u0A38-\u0A39'
          r'\u0A59-\u0A5C'
          r'\u0A5E'
          r'\u0A72-\u0A74'
          r'\u0A85-\u0A8D'
          r'\u0A8F-\u0A91'
          r'\u0A93-\u0AA8'
          r'\u0AAA-\u0AB0'
          r'\u0AB2-\u0AB3'
          r'\u0AB5-\u0AB9'
          r'\u0ABD'
          r'\u0AD0'
          r'\u0AE0-\u0AE1'
          r'\u0B05-\u0B0C'
          r'\u0B0F-\u0B10'
          r'\u0B13-\u0B28'
          r'\u0B2A-\u0B30'
          r'\u0B32-\u0B33'
          r'\u0B35-\u0B39'
          r'\u0B3D'
          r'\u0B5C-\u0B5D'
          r'\u0B5F-\u0B61'
          r'\u0B71'
          r'\u0B83'
          r'\u0B85-\u0B8A'
          r'\u0B8E-\u0B90'
          r'\u0B92-\u0B95'
          r'\u0B99-\u0B9A'
          r'\u0B9C'
          r'\u0B9E-\u0B9F'
          r'\u0BA3-\u0BA4'
          r'\u0BA8-\u0BAA'
          r'\u0BAE-\u0BB9'
          r'\u0BD0'
          r'\u0C05-\u0C0C'
          r'\u0C0E-\u0C10'
          r'\u0C12-\u0C28'
          r'\u0C2A-\u0C33'
          r'\u0C35-\u0C39'
          r'\u0C3D'
          r'\u0C58-\u0C59'
          r'\u0C60-\u0C61'
          r'\u0C85-\u0C8C'
          r'\u0C8E-\u0C90'
          r'\u0C92-\u0CA8'
          r'\u0CAA-\u0CB3'
          r'\u0CB5-\u0CB9'
          r'\u0CBD'
          r'\u0CDE'
          r'\u0CE0-\u0CE1'
          r'\u0D05-\u0D0C'
          r'\u0D0E-\u0D10'
          r'\u0D12-\u0D28'
          r'\u0D2A-\u0D39'
          r'\u0D3D'
          r'\u0D60-\u0D61'
          r'\u0D7A-\u0D7F'
          r'\u0D85-\u0D96'
          r'\u0D9A-\u0DB1'
          r'\u0DB3-\u0DBB'
          r'\u0DBD'
          r'\u0DC0-\u0DC6'
          r'\u0E01-\u0E30'
          r'\u0E32-\u0E33'
          r'\u0E40-\u0E46'
          r'\u0E81-\u0E82'
          r'\u0E84'
          r'\u0E87-\u0E88'
          r'\u0E8A'
          r'\u0E8D'
          r'\u0E94-\u0E97'
          r'\u0E99-\u0E9F'
          r'\u0EA1-\u0EA3'
          r'\u0EA5'
          r'\u0EA7'
          r'\u0EAA-\u0EAB'
          r'\u0EAD-\u0EB0'
          r'\u0EB2-\u0EB3'
          r'\u0EBD'
          r'\u0EC0-\u0EC4'
          r'\u0EC6'
          r'\u0EDC-\u0EDD'
          r'\u0F00'
          r'\u0F40-\u0F47'
          r'\u0F49-\u0F6C'
          r'\u0F88-\u0F8B'
          r'\u1000-\u102A'
          r'\u103F'
          r'\u1050-\u1055'
          r'\u105A-\u105D'
          r'\u1061'
          r'\u1065-\u1066'
          r'\u106E-\u1070'
          r'\u1075-\u1081'
          r'\u108E'
          r'\u10A0-\u10C5'
          r'\u10D0-\u10FA'
          r'\u10FC'
          r'\u1100-\u1159'
          r'\u115F-\u11A2'
          r'\u11A8-\u11F9'
          r'\u1200-\u1248'
          r'\u124A-\u124D'
          r'\u1250-\u1256'
          r'\u1258'
          r'\u125A-\u125D'
          r'\u1260-\u1288'
          r'\u128A-\u128D'
          r'\u1290-\u12B0'
          r'\u12B2-\u12B5'
          r'\u12B8-\u12BE'
          r'\u12C0'
          r'\u12C2-\u12C5'
          r'\u12C8-\u12D6'
          r'\u12D8-\u1310'
          r'\u1312-\u1315'
          r'\u1318-\u135A'
          r'\u1380-\u138F'
          r'\u13A0-\u13F4'
          r'\u1401-\u166C'
          r'\u166F-\u1676'
          r'\u1681-\u169A'
          r'\u16A0-\u16EA'
          r'\u16EE-\u16F0'
          r'\u1700-\u170C'
          r'\u170E-\u1711'
          r'\u1720-\u1731'
          r'\u1740-\u1751'
          r'\u1760-\u176C'
          r'\u176E-\u1770'
          r'\u1780-\u17B3'
          r'\u17D7'
          r'\u17DC'
          r'\u1820-\u1877'
          r'\u1880-\u18A8'
          r'\u18AA'
          r'\u1900-\u191C'
          r'\u1950-\u196D'
          r'\u1970-\u1974'
          r'\u1980-\u19A9'
          r'\u19C1-\u19C7'
          r'\u1A00-\u1A16'
          r'\u1B05-\u1B33'
          r'\u1B45-\u1B4B'
          r'\u1B83-\u1BA0'
          r'\u1BAE-\u1BAF'
          r'\u1C00-\u1C23'
          r'\u1C4D-\u1C4F'
          r'\u1C5A-\u1C7D'
          r'\u1D00-\u1DBF'
          r'\u1E00-\u1F15'
          r'\u1F18-\u1F1D'
          r'\u1F20-\u1F45'
          r'\u1F48-\u1F4D'
          r'\u1F50-\u1F57'
          r'\u1F59'
          r'\u1F5B'
          r'\u1F5D'
          r'\u1F5F-\u1F7D'
          r'\u1F80-\u1FB4'
          r'\u1FB6-\u1FBC'
          r'\u1FBE'
          r'\u1FC2-\u1FC4'
          r'\u1FC6-\u1FCC'
          r'\u1FD0-\u1FD3'
          r'\u1FD6-\u1FDB'
          r'\u1FE0-\u1FEC'
          r'\u1FF2-\u1FF4'
          r'\u1FF6-\u1FFC'
          r'\u2071'
          r'\u207F'
          r'\u2090-\u2094'
          r'\u2102'
          r'\u2107'
          r'\u210A-\u2113'
          r'\u2115'
          r'\u2119-\u211D'
          r'\u2124'
          r'\u2126'
          r'\u2128'
          r'\u212A-\u212D'
          r'\u212F-\u2139'
          r'\u213C-\u213F'
          r'\u2145-\u2149'
          r'\u214E'
          r'\u2160-\u2188'
          r'\u2C00-\u2C2E'
          r'\u2C30-\u2C5E'
          r'\u2C60-\u2C6F'
          r'\u2C71-\u2C7D'
          r'\u2C80-\u2CE4'
          r'\u2D00-\u2D25'
          r'\u2D30-\u2D65'
          r'\u2D6F'
          r'\u2D80-\u2D96'
          r'\u2DA0-\u2DA6'
          r'\u2DA8-\u2DAE'
          r'\u2DB0-\u2DB6'
          r'\u2DB8-\u2DBE'
          r'\u2DC0-\u2DC6'
          r'\u2DC8-\u2DCE'
          r'\u2DD0-\u2DD6'
          r'\u2DD8-\u2DDE'
          r'\u2E2F'
          r'\u3005-\u3007'
          r'\u3021-\u3029'
          r'\u3031-\u3035'
          r'\u3038-\u303C'
          r'\u3041-\u3096'
          r'\u309D-\u309F'
          r'\u30A1-\u30FA'
          r'\u30FC-\u30FF'
          r'\u3105-\u312D'
          r'\u3131-\u318E'
          r'\u31A0-\u31B7'
          r'\u31F0-\u31FF'
          r'\u3400'
          r'\u4DB5'
          r'\u4E00'
          r'\u9FC3'
          r'\uA000-\uA48C'
          r'\uA500-\uA60C'
          r'\uA610-\uA61F'
          r'\uA62A-\uA62B'
          r'\uA640-\uA65F'
          r'\uA662-\uA66E'
          r'\uA67F-\uA697'
          r'\uA717-\uA71F'
          r'\uA722-\uA788'
          r'\uA78B-\uA78C'
          r'\uA7FB-\uA801'
          r'\uA803-\uA805'
          r'\uA807-\uA80A'
          r'\uA80C-\uA822'
          r'\uA840-\uA873'
          r'\uA882-\uA8B3'
          r'\uA90A-\uA925'
          r'\uA930-\uA946'
          r'\uAA00-\uAA28'
          r'\uAA40-\uAA42'
          r'\uAA44-\uAA4B'
          r'\uAC00'
          r'\uD7A3'
          r'\uF900-\uFA2D'
          r'\uFA30-\uFA6A'
          r'\uFA70-\uFAD9'
          r'\uFB00-\uFB06'
          r'\uFB13-\uFB17'
          r'\uFB1D'
          r'\uFB1F-\uFB28'
          r'\uFB2A-\uFB36'
          r'\uFB38-\uFB3C'
          r'\uFB3E'
          r'\uFB40-\uFB41'
          r'\uFB43-\uFB44'
          r'\uFB46-\uFBB1'
          r'\uFBD3-\uFD3D'
          r'\uFD50-\uFD8F'
          r'\uFD92-\uFDC7'
          r'\uFDF0-\uFDFB'
          r'\uFE70-\uFE74'
          r'\uFE76-\uFEFC'
          r'\uFF21-\uFF3A'
          r'\uFF41-\uFF5A'
          r'\uFF66-\uFFBE'
          r'\uFFC2-\uFFC7'
          r'\uFFCA-\uFFCF'
          r'\uFFD2-\uFFD7'
          r'\uFFDA-\uFFDC'),

    # Uppercase letters.
    'Lu': (r'\u0041-\u005a'
           r'\u00c0-\u00d6'
           r'\u00d8-\u00de'
           r'\u0100'
           r'\u0102'
           r'\u0104'
           r'\u0106'
           r'\u0108'
           r'\u010a'
           r'\u010c'
           r'\u010e'
           r'\u0110'
           r'\u0112'
           r'\u0114'
           r'\u0116'
           r'\u0118'
           r'\u011a'
           r'\u011c'
           r'\u011e'
           r'\u0120'
           r'\u0122'
           r'\u0124'
           r'\u0126'
           r'\u0128'
           r'\u012a'
           r'\u012c'
           r'\u012e'
           r'\u0130'
           r'\u0132'
           r'\u0134'
           r'\u0136'
           r'\u0139'
           r'\u013b'
           r'\u013d'
           r'\u013f'
           r'\u0141'
           r'\u0143'
           r'\u0145'
           r'\u0147'
           r'\u014a'
           r'\u014c'
           r'\u014e'
           r'\u0150'
           r'\u0152'
           r'\u0154'
           r'\u0156'
           r'\u0158'
           r'\u015a'
           r'\u015c'
           r'\u015e'
           r'\u0160'
           r'\u0162'
           r'\u0164'
           r'\u0166'
           r'\u0168'
           r'\u016a'
           r'\u016c'
           r'\u016e'
           r'\u0170'
           r'\u0172'
           r'\u0174'
           r'\u0176'
           r'\u0178'
           r'\u0179'
           r'\u017b'
           r'\u017d'
           r'\u0181'
           r'\u0182'
           r'\u0184'
           r'\u0186'
           r'\u0187'
           r'\u0189-'
           r'\u018b'
           r'\u018e-\u0191'
           r'\u0193'
           r'\u0194'
           r'\u0196-'
           r'\u0198'
           r'\u019c'
           r'\u019d'
           r'\u019f'
           r'\u01a0'
           r'\u01a2'
           r'\u01a4'
           r'\u01a6'
           r'\u01a7'
           r'\u01a9'
           r'\u01ac'
           r'\u01ae'
           r'\u01af'
           r'\u01b1-\u01b3'
           r'\u01b5'
           r'\u01b7'
           r'\u01b8'
           r'\u01bc'
           r'\u01c4'
           r'\u01c7'
           r'\u01ca'
           r'\u01cd'
           r'\u01cf'
           r'\u01d1'
           r'\u01d3'
           r'\u01d5'
           r'\u01d7'
           r'\u01d9'
           r'\u01db'
           r'\u01de'
           r'\u01e0'
           r'\u01e2'
           r'\u01e4'
           r'\u01e6'
           r'\u01e8'
           r'\u01ea'
           r'\u01ec'
           r'\u01ee'
           r'\u01f1'
           r'\u01f4'
           r'\u01f6-\u01f8'
           r'\u01fa'
           r'\u01fc'
           r'\u01fe'
           r'\u0200'
           r'\u0202'
           r'\u0204'
           r'\u0206'
           r'\u0208'
           r'\u020a'
           r'\u020c'
           r'\u020e'
           r'\u0210'
           r'\u0212'
           r'\u0214'
           r'\u0216'
           r'\u0218'
           r'\u021a'
           r'\u021c'
           r'\u021e'
           r'\u0220'
           r'\u0222'
           r'\u0224'
           r'\u0226'
           r'\u0228'
           r'\u022a'
           r'\u022c'
           r'\u022e'
           r'\u0230'
           r'\u0232'
           r'\u023a'
           r'\u023b'
           r'\u023d'
           r'\u023e'
           r'\u0241'
           r'\u0243-\u0246'
           r'\u0248'
           r'\u024a'
           r'\u024c'
           r'\u024e'
           r'\u0386'
           r'\u0388-\u038a'
           r'\u038c'
           r'\u038e'
           r'\u038f'
           r'\u0391-\u03a1'
           r'\u03a3-\u03ab'
           r'\u03d2-\u03d4'
           r'\u03d8'
           r'\u03da'
           r'\u03dc'
           r'\u03de'
           r'\u03e0'
           r'\u03e2'
           r'\u03e4'
           r'\u03e6'
           r'\u03e8'
           r'\u03ea'
           r'\u03ec'
           r'\u03ee'
           r'\u03f4'
           r'\u03f7'
           r'\u03f9'
           r'\u03fa'
           r'\u03fd-\u042f'
           r'\u0460'
           r'\u0462'
           r'\u0464'
           r'\u0466'
           r'\u0468'
           r'\u046a'
           r'\u046c'
           r'\u046e'
           r'\u0470'
           r'\u0472'
           r'\u0474'
           r'\u0476'
           r'\u0478'
           r'\u047a'
           r'\u047c'
           r'\u047e'
           r'\u0480'
           r'\u048a'
           r'\u048c'
           r'\u048e'
           r'\u0490'
           r'\u0492'
           r'\u0494'
           r'\u0496'
           r'\u0498'
           r'\u049a'
           r'\u049c'
           r'\u049e'
           r'\u04a0'
           r'\u04a2'
           r'\u04a4'
           r'\u04a6'
           r'\u04a8'
           r'\u04aa'
           r'\u04ac'
           r'\u04ae'
           r'\u04b0'
           r'\u04b2'
           r'\u04b4'
           r'\u04b6'
           r'\u04b8'
           r'\u04ba'
           r'\u04bc'
           r'\u04be'
           r'\u04c0'
           r'\u04c1'
           r'\u04c3'
           r'\u04c5'
           r'\u04c7'
           r'\u04c9'
           r'\u04cb'
           r'\u04cd'
           r'\u04d0'
           r'\u04d2'
           r'\u04d4'
           r'\u04d6'
           r'\u04d8'
           r'\u04da'
           r'\u04dc'
           r'\u04de'
           r'\u04e0'
           r'\u04e2'
           r'\u04e4'
           r'\u04e6'
           r'\u04e8'
           r'\u04ea'
           r'\u04ec'
           r'\u04ee'
           r'\u04f0'
           r'\u04f2'
           r'\u04f4'
           r'\u04f6'
           r'\u04f8'
           r'\u04fa'
           r'\u04fc'
           r'\u04fe'
           r'\u0500'
           r'\u0502'
           r'\u0504'
           r'\u0506'
           r'\u0508'
           r'\u050a'
           r'\u050c'
           r'\u050e'
           r'\u0510'
           r'\u0512'
           r'\u0531-\u0556'
           r'\u10a0-\u10c5'
           r'\u1e00'
           r'\u1e02'
           r'\u1e04'
           r'\u1e06'
           r'\u1e08'
           r'\u1e0a'
           r'\u1e0c'
           r'\u1e0e'
           r'\u1e10'
           r'\u1e12'
           r'\u1e14'
           r'\u1e16'
           r'\u1e18'
           r'\u1e1a'
           r'\u1e1c'
           r'\u1e1e'
           r'\u1e20'
           r'\u1e22'
           r'\u1e24'
           r'\u1e26'
           r'\u1e28'
           r'\u1e2a'
           r'\u1e2c'
           r'\u1e2e'
           r'\u1e30'
           r'\u1e32'
           r'\u1e34'
           r'\u1e36'
           r'\u1e38'
           r'\u1e3a'
           r'\u1e3c'
           r'\u1e3e'
           r'\u1e40'
           r'\u1e42'
           r'\u1e44'
           r'\u1e46'
           r'\u1e48'
           r'\u1e4a'
           r'\u1e4c'
           r'\u1e4e'
           r'\u1e50'
           r'\u1e52'
           r'\u1e54'
           r'\u1e56'
           r'\u1e58'
           r'\u1e5a'
           r'\u1e5c'
           r'\u1e5e'
           r'\u1e60'
           r'\u1e62'
           r'\u1e64'
           r'\u1e66'
           r'\u1e68'
           r'\u1e6a'
           r'\u1e6c'
           r'\u1e6e'
           r'\u1e70'
           r'\u1e72'
           r'\u1e74'
           r'\u1e76'
           r'\u1e78'
           r'\u1e7a'
           r'\u1e7c'
           r'\u1e7e'
           r'\u1e80'
           r'\u1e82'
           r'\u1e84'
           r'\u1e86'
           r'\u1e88'
           r'\u1e8a'
           r'\u1e8c'
           r'\u1e8e'
           r'\u1e90'
           r'\u1e92'
           r'\u1e94'
           r'\u1ea0'
           r'\u1ea2'
           r'\u1ea4'
           r'\u1ea6'
           r'\u1ea8'
           r'\u1eaa'
           r'\u1eac'
           r'\u1eae'
           r'\u1eb0'
           r'\u1eb2'
           r'\u1eb4'
           r'\u1eb6'
           r'\u1eb8'
           r'\u1eba'
           r'\u1ebc'
           r'\u1ebe'
           r'\u1ec0'
           r'\u1ec2'
           r'\u1ec4'
           r'\u1ec6'
           r'\u1ec8'
           r'\u1eca'
           r'\u1ecc'
           r'\u1ece'
           r'\u1ed0'
           r'\u1ed2'
           r'\u1ed4'
           r'\u1ed6'
           r'\u1ed8'
           r'\u1eda'
           r'\u1edc'
           r'\u1ede'
           r'\u1ee0'
           r'\u1ee2'
           r'\u1ee4'
           r'\u1ee6'
           r'\u1ee8'
           r'\u1eea'
           r'\u1eec'
           r'\u1eee'
           r'\u1ef0'
           r'\u1ef2'
           r'\u1ef4'
           r'\u1ef6'
           r'\u1ef8'
           r'\u1f08-\u1f0f'
           r'\u1f18-\u1f1d'
           r'\u1f28-\u1f2f'
           r'\u1f38-\u1f3f'
           r'\u1f48-\u1f4d'
           r'\u1f59'
           r'\u1f5b'
           r'\u1f5d'
           r'\u1f5f'
           r'\u1f68-\u1f6f'
           r'\u1fb8-\u1fbb'
           r'\u1fc8-\u1fcb'
           r'\u1fd8-\u1fdb'
           r'\u1fe8-\u1fec'
           r'\u1ff8-\u1ffb'
           r'\u2102'
           r'\u2107'
           r'\u210b-\u210d'
           r'\u2110-\u2112'
           r'\u2115'
           r'\u2119-\u211d'
           r'\u2124'
           r'\u2126'
           r'\u2128'
           r'\u212a-\u212d'
           r'\u2130-\u2133'
           r'\u213e'
           r'\u213f'
           r'\u2145'
           r'\u2183'
           r'\u2c00-\u2c2e'
           r'\u2c60'
           r'\u2c62-\u2c64'
           r'\u2c67'
           r'\u2c69'
           r'\u2c6b'
           r'\u2c75'
           r'\u2c80'
           r'\u2c82'
           r'\u2c84'
           r'\u2c86'
           r'\u2c88'
           r'\u2c8a'
           r'\u2c8c'
           r'\u2c8e'
           r'\u2c90'
           r'\u2c92'
           r'\u2c94'
           r'\u2c96'
           r'\u2c98'
           r'\u2c9a'
           r'\u2c9c'
           r'\u2c9e'
           r'\u2ca0'
           r'\u2ca2'
           r'\u2ca4'
           r'\u2ca6'
           r'\u2ca8'
           r'\u2caa'
           r'\u2cac'
           r'\u2cae'
           r'\u2cb0'
           r'\u2cb2'
           r'\u2cb4'
           r'\u2cb6'
           r'\u2cb8'
           r'\u2cba'
           r'\u2cbc'
           r'\u2cbe'
           r'\u2cc0'
           r'\u2cc2'
           r'\u2cc4'
           r'\u2cc6'
           r'\u2cc8'
           r'\u2cca'
           r'\u2ccc'
           r'\u2cce'
           r'\u2cd0'
           r'\u2cd2'
           r'\u2cd4'
           r'\u2cd6'
           r'\u2cd8'
           r'\u2cda'
           r'\u2cdc'
           r'\u2cde'
           r'\u2ce0'
           r'\u2ce2'
           r'\uff21-\uff3a'),

    # Decimal numbers.
    'Nd': (r'\u0030-\u0039'
           r'\u0660-\u0669'
           r'\u06f0-\u06f9'
           r'\u07c0-\u07c9'
           r'\u0966-\u096f'
           r'\u09e6-\u09ef'
           r'\u0a66-\u0a6f'
           r'\u0ae6-\u0aef'
           r'\u0b66-\u0b6f'
           r'\u0be6-\u0bef'
           r'\u0c66-\u0c6f'
           r'\u0ce6-\u0cef'
           r'\u0d66-\u0d6f'
           r'\u0e50-\u0e59'
           r'\u0ed0-\u0ed9'
           r'\u0f20-\u0f29'
           r'\u1040-\u1049'
           r'\u17e0-\u17e9'
           r'\u1810-\u1819'
           r'\u1946-\u194f'
           r'\u19d0-\u19d9'
           r'\u1b50-\u1b59'
           r'\uff10-\uff19'),
}


def re_replace_unicode(regexp):
    """Substitute Unicode Properties in regular expressions with their
    corresponding expanded ranges.

    Args:
      regexp: A regular expression string.
    Returns:
      Return the regular expression with Unicode Properties substituted.
    """
    for category, rangestr in UNICODE_RANGES.items():
        regexp = regexp.replace(r'\p{' + category + '}', rangestr)
    return regexp
