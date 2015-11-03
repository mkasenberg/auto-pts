"""GATT test cases"""

try:
    from ptsprojects.testcase import TestCase, TestCmd, TestFunc, \
        TestFuncCleanUp
    from ptsprojects.zephyr.qtestcase import QTestCase

except ImportError: # running this module as script
    import sys
    sys.path.append("../..") # to be able to locate the following imports

    from ptsprojects.testcase import TestCase, TestCmd, TestFunc, \
        TestFuncCleanUp
    from ptsprojects.zephyr.qtestcase import QTestCase

from ptsprojects.zephyr.iutctl import get_zephyr
import btp

def test_cases():
    """Returns a list of GAP test cases
    pts -- Instance of PyPTS"""

    zephyrctl = get_zephyr()

    test_cases = [
        #QTestCase("GATT", "TC_GAC_SR_BV_01_C"),
        QTestCase("GATT", "TC_GAD_SR_BV_01_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
       QTestCase("GATT", "TC_GAD_SR_BV_02_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAD_SR_BV_03_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_inc_svc, 1),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAD_SR_BV_04_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'bbbb'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAD_SR_BV_05_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBBB'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAD_SR_BV_06_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBBB'),
                   TestFunc(btp.gatts_add_desc, 2, 0x03, 'CCCC'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BV_01_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBBB'),
                   TestFunc(btp.gatts_set_val, 2, '01234abc'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_01_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x00, 0x00, 'BBBB'),
                   TestFunc(btp.gatts_set_val, 2, '0123'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_02_C",
                  edit1_wids = {118 : "ffff"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                      TestFunc(btp.gatts_add_char, 1, 0x01, 0x02, 'BBBB'),
                      TestFunc(btp.gatts_set_val, 2, '0123'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_05_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BV_03_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03,
                            '0123456789abcdef0123456789abcdef'),
                   TestFunc(btp.gatts_set_val, 2, '0123'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_06_C",
                  edit1_wids = {111 : "BBBB", 110 : "0003"},
                  cmds = [TestFunc(btp.core_reg_svc_gap),
                          TestFunc(btp.core_reg_svc_gatts),
                          TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                          TestFunc(btp.gatts_add_char, 1, 0x00, 0x00, 'BBBB'),
                          TestFunc(btp.gatts_set_val, 2, '01234abc'),
                          TestFunc(btp.gatts_start_server),
                          TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_07_C",
                  edit1_wids = {119 : "BBBC"},
                  cmds = [TestFunc(btp.core_reg_svc_gap),
                          TestFunc(btp.core_reg_svc_gatts),
                          TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                          TestFunc(btp.gatts_add_char, 1, 0x03, 0x03, 'BBBB'),
                          TestFunc(btp.gatts_set_val, 2, '0123'),
                          TestFunc(btp.gatts_start_server),
                          TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_08_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x03, 0x03, 'BBBB'),
                   TestFunc(btp.gatts_set_val, 2, '0123'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_11_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BV_04_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBBB'),
                   TestFunc(btp.gatts_set_val, 2, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_12_C",
                  edit1_wids = {110 : "0003"},
                  cmds = [TestFunc(btp.core_reg_svc_gap),
                          TestFunc(btp.core_reg_svc_gatts),
                          TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                          TestFunc(btp.gatts_add_char, 1, 0x00, 0x00, 'BBBB'),
                          TestFunc(btp.gatts_set_val, 2, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF'),
                          TestFunc(btp.gatts_start_server),
                          TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_13_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBBB'),
                   TestFunc(btp.gatts_set_val, 2, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_14_C",
                  edit1_wids = {118 : "ffff"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                      TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBBB'),
                      TestFunc(btp.gatts_set_val, 2, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_17_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BV_05_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x03, '2A00'),
                   TestFunc(btp.gatts_set_val, 2, '0123'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x03, '2a01'),
                   TestFunc(btp.gatts_set_val, 4, '4567'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_18_C",
                  edit1_wids = {110 : "0003"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                      TestFunc(btp.gatts_add_char, 1, 0x08, 0x02, 'BBB1'),
                      TestFunc(btp.gatts_set_val, 2, '0123'),
                      TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBB2'),
                      TestFunc(btp.gatts_set_val, 4, '4567'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_19_C",
                  edit1_wids = {118 : "ffff"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                      TestFunc(btp.gatts_add_char, 1, 0x08, 0x02, 'BBB1'),
                      TestFunc(btp.gatts_set_val, 2, '0123'),
                      TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'BBB2'),
                      TestFunc(btp.gatts_set_val, 4, '4567'),
                      TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBB3'),
                      TestFunc(btp.gatts_set_val, 6, '4567'),
                      TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBB4'),
                      TestFunc(btp.gatts_set_val, 8, '4567'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_22_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x0B, 0x05, 'BBB1'),
                   TestFunc(btp.gatts_set_val, 2, '0123'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'BBB2'),
                   TestFunc(btp.gatts_set_val, 4, '4567'),
                   TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBB3'),
                   TestFunc(btp.gatts_set_val, 6, '4567'),
                   TestFunc(btp.gatts_add_char, 1, 0x08, 0x03, 'BBB4'),
                   TestFunc(btp.gatts_set_val, 8, '4567'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BV_06_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x01, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_23_C",
                  edit1_wids = {110 : "0004"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                      TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                      TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                      TestFunc(btp.gatts_add_desc, 2, 0x00, 'AA52'),
                      TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_24_C",
                  edit1_wids = {118 : "0005"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'F000AA5004514000B123456789ABCDEF'),
                      TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                      TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                      TestFunc(btp.gatts_add_desc, 2, 0x01, 'AA52'),
                      TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_25_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'F000AA5104514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x41, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_26_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'F000AA5004514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'F000AA5104514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x11, 'F000AA5204514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_27_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x05, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BV_07_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '1234'),
                   TestFunc(btp.gatts_add_desc, 2, 0x01, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BV_08_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABFFFF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x01, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_28_C",
                  edit1_wids = {110 : "0004"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                      TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                      TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                      TestFunc(btp.gatts_add_desc, 2, 0x00, 'AA52'),
                      TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_29_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '1234'),
                   TestFunc(btp.gatts_add_desc, 2, 0x01, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_30_C",
                  edit1_wids = {118 : "FFFF"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                      TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                      TestFunc(btp.gatts_set_val, 2, '1234'),
                      TestFunc(btp.gatts_add_desc, 2, 0x01, 'AA52'),
                      TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_31_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'F000AA5104514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x41, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_32_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'F000AA5004514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'F000AA5104514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x11, 'F000AA5204514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAR_SR_BI_33_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x05, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        #QTestCase("GATT", "TC_GAW_SR_BV_01_C"),
        #QTestCase("GATT", "TC_GAW_SR_BV_02_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_01_C"),
        #QTestCase("GATT", "TC_GAW_SR_BV_03_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_02_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_03_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_06_C"),
        #QTestCase("GATT", "TC_GAW_SR_BV_05_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_07_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_08_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_09_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_13_C"),
        #QTestCase("GATT", "TC_GAW_SR_BV_06_C"),
        #QTestCase("GATT", "TC_GAW_SR_BV_10_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_14_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_15_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_19_C"),
        #QTestCase("GATT", "TC_GAW_SR_BV_07_C"),
        QTestCase("GATT", "TC_GAW_SR_BV_08_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x03, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_20_C",
                  edit1_wids = {118 : "FFFF"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                      TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                      TestFunc(btp.gatts_set_val, 2, 'DCBA'),
                      TestFunc(btp.gatts_add_desc, 2, 0x00, 'AA52'),
                      TestFunc(btp.gatts_set_val, 4, 'ABCD'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_21_C",
                  edit1_wids = {120 : "0004"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                      TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                      TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                      TestFunc(btp.gatts_add_desc, 2, 0x01, 'AA52'),
                      TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_22_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'F000AA5104514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x43, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_23_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'F000AA5004514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'F000AA5104514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x23, 'F000AA5204514000B123456789ABCDEF'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_24_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x0B, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA9876543210'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BV_09_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x03, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_25_C",
                  edit1_wids = {118 : "ABCD"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                      TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                      TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                      TestFunc(btp.gatts_add_desc, 2, 0x00, 'AA52'),
                      TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_26_C",
                  edit1_wids = {120 : "0004"},
                  cmds = [
                      TestFunc(btp.core_reg_svc_gap),
                      TestFunc(btp.core_reg_svc_gatts),
                      TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                      TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                      TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                      TestFunc(btp.gatts_add_desc, 2, 0x01, 'AA52'),
                      TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                      TestFunc(btp.gatts_start_server),
                      TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_27_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x03, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_29_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x43, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_30_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x23, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        QTestCase("GATT", "TC_GAW_SR_BI_31_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AA50'),
                   TestFunc(btp.gatts_add_char, 1, 0x02, 0x01, 'AA51'),
                   TestFunc(btp.gatts_set_val, 2, '0123456789ABCDEF'),
                   TestFunc(btp.gatts_add_desc, 2, 0x0B, 'AA52'),
                   TestFunc(btp.gatts_set_val, 4, 'FEDCBA98765432100123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        #QTestCase("GATT", "TC_GAW_SR_BI_32_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_33_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_34_C"),
        #QTestCase("GATT", "TC_GAW_SR_BI_35_C"),
        QTestCase("GATT", "TC_GAN_SR_BV_01_C",
                  [TestFunc(btp.core_reg_svc_gap),
                   TestFunc(btp.core_reg_svc_gatts),
                   TestFunc(btp.gatts_add_svc, 0, 'AAAA'),
                   TestFunc(btp.gatts_add_char, 1, 0x1a, 0x03, 'BBBB'),
                   TestFunc(btp.gatts_set_val, 2, '00'),
                   TestFunc(btp.gatts_add_desc, 2, 0x03, '2902'),
                   TestFunc(btp.gatts_set_val, 2, '01'),
                   TestFunc(btp.gatts_start_server),
                   TestFunc(btp.gap_adv_ind_on)]),
        #QTestCase("GATT", "TC_GPA_SR_BV_01_C"),
        #QTestCase("GATT", "TC_GPA_SR_BV_02_C"),
        #QTestCase("GATT", "TC_GPA_SR_BV_03_C"),
        #QTestCase("GATT", "TC_GPA_SR_BV_04_C"),
        #QTestCase("GATT", "TC_GPA_SR_BV_05_C"),
        #QTestCase("GATT", "TC_GPA_SR_BV_06_C"),
        #QTestCase("GATT", "TC_GPA_SR_BV_07_C"),
        #QTestCase("GATT", "TC_GPA_SR_BV_08_C"),
        #QTestCase("GATT", "TC_GPA_SR_BV_11_C"),
        #QTestCase("GATT", "TC_GPA_SR_BV_12_C"),
    ]

    return test_cases

def main():
    """Main."""
    import sys
    import ptsprojects.zephyr.iutctl as iutctl

    iutctl.init_stub()

    # to be able to successfully create ZephyrCtl in QTestCase
    iutctl.ZEPHYR_KERNEL_IMAGE = sys.argv[0]

    test_cases_ = test_cases()

    for test_case in test_cases_:
        print
        print test_case

        if test_case.edit1_wids:
            print "edit1_wids: %r" % test_case.edit1_wids

        for index, cmd in enumerate(test_case.cmds):
            print "%d) %s" % (index, cmd)

if __name__ == "__main__":
    main()
