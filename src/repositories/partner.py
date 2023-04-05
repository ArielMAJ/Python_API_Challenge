""" Defines the Partner repository """

from models import Partner


class PartnerRepository:
    """The repository for the partner model"""

    @staticmethod
    def get(partner_id):
        """Query a partner by partner_id"""
        return Partner.query.filter_by(partner_id=partner_id).first()

    @staticmethod
    def get_all():
        """Query all partners"""
        return Partner.query.all()

    def update(self, partner_id, name, cnpj, email, password):
        """Update a partner's data"""
        partner = self.get(partner_id)
        if partner is None:
            return None

        partner.name = name
        partner.cnpj = cnpj
        partner.email = email
        partner.set_password(password)

        return partner.save()

    @staticmethod
    def create(name, cnpj, email, password):
        """Create a new partner"""
        if Partner.query.filter_by(cnpj=cnpj).first() is not None:
            return None
        if Partner.query.filter_by(email=email).first() is not None:
            return None

        partner = Partner(name=name, cnpj=cnpj, email=email, password=password)

        return partner.save()

    @staticmethod
    def delete(partner_id):
        """Delete a partner"""
        partner = PartnerRepository.get(partner_id)
        if partner is None:
            return None

        return partner.delete()
