""" Defines the Partner repository """

from pyisemail import is_email
from validate_docbr import CNPJ

from models import Partner
import util

class PartnerRepository:
    """The repository for the partner model"""

    @staticmethod
    def get(partner_id):
        """Query a partner by partner_id"""
        partner = PartnerRepository.get_by(partner_id=partner_id)
        if partner is None:
            return "Partner not found."
        return partner

    @staticmethod
    def get_all():
        """Query all partners"""
        return Partner.query.all()

    @staticmethod
    def get_last(last):
        """Query the last added partners, by created_at (creation time)"""
        return Partner.query.order_by(Partner.created_at.desc()).limit(last)

    def update(self, partner_id, name, cnpj, email, password, updated_at):
        """Update a partner's data"""
        email = email.lower()
        cnpj = util.cnpj.process(cnpj)
        partner = self.get(partner_id)
        if not isinstance(partner, Partner):
            return partner

        if error := PartnerRepository.check_partner_is_valid_when_updating(
            partner, name, cnpj, email, password
        ):
            return error.rstrip()

        partner.name = name
        partner.cnpj = cnpj
        partner.email = email
        partner.set_password(password)
        partner.updated_at = updated_at

        return partner.save()

    @staticmethod
    def create(name, cnpj, email, password):
        """Create a new partner"""
        email = email.lower()
        cnpj = util.cnpj.process(cnpj)
        partner = Partner(name=name, cnpj=cnpj, email=email, password=password)

        if errors := PartnerRepository.check_partner_is_valid_when_creating(
            partner, password
        ):
            return errors.rstrip()

        return partner.save()

    @staticmethod
    def delete(partner_id):
        """Delete a partner"""
        partner = PartnerRepository.get(partner_id)
        if isinstance(partner, Partner):
            return partner.delete()
        return partner

    @staticmethod
    def get_by(**kwargs):
        """Query a partner by any of its attributes"""
        if len(kwargs) == 0:
            return "No get/filter parameter provided."
        if len(kwargs) > 1:
            return "Too many get/filter parameters provided."
        return Partner.query.filter_by(**kwargs).first()

    @staticmethod
    def check_cnpj_is_valid(cnpj):
        """Check if a cnpj is valid"""

        if not CNPJ().validate(cnpj):
            return "CNPJ is invalid. "
        return ""

    @staticmethod
    def check_email_is_valid(email):
        """Check if an email is valid"""
        if not is_email(email, check_dns=True):
            return "Invalid email. "
        return ""

    @staticmethod
    def check_cnpj_exists(cnpj):
        """Check if a cnpj already exists"""
        if PartnerRepository.get_by(cnpj=cnpj) is not None:
            return "CNPJ already exists. "
        return ""

    @staticmethod
    def check_email_exists(email):
        """Check if an email already exists"""
        if PartnerRepository.get_by(email=email) is not None:
            return "Email already exists. "
        return ""

    @staticmethod
    def check_password_is_valid(password):
        """Check if a password is valid"""
        if len(password) < 8:
            return "Password is too short. "
        return ""

    @staticmethod
    def check_name_is_valid(name):
        """Check if a name is valid"""
        if len(name) < 3:
            return "Name is too short. "
        return ""

    @staticmethod
    def check_partner_is_Partner(partner):
        """Check if a partner is an instance of Partner"""
        if not isinstance(partner, Partner):
            return partner + " "
        return ""

    @staticmethod
    def check_partner_is_valid_when_creating(partner, password):
        """Check if a partner is valid"""
        errors = ""
        errors += PartnerRepository.check_name_is_valid(partner.name)
        errors += PartnerRepository.check_password_is_valid(password)
        errors += PartnerRepository.check_email_is_valid(partner.email)
        errors += PartnerRepository.check_email_exists(partner.email)
        errors += PartnerRepository.check_cnpj_is_valid(partner.cnpj)
        errors += PartnerRepository.check_cnpj_exists(partner.cnpj)
        return errors

    @staticmethod
    def check_partner_is_valid_when_updating(
        partner,
        name,
        cnpj,
        email,
        password,
    ):
        """Check if a partner is valid"""
        errors = ""
        errors += PartnerRepository.check_partner_is_Partner(partner)
        errors += PartnerRepository.check_password_is_valid(password)
        if name != partner.name:
            errors += PartnerRepository.check_name_is_valid(name)
        if email != partner.email:
            errors += PartnerRepository.check_email_is_valid(email)
            errors += PartnerRepository.check_email_exists(email)
        if cnpj != partner.cnpj:
            errors += PartnerRepository.check_cnpj_is_valid(cnpj)
            errors += PartnerRepository.check_cnpj_exists(cnpj)

        return errors
