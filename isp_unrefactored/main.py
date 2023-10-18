from dao.contract_model import ContractModel
from dao.lead_model import LeadModel
from dao.user_mode import UserModel


def main():
    contract_model = ContractModel()
    print(contract_model.connect)

    lead_model = LeadModel()
    print(lead_model)

    user_model = UserModel()
    print(user_model)


if __name__ == '__main__':
    main()