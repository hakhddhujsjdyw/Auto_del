#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "28704037"))
API_HASH     = os.environ.get("API_HASH", "e27aa014fb9668024cb7375d90014493")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "7911558932:AAFU9ksjmqWqlBiLgcZcp7c8H1Pa_mR_WZY")
SESSION      = os.environ.get("SESSION", "BQEjAcAAje8tfsiqbkJTc2zycwtbqfrENn1EPRC3HfI_ax_Zr7hB2PnATvTF-AaHV9S0pLnx4hW8cBWhMMW7-IKtSR1m26gC8o0edAzhikphc1CMmo5TTIc3hbTY-SBE_xypQ-v_rXtPhG7DhdcYiJOikKk0j_em-I-1IoHsxg_VbaNRWZqrBKaMgAws6gI6VnmU1kcr4TBRQQ0uXjlsREu2Ie5E32NglBscUllxcySd2Rg_pyMQiDsJ9IVXCaFbLwBlqjVJilKoc5BOCkJTUmNhGcgs8mwLAV71NhoP4bby_VTf1I5lYu1OK-XBYP6gIoR1-n84o7HKzUo34RRSRRYQTHvXcwAAAAAgJabsAA")
TIME         = int(os.environ.get("TIME", 1))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002413806904 -1002423467975 -1002398417852 -1002197221746 -1002416597824").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Ramanan:Ramanan@cluster0.lvbe2wu.mongodb.net/")
PORT         = os.environ.get("PORT", "8080")
