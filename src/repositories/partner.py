""" Defines the Partner repository """

from models import Partner


class PartnerRepository:
    """The repository for the partner model"""

    @staticmethod
    def get(partner_id):
        """Query a partner by partner_id"""
        partner = Partner.query.filter_by(partner_id=partner_id).first()
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
        partner = self.get(partner_id)

        if not isinstance(partner, Partner):
            return partner
        if (
            cnpj != partner.cnpj
            and Partner.query.filter_by(cnpj=cnpj).first() is not None
        ):
            return "CNPJ already exists."
        if (
            email != partner.email
            and Partner.query.filter_by(email=email).first() is not None
        ):
            return "Email already exists."

        partner.name = name
        partner.cnpj = cnpj
        partner.email = email
        partner.set_password(password)
        partner.updated_at = updated_at

        return partner.save()

    @staticmethod
    def create(name, cnpj, email, password):
        """Create a new partner"""
        if Partner.query.filter_by(cnpj=cnpj).first() is not None:
            return "CNPJ already exists."
        if Partner.query.filter_by(email=email.lower()).first() is not None:
            return "Email already exists."

        partner = Partner(name=name, cnpj=cnpj, email=email, password=password)

        return partner.save()

    @staticmethod
    def delete(partner_id):
        """Delete a partner"""
        partner = PartnerRepository.get(partner_id)
        if isinstance(partner, Partner):
            return partner.delete()
        return partner
