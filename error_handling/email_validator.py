class NameTooShortError(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError (Exception):
    pass

emails = input()

valid_domains = {'com','bg','org','net'}

while emails!='End':
    infos_without_domain = emails.split('@')
    name=infos_without_domain[0]

    if len(name)<=4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif len(infos_without_domain)<2:
        raise MustContainAtSymbolError('Email must contain @')

    infos_with_domain = infos_without_domain[1]
    domain = infos_with_domain.split('.')[1]
    if domain not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    print('Email is valid')
    emails = input()
