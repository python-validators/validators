"""Test BTC address."""

# external
import pytest

# local
from validators import ValidationError, btc_address


@pytest.mark.parametrize(
    "value",
    [
        # P2PKH (Pay-to-PubkeyHash) type
        "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2",
        # P2SH (Pay to script hash) type
        "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",
        # Testnet P2PKH and P2SH
        "mipcBbFg9gMiCh81Kj8tqqdgoZub1ZJRfn",
        "n4fajahJrAuKbN7uNsKjLjQkz9Qn5ewJXQ",
        "2MzQwSSnBHWHqSAqtTVQ6v47XtaisrJa1Vc",
        # Bech32/segwit v0 type
        "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq",
        "bc1qc7slrfxkknqcq2jevvvkdgvrt8080852dfjewde450xdlk4ugp7szw5tk9",
        # Bech32/segwit v0 testnet
        "tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx",
        "tb1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3",
        # Bech32m/segwit v1-16
        "bc1p0xlxvlhemja6c4dqv22uapctqupfhlxm9h8z3k2e72q4k9hcz7vqzk5jj0",
        "tb1pqqqqp399et2xygdj5xreqhjjvcmzhxw4aywxecjdzew6hylgvsesf3hn0c",
        "bc1sw50qgdz25j",
        "bc1pw508d6qejxtdg4y5r3zarvary0c5xw7kw508d6qejxtdg4y5r3zarvary0c5xw7kt5nd6y",
    ],
)
def test_returns_true_on_valid_btc_address(value: str):
    """Test returns true on valid btc address."""
    assert btc_address(value)


@pytest.mark.parametrize(
    "value",
    [
        "ff3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69",
        "b3Cgwgr2g7vsi1bXyjyDUkphEnVoRLA9w4FZfC69",
        # incorrect header
        "1BvBMsEYstWetqTFn5Au4m4GFg7xJaNVN2",
        # incorrect checksum
        "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLz",
        # valid Base58Check addresses from other blockchains
        "TLjfbTbpZYDQ4EoA4N5CLNgGjfbF8ZWz38",  # TRON (0x41)
        "LajyQBeZaBA1NkZDeY8YT5RYYVRkXMvb2T",  # Litecoin P2PKH (0x30)
        "DH5yaieqoZN36fDVciNyRueRGvGLR3mr7L",  # Dogecoin P2PKH (0x1e)
        # valid Base58Check with matching Bitcoin prefix/length but non-Bitcoin version byte
        "3R2e7gNMbRpjEZu5DCiLWBH8siHBC8immQ",  # version 0x06
        "2NGarBRJPCtL5SMXctLLD88GQ64VLy8dGrv",  # version 0xc5
        # leading '1' prepended to valid 34-char P2SH address
        "13J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",
        # 35-char Base58 strings overflowing 25 bytes
        "z" * 35,
        "2" + "z" * 34,
        # invalid Bech32 separator
        "bc0qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4",
        "bc2qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4",
        "bc3qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4",
        "tb0qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx",
        # invalid witness version
        "bc13w508d6qejxtdg4y5r3zarvary0c5xw7kn40wf2",
        # invalid witness v0 program length
        "bc1qr508d6qejxtdg4y5r3zarvaryv98gj9p",
        "bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4a",
        # invalid witness v1-16 program length
        "bc1rw5uspcuh",
        "bc10w508d6qejxtdg4y5r3zarvary0c5xw7kw508d6qejxtdg4y5r3zarvary0c5xw7kw5rljs90",
    ],
)
def test_returns_failed_validation_on_invalid_btc_address(value: str):
    """Test returns failed validation on invalid btc address."""
    assert isinstance(btc_address(value), ValidationError)
