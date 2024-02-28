from typing import TYPE_CHECKING, Optional, Set

from .Locations import ID_BASE
from .Rom import Addr

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext


class MarioKart64Client(BizHawkClient):
    game = "Mario Kart 64"
    system = "N64"
    patch_suffix = ".apmk64"
    local_checked_locations: Set[int]
    rom_slot_name: Optional[str]

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.rom_slot_name = None
        self.unchecked_locs: bytearray = bytearray([0xFF] * Addr.SAVE_UNCHECKED_LOCATIONS_SIZE)

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger

        try:
            # Check if ROM is some version of MK64 patched with the Archipelago basepatch
            game_name = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x20, 0x10, "ROM")]))[0]).decode("ascii")
            if game_name != "MK64 ARCHIPELAGO":
                return False

            # Check if we can read the slot name. Doing this here instead of set_auth as a protection against
            # validating a ROM where there's no slot name to read.
            try:
                player_name_bytes = (await bizhawk.read(ctx.bizhawk_ctx,
                                                      [(Addr.PLAYER_NAME, Addr.PLAYER_NAME_SIZE, "ROM")]))[0]
                seed_name_bytes = (await bizhawk.read(ctx.bizhawk_ctx,
                                                      [(Addr.SEED_NAME, Addr.SEED_NAME_SIZE, "ROM")]))[0]
                self.rom_slot_name = (bytes([byte for byte in player_name_bytes if byte != 0]).decode("utf-8")
                                      + "_"
                                      + bytes([byte for byte in seed_name_bytes if byte != 0]).decode("ascii"))
            except UnicodeDecodeError:
                logger.info("Could not read slot name from ROM. Are you sure this ROM matches this client version?")
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        ctx.items_handling = 0b001  # Client handles items sent from other worlds, but not from your own world.
        ctx.want_slot_data = False
        return True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        ctx.auth = self.rom_slot_name

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        # from BizHawkClient import RequestFailedError, bizhawk_write, bizhawk_guarded_write, bizhawk_read

        try:
            # Read Game State
            read_state = await bizhawk.read(ctx.bizhawk_ctx, [
                (Addr.GAME_STATUS_BYTE, 1, "RDRAM"),
                (Addr.NUM_ITEMS_RECEIVED, 1, "RDRAM"),
                (Addr.LOCATIONS_UNCHECKED, Addr.SAVE_UNCHECKED_LOCATIONS_SIZE, "RDRAM")])

            if not read_state[0][0]:  # first bit is always 1 to indicate valid connection
                return

            game_clear = (read_state[0][0] >> 1) & 1
            num_received_items = read_state[1][0]
            locs_state = read_state[2]

            # Receive item if we have one
            if num_received_items < len(ctx.items_received):
                receive_item = ctx.items_received[num_received_items]
                local_id = receive_item.item - ID_BASE
                receive_player = ctx.player_names[receive_item.player].encode("ascii")[:Addr.ASCII_PLAYER_NAME_SIZE]
                receive_item_name = ctx.item_names[receive_item.item].encode("ascii")[:Addr.ITEM_NAME_SIZE]
                await bizhawk.guarded_write(ctx.bizhawk_ctx,
                    [(Addr.RECEIVE_ITEM_ID, local_id.to_bytes(1, "big"), "RDRAM"),
                        (Addr.RECEIVE_CLASSIFICATION, receive_item.flags.to_bytes(1, "big"), "RDRAM"),
                        (Addr.RECEIVE_PLAYER_NAME, receive_player, "RDRAM"),
                        (Addr.RECEIVE_ITEM_NAME, receive_item_name, "RDRAM")],
                    [(Addr.RECEIVE_ITEM_ID, [0xFF], "RDRAM")])

            # Check for new locations to send
            new_locs = list()
            for i, byte in enumerate(locs_state):
                if byte != self.unchecked_locs[i]:
                    for j in range(8):
                        if byte & 1 << j != self.unchecked_locs[i] & 1 << j:
                            new_locs.append(ID_BASE + 8 * i + j)
                    self.unchecked_locs[i] = byte

            # Send new locations
            if new_locs is not None:
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": new_locs
                }])

            # Send game clear
            if not ctx.finished_game and game_clear:
                await ctx.send_msgs([{
                    "cmd":    "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect.
            pass
