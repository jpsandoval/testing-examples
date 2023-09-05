import unittest
from data import *
from queries import *


class InstrospectionTests(unittest.TestCase):

    def test_hasConstructor(self):
        self.assertTrue(hasConstructor(Client))
        self.assertTrue(hasConstructor(Address))
        self.assertTrue(hasConstructor(Account))
        self.assertTrue(hasConstructor(Robot))

    def test_dont_haveConstructor(self):
        self.assertFalse(hasConstructor(WrongPinException))
        self.assertFalse(hasConstructor(DebtNotAllowed))
        self.assertFalse(hasConstructor(QuickSort))
        self.assertFalse(hasConstructor(OutOffPowerError))

    def test_methodsWith(self):
        results_account = methodsWith('Check', Account)
        results_robot = methodsWith('Check', Robot)
        self.assertEqual(results_account, ['CheckIfWithdrawalPossible', 'CheckPin'])
        self.assertEqual(results_robot, ['Check_power'])

    def test_methodsWithout(self):
        results_account = methodsWith('Steal', Account)
        results_robot = methodsWith('blow', Robot)
        self.assertEqual(results_account, [])
        self.assertEqual(results_robot, [])

    def test_undocumentedMethods(self):
        results_client = sorted(undocumentedMethods(Client))
        results_account = sorted(undocumentedMethods(Account))
        self.assertEqual(results_client, ['__init__', 'expiry_check'])
        self.assertEqual(results_account, ['CheckIfWithdrawalPossible', 'CheckPin', '__init__', 'accountStatus',
                                           'deposit', 'withdrawal'])

    def test_documentedMethods(self):
        results_sort = undocumentedMethods(QuickSort)
        results_error = undocumentedMethods(WrongPinException)
        self.assertEqual(results_sort, [])
        self.assertEqual(results_error, [])

    def test_hasAttributes(self):
        self.assertTrue(hasAttributes(Address("Valley Avenie", "2342", "Denver", "546846")))
        self.assertTrue(hasAttributes(Robot("Soto")))
        self.assertTrue(hasAttributes(Client("64354564553", "Adam", "Nowak", "20/09/2024",
                                             "M", "03/05/1989", "Grzybowska 79")))

    def test_dont_haveAttributes(self):
        self.assertFalse(hasAttributes(QuickSort()))
        self.assertFalse(hasAttributes(DebtNotAllowed()))
        self.assertFalse(hasAttributes(OutOffPowerError()))

    def test_noArgMethods(self):
        results_client = sorted(noArgMethods(Client))
        result_robot = sorted(noArgMethods(Robot))
        self.assertEqual(results_client, ['expiry_check', 'print_data'])
        self.assertEqual(result_robot, ['Check_power', '__repr__', '__str__'])

    def test_withArgMethods(self):
        results_account = noArgMethods(Account)
        result_address = noArgMethods(Address)
        self.assertEqual(results_account, [])
        self.assertEqual(result_address, [])

    def test_allLowerCase(self):
        self.assertTrue(allLowerCase(Client))
        self.assertTrue(allLowerCase(QuickSort))
        self.assertTrue(allLowerCase(Address))

    def test_not_allLowerCase(self):
        self.assertFalse(allLowerCase(Account))
        self.assertFalse(allLowerCase(Robot))

    def test_longMethods(self):
        results_client = sorted(longMethods(Client, 3))
        results_robot = sorted(longMethods(Robot, 3))
        self.assertEqual(results_client, ['__init__', 'print_data'])
        self.assertEqual(results_robot, ['__init__', '__move'])

    def test_not_longMethods(self):
        results_client = sorted(longMethods(Client, 12))
        results_robot = sorted(longMethods(Robot, 14))
        self.assertEqual(results_client, [])
        self.assertEqual(results_robot, [])

    def test_checkNone_with(self):
        account = Account(None, "Villa Ingenio", "1234")
        address = Address(None, "547", "Macul, Santiago", "7820244")
        client = Client("64354564553", "Adam", "Nowak", None,
                        "M", None, "Grzybowska 79")
        self.assertTrue(checkNone(account))
        self.assertTrue(checkNone(address))
        self.assertTrue(checkNone(client))

    def test_checkNone_without(self):
        account = Account("Juan", "Villa Ingenio", "1234")
        address = Address("Monseñor Carlos Casanueva", "547", "Macul, Santiago", "7820244")
        client = Client("64354564553", "Adam", "Nowak", "20/09/2024",
                        "M", "03/05/1989", "Grzybowska 79")
        self.assertFalse(checkNone(account))
        self.assertFalse(checkNone(address))
        self.assertFalse(checkNone(client))


if __name__ == '__main__':
    unittest.main()
