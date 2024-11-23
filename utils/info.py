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

API_ID       = int(os.environ.get("API_ID", "23441722"))
API_HASH     = os.environ.get("API_HASH", "e72792e59b9cffd23ac2c1a989803cde")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "7911558932:AAFU9ksjmqWqlBiLgcZcp7c8H1Pa_mR_WZY")
SESSION      = os.environ.get("SESSION", "1BVtsOMQBu0Udvqi_Mkb6Pjr3lS2B12oUUgO28Rss-7PVCQqciRM46j9Do10HpZljVG3u-gBxs-QSVLQ-8EFUdNOgTjDGXE15WhEa0nbLUr7T6AOSRWUdVfR4qLkAhb7KmnEsNnwEcGfUq_nurozfLi8hdqxkOZqD2r-L47UWGcpjHRrTlOJGlE6yIPI1xOraH3fRAf5ZZbiGScBPhPDJJn8QJejgUZcPsBzoI-9DRCCuhMlOxBUqpkPB_OrlLGLQ8jgn4S1Z4sQbBWpOFW6dnse1Dz51tMm4JvwchDfU7A68nWYpPU5Low0kDpBAxUfO6I_4Pk8pHnOl8bpSxwMHrfapsrAn840=")
TIME         = int(os.environ.get("TIME", 1))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002413806904 -1002423467975 -1002398417852 -1002197221746 -1002416597824").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Ramanan:Ramanan@cluster0.lvbe2wu.mongodb.net/")
PORT         = os.environ.get("PORT", "8080")
