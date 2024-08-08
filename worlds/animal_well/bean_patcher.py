from time import time

from typing import List

from .patch import *

# Extending the Patch class with some Animal Well specific methods
class Patch(Patch):
    def push_shader_to_stack(self, shaderId):
        """
        Pushes a new shader to the shader stack
        """
        return self.mov_ecx(shaderId).call_via_rax(push_shader_to_stack)

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

    def set_current_shader(self, shaderId):
        """
        Sets the shader on the top of the stack
        shaderId: which shader to switch to
        """
        return self.mov_ecx(shaderId).call_via_rax(set_current_shader)

    def set_current_color(self, color):
        """
        Sets the color on the top of the stack
        colo: new color in the format #AABBGGRR
        """
        return self.mov_ecx(color).call_via_rax(set_current_color)

    def draw_small_text(self, x, y, textAddress):
        """
        Draw text on the screen using the current shader, color, and tall text mode
        x: x position
        y: y position
        textAddress: location in the process's memory where the Unicode text is stored
        """
        return self.mov_ecx(x).mov_edx(y).mov_to_rax(textAddress).mov_rax_to_r8().call_via_rax(draw_small_text)

    def draw_symbol(self, x, y, spriteId, frame, arg5, arg6, arg7):
        """
        Draw a symbol on the screen using the current shader and color
        x: x position
        y: y position
        spriteId: id of the sprite to draw
        frame: either which frame of an animation to display or which subsprite
        arg5: idk
        arg6: idk
        arg7: idk
        """
        return self.mov_ecx(x).mov_edx(y).mov_r8(spriteId).mov_r9(frame).push(0).push(arg7).push(arg6).push(arg5).push(0).push(0).push(0).push(0).call_far(draw_symbol).add_rsp(0x40)

    def draw_symbol_pointer_x_and_y(self, xAddress, yAddress, spriteId, frame, arg5, arg6, arg7):
        """
        Draw a symbol on the screen using the current shader and color, at a location stored in the process's memory
        xAddress: the address in the process's memory where the x position is stored
        yAddress: the address in the process's memory where the y position is stored
        spriteId: id of the sprite to draw
        frame: either which frame of an animation to display or which subsprite
        arg5: idk
        arg6: idk
        arg7: idk
        """
        return (self.mov_to_rax(xAddress).mov_rax_pointer_contents_to_rcx().mov_to_rax(yAddress).mov_rax_pointer_contents_to_rdx()
                .mov_r8(spriteId).mov_r9(frame).push(0).push(arg7).push(arg6).push(arg5).push(0).push(0).push(0).push(0).call_far(draw_symbol).add_rsp(0x40))

    def warp(self, player, roomX, roomY, tileX, tileY, map):
        """
        Warps the player to a specific room and tile
        player: pointer to the player in the process's memory
        roomX: the X coordinate of the room to warp to
        roomY: the Y coordinate of the room to warp to
        tileX: the X coordinate of the tile to warp the player to
        tileY: the Y coordinate of the tile to warp the player to
        map: which map to warp to
        """
        return (self.mov_rcx(player)
                .mov_rdx((roomY << 32) + roomX)
                .mov_r8((tileY << 32) + tileX)
                .mov_r9(map)
                .call_far(warp))

    def get_key_pressed(self, key):
        return (self
                .mov_ecx(key)
                .call_far(get_key_pressed))

    def get_an_item(self, save_slot_address, itemId, eggPosition = 0, locationId = 0xff):
        return (self
                .mov_rcx(save_slot_address)
                .mov_rdx(itemId)
                .mov_r8(eggPosition)
                .mov_r9(locationId)
                .call_far(get_an_item))

    def get_sprite(self, spriteId):
        """
        Retrieves a sprite based on its spriteId
        """
        return self.mov_cl(spriteId).call_via_rax(get_sprite)

# region FunctionOffsets
# Accurate as of AW file version 1.0.0.18
draw_small_text: int             = 0x14006E3F0
draw_symbol: int                 = 0x14006A6C0
draw_sprite: int                 = 0x14001AEC0
get_sprite: int                  = 0x140063CA0
push_shader_to_stack: int        = 0x140017840
pop_shader_from_stack: int       = 0x1400178A0
push_color_to_stack: int         = 0x1400177D0
pop_color_from_stack: int        = 0x140017830
pop_from_position_stack: int     = 0x140017920
set_tall_text_mode: int          = 0x14006DC00
set_current_color: int           = 0x1400177B0
set_current_shader: int          = 0x14001A280
get_key_pressed: int             = 0x140011C70
get_gamepad_button_pressed: int  = 0x140011EA0
get_an_item: int                 = 0x1400C15C0
warp: int                        = 0x140074DD0
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
CUSTOM_MEMORY_SIZE = 0x20000
# endregion

class Bean_Patcher:
    def set_logger(self, logger):
        self.logger = logger
        return self

    def set_process(self, process):
        self.process = process
        return self

    def set_name(self, name):
        self.name = name
        return self

    def log_info(self, text):
        if self.logger != None:
            self.logger.info(text)
        return self

    def log_error(self, text):
        if self.logger != None:
            self.logger.error(text)
        return self

    def __init__(self, process=None, logger=None):
        self.process = process
        self.attached_to_process = False

        self.logger = logger
        self.log_debug_info = True

        self.module_base = 0
        self.application_state_address = 0
        self.last_game_state = 0
        self.custom_memory_base = None
        self.custom_memory_current_offset = None

        self.revertable_patches: List[Patch]  = []
        self.fullbright_patch: Patch = None
        self.room_palette_override_patch: Patch = None
        self.room_palette_override_shader: int = 0x16

        self.game_draw_routine_string_addr = None
        self.game_draw_routine_string_size = 256
        self.game_draw_routine_default_string = 'Connected to the Well'

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

    def get_current_save_slot(self):
        if not self.attached_to_process:
            self.log_error("Can't get current save slot without being attached to a process.")
            return None
        if self.application_state_address is None or self.application_state_address == 0:
            self.log_error("Can't get current save slot without knowing the application state's address.")
            return None

        return self.process.read_uchar(self.application_state_address + 0x40C)

    def get_current_save_address(self):
        current_save_slot = self.get_current_save_slot()

        if current_save_slot is None:
            self.log_error("Failed to get the current save slot.")
            return None

        return self.application_state_address + 0x400 + HEADER_LENGTH + (SAVE_SLOT_LENGTH * current_save_slot)

    def attach_to_process(self, process=None):
        if process != None:
            self.process = process

        if process == None:
            self.log_error('No process handle provided. Cannot attach to process!')
            self.attached_to_process = False
            return False

        if self.log_debug_info: self.log_info("Searching for 'Animal Well.exe' module in process memory...")
        self.aw_module = next(f for f in list(self.process.list_modules()) if f.name.startswith("Animal Well.exe"))

        if self.aw_module == None:
            self.log_error(f'Failed to find Animal Well module within the Animal Well process!')
            self.attached_to_process = False
            return

        if self.log_debug_info: self.log_info(f'Found it: Name({self.aw_module.name}), BaseOfDll({hex(self.aw_module.lpBaseOfDll)})')

        self.module_base = self.aw_module.lpBaseOfDll

        application_state_pointer_address = self.module_base + 0x02BD5308
        if self.log_debug_info: self.log_info(f'Attempting to find start address via pointer at {hex(application_state_pointer_address)}')

        self.application_state_address = self.process.read_uint(application_state_pointer_address)
        if self.log_debug_info: self.log_info(f'application_state address: {hex(self.application_state_address)}')

        self.application_state_address = self.application_state_address
        self.attached_to_process = True

        return True

    def apply_patches(self):
        if not self.attached_to_process:
            self.log_error('Cannot apply patches, not attached to Animal Well process!')
            return False

        if self.log_debug_info: self.log_info('Applying patches...')

        self.custom_memory_base = self.process.allocate(CUSTOM_MEMORY_SIZE)
        self.custom_memory_current_offset = self.custom_memory_base

        if self.log_debug_info: self.log_info(f'Custom memory space: {hex(self.custom_memory_base)}, length of {hex(CUSTOM_MEMORY_SIZE)}')

        self.apply_main_menu_draw_patch()

        self.apply_in_game_draw_patch()

        self.apply_disable_anticheat_patch()

        if self.log_debug_info: self.log_info('Misc patches...')

        self.generate_room_palette_override_patch()

        # self.apply_input_reader_patch()

        self.apply_pause_menu_patch()

        self.generate_fullbright_patch()

        self.apply_item_collection_patches()

        self.apply_receive_item_patch()

        # mural bytes at slot + 0x26eaf
        # default mural bytes at 0x142094600
        # solved bunny bytes = bytearray.fromhex('37 00 00 00 40 01 05 00 00 00 0C 00 40 00 40 46 05 0C 18 09 08 01 90 31 40 46 05 37 F4 07 48 04 40 0E 40 19 01 0C F0 03 32 09 00 02 00 59 00 18 F4 07 02 48 00 02 00 54 05 44 98 09 02 98 01 08 00 55 14 10 80 00 0E 42 00 58 05 15 52 20 8C 00 32 82 00 55 55 55 50 82 8C 08 82 80 40 55 55 55 55 81 88 32 88 80 50 55 55 55 55 81 88 C0 88 80 54 55 55 55 55 20 20 88 88 20 54 55 55 55 15 20 20 20 8C 23 54 55 55 55 E5 EF 23 2C EF FE 56 55 55 55 E5 FF EF EF BE FD 56 55 55 55 E5 FF FF BB 7B F6 54 55 55 55 01 FC E7 EE EF F9 50 55 55 55 00 F0 99 BB BE EF 43 55 55 15 00 FF E6 EE FB BE 0F 00 00 00 FC BF BB BB')

        self.log_info('Patches applied successfully!')
        
        return True

    def apply_main_menu_draw_patch(self):
        """
            This patch displays the text "AP Randomizer" on the title screen.
        """
        title_screen_text = 'AP Randomizer'.encode('utf-16le') + b'\x00'
        main_menu_draw_injection_address = self.module_base + 0x1f025
        self.main_menu_draw_string_addr = self.custom_memory_current_offset
        self.custom_memory_current_offset += len(title_screen_text)
        main_menu_draw_routine_address = self.custom_memory_current_offset
        main_menu_draw_trampoline = (Patch('main_menu_draw_trampoline', main_menu_draw_injection_address, self.process)
                                     .mov_to_rax(main_menu_draw_routine_address).jmp_rax().nop(3))
        title_text_x = 190  # below the right side of the ANIMAL WELL logo
        title_text_y = 74
        title_text_color = 0xff44ffff
        title_text_shader = 0x0f  # 07 and 0f are both good options, 07 shows more of the background through it (values over 0x34 will crash)
        title_text_tall_font = 0x00  # 01 to use a TALL font
        main_menu_draw_patch = (Patch('main_menu_draw_randomizer_info', main_menu_draw_routine_address, self.process)
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
                                .mov_to_rax(main_menu_draw_injection_address + len(main_menu_draw_trampoline.byte_list)).jmp_rax())
        self.custom_memory_current_offset += len(main_menu_draw_patch) + 0x10
        self.process.write_bytes(self.main_menu_draw_string_addr, title_screen_text, len(title_screen_text))
        if self.log_debug_info: self.log_info('Applying main menu draw patches...')
        main_menu_draw_patch.apply()
        if main_menu_draw_trampoline.apply():
            self.revertable_patches.append(main_menu_draw_trampoline)
        # endregion

    def apply_in_game_draw_patch(self):
        """
        This patch adds a text display at the top of the screen that displays messages that the AP Client receives. It additionally pushes the steps and time counters
        lower on the screen to make room for the new text display. This patch can also be extended in the future to display other things in-game.
        """
        self.draw_routine_string_size = 400
        game_draw_injection_address = self.module_base + 0x5068b
        self.game_draw_routine_string_addr = self.custom_memory_current_offset
        self.custom_memory_current_offset += self.draw_routine_string_size + 0x10
        # self.game_draw_symbol_x_address = self.custom_memory_current_offset
        # self.custom_memory_current_offset += 4
        # self.game_draw_symbol_y_address = self.custom_memory_current_offset
        # self.custom_memory_current_offset += 4
        game_draw_code_address = self.custom_memory_current_offset
        draw_trampoline_patch = (Patch('game_draw_trampoline', game_draw_injection_address, self.process)
                                 .mov_to_rax(game_draw_code_address).jmp_rax().nop())
        for offset, value in STEP_AND_TIME_DISPLAY_UPDATED_VALUES.items():
            if type(value) == int:
                self.process.write_uint(self.module_base + offset, value)
            elif type(value) == float:
                self.process.write_float(self.module_base + offset, value)
        client_text_display_x = 1
        client_text_display_y = 1  # lines the text up with the very top tile row
        # TODO: store the display color somewhere so we can change it appropriate to each message we show
        client_text_display_color = 0xffffaaaa  # format is aabbggrr (alpha, blue, green, red)
        # 0x29: foreground, ignore lights, color. 0x21: foreground, glowing, white. 0x1f: foreground, glowing, color. (values over 0x34 will crash)
        client_text_display_shader = 0x1f
        # draw_bean_echo_patch_enabled = False
        draw_patch = (Patch('game_draw_client_text', game_draw_code_address, self.process)
                      .push_shader_to_stack(client_text_display_shader)
                      .push_color_to_stack(0xff000000)
                      .draw_small_text(client_text_display_x - 1, client_text_display_y, self.game_draw_routine_string_addr)
                      .pop_color_from_stack()
                      .push_color_to_stack(client_text_display_color)
                      .draw_small_text(client_text_display_x, client_text_display_y, self.game_draw_routine_string_addr))
        (draw_patch.pop_color_from_stack()
         .pop_shader_from_stack()
         .nop(0x200)
         .add_rsp(0x00000198).pop_rbx().pop_rbp().pop_rdi().pop_rsi().pop_r12()
         .mov_to_rax(game_draw_injection_address + 0xd).jmp_rax())
        self.custom_memory_current_offset += len(draw_patch) + 0x10
        default_in_game_message = self.game_draw_routine_default_string.encode('utf-16le')
        self.process.write_bytes(self.game_draw_routine_string_addr, default_in_game_message, len(default_in_game_message))
        self.last_message_time = time()
        if self.log_debug_info: self.log_info(f'Applying in-game draw patches...\n{draw_patch}')
        draw_patch.apply()
        if draw_trampoline_patch.apply():
            self.revertable_patches.append(draw_trampoline_patch)

    def apply_pause_menu_patch(self):
        """
        This set of patches updates the pause menu to have a new "Warp to hub" option. When selected, this option warps the bean back to the flame statue room.
        Useful for getting out of potential softlocks.
        """
        pause_menu_patch_update_option_text = (Patch('pause_menu_patch_update_option_text', self.custom_memory_current_offset, self.process)
                                               .mov_to_rsp_offset(0x50, 1)
                                               .mov_to_rsp_offset(0x58, 5)
                                               .mov_to_rsp_offset(0x60, 4)  # 0x4 is "Pre-Alpha", we'll update it with our new text
                                               # 0x69 -> blocked, 0x72 -> wake up, 0x73 -> locked, 0xae -> beacon, 0xb2 -> travel
                                               .mov_to_rax(0xc)
                                               .mov_rax_to_rsp_offset(0x68)
                                               .jmp_far(0x140043cdf)  # 84 -> control panel
                                               .nop(0x10))
        self.custom_memory_current_offset += len(pause_menu_patch_update_option_text)
        pause_menu_resume_and_warp_patch = (Patch('pause_menu_resume_and_warp_patch', self.custom_memory_current_offset, self.process)
                                            .warp(self.application_state_address + 0x93670, self.unstuck_room_x, self.unstuck_room_y, self.unstuck_pos_x, self.unstuck_pos_y, self.unstuck_map)
                                            .pop_r9().pop_r8().pop_rdx().pop_rcx()
                                            .mov_to_rax(self.application_state_address)
                                            .jmp_far(0x140044223)
                                            .nop(0x10))
        self.custom_memory_current_offset += len(pause_menu_resume_and_warp_patch)
        pause_menu_patch_update_option_text_trampoline = (Patch('pause_menu_patch_update_option_text_trampoline', 0x140043cc4, self.process)
                                                          .jmp_far(pause_menu_patch_update_option_text.base_address)
                                                          .nop(0xd))
        warp_to_hub_text = 'warp to hub'.encode('utf-16le') + b'\x00\x00'
        self.process.write_bytes(self.custom_memory_current_offset, warp_to_hub_text, len(warp_to_hub_text))
        self.process.write_bytes(0x142D93F00, self.custom_memory_current_offset.to_bytes(8, 'little', signed=False), 8)
        self.custom_memory_current_offset += len(warp_to_hub_text)
        pause_menu_increase_option_count_1_patch = (Patch('pause_menu_increase_option_count_1_patch', 0x140043cf7, self.process)
                                                    .add_bytes(b'\x02'))
        pause_menu_increase_option_count_2_patch = (Patch('pause_menu_increase_option_count_2_patch', 0x140044052, self.process)
                                                    .add_bytes(b'\x03'))
        pause_menu_on_confirm_patch = (Patch('pause_menu_on_confirm_patch', self.custom_memory_current_offset, self.process)
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
                                       .nop(0x10)
                                       )
        self.custom_memory_current_offset += len(pause_menu_on_confirm_patch)
        pause_menu_patch_on_confirm_trampoline_patch = (Patch('pause_menu_patch_on_confirm_trampoline_patch', 0x140044347, self.process)
                                                        .jmp_far(pause_menu_on_confirm_patch.base_address)
                                                        .nop(6)
                                                        )
        if self.log_debug_info: self.log_info(f'Applying pause_menu_resume_and_warp_patch...\n{pause_menu_resume_and_warp_patch}')
        if pause_menu_resume_and_warp_patch.apply():
            self.revertable_patches.append(pause_menu_resume_and_warp_patch)
        if self.log_debug_info: self.log_info(f'Applying pause_menu_patch_update_option_text...\n{pause_menu_patch_update_option_text}')
        if pause_menu_patch_update_option_text.apply():
            self.revertable_patches.append(pause_menu_patch_update_option_text)
        if self.log_debug_info: self.log_info(f'Applying pause_menu_patch_update_option_text_trampoline...\n{pause_menu_patch_update_option_text_trampoline}')
        if pause_menu_patch_update_option_text_trampoline.apply():
            self.revertable_patches.append(pause_menu_patch_update_option_text_trampoline)
        if self.log_debug_info: self.log_info(f'Applying pause_menu_increase_option_count_1_patch...\n{pause_menu_increase_option_count_1_patch}')
        if pause_menu_increase_option_count_1_patch.apply():
            self.revertable_patches.append(pause_menu_increase_option_count_1_patch)
        if self.log_debug_info: self.log_info(f'Applying pause_menu_increase_option_count_2_patch...\n{pause_menu_increase_option_count_2_patch}')
        if pause_menu_increase_option_count_2_patch.apply():
            self.revertable_patches.append(pause_menu_increase_option_count_2_patch)
        if self.log_debug_info: self.log_info(f'Applying pause_menu_on_confirm_patch...\n{pause_menu_on_confirm_patch}')
        if pause_menu_on_confirm_patch.apply():
            self.revertable_patches.append(pause_menu_on_confirm_patch)
        if self.log_debug_info: self.log_info(f'Applying pause_menu_patch_on_confirm_trampoline_patch...\n{pause_menu_patch_on_confirm_trampoline_patch}')
        if pause_menu_patch_on_confirm_trampoline_patch.apply():
            self.revertable_patches.append(pause_menu_patch_on_confirm_trampoline_patch)

    def apply_input_reader_patch(self):
        """
        This patch enables watching for additional input beyond just the default controls and triggers functions when the expected button is pressed.
        Originally used as a Warp To Hub command before the Pause Menu patch was implemented.
        """
        # input_reader_patch = (Patch('input_reader_patch', 0x140133c00, self.process)
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
        input_reader_patch = (Patch('input_reader_patch', self.custom_memory_current_offset, self.process)
                              .get_key_pressed(0x48)
                              .cmp_al1_byte(0)
                              .je_near(0x80)
                              .push_rcx().push_rdx().push_r8().push_r9()
                              .warp(self.application_state_address + 0x93670, self.unstuck_room_x, self.unstuck_room_y, self.unstuck_pos_x, self.unstuck_pos_y, self.unstuck_map)
                              # .get_an_item(slot_address, 0x14c, 0x00, 0xff)
                              .pop_r9().pop_r8().pop_rdx().pop_rcx()
                              .nop(0x80)
                              .mov_edi(0x841c)
                              .mov_from_absolute_address_to_rax(0x1420949D0).movq_rax_to_xmm6()
                              .mov_from_absolute_address_to_rax(0x1420949F4).movq_rax_to_xmm7()
                              .jmp_far(0x14003B7FD)
                              )
        self.custom_memory_current_offset += len(input_reader_patch)
        if self.log_debug_info: self.log_info(f'Applying input_reader_patch...\n{input_reader_patch}')
        if input_reader_patch.apply():
            self.revertable_patches.append(input_reader_patch)
        input_reader_trampoline = (Patch('input_reader_trampoline', 0x14003B7D1, self.process)
                                   .jmp_far(input_reader_patch.base_address).nop(2))
        if self.log_debug_info: self.log_info(f'Applying input_reader_trampoline...\n{input_reader_trampoline}')
        if input_reader_trampoline.apply():
            self.revertable_patches.append(input_reader_trampoline)

    def apply_disable_anticheat_patch(self):
        """
        Disables the built-in anti-cheat that rolls back changes that occur to the player outside of the 'frame' function.
        """
        frame_anticheat_address = self.module_base + 0x6048A
        frame_anticheat_complete_address = self.module_base + 0x605B3
        disable_anticheat_patch = Patch('disable_anti-cheat', frame_anticheat_address, self.process).jmp_far(frame_anticheat_complete_address)
        if self.log_debug_info: self.log_info(f'Disabling anti-cheat...\n{disable_anticheat_patch}')
        if disable_anticheat_patch.apply():
            self.revertable_patches.append(disable_anticheat_patch)

    def enable_room_palette_override(self, palette = 0x14):
        if self.room_palette_override_patch is None:
            return

        if self.room_palette_override_patch.patch_applied:
            self.room_palette_override_patch.revert()

        self.room_palette_override_shader = palette

        if self.log_debug_info: self.log_info(f'Applying room palette override patch...')
        self.room_palette_override_patch.byte_list = b'\xb8' + self.room_palette_override_shader.to_bytes(4, 'little') + b'\x90'
        self.room_palette_override_patch.apply()

    def disable_room_palette_override(self):
        if self.room_palette_override_patch is None or not self.room_palette_override_patch.patch_applied:
            return

        if self.log_debug_info: self.log_info(f'Reverting room palette override patch...')
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
        if self.log_debug_info: self.log_info('Applying room palette override patch...')
        self.room_palette_override_patch = (Patch('override_room_palette', self.module_base + 0x2e26, self.process).mov_to_eax(self.room_palette_override_shader).nop(1))

    def apply_item_collection_patches(self):
        """
        disable_chest_item_patch disables receiving items when you open chests. This means you will no longer get incorrect dialog boxes or have your selected equipment
        change when opening a chest that normally would contain a piece of equipment.

        All the other patches here disable the dialog boxes that show up when you receive an item. Instead, you'll still get the item like normal and have your selected
        equipment automatically updated, and you'll still get the icon of the item over the bean's head, making it clear what items you received but reducing situations
        where you might be performing a trick when receiving a piece of equipment from another player's game.
        """
        disable_chest_item_patch = Patch('disable_chest_item', 0x1400c2871, self.process).xor_r8d_r8d().xor_edx_edx().nop(3)
        disable_item_get_dialog_patch = Patch('disable_item_get_dialog', 0x1400c2161, self.process).nop(5)
        # match, pencil, stethoscope, officeKey, stamps, pedometer, rabbitFig, mockDisc, cake, regularKey, stopwatch, sMedal, eMedal, questionKey
        disable_egg_get_dialog_patch = Patch('disable_egg_get_dialog', 0x1400c24a3, self.process).nop(5)
        disable_lantern_get_dialog_patch = Patch('disable_lantern_get_dialog', 0x1400c1c82, self.process).nop(5)
        disable_flute_get_dialog_patch = Patch('disable_flute_get_dialog', 0x1400c2241, self.process).nop(5)
        disable_bubble_get_dialog_patch = Patch('disable_bubble_get_dialog', 0x1400c21ea, self.process).nop(5)
        disable_uv_get_dialog_patch = Patch('disable_uv_get_dialog', 0x1400c1cd9, self.process).nop(5)
        disable_yoyo_get_dialog_patch = Patch('disable_yoyo_get_dialog', 0x1400c1f21, self.process).nop(5)
        disable_slink_get_dialog_patch = Patch('disable_slink_get_dialog', 0x1400c1bc0, self.process).nop(5)
        disable_remote_get_dialog_patch = Patch('disable_remote_get_dialog', 0x1400c211a, self.process).nop(5)
        disable_wheel_get_dialog_patch = Patch('disable_wheel_get_dialog', 0x1400c22c8, self.process).nop(5)
        disable_wheel_get_without_saving_cats_dialog_patch = Patch('disable_wheel_get_without_saving_cats_dialog', 0x1400c20b2, self.process).nop(5)
        disable_ball_get_dialog_patch = Patch('disable_ball_get_dialog', 0x1400c200d, self.process).nop(5)
        disable_top_get_dialog_patch = Patch('disable_top_get_dialog', 0x1400c1fb6, self.process).nop(5)
        disable_egg65_get_dialog_patch = Patch('disable_egg65_get_dialog', 0x1400c18be, self.process).nop(5)
        disable_bbwand_get_dialog_patch = Patch('disable_bbwand_get_dialog', 0x1400c1d75, self.process).nop(5)
        disable_fannypack_get_dialog_patch = Patch('disable_fannypack_get_dialog', 0x1400c1e81, self.process).nop(5)
        if self.log_debug_info: self.log_info(f'Applying disable_chest_item_patch patch...\n{disable_chest_item_patch}')
        if disable_chest_item_patch.apply(): self.revertable_patches.append(disable_chest_item_patch)
        if self.log_debug_info: self.log_info(f'Applying disable item get dialog patches...')
        if disable_item_get_dialog_patch.apply(): self.revertable_patches.append(disable_item_get_dialog_patch)
        if disable_egg_get_dialog_patch.apply(): self.revertable_patches.append(disable_egg_get_dialog_patch)
        if disable_lantern_get_dialog_patch.apply(): self.revertable_patches.append(disable_lantern_get_dialog_patch)
        if disable_flute_get_dialog_patch.apply(): self.revertable_patches.append(disable_flute_get_dialog_patch)
        if disable_bubble_get_dialog_patch.apply(): self.revertable_patches.append(disable_bubble_get_dialog_patch)
        if disable_uv_get_dialog_patch.apply(): self.revertable_patches.append(disable_uv_get_dialog_patch)
        if disable_yoyo_get_dialog_patch.apply(): self.revertable_patches.append(disable_yoyo_get_dialog_patch)
        if disable_slink_get_dialog_patch.apply(): self.revertable_patches.append(disable_slink_get_dialog_patch)
        if disable_remote_get_dialog_patch.apply(): self.revertable_patches.append(disable_remote_get_dialog_patch)
        if disable_wheel_get_dialog_patch.apply(): self.revertable_patches.append(disable_wheel_get_dialog_patch)
        if disable_wheel_get_without_saving_cats_dialog_patch.apply(): self.revertable_patches.append(disable_wheel_get_without_saving_cats_dialog_patch)
        if disable_ball_get_dialog_patch.apply(): self.revertable_patches.append(disable_ball_get_dialog_patch)
        if disable_top_get_dialog_patch.apply(): self.revertable_patches.append(disable_top_get_dialog_patch)
        if disable_egg65_get_dialog_patch.apply(): self.revertable_patches.append(disable_egg65_get_dialog_patch)
        if disable_bbwand_get_dialog_patch.apply(): self.revertable_patches.append(disable_bbwand_get_dialog_patch)
        if disable_fannypack_get_dialog_patch.apply(): self.revertable_patches.append(disable_fannypack_get_dialog_patch)

    def apply_receive_item_patch(self):
        """
        Set up a piece of code that runs in the normal gameloop that checks a location in memory to see if that location has a value. If it does, that routine will
        trigger getAnItem with the provided itemId, position(for eggs only), and locationId. LocationId will default to 0xff, as negative numbers do not trigger changes
        to the bytes that store which chests have already been opened. After this getAnItem, that location in memory is cleared, preventing the routine from attempting
        to give the item to the player again. This class will keep a buffer of items to receive and will automatically only set the item byte when it is currently 0,
        this will ensure that an item is never skipped if multiple arrive at the same exact time.

        # Relevant item Ids:
        # Unused: Stethoscope 0x14c, Cake 0x20,
        # Upgrades: FannyPack 0x30C, Stopwatch 0x19a, Pedometer 0x108, CRing 0xa1, BBWand 0x2c4,
        # Figs: MamaCha 0x32b, RabbitFig 0x332, SouvenirCup 0xe7,
        # Other: EMedal 0x2a7, SMedal 0x1d5, Pencil 0x1ba, Map 0xd6, Stamps 0x95, Normal Key 0x28, Match 0x29
        # Equipment: Top 0x27a, Ball 0x27d, Wheel 0x283, Remote 0x1d2, Slink 0x1a1, Yoyo 0x14e, UV 0x143, Bubble 0xa2, Flute 0xa9, Lantern 0x6d
        # Quest: Egg65 0x2c7, OfficeKey 0x269, QuestionKey 0x26a, MDisc 0x17e
        # Egg: 0x5a
        """
        # receive_item_patch = (Patch('receive_item', self.custom_memory_current_offset, self.process)
        #                       .get_key_pressed(0x48)
        #                       .cmp_al1_byte(0)
        #                       .je_near(0x80)
        #                       .push_rcx().push_rdx().push_r8().push_r9()
        #                       .warp(self.application_state_address + 0x93670, self.unstuck_room_x, self.unstuck_room_y, self.unstuck_pos_x, self.unstuck_pos_y, self.unstuck_map)
        #                       # .get_an_item(slot_address, 0x14c, 0x00, 0xff)
        #                       .pop_r9().pop_r8().pop_rdx().pop_rcx()
        #                       .nop(0x80)
        #                       .mov_edi(0x841c)
        #                       .mov_from_absolute_address_to_rax(0x1420949D0).movq_rax_to_xmm6()
        #                       .mov_from_absolute_address_to_rax(0x1420949F4).movq_rax_to_xmm7()
        #                       .jmp_far(0x14003B7FD)
        #                       )
        # self.custom_memory_current_offset += len(receive_item_patch)
        # if self.log_debug_info: self.log_info(f'Applying input_reader_patch...\n{receive_item_patch}')
        # if receive_item_patch.apply():
        #     self.revertable_patches.append(receive_item_patch)
        # input_reader_trampoline = (Patch('input_reader_trampoline', 0x14003B7D1, self.process)
        #                            .jmp_far(receive_item_patch.base_address).nop(2))
        # if self.log_debug_info: self.log_info(f'Applying input_reader_trampoline...\n{input_reader_trampoline}')
        # if input_reader_trampoline.apply():
        #     self.revertable_patches.append(input_reader_trampoline)

    def enable_fullbright(self):
        if self.fullbright_patch is None or self.fullbright_patch.patch_applied:
            return

        if self.log_debug_info: self.log_info(f'Applying fullbright patch...')
        self.fullbright_patch.apply()

    def disable_fullbright(self):
        if self.fullbright_patch is None or not self.fullbright_patch.patch_applied:
            return

        if self.log_debug_info: self.log_info(f'Reverting fullbright patch...')
        self.fullbright_patch.revert()

    def toggle_fullbright(self):
        if self.fullbright_patch is None:
            return

        if self.fullbright_patch.patch_applied:
            self.fullbright_patch.revert()
        else:
            self.fullbright_patch.apply()

    def generate_fullbright_patch(self):
        """
        This patch disables darkness in the game, causing all rooms to be equally lit across all tiles. Mostly useful for debugging.
        """
        self.fullbright_patch = Patch('fullbright', 0x140102e63, self.process).add_bytes(b'\xeb\x19')

    def revert_patches(self):
        if not self.attached_to_process:
            self.log_error('Cannot revert patches, not attached to Animal Well process!')
            return False

        if self.log_debug_info: self.log_info('Reverting patches...')

        self.log_info('Reverting any patches that we can...')
        for patch in self.revertable_patches:
            if patch.patch_applied:
                patch.revert()

        self.revertable_patches = []
        self.fullbright_patch = None
        self.room_palette_override_patch = None

        for offset, value in STEP_AND_TIME_DISPLAY_ORIGINAL_VALUES.items():
            if type(value) == int:
                self.process.write_uint(self.module_base + offset, value)
            elif type(value) == float:
                self.process.write_float(self.module_base + offset, value)

        self.custom_memory_base = None  # TODO: Free this memory back when we're unhooking from AW
        self.custom_memory_current_offset = None

        self.log_info('Patches reverted successfully!')

    def read_from_game(self):
        if not self.attached_to_process:
            return

        self.current_frame = self.process.read_uint(self.application_state_address + 0x9360c)
        if self.current_frame != self.last_frame:
            while (len(self.player_position_history) >= 60):
                self.player_position_history.pop(0)

            player_x_pos = int(self.process.read_float(self.application_state_address + 0x93670))  # 92e70
            player_y_pos = int(self.process.read_float(self.application_state_address + 0x93674))  # 92e74
            self.player_position_history.append((player_x_pos, player_y_pos))
        self.last_frame = self.current_frame

    def write_to_game(self):
        if not self.attached_to_process:
            return

        if self.game_draw_symbol_x_address != None and self.game_draw_symbol_y_address != None and len(self.player_position_history) > 0:
            self.process.write_uint(self.game_draw_symbol_x_address, self.player_position_history[0][0])
            self.process.write_uint(self.game_draw_symbol_y_address, self.player_position_history[0][1])

    def tick(self):
        if self.last_message_time != 0:
            if time() - self.last_message_time >= self.message_timeout:
                self.display_to_client('')

    def display_dialog(self, text: str, title: str = '', actionText: str = ''):
        try:
            if self.process != None and self.application_state_address != None:
                text = f'{text:.255}'.encode('utf-16le') + b'\x00\x00'
                title = f'{title:.15}'.encode('utf-16le') + b'\x00\x00'
                actionText = f'{actionText:.15}'.encode('utf-16le') + b'\x00\x00'
                self.process.write_bytes(self.application_state_address + 0xA84B8, text, len(text))
                self.process.write_bytes(self.application_state_address + 0xA84B8 + 0x200, title, len(title))
                self.process.write_bytes(self.application_state_address + 0xA84B8 + 0x240, actionText, len(actionText))
                self.process.write_bytes(self.application_state_address + 0xA84B8 + 0x4a0, b'\x00', 1)
                self.process.write_bytes(self.application_state_address + 0xA84B4, b'\x01', 1)
        except Exception as e:
            self.log_error(f'Error while attempting to trigger dialog box on client: {e}')

    def display_to_client(self, text: str):
        try:
            if type(text) != "str":
                text = str(text)

            if self.game_draw_routine_string_addr != None:
                newStringBuffer = f"{text:.120}".encode('utf-16le') + b'\x00\x00'
                self.process.write_bytes(self.game_draw_routine_string_addr, newStringBuffer, len(newStringBuffer))

                if text != '':
                    self.last_message_time = time()
                else:
                    self.last_message_time = 0
        except Exception as e:
            self.log_error(f"Error while attempting to display text to client: {e}")