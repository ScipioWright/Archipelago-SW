import string
import win32api
import win32gui

from time import time
from typing import List, Optional, Callable, Any, Awaitable, Dict

from .patch import *

keymap = [
    {
        0x20: [' ', ' '],
        0x30: ['0', ')'],
        0x31: ['1', '!'],
        0x32: ['2', '@'],
        0x33: ['3', '#'],
        0x34: ['4', '$'],
        0x35: ['5', '%'],
        0x36: ['6', '^'],
        0x37: ['7', '&'],
        0x38: ['8', '*'],
        0x39: ['9', '('],
        0xba: [';', ':'],
        0xbb: ['=', '+'],
        0xbc: [',', '<'],
        0xbd: ['-', '_'],
        0xbe: ['.', '>'],
        0xbf: ['/', '?'],
        0xdb: ['[', '{'],
        0xdc: ['\\', '|'],
        0xdd: [']', '}'],
        0xde: ['\'', '"'],
    },
    {
        0x20: [' ', ' '],
        0x30: ['0', '=', '}'],
        0x31: ['1', '!'],
        0x32: ['2', '"', '@'],
        0x33: ['3', '#'],
        0x34: ['4', '$'],
        0x35: ['5', '%'],
        0x36: ['6', '&'],
        0x37: ['7', '/', '{'],
        0x38: ['8', '(', '['],
        0x39: ['9', ')', ']'],
        0xba: [']', '}'],
        0xbb: ['+', '?', '\\'],
        0xbc: [',', ';'],
        0xbd: ['-', '_'],
        0xbe: ['.', ':'],
        0xbf: ['-', '_'],
        0xdc: ['\'', '*'],
        0xdd: ['[', '{'],
        0xde: ['\'', '"'],
    }
]

# Extending the Patch class with some Animal Well specific methods
class Patch(Patch):
    def push_shader_to_stack(self, shader_id):
        """
        Pushes a new shader to the shader stack
        """
        return self.mov_ecx(shader_id).call_via_rax(push_shader_to_stack)

    def pop_shader_from_stack(self):
        """
        Pops a new shader from the shader stack
        """
        return self.call_via_rax(pop_shader_from_stack)

    def push_color_to_stack(self, color):
        """
        Pushes a new color to the color stack
        color: new color in the format #AABBGGRR
        """
        return self.mov_ecx(color).call_via_rax(push_color_to_stack)

    def pop_color_from_stack(self):
        """
        Pops a new color from the color stack
        """
        return self.call_via_rax(pop_color_from_stack)

    def pop_from_position_stack(self):
        """
        Pops a position from the position stack
        """
        return self.call_via_rax(pop_from_position_stack)

    def set_tall_text_mode(self, value):
        """
        Sets whether text will be drawn extra tall or normal
        value: 1 -> Tall Text, 0 -> Normal Text
        """
        return self.mov_ecx(value).call_via_rax(set_tall_text_mode)

    def set_current_shader(self, shader_id):
        """
        Sets the shader on the top of the stack
        shader_id: which shader to switch to
        """
        return self.mov_ecx(shader_id).call_via_rax(set_current_shader)

    def set_current_color(self, color):
        """
        Sets the color on the top of the stack
        colo: new color in the format #AABBGGRR
        """
        return self.mov_ecx(color).call_via_rax(set_current_color)

    def draw_small_text(self, x, y, text_address):
        """
        Draw text on the screen using the current shader, color, and tall text mode
        x: x position
        y: y position
        text_address: location in the process's memory where the Unicode text is stored
        """
        return self.mov_ecx(x).mov_edx(y).mov_to_rax(text_address).mov_rax_to_r8().call_via_rax(draw_small_text)

    def draw_big_text(self, x, y, text_address):
        """
        Draw bigger text with a more versatile font on the screen using the current shader and color
        x: x position
        y: y position
        text_address: location in the process's memory where the Unicode text is stored
        """
        return self.mov_ecx(x).mov_edx(y).mov_to_rax(text_address).mov_rax_to_r8().call_via_rax(draw_big_text)

    def draw_symbol(self, x, y, sprite_id, frame, arg5, arg6, arg7):
        """
        Draw a symbol on the screen using the current shader and color
        x: x position
        y: y position
        sprite_id: id of the sprite to draw
        frame: either which frame of an animation to display or which subsprite
        arg5: idk
        arg6: idk
        arg7: idk
        """
        return (self.mov_ecx(x).mov_edx(y).mov_r8(sprite_id).mov_r9(frame).push(0).push(arg7).push(arg6).push(arg5)
                .push(0).push(0).push(0).push(0).call_far(draw_symbol).add_rsp(0x40))

    def draw_symbol_pointer_x_and_y(self, x_address, y_address, sprite_id, frame, arg5, arg6, arg7):
        """
        Draw a symbol on the screen using the current shader and color, at a location stored in the process's memory
        x_address: the address in the process's memory where the x position is stored
        y_address: the address in the process's memory where the y position is stored
        sprite_id: id of the sprite to draw
        frame: either which frame of an animation to display or which subsprite
        arg5: idk
        arg6: idk
        arg7: idk
        """
        return (self.mov_to_rax(x_address).mov_rax_pointer_contents_to_rcx().mov_to_rax(y_address)
                .mov_rax_pointer_contents_to_rdx().mov_r8(sprite_id).mov_r9(frame).push(0).push(arg7).push(arg6)
                .push(arg5).push(0).push(0).push(0).push(0).call_far(draw_symbol).add_rsp(0x40))

    def warp(self, player, room_x, room_y, tile_x, tile_y, map_to_warp):
        """
        Warps the player to a specific room and tile
        player: pointer to the player in the process's memory
        room_x: the X coordinate of the room to warp to
        room_y: the Y coordinate of the room to warp to
        tile_x: the X coordinate of the tile to warp the player to
        tile_y: the Y coordinate of the tile to warp the player to
        map_to_warp: which map to warp to
        56 bytes
        """
        return (self
                .mov_rcx(player)
                .mov_rdx((room_y << 32) + room_x)
                .mov_r8((tile_y << 32) + tile_x)
                .mov_r9(map_to_warp)
                .call_far(warp))

    def get_key_pressed(self, key):
        return (self
                .mov_ecx(key)
                .call_far(get_key_pressed))

    def get_an_item(self, save_slot_address, item_id, egg_position=0, location_id=0xff):
        return (self
                .mov_rcx(save_slot_address)
                .mov_rdx(item_id)
                .mov_r8(egg_position)
                .mov_r9(location_id)
                .call_far(get_an_item))

    def get_sprite(self, sprite_id):
        """
        Retrieves a sprite based on its sprite_id
        """
        return self.mov_cl(sprite_id).call_via_rax(get_sprite)

    def update_player_state(self, player, state, save):
        """
        Updates the player's state
        """
        return self.mov_rcx(player).mov_rdx(state).mov_r8(save).call_far(update_player_state)


# region FunctionOffsets
# Accurate as of AW file version 1.0.0.18
draw_small_text: int = 0x14006E3F0
draw_big_text: int = 0x14006DE30
draw_symbol: int = 0x14006A6C0
draw_sprite: int = 0x14001AEC0
get_sprite: int = 0x140063CA0
push_shader_to_stack: int = 0x140017840
pop_shader_from_stack: int = 0x1400178A0
push_color_to_stack: int = 0x1400177D0
pop_color_from_stack: int = 0x140017830
pop_from_position_stack: int = 0x140017920
set_tall_text_mode: int = 0x14006DC00
set_current_color: int = 0x1400177B0
set_current_shader: int = 0x14001A280
get_key_pressed: int = 0x140011C70
get_gamepad_button_pressed: int = 0x140011EA0
get_an_item: int = 0x1400C15C0
warp: int = 0x140074DD0
update_player_state: int = 0x1400662F0
play_sound: int = 0x140064480
# endregion

# region OtherOffsets
STEP_AND_TIME_DISPLAY_ORIGINAL_VALUES = {
    0x504fb: 2.0,
    0x504ff: 2.0,
    0x5053e: 6,
    0x50543: 6,
    0x5055a: 7,
    0x5055f: 5,
    0x50417: 310.0,
    0x5041b: 3.0,
    0x5044f: 280,
    0x50454: 5,
    0x50481: 278,
    0x50486: 6,
    0x504b3: 279,
    0x504b8: 5
}
STEP_AND_TIME_DISPLAY_UPDATED_VALUES = {
    0x504fb: 2.0,
    0x504ff: 2.0 + 5,
    0x5053e: 6,
    0x50543: 6 + 5,
    0x5055a: 7,
    0x5055f: 5 + 5,
    0x50417: 310.0,
    0x5041b: 3.0 + 5,
    0x5044f: 280,
    0x50454: 5 + 5,
    0x50481: 278,
    0x50486: 6 + 5,
    0x504b3: 279,
    0x504b8: 5 + 5
}
# endregion

# region Other Constants
HEADER_LENGTH = 0x18
SAVE_SLOT_LENGTH = 0x27010
CUSTOM_MEMORY_SIZE = 0x40000
CUSTOM_STAMPS = 255
TITLE_SCREEN_TEXT_TEMPLATE: str = "AP Randomizer {version}"
TITLE_SCREEN_MAX_TEXT_LENGTH: int = 80
MESSAGE_QUEUE_LENGTH: int = 21
# endregion


class BeanPatcher:
    def set_logger(self, logger):
        self.logger = logger
        return self

    def set_process(self, process):
        self.process = process
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_version_string(self, version):
        self.version_string = version
        self.set_title_text(TITLE_SCREEN_TEXT_TEMPLATE.replace("{version}", self.version_string))
        return self

    def log_info(self, text):
        if self.logger is not None:
            self.logger.info(text)
        return self

    def log_error(self, text):
        if self.logger is not None:
            self.logger.error(text)
        return self

    def set_bean_death_function(self, function: Callable):
        self.on_bean_death_function = function
        return self

    def __init__(self, process=None, logger=None):
        self.process = process
        self.attached_to_process = False
        self.name = None
        self.version_string = ""

        self.logger = logger
        self.log_debug_info = True

        self.aw_module = None
        self.module_base = 0
        self.application_state_address = 0
        self.last_game_state = 0
        self.custom_memory_base = None
        self.custom_memory_current_offset: Optional[int] = None

        self.main_menu_draw_string_addr: Optional[int] = None

        self.revertable_patches: List[Patch] = []
        self.fullbright_patch: Patch
        self.room_palette_override_patch: Optional[Patch] = None
        self.room_palette_override_shader: int = 0x16

        self.bean_has_died_address: int = 0
        self.on_bean_death_function: Optional[Callable[[Any], Awaitable[Any]]] = None

        self.trigger_sound_id_address = None

        self.game_draw_routine_string_addr = None
        self.game_draw_routine_string_size = 256*MESSAGE_QUEUE_LENGTH
        self.game_draw_routine_default_string = "Connected to the Well"

        self.draw_bottom_routine_string_size: int = 0
        self.game_draw_bottom_routine_string_addr = None
        self.game_draw_bottom_routine_string_size = 256
        self.game_draw_bottom_routine_default_string = ""

        self.game_draw_symbol_x_address = None
        self.game_draw_symbol_y_address = None
        self.player_position_history = [(-8, -8)]

        self.last_message_time = 0
        self.message_timeout = 6

        self.last_frame = 0
        self.active_slot = 0
        self.slot_address = 0

        self.unstuck_room_x = 0xb
        self.unstuck_room_y = 0xb
        self.unstuck_pos_x = 0x1a
        self.unstuck_pos_y = 0x74
        self.unstuck_map = 0

        self.fullbright_patch: Optional[Patch] = None

        self.cmd_prompt = False
        self.cmd = ""
        self.cmd_ready = False
        self.cmd_patch = []
        self.cmd_keys = None
        self.cmd_keys_old = None
        self.cmd_keymap = 0
        self.cmd_messages = []

        self.revertable_tracker_patches: Dict[str, Patch] = {}
        self.tracker_original_stamp_count: Optional[int] = None
        self.tracker_stamps_addr: Optional[int] = None
        self.tracker_icons_addr: Optional[int] = None
        self.tracker_text_addr: Optional[int] = None
        self.tracker_draw_routine_addr: Optional[int] = None
        self.tracker_color_routine_addr: Optional[int] = None
        self.tracker_total: int = 0
        self.tracker_in_logic: int = 0
        self.tracker_checked: int = 0
        self.tracker_missing: int = 0
        self.tracker_candles: int = 0
        self.tracker_goal: str = ""
        self.tracker_initialized = False

    @property
    def current_save_slot(self):
        if not self.attached_to_process:
            self.log_error("Can't get current save slot without being attached to a process.")
            return None
        if self.application_state_address is None or self.application_state_address == 0:
            self.log_error("Can't get current save slot without knowing the application state's address.")
            return None

        return self.process.read_uchar(self.application_state_address + 0x40C)

    @property
    def current_save_address(self):
        current_save_slot = self.current_save_slot

        if current_save_slot is None:
            self.log_error("Failed to get the current save slot.")
            return None

        return self.application_state_address + 0x400 + HEADER_LENGTH + (SAVE_SLOT_LENGTH * current_save_slot)

    @property
    def player_address(self):
        if not self.attached_to_process:
            self.log_error("Can't get player data address without being attached to a process.")
            return None
        if self.application_state_address is None or self.application_state_address == 0:
            self.log_error("Can't get player data address without knowing the application state's address.")
            return None

        return self.application_state_address + 0x93670

    @property
    def current_frame_address(self):
        if not self.attached_to_process:
            self.log_error("Can't get current frame address without being attached to a process.")
            return None
        if self.application_state_address is None or self.application_state_address == 0:
            self.log_error("Can't get current frame address without knowing the application state's address.")
            return None

        return self.application_state_address + 0x9360c

    @property
    def stamps_address(self):
        if not self.attached_to_process:
            self.log_error("Can't get stamps address without being attached to a process.")
            return None
        if self.tracker_stamps_addr is None or self.tracker_stamps_addr == 0:
            return None

        return self.tracker_stamps_addr

    def attach_to_process(self, process=None) -> bool:
        if process is not None:
            self.process = process

        if process is None:
            self.log_error("No process handle provided. Cannot attach to process!")
            self.attached_to_process = False
            return False

        if self.log_debug_info:
            self.log_info("Searching for 'Animal Well.exe' module in process memory...")
        self.aw_module = next(f for f in list(self.process.list_modules()) if f.name.startswith("Animal Well.exe"))

        if self.aw_module is None:
            self.log_error(f"Failed to find Animal Well module within the Animal Well process!")
            self.attached_to_process = False
            return False

        if self.log_debug_info:
            self.log_info(f"Found it: Name({self.aw_module.name}), BaseOfDll({hex(self.aw_module.lpBaseOfDll)})")

        self.module_base = self.aw_module.lpBaseOfDll

        application_state_pointer_address = self.module_base + 0x02BD5308
        if self.log_debug_info:
            self.log_info(f"Attempting to find start address via pointer at {hex(application_state_pointer_address)}")

        self.application_state_address = self.process.read_uint(application_state_pointer_address)
        if self.log_debug_info:
            self.log_info(f"application_state address: {hex(self.application_state_address)}")

        self.application_state_address = self.application_state_address
        self.attached_to_process = True

        return True

    def apply_patches(self):
        if not self.attached_to_process:
            self.log_error("Cannot apply patches, not attached to Animal Well process!")
            return False

        if self.log_debug_info:
            self.log_info("Applying patches...")

        self.custom_memory_base = self.process.allocate(CUSTOM_MEMORY_SIZE)
        self.custom_memory_current_offset = self.custom_memory_base

        if self.log_debug_info:
            self.log_info(f"Custom memory space: {hex(self.custom_memory_base)}, length of {hex(CUSTOM_MEMORY_SIZE)}")

        self.apply_main_menu_draw_patch()

        self.apply_in_game_draw_patch()

        self.apply_disable_anticheat_patch()

        if self.log_debug_info:
            self.log_info("Misc patches...")

        self.generate_room_palette_override_patch()

        self.apply_every_frame_patch()

        self.apply_pause_menu_patch()

        self.generate_fullbright_patch()

        self.apply_item_collection_patches()

        self.apply_receive_item_patch()

        self.apply_skip_credits_patch()

        self.apply_deathlink_patch()

        # mural bytes at slot + 0x26eaf
        # default mural bytes at 0x142094600
        # solved bunny bytes = bytearray.fromhex("37 00 00 00 40 01 05 00 00 00 0C 00 40 00 40 46 05 0C 18 09 08 01 90 31 40 46 05 37 F4 07 48 04 40 0E 40 19 01 0C F0 03 32 09 00 02 00 59 00 18 F4 07 02 48 00 02 00 54 05 44 98 09 02 98 01 08 00 55 14 10 80 00 0E 42 00 58 05 15 52 20 8C 00 32 82 00 55 55 55 50 82 8C 08 82 80 40 55 55 55 55 81 88 32 88 80 50 55 55 55 55 81 88 C0 88 80 54 55 55 55 55 20 20 88 88 20 54 55 55 55 15 20 20 20 8C 23 54 55 55 55 E5 EF 23 2C EF FE 56 55 55 55 E5 FF EF EF BE FD 56 55 55 55 E5 FF FF BB 7B F6 54 55 55 55 01 FC E7 EE EF F9 50 55 55 55 00 F0 99 BB BE EF 43 55 55 15 00 FF E6 EE FB BE 0F 00 00 00 FC BF BB BB")

        self.log_info("Patches applied successfully!")

        return True

    def apply_tracker_patches(self):
        if not self.attached_to_process:
            self.log_error("Cannot apply tracker patches, not attached to Animal Well process!")
            return False

        if self.log_debug_info:
            self.log_info("Applying tracker patches...")

        if self.tracker_original_stamp_count is None:
            self.tracker_original_stamp_count = self.process.read_bytes(self.current_save_address + 0x225, 1)[0]
        self.apply_redirect_stamps_patch()
        self.apply_colored_stamps_patch()
        self.apply_tracker_draw_text_patch()
        self.tracker_initialized = True

        if self.log_debug_info:
            self.log_info("Tracker patches applied successfully!")

    def revert_tracker_patches(self):
        if not self.tracker_initialized or not self.revertable_tracker_patches:
            return True
        if not self.attached_to_process:
            self.log_error("Cannot revert tracker patches, not attached to Animal Well process!")
            return False

        for name,patch in self.revertable_tracker_patches.items():
            if patch.patch_applied:
                patch.revert()

        self.revertable_tracker_patches.clear()

        if self.tracker_original_stamp_count is not None:
            self.process.write_bytes(self.current_save_address + 0x225, self.tracker_original_stamp_count.to_bytes(1, "little", signed=False), 1)
            self.tracker_original_stamp_count = None

        if self.log_debug_info:
            self.log_info("Tracker patches reverted successfully!")

    def apply_main_menu_draw_patch(self):
        """
            This patch displays the text "AP Randomizer" on the title screen.
        """
        main_menu_draw_injection_address = self.module_base + 0x1f025
        self.main_menu_draw_string_addr = self.custom_memory_current_offset
        self.custom_memory_current_offset += TITLE_SCREEN_MAX_TEXT_LENGTH
        main_menu_draw_routine_address = self.custom_memory_current_offset
        main_menu_draw_trampoline = (Patch("main_menu_draw_trampoline", main_menu_draw_injection_address, self.process)
                                     .mov_to_rax(main_menu_draw_routine_address).jmp_rax().nop(3))
        title_text_x = 151  # below the right side of the ANIMAL WELL logo
        title_text_y = 74
        title_text_color = 0xff44ffff
        title_text_shader = 0x0f  # 07 and 0f are both good options, 07 shows more of the background through it (values over 0x34 will crash)
        title_text_tall_font = 0x00  # 01 to use a TALL font
        main_menu_draw_patch = (Patch("main_menu_draw_randomizer_info", main_menu_draw_routine_address, self.process)
                                .set_current_shader(0x0f)
                                .set_current_color(0xff000000)
                                .set_tall_text_mode(title_text_tall_font)
                                .draw_small_text(title_text_x - 1, title_text_y, self.main_menu_draw_string_addr)
                                .set_current_shader(title_text_shader)
                                .set_current_color(title_text_color)
                                .set_tall_text_mode(title_text_tall_font)
                                .draw_small_text(title_text_x, title_text_y, self.main_menu_draw_string_addr)
                                .set_tall_text_mode(0x0)
                                .pop_shader_from_stack()
                                .pop_color_from_stack()
                                .pop_from_position_stack()
                                .mov_to_rax(main_menu_draw_injection_address + len(main_menu_draw_trampoline.byte_list))
                                .jmp_rax())
        self.custom_memory_current_offset += len(main_menu_draw_patch) + 0x10
        self.set_title_text(TITLE_SCREEN_TEXT_TEMPLATE.replace("{version}", self.version_string or ""))
        if self.log_debug_info:
            self.log_info("Applying main menu draw patches...")
        main_menu_draw_patch.apply()
        if main_menu_draw_trampoline.apply():
            self.revertable_patches.append(main_menu_draw_trampoline)
        # endregion

    def apply_in_game_draw_patch(self):
        """
        This patch adds a text display at the top of the screen that displays messages that the AP Client receives.
        It additionally pushes the steps and time counters lower on the screen to make room for the new text display.
        This patch can also be extended in the future to display other things in-game.
        """
        game_draw_injection_address = self.module_base + 0x5068b
        self.game_draw_routine_string_addr = self.custom_memory_current_offset
        self.custom_memory_current_offset += self.game_draw_routine_string_size + 0x10

        self.draw_bottom_routine_string_size = 400
        self.game_draw_bottom_routine_string_addr = self.custom_memory_current_offset
        self.custom_memory_current_offset += self.draw_bottom_routine_string_size + 0x10

        # self.game_draw_symbol_x_address = self.custom_memory_current_offset
        # self.custom_memory_current_offset += 4
        # self.game_draw_symbol_y_address = self.custom_memory_current_offset
        # self.custom_memory_current_offset += 4
        game_draw_code_address = self.custom_memory_current_offset
        draw_trampoline_patch = (Patch("game_draw_trampoline", game_draw_injection_address, self.process)
                                 .mov_to_rax(game_draw_code_address).jmp_rax().nop())
        for offset, value in STEP_AND_TIME_DISPLAY_UPDATED_VALUES.items():
            if value is int:
                self.process.write_uint(self.module_base + offset, value)
            elif value is float:
                self.process.write_float(self.module_base + offset, value)
        client_text_display_x = 1
        client_text_display_y = 1  # lines the text up with the very top tile row
        # TODO: store the display color somewhere so we can change it appropriate to each message we show
        client_text_display_color = 0xffffaaaa  # format is aabbggrr (alpha, blue, green, red)
        # 0x29: foreground, ignore lights, color. 0x21: foreground, glowing, white. 0x1f: foreground, glowing, color. (values over 0x34 will crash)
        client_text_display_shader = 0x1f
        client_text_bottom_display_x = 1
        client_text_bottom_display_y = 171  # lines the text up with the very bottom tile row
        # TODO: store the display color somewhere so we can change it appropriate to each message we show
        client_text_bottom_display_color = 0xff43ff23  # format is aabbggrr (alpha, blue, green, red)
        # 0x29: foreground, ignore lights, color. 0x21: foreground, glowing, white. 0x1f: foreground, glowing, color. (values over 0x34 will crash)
        client_text_bottom_display_shader = 0x0f
        # draw_bean_echo_patch_enabled = False
        draw_patch = (
            Patch("game_draw_client_text", game_draw_code_address, self.process)
            .push_shader_to_stack(client_text_display_shader)
            .push_color_to_stack(0xff000000)
            .draw_small_text(client_text_display_x - 1, client_text_display_y, self.game_draw_routine_string_addr)
            .pop_color_from_stack()
            .push_color_to_stack(client_text_display_color)
            .draw_small_text(client_text_display_x, client_text_display_y, self.game_draw_routine_string_addr)
            .pop_color_from_stack()
            .pop_shader_from_stack()
            .push_shader_to_stack(client_text_bottom_display_shader)
            .push_color_to_stack(0xff000000)
            .draw_big_text(client_text_bottom_display_x - 1, client_text_bottom_display_y, self.game_draw_bottom_routine_string_addr)
            .pop_color_from_stack()
            .push_color_to_stack(client_text_bottom_display_color)
            .draw_big_text(client_text_bottom_display_x, client_text_bottom_display_y, self.game_draw_bottom_routine_string_addr))
        (draw_patch.pop_color_from_stack()
         .pop_shader_from_stack()
         .nop(0x200)
         .add_rsp(0x00000198).pop_rbx().pop_rbp().pop_rdi().pop_rsi().pop_r12()
         .mov_to_rax(game_draw_injection_address + 0xd).jmp_rax())
        self.custom_memory_current_offset += len(draw_patch) + 0x10
        default_in_game_message = self.game_draw_routine_default_string.encode("utf-16le")
        self.process.write_bytes(self.game_draw_routine_string_addr, default_in_game_message, len(default_in_game_message))
        default_bottom_in_game_message = self.game_draw_bottom_routine_default_string.encode("utf-16le")
        self.process.write_bytes(self.game_draw_bottom_routine_string_addr, default_bottom_in_game_message, len(default_bottom_in_game_message))
        self.last_message_time = time()
        if self.log_debug_info:
            self.log_info(f"Applying in-game draw patches...\n{draw_patch}")
        draw_patch.apply()
        if draw_trampoline_patch.apply():
            self.revertable_patches.append(draw_trampoline_patch)

    def apply_pause_menu_patch(self):
        """
        This set of patches updates the pause menu to have a new "Warp to hub" option.
        When selected, this option warps the bean back to the flame statue room.
        Useful for getting out of potential softlocks.
        """
        pause_menu_patch_update_option_text = (
            Patch("pause_menu_patch_update_option_text", self.custom_memory_current_offset, self.process)
            .mov_to_rsp_offset(0x50, 1)
            .mov_to_rsp_offset(0x58, 5)
            .mov_to_rsp_offset(0x60, 4)  # 0x4 is "Pre-Alpha", we'll update it with our new text
            # 0x69 -> blocked, 0x72 -> wake up, 0x73 -> locked, 0xae -> beacon, 0xb2 -> travel
            .mov_to_rax(0xc)
            .mov_rax_to_rsp_offset(0x68)
            .jmp_far(0x140043cdf)  # 84 -> control panel
            .nop(0x10))
        self.custom_memory_current_offset += len(pause_menu_patch_update_option_text)
        pause_menu_resume_and_warp_patch = (
            Patch("pause_menu_resume_and_warp_patch", self.custom_memory_current_offset, self.process)
            .mov_from_absolute_address_to_eax(self.player_address + 0x5D)  # get player state
            .cmp_eax(5)  # only allow warp while idle, walking, jumping, falling, or climbing a ladder
            .jnl_short(56)
            .warp(self.player_address, self.unstuck_room_x, self.unstuck_room_y, self.unstuck_pos_x, self.unstuck_pos_y, self.unstuck_map)
            .pop_r9().pop_r8().pop_rdx().pop_rcx()
            .mov_to_rax(self.application_state_address)
            .jmp_far(0x140044223)
            .nop(0x10))
        self.custom_memory_current_offset += len(pause_menu_resume_and_warp_patch)
        pause_menu_patch_update_option_text_trampoline = (
            Patch("pause_menu_patch_update_option_text_trampoline", 0x140043cc4, self.process)
            .jmp_far(pause_menu_patch_update_option_text.base_address)
            .nop(0xd))
        warp_to_hub_text = "warp to hub".encode("utf-16le") + b"\x00\x00"
        self.process.write_bytes(self.custom_memory_current_offset, warp_to_hub_text, len(warp_to_hub_text))
        self.process.write_bytes(0x142D93F00, self.custom_memory_current_offset.to_bytes(8, "little", signed=False), 8)
        self.custom_memory_current_offset += len(warp_to_hub_text)
        pause_menu_increase_option_count_1_patch = (
            Patch("pause_menu_increase_option_count_1_patch", 0x140043cf7, self.process)
            .add_bytes(b"\x02"))
        pause_menu_increase_option_count_2_patch = (
            Patch("pause_menu_increase_option_count_2_patch", 0x140044052, self.process)
            .add_bytes(b"\x03"))
        pause_menu_on_confirm_patch = (
            Patch("pause_menu_on_confirm_patch", self.custom_memory_current_offset, self.process)
            .call_far(0x14006ec30)
            .push_rcx().push_rdx().push_r8().push_r9()
            .mov_from_absolute_address_to_eax(self.application_state_address + 0x93610)
            .cmp_eax(2)
            .je_far(pause_menu_resume_and_warp_patch.base_address)
            .pop_r9().pop_r8().pop_rdx().pop_rcx()
            .mov_rdx(self.application_state_address)
            .cmp_ebx(0xe10)
            .jl_far(0x140044391)
            .jmp_far(0x14004435b)
            .nop(0x10))
        self.custom_memory_current_offset += len(pause_menu_on_confirm_patch)
        pause_menu_patch_on_confirm_trampoline_patch = (
            Patch("pause_menu_patch_on_confirm_trampoline_patch", 0x140044347, self.process)
            .jmp_far(pause_menu_on_confirm_patch.base_address)
            .nop(6))
        if self.log_debug_info:
            self.log_info(f"Applying pause_menu_resume_and_warp_patch..."
                          f"\n{pause_menu_resume_and_warp_patch}")
        if pause_menu_resume_and_warp_patch.apply():
            self.revertable_patches.append(pause_menu_resume_and_warp_patch)
        if self.log_debug_info:
            self.log_info(f"Applying pause_menu_patch_update_option_text..."
                          f"\n{pause_menu_patch_update_option_text}")
        if pause_menu_patch_update_option_text.apply():
            self.revertable_patches.append(pause_menu_patch_update_option_text)
        if self.log_debug_info:
            self.log_info(f"Applying pause_menu_patch_update_option_text_trampoline..."
                          f"\n{pause_menu_patch_update_option_text_trampoline}")
        if pause_menu_patch_update_option_text_trampoline.apply():
            self.revertable_patches.append(pause_menu_patch_update_option_text_trampoline)
        if self.log_debug_info:
            self.log_info(f"Applying pause_menu_increase_option_count_1_patch..."
                          f"\n{pause_menu_increase_option_count_1_patch}")
        if pause_menu_increase_option_count_1_patch.apply():
            self.revertable_patches.append(pause_menu_increase_option_count_1_patch)
        if self.log_debug_info:
            self.log_info(f"Applying pause_menu_increase_option_count_2_patch..."
                          f"\n{pause_menu_increase_option_count_2_patch}")
        if pause_menu_increase_option_count_2_patch.apply():
            self.revertable_patches.append(pause_menu_increase_option_count_2_patch)
        if self.log_debug_info:
            self.log_info(f"Applying pause_menu_on_confirm_patch..."
                          f"\n{pause_menu_on_confirm_patch}")
        if pause_menu_on_confirm_patch.apply():
            self.revertable_patches.append(pause_menu_on_confirm_patch)
        if self.log_debug_info:
            self.log_info(f"Applying pause_menu_patch_on_confirm_trampoline_patch..."
                          f"\n{pause_menu_patch_on_confirm_trampoline_patch}")
        if pause_menu_patch_on_confirm_trampoline_patch.apply():
            self.revertable_patches.append(pause_menu_patch_on_confirm_trampoline_patch)

    def apply_every_frame_patch(self):
        """
        This patch provides a place to run additional every-frame code from within the loop that runs every frame.
        Useful for reading input or triggering things when the patch sees a watched value change.
        """
        # input_reader_patch = (Patch("input_reader_patch", 0x140133c00, self.process)
        #                        .push_r15().push_r14().push_rsi().push_rdi().push_rbp().push_rbx()#.mov_to_rax(self.application_state_address + 0x93670)
        #                        .nop(0x100).pop_rbx().pop_rbp().pop_rdi().pop_rsi().pop_r14().pop_r15().mov_to_eax(0x27168).call_far(0x140104800).jmp_far(0x14003B679) #.nop(0x100)
        #                        )
        #   originalCode
        #   14003B7D1:  mov         edi,        841C
        #   14003B7D6:  movss       xmm6,       cs:dword_1420949D0
        #   14003B7DE:  movss       xmm7,       cs:dword_1420949f4
        #   14003B7E6:  movss       jmp short   loc_14003b7fd
        #   replacing with
        #               <new code>
        #               mov         rax,        [1420949d0]
        #               movq        xmm6,       rax
        #               mov         rax,        [1420949f4]
        #               movq        xmm7,       rax
        #               jmp far     14003b7fd
        # flameStatue   116/026,    740000001a, 0b0b,   0
        # bunnyStatue   136/048,    8000000030, 0c0b,   1
        # space         144/074,    800000004a, 130a,   2
        # bunnyTemple   152/222,    8a000000df, 080c,   3
        # timeCapsule   080/216,    50000000d8, 0c0b,   4 # teleports you out of world unless you set bdtp path variable
        # Relevant item Ids:
        # Unused: Stethoscope 0x14c, Cake 0x20,
        # Upgrades: FannyPack 0x30C, Stopwatch 0x19a, Pedometer 0x108, CRing 0xa1, BBWand 0x2c4,
        # Figs: MamaCha 0x32b, RabbitFig 0x332, SouvenirCup 0xe7,
        # Other: EMedal 0x2a7, SMedal 0x1d5, Pencil 0x1ba, Map 0xd6, Stamps 0x95, Normal Key 0x28, Match 0x29
        # Equipment: Top 0x27a, Ball 0x27d, Wheel 0x283, Remote 0x1d2, Slink 0x1a1, Yoyo 0x14e, UV 0x143, Bubble 0xa2, Flute 0xa9, Lantern 0x6d
        # Quest: Egg65 0x2c7, OfficeKey 0x269, QuestionKey 0x26a, MDisc 0x17e
        # Egg: 0x5a

        self.trigger_sound_id_address = self.custom_memory_current_offset
        self.custom_memory_current_offset += 0x4
        self.process.write_bytes(self.trigger_sound_id_address, b'\x00\x00\x00\x00', 4)
        frame_patch = (Patch("frame_patch", self.custom_memory_current_offset, self.process)
                              # .get_key_pressed(0x48)
                              # .cmp_al1_byte(0)
                              # .je_near(0x80)
                              # .push_rcx().push_rdx().push_r8().push_r9()
                              # .mov_from_absolute_address_to_eax(self.player_address + 0x5D)  # get player state
                              # .cmp_eax(5)  # only allow warp while idle, walking, jumping, falling, or climbing a ladder
                              # .jnl_short(56)
                              # .warp(self.player_address, self.unstuck_room_x, self.unstuck_room_y, self.unstuck_pos_x, self.unstuck_pos_y, self.unstuck_map)
                              # .get_an_item(slot_address, 0x14c, 0x00, 0xff)
                              # .pop_r9().pop_r8().pop_rdx().pop_rcx()
                              # .nop(0x80)
                              .mov_from_absolute_address_to_eax(self.trigger_sound_id_address)
                              .cmp_al1_byte(0)
                              .je_near(100)
                              # .je_near(81)
                              .mov_to_rax(self.trigger_sound_id_address)
                              .mov_rax_pointer_contents_to_rcx() # sound_id
                              .mov_rdx(1) # volume I think, but this particular sound function ignores this and always sends the same volume
                              .mov_to_rax(self.player_address)
                              .mov_rax_pointer_contents_to_r8() # position to play the sound at (we're playing it right on the bean)
                              .mov_r9(0x0) # not sure what this arg is, can't tell any obvious difference from playing around with it
                              .call_far(play_sound)

                              .mov_rbx(self.trigger_sound_id_address)
                              .mov_to_eax(0x00000000)
                              .mov_eax_to_address_in_rbx()

                              .nop(0x100)
                              # .mov_ecx(0x41)
                              # .mov_to_rax(self.player_address)
                              # .mov_rax_pointer_contents_to_rdx()
                              # .mov_r8(0x6)
                              # .mov_r9(0x0)
                              # .call_far(0x140064480)

                              .mov_edi(0x841c)
                              .mov_from_absolute_address_to_rax(0x1420949D0).movq_rax_to_xmm6()
                              .mov_from_absolute_address_to_rax(0x1420949F4).movq_rax_to_xmm7()
                              .jmp_far(0x14003B7FD)
                              )
        self.custom_memory_current_offset += len(frame_patch)
        if self.log_debug_info:
            self.log_info(f"Applying frame_patch...\n{frame_patch}")
        if frame_patch.apply():
            self.revertable_patches.append(frame_patch)
        frame_trampoline = (Patch("frame_trampoline", 0x14003B7D1, self.process)
                                   .jmp_far(frame_patch.base_address).nop(2))
        if self.log_debug_info:
            self.log_info(f"Applying frame_trampoline...\n{frame_trampoline}")
        if frame_trampoline.apply():
            self.revertable_patches.append(frame_trampoline)

        if self.log_debug_info:
            self.log_info(f"trigger_sound_id_address: {hex(self.trigger_sound_id_address)}")

    def apply_disable_anticheat_patch(self):
        """
        Disables the built-in anti-cheat that rolls back changes that occur to the player outside the frame function.
        """
        frame_anticheat_address = self.module_base + 0x6048A
        frame_anticheat_complete_address = self.module_base + 0x605B3
        disable_anticheat_patch = Patch(
            "disable_anti-cheat", frame_anticheat_address, self.process).jmp_far(frame_anticheat_complete_address)
        if self.log_debug_info:
            self.log_info(f"Disabling anti-cheat...\n{disable_anticheat_patch}")
        if disable_anticheat_patch.apply():
            self.revertable_patches.append(disable_anticheat_patch)

    def enable_room_palette_override(self, palette=0x14):
        if self.room_palette_override_patch is None:
            return

        if self.room_palette_override_patch.patch_applied:
            self.room_palette_override_patch.revert()

        self.room_palette_override_shader = palette

        if self.log_debug_info:
            self.log_info(f"Applying room palette override patch...")
        self.room_palette_override_patch.byte_list = b"\xb8" + self.room_palette_override_shader.to_bytes(4, "little") + b"\x90"
        self.room_palette_override_patch.apply()

    def disable_room_palette_override(self):
        if self.room_palette_override_patch is None or not self.room_palette_override_patch.patch_applied:
            return

        if self.log_debug_info:
            self.log_info(f"Reverting room palette override patch...")
        self.room_palette_override_patch.revert()

    def toggle_room_palette_override(self):
        if self.room_palette_override_patch is None:
            return

        if self.room_palette_override_patch.patch_applied:
            self.room_palette_override_patch.revert()
        else:
            self.room_palette_override_patch.apply()

    def generate_room_palette_override_patch(self):
        """
        Forces every room to use the specified palette. Adds a little extra visual variety to randomizer runs.
        """
        self.room_palette_override_shader = 0x14
        if self.log_debug_info:
            self.log_info("Applying room palette override patch...")
        self.room_palette_override_patch = (
            Patch("override_room_palette", self.module_base + 0x2e26, self.process)
            .mov_to_eax(self.room_palette_override_shader).nop(1))

    def apply_item_collection_patches(self):
        """
        disable_chest_item_patch disables receiving items when you open chests. This means you will no longer get
        incorrect dialog boxes or have your selected equipment change when opening a chest that normally would contain
        a piece of equipment.

        All the other patches here disable the dialog boxes that show up when you receive an item.
        Instead, you"ll still get the item like normal and have your selected equipment automatically updated,
        and you"ll still get the icon of the item over the bean"s head, making it clear what items you received
        but reducing situations where you might be performing a trick when receiving a piece of equipment from
        another player"s game.
        """
        disable_chest_item_patch = Patch("disable_chest_item", 0x1400c2871, self.process).xor_r8d_r8d().xor_edx_edx().nop(3)
        disable_item_get_dialog_patch = Patch("disable_item_get_dialog", 0x1400c2161, self.process).nop(5)
        # match, pencil, stethoscope, officeKey, stamps, pedometer, rabbitFig, mockDisc, cake, regularKey, stopwatch, sMedal, eMedal, questionKey
        disable_egg_get_dialog_patch = Patch("disable_egg_get_dialog", 0x1400c24a3, self.process).nop(5)
        disable_lantern_get_dialog_patch = Patch("disable_lantern_get_dialog", 0x1400c1c82, self.process).nop(5)
        disable_flute_get_dialog_patch = Patch("disable_flute_get_dialog", 0x1400c2241, self.process).nop(5)
        disable_bubble_get_dialog_patch = Patch("disable_bubble_get_dialog", 0x1400c21ea, self.process).nop(5)
        disable_uv_get_dialog_patch = Patch("disable_uv_get_dialog", 0x1400c1cd9, self.process).nop(5)
        disable_yoyo_get_dialog_patch = Patch("disable_yoyo_get_dialog", 0x1400c1f21, self.process).nop(5)
        disable_slink_get_dialog_patch = Patch("disable_slink_get_dialog", 0x1400c1bc0, self.process).nop(5)
        disable_remote_get_dialog_patch = Patch("disable_remote_get_dialog", 0x1400c211a, self.process).nop(5)
        disable_wheel_get_dialog_patch = Patch("disable_wheel_get_dialog", 0x1400c22c8, self.process).nop(5)
        disable_wheel_get_without_saving_cats_dialog_patch = Patch("disable_wheel_get_without_saving_cats_dialog", 0x1400c20b2, self.process).nop(5)
        disable_ball_get_dialog_patch = Patch("disable_ball_get_dialog", 0x1400c200d, self.process).nop(5)
        disable_top_get_dialog_patch = Patch("disable_top_get_dialog", 0x1400c1fb6, self.process).nop(5)
        disable_egg65_get_dialog_patch = Patch("disable_egg65_get_dialog", 0x1400c18be, self.process).nop(5)
        disable_bbwand_get_dialog_patch = Patch("disable_bbwand_get_dialog", 0x1400c1d75, self.process).nop(5)
        disable_fannypack_get_dialog_patch = Patch("disable_fannypack_get_dialog", 0x1400c1e81, self.process).nop(5)
        disable_firecracker_get_dialog_patch = Patch("disable_firecracker_get_dialog", 0x14002cb59, self.process).nop(5)
        disable_firecracker_selected_equipment_patch = Patch("disable_firecracker_selected_equipment", 0x14002caea, self.process).nop(5)
        disable_mockdisc_flags_check_patch = Patch("disable_mockdisc_flags_check", 0x1400c1003, self.process).add_bytes(bytearray([0xEB]))
        disable_sack_spawn_patch = Patch("disable_sack_spawn_patch", 0x140074710, self.process).add_bytes(bytearray([0xc3]))

        if self.log_debug_info:
            self.log_info(f"Applying disable_chest_item_patch patch...")
        if disable_chest_item_patch.apply():
            self.revertable_patches.append(disable_chest_item_patch)
        if self.log_debug_info:
            self.log_info(f"Applying disable item get dialog patches...")
        if disable_item_get_dialog_patch.apply():
            self.revertable_patches.append(disable_item_get_dialog_patch)
        if disable_egg_get_dialog_patch.apply():
            self.revertable_patches.append(disable_egg_get_dialog_patch)
        if disable_lantern_get_dialog_patch.apply():
            self.revertable_patches.append(disable_lantern_get_dialog_patch)
        if disable_flute_get_dialog_patch.apply():
            self.revertable_patches.append(disable_flute_get_dialog_patch)
        if disable_bubble_get_dialog_patch.apply():
            self.revertable_patches.append(disable_bubble_get_dialog_patch)
        if disable_uv_get_dialog_patch.apply():
            self.revertable_patches.append(disable_uv_get_dialog_patch)
        if disable_yoyo_get_dialog_patch.apply():
            self.revertable_patches.append(disable_yoyo_get_dialog_patch)
        if disable_slink_get_dialog_patch.apply():
            self.revertable_patches.append(disable_slink_get_dialog_patch)
        if disable_remote_get_dialog_patch.apply():
            self.revertable_patches.append(disable_remote_get_dialog_patch)
        if disable_wheel_get_dialog_patch.apply():
            self.revertable_patches.append(disable_wheel_get_dialog_patch)
        if disable_wheel_get_without_saving_cats_dialog_patch.apply():
            self.revertable_patches.append(disable_wheel_get_without_saving_cats_dialog_patch)
        if disable_ball_get_dialog_patch.apply():
            self.revertable_patches.append(disable_ball_get_dialog_patch)
        if disable_top_get_dialog_patch.apply():
            self.revertable_patches.append(disable_top_get_dialog_patch)
        if disable_egg65_get_dialog_patch.apply():
            self.revertable_patches.append(disable_egg65_get_dialog_patch)
        if disable_bbwand_get_dialog_patch.apply():
            self.revertable_patches.append(disable_bbwand_get_dialog_patch)
        if disable_fannypack_get_dialog_patch.apply():
            self.revertable_patches.append(disable_fannypack_get_dialog_patch)
        if disable_firecracker_get_dialog_patch.apply():
            self.revertable_patches.append(disable_firecracker_get_dialog_patch)
        if disable_firecracker_selected_equipment_patch.apply():
            self.revertable_patches.append(disable_firecracker_selected_equipment_patch)
        if disable_mockdisc_flags_check_patch.apply():
            self.revertable_patches.append(disable_mockdisc_flags_check_patch)
        if disable_sack_spawn_patch.apply():
            self.revertable_patches.append(disable_sack_spawn_patch)

    def apply_receive_item_patch(self):
        """
        Set up a piece of code that runs in the normal gameloop that checks a location in memory to see if that
        location has a value. If it does, that routine will trigger getAnItem with the provided item_id,
        position(for eggs only), and location_id.
        LocationId will default to 0xff, as negative numbers do not trigger changes to the bytes that store which
        chests have already been opened.
        After this getAnItem, that location in memory is cleared, preventing the routine from attempting to give the
        item to the player again.
        This class will keep a buffer of items to receive and will automatically only set the item byte when it is
        currently 0, this will ensure that an item is never skipped if multiple arrive at the same exact time.

        # Relevant item Ids:
        # Unused: Stethoscope 0x14c, Cake 0x20,
        # Upgrades: FannyPack 0x30C, Stopwatch 0x19a, Pedometer 0x108, CRing 0xa1, BBWand 0x2c4,
        # Figs: MamaCha 0x32b, RabbitFig 0x332, SouvenirCup 0xe7,
        # Other: EMedal 0x2a7, SMedal 0x1d5, Pencil 0x1ba, Map 0xd6, Stamps 0x95, Normal Key 0x28, Match 0x29
        # Equipment: Top 0x27a, Ball 0x27d, Wheel 0x283, Remote 0x1d2, Slink 0x1a1, Yoyo 0x14e, UV 0x143, Bubble 0xa2, Flute 0xa9, Lantern 0x6d
        # Quest: Egg65 0x2c7, OfficeKey 0x269, QuestionKey 0x26a, MDisc 0x17e
        # Egg: 0x5a
        """
        # receive_item_patch = (Patch("receive_item", self.custom_memory_current_offset, self.process)
        #                       .get_key_pressed(0x48)
        #                       .cmp_al1_byte(0)
        #                       .je_near(0x80)
        #                       .push_rcx().push_rdx().push_r8().push_r9()
        #                       .warp(self.player_address, self.unstuck_room_x, self.unstuck_room_y, self.unstuck_pos_x, self.unstuck_pos_y, self.unstuck_map)
        #                       # .get_an_item(slot_address, 0x14c, 0x00, 0xff)
        #                       .pop_r9().pop_r8().pop_rdx().pop_rcx()
        #                       .nop(0x80)
        #                       .mov_edi(0x841c)
        #                       .mov_from_absolute_address_to_rax(0x1420949D0).movq_rax_to_xmm6()
        #                       .mov_from_absolute_address_to_rax(0x1420949F4).movq_rax_to_xmm7()
        #                       .jmp_far(0x14003B7FD)
        #                       )
        # self.custom_memory_current_offset += len(receive_item_patch)
        # if self.log_debug_info: self.log_info(f"Applying input_reader_patch...\n{receive_item_patch}")
        # if receive_item_patch.apply():
        #     self.revertable_patches.append(receive_item_patch)
        # input_reader_trampoline = (Patch("input_reader_trampoline", 0x14003B7D1, self.process)
        #                            .jmp_far(receive_item_patch.base_address).nop(2))
        # if self.log_debug_info: self.log_info(f"Applying input_reader_trampoline...\n{input_reader_trampoline}")
        # if input_reader_trampoline.apply():
        #     self.revertable_patches.append(input_reader_trampoline)

    def apply_skip_credits_patch(self):
        """
        Disables the credits by NOPing out a check that checks if the credits timer is still running,
        effectively jumping to the end of the credits instantly when they start rolling.
        """
        skip_credits_address = self.module_base + 0x476D9
        skip_credits_patch = Patch(
            "skip_credits", skip_credits_address, self.process).nop(2)
        if self.log_debug_info:
            self.log_info(f"Disabling credits...\n{skip_credits_patch}")
        if skip_credits_patch.apply():
            self.revertable_patches.append(skip_credits_patch)

    def apply_redirect_stamps_patch(self):
        """
        Redirects stamps to a custom array of the in-game tracker.
        """
        if not self.tracker_initialized:
            self.tracker_stamps_addr = self.custom_memory_current_offset
            self.custom_memory_current_offset += CUSTOM_STAMPS * 6
        redirect_stamps_address = self.module_base + 0x42AEE
        redirect_stamps_patch = Patch(
            "redirect_stamps", redirect_stamps_address, self.process).mov_rdi(self.tracker_stamps_addr+4).nop(3)
        if self.log_debug_info and not self.tracker_initialized:
            self.log_info(f"Applying in-game tracker stamps patch...")
        if "stamps" not in self.revertable_tracker_patches and redirect_stamps_patch.apply():
            self.revertable_tracker_patches["stamps"] = redirect_stamps_patch

    def apply_colored_stamps_patch(self):
        """
        Reads stamp color from our custom array. Logic status is baked into high nibble of
        stamp type in our custom stamps, used to index the color array to set the color and
        then removed before handing the stamp type back to the game.
        """
        injection_address = self.module_base + 0x42ce8
        if not self.tracker_initialized:
            self.tracker_icons_addr = self.custom_memory_current_offset
            tracker_icons_patch = (
                Patch("tracker_icons", self.tracker_icons_addr, self.process)
                .add_bytes(bytearray([
                    # 4 custom colors for CheckStatus 0-3 respectively
                    0xCC, 0x00, 0x00, 0xFF, # red, unreachable
                    0xDD, 0xAA, 0x00, 0xFF, # orange, out_of_logic
                    0x00, 0xEE, 0x00, 0xFF, # green, in_logic
                    0x88, 0x88, 0xAA, 0xCC, # gray, checked

                    # 8 custom map icons for stamp ids 0-7 respectively, u16 tile id
                    0x5B, 0x00,
                    0x18, 0x00, # replace heart (0x5c) with bunny head
                    0x3E, 0x00, # replace skull (0x5d) with disc shape
                    0x25, 0x00, # replace shard (0x5e) with candle
                    0x5F, 0x00,
                    0x60, 0x00,
                    0x9D, 0x02,
                    0x9E, 0x02
                ])))
            self.custom_memory_current_offset += len(tracker_icons_patch)

            self.tracker_color_routine_addr = self.custom_memory_current_offset
            tracker_color_patch = (
                Patch("tracker_color_patch", self.tracker_color_routine_addr, self.process)
                .add_bytes(bytearray([0x41, 0x57, 0x41, 0x56, 0x41, 0x55, 0x48, 0x0F, 0xBE, 0x07, 0x49, 0xBD]))
                .add_bytes(self.tracker_icons_addr.to_bytes(8, "little"))
                .add_bytes(bytearray([0x49, 0xC7, 0xC6, 0x0F, 0x00, 0x00, 0x00, 0x49, 0xC7, 0xC7, 0xF0, 0x00, 0x00, 0x00, 0x49, 0x21, 0xC7, 0x4C, 0x21, 0xF0, 0x50, 0x49, 0xC1, 0xEF, 0x02, 0x4D, 0x01, 0xFD, 0x41, 0x8B, 0x4D, 0x00]))
                .call_via_rax(set_current_color)
                .add_bytes(bytearray([0x58, 0x41, 0x5D, 0x41, 0x5E, 0x41, 0x5F]))
                .add_bytes(bytearray([0x49, 0xBE]))
                .add_bytes((self.tracker_icons_addr+16).to_bytes(8, "little"))
                .jmp_far(self.module_base + 0x42b20)
                )
            self.custom_memory_current_offset += len(tracker_color_patch)
            tracker_icons_patch.apply()
            tracker_color_patch.apply()

        if self.log_debug_info and not self.tracker_initialized:
            self.log_info(f"Applying colored tracker stamp patches...")
        tracker_trampoline_patch = (Patch("tracker_color_trampoline", injection_address, self.process)
                                 .mov_to_rax(self.tracker_color_routine_addr).jmp_rax().nop())
        if "color" not in self.revertable_tracker_patches and tracker_trampoline_patch.apply():
            self.revertable_tracker_patches["color"] = tracker_trampoline_patch

    def apply_tracker_draw_text_patch(self):
        """
            This patch displays various tracker stats on the map screen.
        """
        checked_name = "Checked:\x00"
        in_logic_name = "In logic:\x00"
        candles_name = "Candles lit:\x00"
        goal_name = "Goal:\x00"

        checked_text = "?".ljust(7)+"\x00"
        in_logic_text = "?".ljust(7)+"\x00"
        candles_text = "?".ljust(5)+"\x00"
        goal_text = "?"+"\x00"

        tracker_text = f"{checked_name}{checked_text}{in_logic_name}{in_logic_text}{candles_name}{candles_text}{goal_name}{goal_text}".encode("utf-16le")

        offset_checked_name = 0
        offset_checked_text = offset_checked_name + len(checked_name)*2
        offset_in_logic_name = offset_checked_text + len(checked_text)*2
        offset_in_logic_text = offset_in_logic_name + len(in_logic_name)*2
        offset_candles_name = offset_in_logic_text + len(in_logic_text)*2
        offset_candles_text = offset_candles_name + len(candles_name)*2
        offset_goal_name = offset_candles_text + len(candles_text)*2
        offset_goal_text = offset_goal_name + len(goal_name)*2

        if not self.tracker_initialized:
            self.tracker_text_addr = self.custom_memory_current_offset
            self.custom_memory_current_offset += 256
            self.tracker_draw_routine_addr = self.custom_memory_current_offset

        tracker_draw_injection_address = self.module_base + 0x40d21
        tracker_draw_trampoline = (Patch("tracker_draw_trampoline", tracker_draw_injection_address, self.process)
                                     .mov_to_rax(self.tracker_draw_routine_addr).jmp_rax().nop(3))

        if not self.tracker_initialized:
            tracker_draw_text_patch = (Patch("tracker_draw_text", self.tracker_draw_routine_addr, self.process)
                                    .push_shader_to_stack(0x29)
                                    .push_color_to_stack(0xffffffff)
                                    .draw_small_text(73, 162, self.tracker_text_addr+offset_in_logic_name)
                                    .draw_small_text(103, 162, self.tracker_text_addr+offset_in_logic_text)
                                    .draw_small_text(73, 170, self.tracker_text_addr+offset_candles_name)
                                    .draw_small_text(113, 170, self.tracker_text_addr+offset_candles_text)

                                    .draw_small_text(195, 162, self.tracker_text_addr+offset_checked_name)
                                    .draw_small_text(223, 162, self.tracker_text_addr+offset_checked_text)
                                    .draw_small_text(195, 170, self.tracker_text_addr+offset_goal_name)
                                    .draw_small_text(215, 170, self.tracker_text_addr+offset_goal_text)
                                    .pop_color_from_stack()
                                    .pop_shader_from_stack()
                                    .push_color_to_stack(0x645a6e82)
                                    .mov_to_rax(tracker_draw_injection_address + len(tracker_draw_trampoline.byte_list))
                                    .jmp_rax())
            tracker_draw_text_patch.apply()
            self.custom_memory_current_offset += len(tracker_draw_text_patch) + 0x10

        self.process.write_bytes(self.tracker_text_addr, tracker_text, len(tracker_text))
        if self.log_debug_info and not self.tracker_initialized:
            self.log_info("Applying tracker draw patches...")
        if "draw" not in self.revertable_tracker_patches and tracker_draw_trampoline.apply():
            self.revertable_tracker_patches["draw"] = tracker_draw_trampoline

    def update_tracker_text(self) -> None:
        if self.tracker_text_addr is None:
            return

        checked_name = "Checked:\x00"
        in_logic_name = "In logic:\x00"
        candles_name = "Candles lit:\x00"
        goal_name = "Goal:\x00"

        checked_text = f"{self.tracker_checked}/{self.tracker_total}".ljust(7)+"\x00"
        in_logic_text = f"{self.tracker_in_logic}/{self.tracker_missing}".ljust(7)+"\x00"
        candles_text = f"{self.tracker_candles}/9".ljust(5)+"\x00"
        goal_text = self.tracker_goal+"\x00"

        tracker_text = f"{checked_name}{checked_text}{in_logic_name}{in_logic_text}{candles_name}{candles_text}{goal_name}{goal_text}".encode("utf-16le")

        self.process.write_bytes(self.tracker_text_addr, tracker_text, len(tracker_text))

    def apply_deathlink_patch(self):
        """
        Sends a deathlink message when the bean is killed (by another that isn't deathlink)

        Original code:
        0x14003BA8A 48 89 F1                                mov     rcx, rsi                  ; player
        0x14003BA8D B2 05                                   mov     dl, 5                     ; newPlayerState
        0x14003BA8F 49 89 F8                                mov     r8, rdi                   ; save
        0x14003BA92 E8 59 A8 02 00                          call    updatePlayerState
        """
        bean_died_address = self.module_base + 0x3BA8A

        self.bean_has_died_address = self.custom_memory_current_offset

        if self.log_debug_info:
            self.log_info(f"bean_has_died_address: {hex(self.bean_has_died_address)}")

        self.custom_memory_current_offset += 1

        bean_died_routine_address = self.custom_memory_current_offset

        bean_died_trampoline = (Patch("bean_died_trampoline", bean_died_address, self.process)
                           .mov_to_rax(bean_died_routine_address)
                           .jmp_rax()
                           )

        bean_died_routine = (Patch("bean_died_routine", bean_died_routine_address, self.process)
                             .mov_to_al(1)
                             .mov_rbx(self.bean_has_died_address)
                             .mov_al_to_address_in_rbx()
                             .update_player_state(self.player_address, 5, self.current_save_address)
                             .jmp_far(self.module_base + 0x3BA97)
                             )

        self.custom_memory_current_offset += len(bean_died_routine)

        if self.log_debug_info:
            self.log_info(f"Applying deathlink patch...\n{bean_died_routine}")

        if bean_died_routine.apply():
            self.revertable_patches.append(bean_died_routine)

        if bean_died_trampoline.apply():
            self.revertable_patches.append(bean_died_trampoline)

    def enable_fullbright(self) -> None:
        if self.fullbright_patch is None or self.fullbright_patch.patch_applied:
            return None

        if self.log_debug_info:
            self.log_info(f"Applying fullbright patch...")
        self.fullbright_patch.apply()

    def disable_fullbright(self) -> None:
        if self.fullbright_patch is None or not self.fullbright_patch.patch_applied:
            return None

        if self.log_debug_info:
            self.log_info(f"Reverting fullbright patch...")
        self.fullbright_patch.revert()

    def toggle_fullbright(self) -> None:
        if self.fullbright_patch is None:
            return None

        if self.fullbright_patch.patch_applied:
            self.fullbright_patch.revert()
        else:
            self.fullbright_patch.apply()

    def generate_fullbright_patch(self):
        """
        This patch disables darkness in the game, causing all rooms to be equally lit across all tiles.
        Mostly useful for debugging.
        """
        self.fullbright_patch = Patch("fullbright", 0x140102e63, self.process).add_bytes(b"\xeb\x19")

    def revert_patches(self):
        if not self.attached_to_process:
            self.log_error("Cannot revert patches, not attached to Animal Well process!")
            return False

        if self.log_debug_info:
            self.log_info("Reverting patches...")

        self.log_info("Reverting any patches that we can...")
        for patch in self.revertable_patches:
            if patch.patch_applied:
                patch.revert()

        self.revertable_patches = []
        self.fullbright_patch = None
        self.room_palette_override_patch = None

        for offset, value in STEP_AND_TIME_DISPLAY_ORIGINAL_VALUES.items():
            if value is int:
                self.process.write_uint(self.module_base + offset, value)
            elif value is float:
                self.process.write_float(self.module_base + offset, value)

        self.custom_memory_base = None  # TODO: Free this memory back when we're unhooking from AW
        self.custom_memory_current_offset = None

        self.log_info("Patches reverted successfully!")

    def read_from_game(self):
        if not self.attached_to_process:
            return

        self.current_frame = self.process.read_uint(self.application_state_address + 0x9360c)
        if self.current_frame != self.last_frame:
            while len(self.player_position_history) >= 60:
                self.player_position_history.pop(0)

            player_x_pos = int(self.process.read_float(self.application_state_address + 0x93670))  # 92e70
            player_y_pos = int(self.process.read_float(self.application_state_address + 0x93674))  # 92e74
            self.player_position_history.append((player_x_pos, player_y_pos))
        self.last_frame = self.current_frame

    def write_to_game(self):
        if not self.attached_to_process:
            return

        if (self.game_draw_symbol_x_address is not None
                and self.game_draw_symbol_y_address is not None
                and len(self.player_position_history) > 0):
            self.process.write_uint(self.game_draw_symbol_x_address, self.player_position_history[0][0])
            self.process.write_uint(self.game_draw_symbol_y_address, self.player_position_history[0][1])

    async def tick(self):
        if self.last_message_time != 0 and not self.cmd_prompt:
            if time() - self.last_message_time >= self.message_timeout:
                self.display_to_client("")
        elif self.cmd_prompt and self.game_draw_routine_string_addr is not None:
            text = "\n".join(self.cmd_messages)
            new_string_buffer = f"{text}".encode("utf-16le") + b"\x00\x00"
            self.process.write_bytes(self.game_draw_routine_string_addr, new_string_buffer, len(new_string_buffer))
            self.last_message_time = time()-self.message_timeout

        if self.bean_has_died_address != 0:
            if self.process.read_bool(self.bean_has_died_address):
                self.process.write_bool(self.bean_has_died_address, False)
                if self.on_bean_death_function is not None:
                    await self.on_bean_death_function()

    def key_pressed(self, key):
        if self.cmd_keys is None or self.cmd_keys_old is None:
            return False
        return self.cmd_keys[key] and not self.cmd_keys_old[key]

    def key_down(self, key):
        if self.cmd_keys is None:
            return False
        return self.cmd_keys[key]

    def run_cmd_prompt(self):
        if win32gui.GetWindowText(win32gui.GetForegroundWindow()) != "ANIMAL WELL":
            return
        self.cmd_keys = []
        for key in range(0xff):
            self.cmd_keys.append(win32api.GetAsyncKeyState(key) != 0)
        self.update_cmd_prompt()
        self.cmd_keys_old = self.cmd_keys

    def update_cmd_prompt(self):
        if not self.cmd_prompt:
            if self.process.read_bytes(self.application_state_address + 0x93644, 1)[0] in (0, 8):
                if self.key_pressed(0xc0):
                    self.cmd_keymap = 0
                    self.cmd_prompt = True
                elif self.key_pressed(0xdc):
                    self.cmd_keymap = 1
                    self.cmd_prompt = True

        if self.cmd_prompt:
            if not self.cmd_patch:
                self.cmd = ""
                self.display_to_client_bottom(f"> {self.cmd}")
                self.process.write_bytes(self.application_state_address + 0x93608, b'\x01', 1)
                self.cmd_patch.append(Patch("block_keyboard", self.module_base + 0x11c82, self.process, True).nop(2))
                for patch in self.cmd_patch:
                    patch.apply()
            else:
                if self.key_pressed(0xd): # enter
                    if not self.key_down(0x11): # ctrl+enter to leave console open on send
                        for patch in self.cmd_patch:
                            patch.revert()
                        self.cmd_patch.clear()
                        self.cmd_prompt = False
                        self.display_to_client_bottom("")
                        if self.process.read_bytes(self.application_state_address + 0x93644, 1)[0] == 0:  # don't disable pause if game is actually paused
                            self.process.write_bytes(self.application_state_address + 0x93608, b'\x00', 1)
                    self.cmd_ready = True
                    return
                elif self.key_pressed(0x1b) or self.key_pressed(0xc0) or self.key_pressed(0xdc) or not self.process.read_bytes(self.application_state_address + 0x93608, 1)[0]: # esc, console keys
                    for patch in self.cmd_patch:
                        patch.revert()
                    self.cmd_patch.clear()
                    self.cmd_prompt = False
                    self.cmd = ""
                    self.display_to_client_bottom("")
                    if self.process.read_bytes(self.application_state_address + 0x93644, 1)[0] == 0: # don't disable pause if game is actually paused
                        self.process.write_bytes(self.application_state_address + 0x93608, b'\x00', 1)
                    return
                elif self.key_pressed(0x8): # backspace
                    self.cmd = self.cmd[:-1]
                else:
                    for key in range(0x08, 0xff):
                        if self.key_pressed(key):
                            mod = self.key_down(0x10)
                            if self.key_down(0x12):
                                mod = 2
                            if chr(key) in string.ascii_uppercase:
                                if not self.key_down(0x10):
                                    key += 0x20
                                self.cmd += chr(key)
                            elif key in keymap[self.cmd_keymap] and len(keymap[self.cmd_keymap][key]) > mod:
                                char = keymap[self.cmd_keymap][key][mod]
                                self.cmd += char
                self.cmd = self.cmd[:100]
                self.display_to_client_bottom(f"> {self.cmd}" + ("|" if (time() % 1 < 0.5) else ""))

    def get_cmd(self):
        self.run_cmd_prompt()
        if self.cmd_ready:
            self.cmd_ready = False
            cmd = self.cmd.strip()
            self.cmd = ""
            if cmd:
                return cmd
        return None

    def display_dialog(self, text: str, title: str = "", action_text: str = ""):
        try:
            if self.process is not None and self.application_state_address is not None:
                text = f"{text:.255}".encode("utf-16le") + b"\x00\x00"
                title = f"{title:.15}".encode("utf-16le") + b"\x00\x00"
                action_text = f"{action_text:.15}".encode("utf-16le") + b"\x00\x00"
                self.process.write_bytes(self.application_state_address + 0xA84B8, text, len(text))
                self.process.write_bytes(self.application_state_address + 0xA84B8 + 0x200, title, len(title))
                self.process.write_bytes(self.application_state_address + 0xA84B8 + 0x240, action_text, len(action_text))
                self.process.write_bytes(self.application_state_address + 0xA84B8 + 0x4a0, b"\x00", 1)
                self.process.write_bytes(self.application_state_address + 0xA84B4, b"\x01", 1)
        except Exception as e:
            self.log_error(f"Error while attempting to trigger dialog box on client: {e}")

    def display_to_client(self, text: str):
        try:
            text = f"{str(text):.120}"
            if text != "":
                self.cmd_messages.append(text)
                if len(self.cmd_messages) > MESSAGE_QUEUE_LENGTH:
                    self.cmd_messages = self.cmd_messages[1:]

            if self.game_draw_routine_string_addr is not None and not self.cmd_prompt:
                new_string_buffer = text.encode("utf-16le") + b"\x00\x00"
                self.process.write_bytes(self.game_draw_routine_string_addr, new_string_buffer, len(new_string_buffer))
                if text != "":
                    self.last_message_time = time()
                else:
                    self.last_message_time = 0
        except Exception as e:
            self.log_error(f"Error while attempting to display text to client: {e}")

    def display_to_client_bottom(self, text: str):
        try:
            text = str(text)

            if self.game_draw_bottom_routine_string_addr is not None:
                new_string_buffer = f"{text:.120}".encode("utf-16le") + b"\x00\x00"
                self.process.write_bytes(self.game_draw_bottom_routine_string_addr, new_string_buffer, len(new_string_buffer))

        except Exception as e:
            self.log_error(f"Error while attempting to display bottom text to client: {e}")

    def set_player_state(self, state: int):
        try:
            if self.attached_to_process and self.application_state_address:
                self.process.write_uchar(self.player_address + 0x5d, state)
        except Exception as e:
            self.log_error(f"Error while attempting to set player state: {e}")

    def play_sound(self, sound: int):
        try:
            if self.attached_to_process and self.trigger_sound_id_address:
                self.process.write_uint(self.trigger_sound_id_address, sound)
        except Exception as e:
            self.log_error(f"Error while attempting to set player state: {e}")

    def set_title_text(self, text: str):
        try:
            if not self.attached_to_process or self.main_menu_draw_string_addr is None:
                return

            new_text_bytes = text[0:TITLE_SCREEN_MAX_TEXT_LENGTH-2].encode("utf-16le") + b"\x00\x00"
            self.process.write_bytes(self.main_menu_draw_string_addr, new_text_bytes, len(new_text_bytes))
            self.process.read_string(self.main_menu_draw_string_addr, TITLE_SCREEN_MAX_TEXT_LENGTH, encoding="utf-16le")
        except Exception as e:
            self.log_error(f"Error while attempting to update title screen text: {e}")
