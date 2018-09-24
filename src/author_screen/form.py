from typing import NamedTuple
from pdfrw import PdfReader


class Signatory(NamedTuple):
    """Represents one of the author form signature fields."""
    name: str
    degree: str
    signature: bool
    date: str


class AuthorForm:
    """A programmatic representation of a GBD Authorship form."""

    def __init__(self, path):
        self.reader = PdfReader(str(path))

    @property
    def title(self):
        """The title of the manuscript the author contributed to."""
        return self.reader.pages[0].Annots[1].V[1:-1]

    @property
    def author(self):
        """The manuscripts's corresponding author."""
        return self.reader.pages[0].Annots[2].V[1:-1]

    @property
    def article_type(self):
        """The format of the manuscript."""
        return self.reader.pages[0].Annots[3].V[1:-1]

    @property
    def has_reference_number(self):
        """Whether this manuscript has an associated reference number."""
        return self.reader.pages[0].Annots[5].AS == '/Off'

    @property
    def reference_number(self):
        """The reference number for this manuscript, if it exists."""
        if self.has_reference_number:
            return self.reader.pages[0].Annots[4].V[1:-1]

    @property
    def has_editor(self):
        """Whether this manuscript has a handling editor."""
        return self.reader.pages[0].Annots[8].AS == '/Off'

    @property
    def editor(self):
        """The name of this manuscript's handling editor, if one exists."""
        if self.has_editor:
            return self.reader.pages[0].Annots[7].V[1:-1]

    @property
    def contributions(self):
        """A description of the contributor's contributions to the manuscript."""
        return self.reader.pages[0].Annots[10].V[1:-1]

    @property
    def conflicts(self):
        """Disclosure of the funding source's role in any aspect of the manuscript production."""
        return self.reader.pages[1].Annots[1].V[1:-1]

    def get_signature(self, number: int):
        """Get's a representation of one of the author form signatories.

        Parameters
        ----------
        number :
            Which signatory to get. Between 1 and 10.

        Returns
        -------
            One of the author form signatories.
        """
        n = 4 * (number - 1) + 2
        a = self.reader.pages[1].Annots

        return Signatory(
            name=a[n].V[1:-1] if '/V' in a[n] else '',
            degree=a[n+1].V[1:-1] if '/V' in a[n+1] else '',
            signature=True if '/V' in a[n+2] else False,
            date=a[n+3].V[1:-1] if '/V' in a[n+3] else ''
        )

    def __repr__(self):
        """Get a string representation of the author form."""
        out =  f"AuthorForm(title={self.title}\n"
        out += f"           author={self.author}\n"
        out += f"           article_type={self.article_type}\n"
        out += f"           reference_number={self.reference_number}\n"
        out += f"           editor={self.editor}\n"
        out += f"           contributions={self.contributions}\n"
        out += f"           conflicts={self.conflicts}\n"
        for i in range(10):
            out += f"           signatory_{i+1}={self.get_signature(i+1)}\n"

        return out
