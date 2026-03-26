"""
ValidatorRegistry — Structure de classe optimisée pour le RAG.

Fournit un registre centralisé de toutes les fonctions de validation
avec métadonnées, catégorisation et interface unifiée.

Conçu pour être ingéré dans un moteur RAG : chaque validateur expose
sa docstring structurée, ses exemples, ses tags et son domaine d'usage.

Examples:
    >>> from validators.registry import ValidatorRegistry
    >>> reg = ValidatorRegistry()
    >>> reg.validate("email", "test@example.com")
    True
    >>> reg.by_category("hash")
    ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    >>> reg.search("ip")
    ['ip_address', 'ipv4', 'ipv6', 'ipv4_cidr', 'ipv6_cidr']
    >>> reg.describe("email")
    {'name': 'email', 'category': 'network', 'tags': [...], 'doc': '...'}
"""

from __future__ import annotations

import inspect
from dataclasses import dataclass, field
from typing import Any, Callable

from validators.utils import ValidationError


@dataclass(frozen=True)
class ValidatorMeta:
    """Metadata attached to each registered validator — optimised for RAG retrieval.

    Attributes:
        name:       Canonical name of the validator function.
        category:   High-level domain (e.g. ``"hash"``, ``"network"``, ``"finance"``).
        tags:       Search keywords for semantic lookup.
        doc:        Full docstring of the underlying function.
        examples:   Extracted ``(input, expected)`` pairs from the docstring.
        func:       Reference to the decorated validator callable.
    """

    name:     str
    category: str
    tags:     tuple[str, ...]
    doc:      str
    examples: tuple[tuple[str, str], ...]
    func:     Callable[..., Any]

    def to_dict(self) -> dict:
        """Serialise to a plain dict suitable for RAG ingestion."""
        return {
            "name":     self.name,
            "category": self.category,
            "tags":     list(self.tags),
            "doc":      self.doc,
            "examples": [{"input": i, "expected": e} for i, e in self.examples],
        }

    def __call__(self, value: Any) -> bool | ValidationError:
        """Delegate validation to the underlying function."""
        return self.func(value)


def _extract_examples(func: Callable) -> tuple[tuple[str, str], ...]:
    """Parse ``>>>`` lines from a function docstring into ``(input, expected)`` pairs."""
    doc = inspect.getdoc(func) or ""
    examples: list[tuple[str, str]] = []
    lines = doc.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith(">>> "):
            call = line[4:]
            expected = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if not expected.startswith(">>> "):
                examples.append((call, expected))
                i += 2
                continue
        i += 1
    return tuple(examples)


# ── Category and tag mapping ──────────────────────────────────────────────────

_CATEGORY_MAP: dict[str, tuple[str, tuple[str, ...]]] = {
    # name         → (category,  tags)
    "email":       ("network",  ("email", "address", "smtp", "rfc5322")),
    "url":         ("network",  ("url", "http", "https", "uri", "link", "web")),
    "domain":      ("network",  ("domain", "hostname", "dns", "fqdn")),
    "hostname":    ("network",  ("hostname", "host", "dns", "fqdn")),
    "ip_address":  ("network",  ("ip", "address", "ipv4", "ipv6", "network")),
    "ipv4":        ("network",  ("ipv4", "ip", "address", "network")),
    "ipv6":        ("network",  ("ipv6", "ip", "address", "network")),
    "ipv4_cidr":   ("network",  ("ipv4", "cidr", "subnet", "network")),
    "ipv6_cidr":   ("network",  ("ipv6", "cidr", "subnet", "network")),
    "mac_address": ("network",  ("mac", "hardware", "ethernet", "network")),
    "slug":        ("web",      ("slug", "url", "seo", "path")),
    "uri":         ("web",      ("uri", "url", "iri", "rfc3986")),
    "md5":         ("hash",     ("md5", "hash", "checksum", "digest")),
    "sha1":        ("hash",     ("sha1", "hash", "checksum", "digest")),
    "sha224":      ("hash",     ("sha224", "sha2", "hash", "digest")),
    "sha256":      ("hash",     ("sha256", "sha2", "hash", "digest")),
    "sha384":      ("hash",     ("sha384", "sha2", "hash", "digest")),
    "sha512":      ("hash",     ("sha512", "sha2", "hash", "digest")),
    "base16":      ("encoding", ("base16", "hex", "encoding")),
    "base32":      ("encoding", ("base32", "encoding", "rfc4648")),
    "base58":      ("encoding", ("base58", "bitcoin", "encoding")),
    "base64":      ("encoding", ("base64", "encoding", "rfc4648")),
    "uuid":        ("identifier", ("uuid", "guid", "identifier", "rfc4122")),
    "iban":        ("finance",  ("iban", "bank", "account", "iso13616")),
    "bic":         ("finance",  ("bic", "swift", "bank", "iso9362")),
    "cusip":       ("finance",  ("cusip", "security", "finance")),
    "isin":        ("finance",  ("isin", "security", "finance", "iso6166")),
    "card":        ("finance",  ("card", "credit", "debit", "payment", "luhn")),
    "visa":        ("finance",  ("visa", "card", "credit", "payment")),
    "mastercard":  ("finance",  ("mastercard", "card", "credit", "payment")),
    "amex":        ("finance",  ("amex", "card", "credit", "payment")),
    "between":     ("numeric",  ("between", "range", "numeric", "bounds")),
    "length":      ("string",   ("length", "string", "size", "bounds")),
    "cron":        ("time",     ("cron", "schedule", "job", "unix")),
    "timezone":    ("time",     ("timezone", "tz", "pytz", "time")),
    "country":     ("locale",   ("country", "iso3166", "locale")),
    "i18n":        ("locale",   ("locale", "i18n", "language", "country")),
    "eth_address": ("crypto",   ("ethereum", "eth", "erc20", "blockchain", "crypto")),
    "btc_address": ("crypto",   ("bitcoin", "btc", "blockchain", "crypto")),
    "bsc_address": ("crypto",   ("binance", "bsc", "blockchain", "crypto")),
    "trx_address": ("crypto",   ("tron", "trx", "blockchain", "crypto")),
}

_DEFAULT_CATEGORY = "general"
_DEFAULT_TAGS: tuple[str, ...] = ("validation",)


class ValidatorRegistry:
    """Centralised registry of all validators with RAG-friendly metadata.

    Lazily imports validators on first access. Thread-safe for reads.

    Examples:
        >>> reg = ValidatorRegistry()
        >>> reg.validate("email", "user@example.com")
        True
        >>> reg.by_category("hash")
        ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
        >>> reg.search("bitcoin")
        ['btc_address', 'bsc_address']
        >>> reg.to_rag_documents()[:1]
        [{'name': ..., 'category': ..., 'tags': [...], 'doc': ..., 'examples': [...]}]
    """

    def __init__(self) -> None:
        self._registry: dict[str, ValidatorMeta] = {}
        self._build()

    # ── Build ─────────────────────────────────────────────────────────────────

    def _build(self) -> None:
        """Import all validators and register them with metadata."""
        import validators as _v

        for name in dir(_v):
            if name.startswith("_"):
                continue
            obj = getattr(_v, name)
            if not callable(obj) or isinstance(obj, type):
                continue
            # Only register actual validator-decorated functions
            doc = inspect.getdoc(obj) or ""
            if not doc or "ValidationError" not in doc:
                continue

            cat, tags = _CATEGORY_MAP.get(name, (_DEFAULT_CATEGORY, _DEFAULT_TAGS))
            self._registry[name] = ValidatorMeta(
                name=name,
                category=cat,
                tags=tags,
                doc=doc,
                examples=_extract_examples(obj),
                func=obj,
            )

    # ── Lookup ────────────────────────────────────────────────────────────────

    def __getitem__(self, name: str) -> ValidatorMeta:
        """Return metadata for a validator by exact name."""
        return self._registry[name]

    def __contains__(self, name: str) -> bool:
        return name in self._registry

    def __len__(self) -> int:
        return len(self._registry)

    def __iter__(self):
        return iter(self._registry.values())

    def get(self, name: str) -> ValidatorMeta | None:
        """Return metadata or None if not found."""
        return self._registry.get(name)

    def describe(self, name: str) -> dict | None:
        """Return a plain dict description of a validator (RAG-ready)."""
        meta = self.get(name)
        return meta.to_dict() if meta else None

    # ── Validation ────────────────────────────────────────────────────────────

    def validate(self, name: str, value: Any) -> bool | ValidationError:
        """Run a validator by name.

        Args:
            name:   Validator name (e.g. ``"email"``, ``"md5"``).
            value:  Value to validate.

        Returns:
            ``True`` if valid, ``ValidationError`` otherwise.

        Raises:
            KeyError: If ``name`` is not a registered validator.
        """
        return self._registry[name](value)

    def is_valid(self, name: str, value: Any) -> bool:
        """Return ``True``/``False`` without exposing ValidationError objects."""
        result = self.validate(name, value)
        return result is True

    # ── Filtering ─────────────────────────────────────────────────────────────

    def by_category(self, category: str) -> list[str]:
        """Return sorted list of validator names in a given category.

        Examples:
            >>> reg.by_category("hash")
            ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
        """
        return sorted(
            name for name, meta in self._registry.items()
            if meta.category == category
        )

    def categories(self) -> list[str]:
        """Return all unique categories."""
        return sorted({meta.category for meta in self._registry.values()})

    def search(self, keyword: str) -> list[str]:
        """Return validators whose name, category, or tags contain *keyword*.

        Case-insensitive. Ordered: exact-name match first, then tag matches.

        Examples:
            >>> reg.search("ip")
            ['ip_address', 'ipv4', 'ipv4_cidr', 'ipv6', 'ipv6_cidr']
        """
        kw = keyword.lower()
        exact, tagged = [], []
        for name, meta in self._registry.items():
            if kw in name:
                exact.append(name)
            elif kw in meta.category or any(kw in t for t in meta.tags):
                tagged.append(name)
        return sorted(exact) + sorted(tagged)

    # ── RAG export ────────────────────────────────────────────────────────────

    def to_rag_documents(self) -> list[dict]:
        """Export all validators as a list of RAG-ingestible documents.

        Each document contains ``name``, ``category``, ``tags``,
        ``doc`` (full docstring), and ``examples``.

        Returns:
            List of dicts sorted by category then name.
        """
        return [
            meta.to_dict()
            for meta in sorted(
                self._registry.values(),
                key=lambda m: (m.category, m.name),
            )
        ]

    def to_rag_text(self) -> str:
        """Export all validators as a single text blob for embedding.

        Format per validator::

            [category/name] tags: tag1, tag2
            <docstring>
            ---
        """
        parts: list[str] = []
        for meta in sorted(self._registry.values(), key=lambda m: (m.category, m.name)):
            tags = ", ".join(meta.tags)
            parts.append(
                f"[{meta.category}/{meta.name}] tags: {tags}\n{meta.doc}\n---"
            )
        return "\n\n".join(parts)

    # ── Repr ──────────────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        cats = ", ".join(f"{c}({len(self.by_category(c))})" for c in self.categories())
        return f"ValidatorRegistry({len(self)} validators: {cats})"
