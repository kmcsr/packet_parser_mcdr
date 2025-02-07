
from typing import ClassVar
from loginproxy import Protocol

__all__ = ['PacketIdSet']

class PacketIdSet:
	__slots__ = (
		'version',
		# S2C
		'configuration_add_resource_pack', # 1_21_1, 1_21_4
		'configuration_cookie_request', # 1_21_1, 1_21_4
		'configuration_custom_report_details', # 1_21_1, 1_21_4
		'configuration_disconnect', # 1_21_1, 1_21_4
		'configuration_feature_flags', # 1_21_1, 1_21_4
		'configuration_finish_configuration', # 1_21_1, 1_21_4
		'configuration_keep_alive_s2c', # 1_21_1, 1_21_4
		'configuration_known_packs_s2c', # 1_21_1, 1_21_4
		'configuration_ping', # 1_21_1, 1_21_4
		'configuration_plugin_message_s2c', # 1_21_1, 1_21_4
		'configuration_registry_data', # 1_21_1, 1_21_4
		'configuration_remove_resource_pack', # 1_21_1, 1_21_4
		'configuration_reset_chat', # 1_21_1, 1_21_4
		'configuration_server_links', # 1_21_1, 1_21_4
		'configuration_store_cookie', # 1_21_1, 1_21_4
		'configuration_transfer', # 1_21_1, 1_21_4
		'configuration_update_tags', # 1_21_1, 1_21_4
		'login_cookie_request', # 1_21_1, 1_21_4
		'login_disconnect', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'login_encryption_request', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'login_plugin_request', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'login_set_compression', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'login_success', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_acknowledge_block_change', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_add_resource_pack', # 1_21_1, 1_21_4
		'play_award_statistics', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_block_action', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_block_break_animation', # 1_18_2
		'play_block_entity_data', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_block_update', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_boss_bar', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_bundle_delimiter', # 1_20_1, 1_21_1, 1_21_4
		'play_change_difficulty_s2c', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_chat_preview_s2c', # 1_19_2
		'play_chat_suggestions', # 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_chunk_batch_finished', # 1_21_1, 1_21_4
		'play_chunk_batch_start', # 1_21_1, 1_21_4
		'play_chunk_biomes', # 1_20_1, 1_21_1, 1_21_4
		'play_chunk_data_and_update_light', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_clear_titles', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_close_container_s2c', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_combat_death', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_command_suggestions_response', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_commands', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_cookie_request', # 1_21_1, 1_21_4
		'play_custom_report_details', # 1_21_1, 1_21_4
		'play_custom_sound_effect', # 1_18_2, 1_19_2
		'play_damage_event', # 1_20_1, 1_21_1, 1_21_4
		'play_debug_sample', # 1_21_1, 1_21_4
		'play_delete_message', # 1_20_1, 1_21_1, 1_21_4
		'play_disconnect', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_disguised_chat_message', # 1_20_1, 1_21_1, 1_21_4
		'play_display_objective', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_end_combat', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_enter_combat', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_entity_animation', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_entity_effect', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_entity_event', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_entity_sound_effect', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_explosion', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_feature_flags', # 1_20_1
		'play_game_event', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_hide_message', # 1_19_2
		'play_hurt_animation', # 1_20_1, 1_21_1, 1_21_4
		'play_initialize_world_border', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_keep_alive_s2c', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_link_entities', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_login', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_look_at', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_map_data', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_merchant_offers', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_message_header', # 1_19_2
		'play_move_minecart_along_track', # 1_21_4
		'play_move_vehicle_s2c', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_open_book', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_open_horse_screen', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_open_screen', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_open_sign_editor', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_particle', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_pickup_item', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_ping', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_ping_response', # 1_21_1, 1_21_4
		'play_place_ghost_recipe', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_player_abilities_s2c', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_player_chat_message', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_player_info', # 1_18_2, 1_19_2
		'play_player_info_remove', # 1_20_1, 1_21_1, 1_21_4
		'play_player_info_update', # 1_20_1, 1_21_1, 1_21_4
		'play_plugin_message_s2c', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_projectile_power', # 1_21_1, 1_21_4
		'play_recipe_book_add', # 1_21_4
		'play_recipe_book_remove', # 1_21_4
		'play_recipe_book_settings', # 1_21_4
		'play_remove_entities', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_remove_entity_effect', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_remove_resource_pack', # 1_21_1, 1_21_4
		'play_reset_score', # 1_21_1, 1_21_4
		'play_resource_pack_s2c', # 1_18_2, 1_19_2, 1_20_1
		'play_respawn', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_sculk_vibration_signal', # 1_18_2
		'play_select_advancements_tab', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_server_data', # 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_server_links', # 1_21_1, 1_21_4
		'play_set_action_bar_text', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_block_destroy_stage', # 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_border_center', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_border_lerp_size', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_border_size', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_border_warning_delay', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_border_warning_distance', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_camera', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_center_chunk', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_container_content', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_container_property', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_container_slot', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_cooldown', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_cursor_item', # 1_21_4
		'play_set_default_spawn_position', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_display_chat_preview', # 1_19_2
		'play_set_entity_metadata', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_entity_velocity', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_equipment', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_experience', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_head_rotation', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_health', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_held_item_s2c', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_passengers', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_player_inventory_slot', # 1_21_4
		'play_set_player_rotation_s2c', # 1_21_4
		'play_set_render_distance', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_simulation_distance', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_subtitle_text', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_tab_list_header_and_footer', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_ticking_state', # 1_21_1, 1_21_4
		'play_set_title_animation_times', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_title_text', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_sound_effect', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_spawn_entity', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_spawn_experience_orb', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_spawn_living_entity', # 1_18_2
		'play_spawn_painting', # 1_18_2
		'play_spawn_player', # 1_18_2, 1_19_2, 1_20_1
		'play_start_configuration', # 1_21_1, 1_21_4
		'play_step_tick', # 1_21_1, 1_21_4
		'play_stop_sound', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_store_cookie', # 1_21_1, 1_21_4
		'play_synchronize_player_position', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_synchronize_vehicle_position', # 1_21_4
		'play_system_chat_message', # 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_tag_query_response', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_teleport_entity', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_transfer', # 1_21_1, 1_21_4
		'play_unload_chunk', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_advancements', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_attributes', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_entity_position', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_entity_position_and_rotation', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_entity_rotation', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_light', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_objectives', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_recipe_book', # 1_18_2, 1_19_2, 1_20_1, 1_21_1
		'play_update_recipes', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_score', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_section_blocks', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_tags', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_teams', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_time', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_world_event', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'status_pong', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'status_response', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		# C2S
		'configuration_acknowledge_finish_configuration', # 1_21_1, 1_21_4
		'configuration_client_information', # 1_21_1, 1_21_4
		'configuration_cookie_response', # 1_21_1, 1_21_4
		'configuration_keep_alive_c2s', # 1_21_1, 1_21_4
		'configuration_known_packs_c2s', # 1_21_1, 1_21_4
		'configuration_plugin_message_c2s', # 1_21_1, 1_21_4
		'configuration_pong', # 1_21_1, 1_21_4
		'configuration_resource_pack_response', # 1_21_1, 1_21_4
		'handshaking_handshake', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'handshaking_legacy_server_list_ping', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'login_acknowledged', # 1_21_1, 1_21_4
		'login_cookie_response', # 1_21_1, 1_21_4
		'login_encryption_response', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'login_plugin_response', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'login_start', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_acknowledge_configuration', # 1_21_1, 1_21_4
		'play_acknowledge_message', # 1_21_1, 1_21_4
		'play_bundle_item_selected', # 1_21_4
		'play_change_container_slot_state', # 1_21_1, 1_21_4
		'play_change_difficulty_c2s', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_change_recipe_book_settings', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_chat_command', # 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_chat_message', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_chat_preview_c2s', # 1_19_2
		'play_chunk_batch_received', # 1_21_1, 1_21_4
		'play_click_container', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_click_container_button', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_client_information', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_client_status', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_client_tick_end', # 1_21_4
		'play_close_container_c2s', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_command_suggestions_request', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_confirm_teleportation', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_cookie_response', # 1_21_1, 1_21_4
		'play_debug_sample_subscription', # 1_21_1, 1_21_4
		'play_edit_book', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_generate_structure', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_interact', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_keep_alive_c2s', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_lock_difficulty', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_message_acknowledgment', # 1_19_2, 1_20_1
		'play_move_vehicle_c2s', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_paddle_boat', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_pick_item', # 1_18_2, 1_19_2, 1_20_1, 1_21_1
		'play_pick_item_from_block', # 1_21_4
		'play_pick_item_from_entity', # 1_21_4
		'play_ping_request', # 1_21_1, 1_21_4
		'play_place_recipe', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_player_abilities_c2s', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_player_action', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_player_command', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_player_input', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_player_loaded', # 1_21_4
		'play_player_session', # 1_20_1, 1_21_1, 1_21_4
		'play_plugin_message_c2s', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_pong', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_program_command_block', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_program_command_block_minecart', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_program_jigsaw_block', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_program_structure_block', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_query_block_entity_tag', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_query_entity_tag', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_rename_item', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_resource_pack_c2s', # 1_18_2, 1_19_2, 1_20_1
		'play_resource_pack_response', # 1_21_1, 1_21_4
		'play_seen_advancements', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_select_trade', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_beacon_effect', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_creative_mode_slot', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_held_item_c2s', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_player_movement_flags', # 1_21_4
		'play_set_player_on_ground', # 1_18_2, 1_19_2, 1_20_1, 1_21_1
		'play_set_player_position', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_player_position_and_rotation', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_player_rotation_c2s', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_set_seen_recipe', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_signed_chat_command', # 1_21_1, 1_21_4
		'play_swing_arm', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_teleport_to_entity', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_update_sign', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_use_item', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'play_use_item_on', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'status_ping', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
		'status_request', # 1_18_2, 1_19_2, 1_20_1, 1_21_1, 1_21_4
	)

	is_c2s = {
		# S2C
		'configuration_add_resource_pack': False,
		'configuration_cookie_request': False,
		'configuration_custom_report_details': False,
		'configuration_disconnect': False,
		'configuration_feature_flags': False,
		'configuration_finish_configuration': False,
		'configuration_keep_alive_s2c': False,
		'configuration_known_packs_s2c': False,
		'configuration_ping': False,
		'configuration_plugin_message_s2c': False,
		'configuration_registry_data': False,
		'configuration_remove_resource_pack': False,
		'configuration_reset_chat': False,
		'configuration_server_links': False,
		'configuration_store_cookie': False,
		'configuration_transfer': False,
		'configuration_update_tags': False,
		'login_cookie_request': False,
		'login_disconnect': False,
		'login_encryption_request': False,
		'login_plugin_request': False,
		'login_set_compression': False,
		'login_success': False,
		'play_acknowledge_block_change': False,
		'play_add_resource_pack': False,
		'play_award_statistics': False,
		'play_block_action': False,
		'play_block_break_animation': False,
		'play_block_entity_data': False,
		'play_block_update': False,
		'play_boss_bar': False,
		'play_bundle_delimiter': False,
		'play_change_difficulty_s2c': False,
		'play_chat_preview_s2c': False,
		'play_chat_suggestions': False,
		'play_chunk_batch_finished': False,
		'play_chunk_batch_start': False,
		'play_chunk_biomes': False,
		'play_chunk_data_and_update_light': False,
		'play_clear_titles': False,
		'play_close_container_s2c': False,
		'play_combat_death': False,
		'play_command_suggestions_response': False,
		'play_commands': False,
		'play_cookie_request': False,
		'play_custom_report_details': False,
		'play_custom_sound_effect': False,
		'play_damage_event': False,
		'play_debug_sample': False,
		'play_delete_message': False,
		'play_disconnect': False,
		'play_disguised_chat_message': False,
		'play_display_objective': False,
		'play_end_combat': False,
		'play_enter_combat': False,
		'play_entity_animation': False,
		'play_entity_effect': False,
		'play_entity_event': False,
		'play_entity_sound_effect': False,
		'play_explosion': False,
		'play_feature_flags': False,
		'play_game_event': False,
		'play_hide_message': False,
		'play_hurt_animation': False,
		'play_initialize_world_border': False,
		'play_keep_alive_s2c': False,
		'play_link_entities': False,
		'play_login': False,
		'play_look_at': False,
		'play_map_data': False,
		'play_merchant_offers': False,
		'play_message_header': False,
		'play_move_minecart_along_track': False,
		'play_move_vehicle_s2c': False,
		'play_open_book': False,
		'play_open_horse_screen': False,
		'play_open_screen': False,
		'play_open_sign_editor': False,
		'play_particle': False,
		'play_pickup_item': False,
		'play_ping': False,
		'play_ping_response': False,
		'play_place_ghost_recipe': False,
		'play_player_abilities_s2c': False,
		'play_player_chat_message': False,
		'play_player_info': False,
		'play_player_info_remove': False,
		'play_player_info_update': False,
		'play_plugin_message_s2c': False,
		'play_projectile_power': False,
		'play_recipe_book_add': False,
		'play_recipe_book_remove': False,
		'play_recipe_book_settings': False,
		'play_remove_entities': False,
		'play_remove_entity_effect': False,
		'play_remove_resource_pack': False,
		'play_reset_score': False,
		'play_resource_pack_s2c': False,
		'play_respawn': False,
		'play_sculk_vibration_signal': False,
		'play_select_advancements_tab': False,
		'play_server_data': False,
		'play_server_links': False,
		'play_set_action_bar_text': False,
		'play_set_block_destroy_stage': False,
		'play_set_border_center': False,
		'play_set_border_lerp_size': False,
		'play_set_border_size': False,
		'play_set_border_warning_delay': False,
		'play_set_border_warning_distance': False,
		'play_set_camera': False,
		'play_set_center_chunk': False,
		'play_set_container_content': False,
		'play_set_container_property': False,
		'play_set_container_slot': False,
		'play_set_cooldown': False,
		'play_set_cursor_item': False,
		'play_set_default_spawn_position': False,
		'play_set_display_chat_preview': False,
		'play_set_entity_metadata': False,
		'play_set_entity_velocity': False,
		'play_set_equipment': False,
		'play_set_experience': False,
		'play_set_head_rotation': False,
		'play_set_health': False,
		'play_set_held_item_s2c': False,
		'play_set_passengers': False,
		'play_set_player_inventory_slot': False,
		'play_set_player_rotation_s2c': False,
		'play_set_render_distance': False,
		'play_set_simulation_distance': False,
		'play_set_subtitle_text': False,
		'play_set_tab_list_header_and_footer': False,
		'play_set_ticking_state': False,
		'play_set_title_animation_times': False,
		'play_set_title_text': False,
		'play_sound_effect': False,
		'play_spawn_entity': False,
		'play_spawn_experience_orb': False,
		'play_spawn_living_entity': False,
		'play_spawn_painting': False,
		'play_spawn_player': False,
		'play_start_configuration': False,
		'play_step_tick': False,
		'play_stop_sound': False,
		'play_store_cookie': False,
		'play_synchronize_player_position': False,
		'play_synchronize_vehicle_position': False,
		'play_system_chat_message': False,
		'play_tag_query_response': False,
		'play_teleport_entity': False,
		'play_transfer': False,
		'play_unload_chunk': False,
		'play_update_advancements': False,
		'play_update_attributes': False,
		'play_update_entity_position': False,
		'play_update_entity_position_and_rotation': False,
		'play_update_entity_rotation': False,
		'play_update_light': False,
		'play_update_objectives': False,
		'play_update_recipe_book': False,
		'play_update_recipes': False,
		'play_update_score': False,
		'play_update_section_blocks': False,
		'play_update_tags': False,
		'play_update_teams': False,
		'play_update_time': False,
		'play_world_event': False,
		'status_pong': False,
		'status_response': False,
		# C2S
		'configuration_acknowledge_finish_configuration': True,
		'configuration_client_information': True,
		'configuration_cookie_response': True,
		'configuration_keep_alive_c2s': True,
		'configuration_known_packs_c2s': True,
		'configuration_plugin_message_c2s': True,
		'configuration_pong': True,
		'configuration_resource_pack_response': True,
		'handshaking_handshake': True,
		'handshaking_legacy_server_list_ping': True,
		'login_acknowledged': True,
		'login_cookie_response': True,
		'login_encryption_response': True,
		'login_plugin_response': True,
		'login_start': True,
		'play_acknowledge_configuration': True,
		'play_acknowledge_message': True,
		'play_bundle_item_selected': True,
		'play_change_container_slot_state': True,
		'play_change_difficulty_c2s': True,
		'play_change_recipe_book_settings': True,
		'play_chat_command': True,
		'play_chat_message': True,
		'play_chat_preview_c2s': True,
		'play_chunk_batch_received': True,
		'play_click_container': True,
		'play_click_container_button': True,
		'play_client_information': True,
		'play_client_status': True,
		'play_client_tick_end': True,
		'play_close_container_c2s': True,
		'play_command_suggestions_request': True,
		'play_confirm_teleportation': True,
		'play_cookie_response': True,
		'play_debug_sample_subscription': True,
		'play_edit_book': True,
		'play_generate_structure': True,
		'play_interact': True,
		'play_keep_alive_c2s': True,
		'play_lock_difficulty': True,
		'play_message_acknowledgment': True,
		'play_move_vehicle_c2s': True,
		'play_paddle_boat': True,
		'play_pick_item': True,
		'play_pick_item_from_block': True,
		'play_pick_item_from_entity': True,
		'play_ping_request': True,
		'play_place_recipe': True,
		'play_player_abilities_c2s': True,
		'play_player_action': True,
		'play_player_command': True,
		'play_player_input': True,
		'play_player_loaded': True,
		'play_player_session': True,
		'play_plugin_message_c2s': True,
		'play_pong': True,
		'play_program_command_block': True,
		'play_program_command_block_minecart': True,
		'play_program_jigsaw_block': True,
		'play_program_structure_block': True,
		'play_query_block_entity_tag': True,
		'play_query_entity_tag': True,
		'play_rename_item': True,
		'play_resource_pack_c2s': True,
		'play_resource_pack_response': True,
		'play_seen_advancements': True,
		'play_select_trade': True,
		'play_set_beacon_effect': True,
		'play_set_creative_mode_slot': True,
		'play_set_held_item_c2s': True,
		'play_set_player_movement_flags': True,
		'play_set_player_on_ground': True,
		'play_set_player_position': True,
		'play_set_player_position_and_rotation': True,
		'play_set_player_rotation_c2s': True,
		'play_set_seen_recipe': True,
		'play_signed_chat_command': True,
		'play_swing_arm': True,
		'play_teleport_to_entity': True,
		'play_update_sign': True,
		'play_use_item': True,
		'play_use_item_on': True,
		'status_ping': True,
		'status_request': True,
	}

	def __init__(self, version: int):
		self.version = version

	@staticmethod
	def from_protocol(protocol: int) -> 'PacketIdSet':
		if protocol >= Protocol.V1_21_4:
			return PacketV1_21_4.INSTANCE
		if protocol >= Protocol.V1_21_1:
			return PacketV1_21_1.INSTANCE
		if protocol >= Protocol.V1_20_1:
			return PacketV1_20_1.INSTANCE
		if protocol >= Protocol.V1_19_2:
			return PacketV1_19_2.INSTANCE
		if protocol >= Protocol.V1_18_2:
			return PacketV1_18_2.INSTANCE
		raise ValueError(f'unsupported version {protocol}')

# Generate from <https://minecraft.wiki/w/Minecraft_Wiki:Projects/wiki.vg_merge/Protocol?oldid=2772783>
class PacketV1_18_2(PacketIdSet):
	INSTANCE: ClassVar[PacketIdSet]
	def __init__(self) -> None:
		super().__init__(Protocol.V1_18_2)
		# Client bounds
		self.status_response = 0x00
		self.status_pong = 0x01
		self.login_disconnect = 0x00
		self.login_encryption_request = 0x01
		self.login_success = 0x02
		self.login_set_compression = 0x03
		self.login_plugin_request = 0x04
		self.play_spawn_entity = 0x00
		self.play_spawn_experience_orb = 0x01
		self.play_spawn_living_entity = 0x02
		self.play_spawn_painting = 0x03
		self.play_spawn_player = 0x04
		self.play_sculk_vibration_signal = 0x05
		self.play_entity_animation = 0x06
		self.play_award_statistics = 0x07
		self.play_acknowledge_block_change = 0x08
		self.play_block_break_animation = 0x09
		self.play_block_entity_data = 0x0A
		self.play_block_action = 0x0B
		self.play_block_update = 0x0C
		self.play_boss_bar = 0x0D
		self.play_change_difficulty = 0x0E
		self.play_player_chat_message = 0x0F
		self.play_clear_titles = 0x10
		self.play_command_suggestions_response = 0x11
		self.play_commands = 0x12
		self.play_close_container_s2c = 0x13
		self.play_set_container_content = 0x14
		self.play_set_container_property = 0x15
		self.play_set_container_slot = 0x16
		self.play_set_cooldown = 0x17
		self.play_plugin_message_s2c = 0x18
		self.play_custom_sound_effect = 0x19
		self.play_disconnect = 0x1A
		self.play_entity_event = 0x1B
		self.play_explosion = 0x1C
		self.play_unload_chunk = 0x1D
		self.play_game_event = 0x1E
		self.play_open_horse_screen = 0x1F
		self.play_initialize_world_border = 0x20
		self.play_keep_alive_s2c = 0x21
		self.play_chunk_data_and_update_light = 0x22
		self.play_world_event = 0x23
		self.play_particle = 0x24
		self.play_update_light = 0x25
		self.play_login = 0x26
		self.play_map_data = 0x27
		self.play_merchant_offers = 0x28
		self.play_update_entity_position = 0x29
		self.play_update_entity_position_and_rotation = 0x2A
		self.play_update_entity_rotation = 0x2B
		self.play_move_vehicle_s2c = 0x2C
		self.play_open_book = 0x2D
		self.play_open_screen = 0x2E
		self.play_open_sign_editor = 0x2F
		self.play_ping = 0x30
		self.play_place_ghost_recipe = 0x31
		self.play_player_abilities_s2c = 0x32
		self.play_end_combat = 0x33
		self.play_enter_combat = 0x34
		self.play_combat_death = 0x35
		self.play_player_info = 0x36
		self.play_look_at = 0x37
		self.play_synchronize_player_position = 0x38
		self.play_update_recipe_book = 0x39
		self.play_remove_entities = 0x3A
		self.play_remove_entity_effect = 0x3B
		self.play_resource_pack_s2c = 0x3C
		self.play_respawn = 0x3D
		self.play_set_head_rotation = 0x3E
		self.play_update_section_blocks = 0x3F
		self.play_select_advancements_tab = 0x40
		self.play_set_action_bar_text = 0x41
		self.play_set_border_center = 0x42
		self.play_set_border_lerp_size = 0x43
		self.play_set_border_size = 0x44
		self.play_set_border_warning_delay = 0x45
		self.play_set_border_warning_distance = 0x46
		self.play_set_camera = 0x47
		self.play_set_held_item_s2c = 0x48
		self.play_set_center_chunk = 0x49
		self.play_set_render_distance = 0x4A
		self.play_set_default_spawn_position = 0x4B
		self.play_display_objective = 0x4C
		self.play_set_entity_metadata = 0x4D
		self.play_link_entities = 0x4E
		self.play_set_entity_velocity = 0x4F
		self.play_set_equipment = 0x50
		self.play_set_experience = 0x51
		self.play_set_health = 0x52
		self.play_update_objectives = 0x53
		self.play_set_passengers = 0x54
		self.play_update_teams = 0x55
		self.play_update_score = 0x56
		self.play_set_simulation_distance = 0x57
		self.play_set_subtitle_text = 0x58
		self.play_update_time = 0x59
		self.play_set_title_text = 0x5A
		self.play_set_title_animation_times = 0x5B
		self.play_entity_sound_effect = 0x5C
		self.play_sound_effect = 0x5D
		self.play_stop_sound = 0x5E
		self.play_set_tab_list_header_and_footer = 0x5F
		self.play_tag_query_response = 0x60
		self.play_pickup_item = 0x61
		self.play_teleport_entity = 0x62
		self.play_update_advancements = 0x63
		self.play_update_attributes = 0x64
		self.play_entity_effect = 0x65
		self.play_update_recipes = 0x66
		self.play_update_tags = 0x67
		# Server bounds
		self.handshaking_handshake = 0x00
		self.handshaking_legacy_server_list_ping = 0xFE
		self.status_request = 0x00
		self.status_ping = 0x01
		self.login_start = 0x00
		self.login_encryption_response = 0x01
		self.login_plugin_response = 0x02
		self.play_confirm_teleportation = 0x00
		self.play_query_block_entity_tag = 0x01
		self.play_change_difficulty_c2s = 0x02
		self.play_chat_message = 0x03
		self.play_client_status = 0x04
		self.play_client_information = 0x05
		self.play_command_suggestions_request = 0x06
		self.play_click_container_button = 0x07
		self.play_click_container = 0x08
		self.play_close_container_c2s = 0x09
		self.play_plugin_message_c2s = 0x0A
		self.play_edit_book = 0x0B
		self.play_query_entity_tag = 0x0C
		self.play_interact = 0x0D
		self.play_generate_structure = 0x0E
		self.play_keep_alive_c2s = 0x0F
		self.play_lock_difficulty = 0x10
		self.play_set_player_position = 0x11
		self.play_set_player_position_and_rotation = 0x12
		self.play_set_player_rotation = 0x13
		self.play_set_player_on_ground = 0x14
		self.play_move_vehicle_c2s = 0x15
		self.play_paddle_boat = 0x16
		self.play_pick_item = 0x17
		self.play_place_recipe = 0x18
		self.play_player_abilities_c2s = 0x19
		self.play_player_action = 0x1A
		self.play_player_command = 0x1B
		self.play_player_input = 0x1C
		self.play_pong = 0x1D
		self.play_change_recipe_book_settings = 0x1E
		self.play_set_seen_recipe = 0x1F
		self.play_rename_item = 0x20
		self.play_resource_pack_c2s = 0x21
		self.play_seen_advancements = 0x22
		self.play_select_trade = 0x23
		self.play_set_beacon_effect = 0x24
		self.play_set_held_item_c2s = 0x25
		self.play_program_command_block = 0x26
		self.play_program_command_block_minecart = 0x27
		self.play_set_creative_mode_slot = 0x28
		self.play_program_jigsaw_block = 0x29
		self.play_program_structure_block = 0x2A
		self.play_update_sign = 0x2B
		self.play_swing_arm = 0x2C
		self.play_teleport_to_entity = 0x2D
		self.play_use_item_on = 0x2E
		self.play_use_item = 0x2F
PacketV1_18_2.INSTANCE = PacketV1_18_2()

# Generate from <https://minecraft.wiki/w/Minecraft_Wiki:Projects/wiki.vg_merge/Protocol?oldid=2772944>
class PacketV1_19_2(PacketIdSet):
	INSTANCE: ClassVar[PacketIdSet]
	def __init__(self) -> None:
		super().__init__(Protocol.V1_19_2)
		# Client bounds
		self.status_response = 0x00
		self.status_pong = 0x01
		self.login_disconnect = 0x00
		self.login_encryption_request = 0x01
		self.login_success = 0x02
		self.login_set_compression = 0x03
		self.login_plugin_request = 0x04
		self.play_spawn_entity = 0x00
		self.play_spawn_experience_orb = 0x01
		self.play_spawn_player = 0x02
		self.play_entity_animation = 0x03
		self.play_award_statistics = 0x04
		self.play_acknowledge_block_change = 0x05
		self.play_set_block_destroy_stage = 0x06
		self.play_block_entity_data = 0x07
		self.play_block_action = 0x08
		self.play_block_update = 0x09
		self.play_boss_bar = 0x0A
		self.play_change_difficulty = 0x0B
		self.play_chat_preview_s2c = 0x0C
		self.play_clear_titles = 0x0D
		self.play_command_suggestions_response = 0x0E
		self.play_commands = 0x0F
		self.play_close_container_s2c = 0x10
		self.play_set_container_content = 0x11
		self.play_set_container_property = 0x12
		self.play_set_container_slot = 0x13
		self.play_set_cooldown = 0x14
		self.play_chat_suggestions = 0x15
		self.play_plugin_message_s2c = 0x16
		self.play_custom_sound_effect = 0x17
		self.play_hide_message = 0x18
		self.play_disconnect = 0x19
		self.play_entity_event = 0x1A
		self.play_explosion = 0x1B
		self.play_unload_chunk = 0x1C
		self.play_game_event = 0x1D
		self.play_open_horse_screen = 0x1E
		self.play_initialize_world_border = 0x1F
		self.play_keep_alive_s2c = 0x20
		self.play_chunk_data_and_update_light = 0x21
		self.play_world_event = 0x22
		self.play_particle = 0x23
		self.play_update_light = 0x24
		self.play_login = 0x25
		self.play_map_data = 0x26
		self.play_merchant_offers = 0x27
		self.play_update_entity_position = 0x28
		self.play_update_entity_position_and_rotation = 0x29
		self.play_update_entity_rotation = 0x2A
		self.play_move_vehicle_s2c = 0x2B
		self.play_open_book = 0x2C
		self.play_open_screen = 0x2D
		self.play_open_sign_editor = 0x2E
		self.play_ping = 0x2F
		self.play_place_ghost_recipe = 0x30
		self.play_player_abilities_s2c = 0x31
		self.play_message_header = 0x32
		self.play_player_chat_message = 0x33
		self.play_end_combat = 0x34
		self.play_enter_combat = 0x35
		self.play_combat_death = 0x36
		self.play_player_info = 0x37
		self.play_look_at = 0x38
		self.play_synchronize_player_position = 0x39
		self.play_update_recipe_book = 0x3A
		self.play_remove_entities = 0x3B
		self.play_remove_entity_effect = 0x3C
		self.play_resource_pack_s2c = 0x3D
		self.play_respawn = 0x3E
		self.play_set_head_rotation = 0x3F
		self.play_update_section_blocks = 0x40
		self.play_select_advancements_tab = 0x41
		self.play_server_data = 0x42
		self.play_set_action_bar_text = 0x43
		self.play_set_border_center = 0x44
		self.play_set_border_lerp_size = 0x45
		self.play_set_border_size = 0x46
		self.play_set_border_warning_delay = 0x47
		self.play_set_border_warning_distance = 0x48
		self.play_set_camera = 0x49
		self.play_set_held_item_s2c = 0x4A
		self.play_set_center_chunk = 0x4B
		self.play_set_render_distance = 0x4C
		self.play_set_default_spawn_position = 0x4D
		self.play_set_display_chat_preview = 0x4E
		self.play_display_objective = 0x4F
		self.play_set_entity_metadata = 0x50
		self.play_link_entities = 0x51
		self.play_set_entity_velocity = 0x52
		self.play_set_equipment = 0x53
		self.play_set_experience = 0x54
		self.play_set_health = 0x55
		self.play_update_objectives = 0x56
		self.play_set_passengers = 0x57
		self.play_update_teams = 0x58
		self.play_update_score = 0x59
		self.play_set_simulation_distance = 0x5A
		self.play_set_subtitle_text = 0x5B
		self.play_update_time = 0x5C
		self.play_set_title_text = 0x5D
		self.play_set_title_animation_times = 0x5E
		self.play_entity_sound_effect = 0x5F
		self.play_sound_effect = 0x60
		self.play_stop_sound = 0x61
		self.play_system_chat_message = 0x62
		self.play_set_tab_list_header_and_footer = 0x63
		self.play_tag_query_response = 0x64
		self.play_pickup_item = 0x65
		self.play_teleport_entity = 0x66
		self.play_update_advancements = 0x67
		self.play_update_attributes = 0x68
		self.play_entity_effect = 0x69
		self.play_update_recipes = 0x6A
		self.play_update_tags = 0x6B
		# Server bounds
		self.handshaking_handshake = 0x00
		self.handshaking_legacy_server_list_ping = 0xFE
		self.status_request = 0x00
		self.status_ping = 0x01
		self.login_start = 0x00
		self.login_encryption_response = 0x01
		self.login_plugin_response = 0x02
		self.play_confirm_teleportation = 0x00
		self.play_query_block_entity_tag = 0x01
		self.play_change_difficulty = 0x02
		self.play_message_acknowledgment = 0x03
		self.play_chat_command = 0x04
		self.play_chat_message = 0x05
		self.play_chat_preview_c2s = 0x06
		self.play_client_status = 0x07
		self.play_client_information = 0x08
		self.play_command_suggestions_request = 0x09
		self.play_click_container_button = 0x0A
		self.play_click_container = 0x0B
		self.play_close_container_c2s = 0x0C
		self.play_plugin_message_c2s = 0x0D
		self.play_edit_book = 0x0E
		self.play_query_entity_tag = 0x0F
		self.play_interact = 0x10
		self.play_generate_structure = 0x11
		self.play_keep_alive_c2s = 0x12
		self.play_lock_difficulty = 0x13
		self.play_set_player_position = 0x14
		self.play_set_player_position_and_rotation = 0x15
		self.play_set_player_rotation = 0x16
		self.play_set_player_on_ground = 0x17
		self.play_move_vehicle_c2s = 0x18
		self.play_paddle_boat = 0x19
		self.play_pick_item = 0x1A
		self.play_place_recipe = 0x1B
		self.play_player_abilities_c2s = 0x1C
		self.play_player_action = 0x1D
		self.play_player_command = 0x1E
		self.play_player_input = 0x1F
		self.play_pong = 0x20
		self.play_change_recipe_book_settings = 0x21
		self.play_set_seen_recipe = 0x22
		self.play_rename_item = 0x23
		self.play_resource_pack_c2s = 0x24
		self.play_seen_advancements = 0x25
		self.play_select_trade = 0x26
		self.play_set_beacon_effect = 0x27
		self.play_set_held_item_c2s = 0x28
		self.play_program_command_block = 0x29
		self.play_program_command_block_minecart = 0x2A
		self.play_set_creative_mode_slot = 0x2B
		self.play_program_jigsaw_block = 0x2C
		self.play_program_structure_block = 0x2D
		self.play_update_sign = 0x2E
		self.play_swing_arm = 0x2F
		self.play_teleport_to_entity = 0x30
		self.play_use_item_on = 0x31
		self.play_use_item = 0x32
PacketV1_19_2.INSTANCE = PacketV1_19_2()

# Generate from <https://minecraft.wiki/w/Minecraft_Wiki:Projects/wiki.vg_merge/Protocol?oldid=2773082>
class PacketV1_20_1(PacketIdSet):
	INSTANCE: ClassVar[PacketIdSet]
	def __init__(self) -> None:
		super().__init__(Protocol.V1_20_1)
		# Client bounds
		self.status_response = 0x00
		self.status_pong = 0x01
		self.login_disconnect = 0x00
		self.login_encryption_request = 0x01
		self.login_success = 0x02
		self.login_set_compression = 0x03
		self.login_plugin_request = 0x04
		self.play_bundle_delimiter = 0x00
		self.play_spawn_entity = 0x01
		self.play_spawn_experience_orb = 0x02
		self.play_spawn_player = 0x03
		self.play_entity_animation = 0x04
		self.play_award_statistics = 0x05
		self.play_acknowledge_block_change = 0x06
		self.play_set_block_destroy_stage = 0x07
		self.play_block_entity_data = 0x08
		self.play_block_action = 0x09
		self.play_block_update = 0x0A
		self.play_boss_bar = 0x0B
		self.play_change_difficulty = 0x0C
		self.play_chunk_biomes = 0x0D
		self.play_clear_titles = 0x0E
		self.play_command_suggestions_response = 0x0F
		self.play_commands = 0x10
		self.play_close_container = 0x11
		self.play_set_container_content = 0x12
		self.play_set_container_property = 0x13
		self.play_set_container_slot = 0x14
		self.play_set_cooldown = 0x15
		self.play_chat_suggestions = 0x16
		self.play_plugin_message = 0x17
		self.play_damage_event = 0x18
		self.play_delete_message = 0x19
		self.play_disconnect = 0x1A
		self.play_disguised_chat_message = 0x1B
		self.play_entity_event = 0x1C
		self.play_explosion = 0x1D
		self.play_unload_chunk = 0x1E
		self.play_game_event = 0x1F
		self.play_open_horse_screen = 0x20
		self.play_hurt_animation = 0x21
		self.play_initialize_world_border = 0x22
		self.play_keep_alive = 0x23
		self.play_chunk_data_and_update_light = 0x24
		self.play_world_event = 0x25
		self.play_particle = 0x26
		self.play_update_light = 0x27
		self.play_login = 0x28
		self.play_map_data = 0x29
		self.play_merchant_offers = 0x2A
		self.play_update_entity_position = 0x2B
		self.play_update_entity_position_and_rotation = 0x2C
		self.play_update_entity_rotation = 0x2D
		self.play_move_vehicle = 0x2E
		self.play_open_book = 0x2F
		self.play_open_screen = 0x30
		self.play_open_sign_editor = 0x31
		self.play_ping = 0x32
		self.play_place_ghost_recipe = 0x33
		self.play_player_abilities = 0x34
		self.play_player_chat_message = 0x35
		self.play_end_combat = 0x36
		self.play_enter_combat = 0x37
		self.play_combat_death = 0x38
		self.play_player_info_remove = 0x39
		self.play_player_info_update = 0x3A
		self.play_look_at = 0x3B
		self.play_synchronize_player_position = 0x3C
		self.play_update_recipe_book = 0x3D
		self.play_remove_entities = 0x3E
		self.play_remove_entity_effect = 0x3F
		self.play_resource_pack = 0x40
		self.play_respawn = 0x41
		self.play_set_head_rotation = 0x42
		self.play_update_section_blocks = 0x43
		self.play_select_advancements_tab = 0x44
		self.play_server_data = 0x45
		self.play_set_action_bar_text = 0x46
		self.play_set_border_center = 0x47
		self.play_set_border_lerp_size = 0x48
		self.play_set_border_size = 0x49
		self.play_set_border_warning_delay = 0x4A
		self.play_set_border_warning_distance = 0x4B
		self.play_set_camera = 0x4C
		self.play_set_held_item = 0x4D
		self.play_set_center_chunk = 0x4E
		self.play_set_render_distance = 0x4F
		self.play_set_default_spawn_position = 0x50
		self.play_display_objective = 0x51
		self.play_set_entity_metadata = 0x52
		self.play_link_entities = 0x53
		self.play_set_entity_velocity = 0x54
		self.play_set_equipment = 0x55
		self.play_set_experience = 0x56
		self.play_set_health = 0x57
		self.play_update_objectives = 0x58
		self.play_set_passengers = 0x59
		self.play_update_teams = 0x5A
		self.play_update_score = 0x5B
		self.play_set_simulation_distance = 0x5C
		self.play_set_subtitle_text = 0x5D
		self.play_update_time = 0x5E
		self.play_set_title_text = 0x5F
		self.play_set_title_animation_times = 0x60
		self.play_entity_sound_effect = 0x61
		self.play_sound_effect = 0x62
		self.play_stop_sound = 0x63
		self.play_system_chat_message = 0x64
		self.play_set_tab_list_header_and_footer = 0x65
		self.play_tag_query_response = 0x66
		self.play_pickup_item = 0x67
		self.play_teleport_entity = 0x68
		self.play_update_advancements = 0x69
		self.play_update_attributes = 0x6A
		self.play_feature_flags = 0x6B
		self.play_entity_effect = 0x6C
		self.play_update_recipes = 0x6D
		self.play_update_tags = 0x6E
		# Server bounds
		self.handshaking_handshake = 0x00
		self.handshaking_legacy_server_list_ping = 0xFE
		self.status_request = 0x00
		self.status_ping = 0x01
		self.login_start = 0x00
		self.login_encryption_response = 0x01
		self.login_plugin_response = 0x02
		self.play_confirm_teleportation = 0x00
		self.play_query_block_entity_tag = 0x01
		self.play_change_difficulty = 0x02
		self.play_message_acknowledgment = 0x03
		self.play_chat_command = 0x04
		self.play_chat_message = 0x05
		self.play_player_session = 0x06
		self.play_client_status = 0x07
		self.play_client_information = 0x08
		self.play_command_suggestions_request = 0x09
		self.play_click_container_button = 0x0A
		self.play_click_container = 0x0B
		self.play_close_container = 0x0C
		self.play_plugin_message = 0x0D
		self.play_edit_book = 0x0E
		self.play_query_entity_tag = 0x0F
		self.play_interact = 0x10
		self.play_generate_structure = 0x11
		self.play_keep_alive = 0x12
		self.play_lock_difficulty = 0x13
		self.play_set_player_position = 0x14
		self.play_set_player_position_and_rotation = 0x15
		self.play_set_player_rotation = 0x16
		self.play_set_player_on_ground = 0x17
		self.play_move_vehicle = 0x18
		self.play_paddle_boat = 0x19
		self.play_pick_item = 0x1A
		self.play_place_recipe = 0x1B
		self.play_player_abilities = 0x1C
		self.play_player_action = 0x1D
		self.play_player_command = 0x1E
		self.play_player_input = 0x1F
		self.play_pong = 0x20
		self.play_change_recipe_book_settings = 0x21
		self.play_set_seen_recipe = 0x22
		self.play_rename_item = 0x23
		self.play_resource_pack = 0x24
		self.play_seen_advancements = 0x25
		self.play_select_trade = 0x26
		self.play_set_beacon_effect = 0x27
		self.play_set_held_item = 0x28
		self.play_program_command_block = 0x29
		self.play_program_command_block_minecart = 0x2A
		self.play_set_creative_mode_slot = 0x2B
		self.play_program_jigsaw_block = 0x2C
		self.play_program_structure_block = 0x2D
		self.play_update_sign = 0x2E
		self.play_swing_arm = 0x2F
		self.play_teleport_to_entity = 0x30
		self.play_use_item_on = 0x31
		self.play_use_item = 0x32
PacketV1_20_1.INSTANCE = PacketV1_20_1()

# Generate from <https://minecraft.wiki/w/Minecraft_Wiki:Projects/wiki.vg_merge/Protocol?oldid=2789623>
class PacketV1_21_1(PacketIdSet):
	INSTANCE: ClassVar[PacketIdSet]
	def __init__(self) -> None:
		super().__init__(Protocol.V1_21_1)
		# Client bounds
		self.status_response = 0x00 # resource: status_response
		self.status_pong = 0x01 # resource: pong_response
		self.login_disconnect = 0x00 # resource: login_disconnect
		self.login_encryption_request = 0x01 # resource: hello
		self.login_success = 0x02 # resource: game_profile
		self.login_set_compression = 0x03 # resource: login_compression
		self.login_plugin_request = 0x04 # resource: custom_query
		self.login_cookie_request = 0x05 # resource: cookie_request
		self.configuration_cookie_request = 0x00 # resource: cookie_request
		self.configuration_plugin_message = 0x01 # resource: custom_payload
		self.configuration_disconnect = 0x02 # resource: disconnect
		self.configuration_finish_configuration = 0x03 # resource: finish_configuration
		self.configuration_keep_alive = 0x04 # resource: keep_alive
		self.configuration_ping = 0x05 # resource: ping
		self.configuration_reset_chat = 0x06 # resource: reset_chat
		self.configuration_registry_data = 0x07 # resource: registry_data
		self.configuration_remove_resource_pack = 0x08 # resource: resource_pack_pop
		self.configuration_add_resource_pack = 0x09 # resource: resource_pack_push
		self.configuration_store_cookie = 0x0A # resource: store_cookie
		self.configuration_transfer = 0x0B # resource: transfer
		self.configuration_feature_flags = 0x0C # resource: update_enabled_features
		self.configuration_update_tags = 0x0D # resource: update_tags
		self.configuration_known_packs = 0x0E # resource: select_known_packs
		self.configuration_custom_report_details = 0x0F # resource: custom_report_details
		self.configuration_server_links = 0x10 # resource: server_links
		self.play_bundle_delimiter = 0x00 # resource: bundle_delimiter
		self.play_spawn_entity = 0x01 # resource: add_entity
		self.play_spawn_experience_orb = 0x02 # resource: add_experience_orb
		self.play_entity_animation = 0x03 # resource: animate
		self.play_award_statistics = 0x04 # resource: award_stats
		self.play_acknowledge_block_change = 0x05 # resource: block_changed_ack
		self.play_set_block_destroy_stage = 0x06 # resource: block_destruction
		self.play_block_entity_data = 0x07 # resource: block_entity_data
		self.play_block_action = 0x08 # resource: block_event
		self.play_block_update = 0x09 # resource: block_update
		self.play_boss_bar = 0x0A # resource: boss_event
		self.play_change_difficulty = 0x0B # resource: change_difficulty
		self.play_chunk_batch_finished = 0x0C # resource: chunk_batch_finished
		self.play_chunk_batch_start = 0x0D # resource: chunk_batch_start
		self.play_chunk_biomes = 0x0E # resource: chunks_biomes
		self.play_clear_titles = 0x0F # resource: clear_titles
		self.play_command_suggestions_response = 0x10 # resource: command_suggestions
		self.play_commands = 0x11 # resource: commands
		self.play_close_container = 0x12 # resource: container_close
		self.play_set_container_content = 0x13 # resource: container_set_content
		self.play_set_container_property = 0x14 # resource: container_set_data
		self.play_set_container_slot = 0x15 # resource: container_set_slot
		self.play_cookie_request = 0x16 # resource: cookie_request
		self.play_set_cooldown = 0x17 # resource: cooldown
		self.play_chat_suggestions = 0x18 # resource: custom_chat_completions
		self.play_plugin_message = 0x19 # resource: custom_payload
		self.play_damage_event = 0x1A # resource: damage_event
		self.play_debug_sample = 0x1B # resource: debug_sample
		self.play_delete_message = 0x1C # resource: delete_chat
		self.play_disconnect = 0x1D # resource: disconnect
		self.play_disguised_chat_message = 0x1E # resource: disguised_chat
		self.play_entity_event = 0x1F # resource: entity_event
		self.play_explosion = 0x20 # resource: explode
		self.play_unload_chunk = 0x21 # resource: forget_level_chunk
		self.play_game_event = 0x22 # resource: game_event
		self.play_open_horse_screen = 0x23 # resource: horse_screen_open
		self.play_hurt_animation = 0x24 # resource: hurt_animation
		self.play_initialize_world_border = 0x25 # resource: initialize_border
		self.play_keep_alive = 0x26 # resource: keep_alive
		self.play_chunk_data_and_update_light = 0x27 # resource: level_chunk_with_light
		self.play_world_event = 0x28 # resource: level_event
		self.play_particle = 0x29 # resource: level_particles
		self.play_update_light = 0x2A # resource: light_update
		self.play_login = 0x2B # resource: login
		self.play_map_data = 0x2C # resource: map_item_data
		self.play_merchant_offers = 0x2D # resource: merchant_offers
		self.play_update_entity_position = 0x2E # resource: move_entity_pos
		self.play_update_entity_position_and_rotation = 0x2F # resource: move_entity_pos_rot
		self.play_update_entity_rotation = 0x30 # resource: move_entity_rot
		self.play_move_vehicle = 0x31 # resource: move_vehicle
		self.play_open_book = 0x32 # resource: open_book
		self.play_open_screen = 0x33 # resource: open_screen
		self.play_open_sign_editor = 0x34 # resource: open_sign_editor
		self.play_ping = 0x35 # resource: ping
		self.play_ping_response = 0x36 # resource: pong_response
		self.play_place_ghost_recipe = 0x37 # resource: place_ghost_recipe
		self.play_player_abilities_s2c = 0x38 # resource: player_abilities
		self.play_player_chat_message = 0x39 # resource: player_chat
		self.play_end_combat = 0x3A # resource: player_combat_end
		self.play_enter_combat = 0x3B # resource: player_combat_enter
		self.play_combat_death = 0x3C # resource: player_combat_kill
		self.play_player_info_remove = 0x3D # resource: player_info_remove
		self.play_player_info_update = 0x3E # resource: player_info_update
		self.play_look_at = 0x3F # resource: player_look_at
		self.play_synchronize_player_position = 0x40 # resource: player_position
		self.play_update_recipe_book = 0x41 # resource: recipe
		self.play_remove_entities = 0x42 # resource: remove_entities
		self.play_remove_entity_effect = 0x43 # resource: remove_mob_effect
		self.play_reset_score = 0x44 # resource: reset_score
		self.play_remove_resource_pack = 0x45 # resource: resource_pack_pop
		self.play_add_resource_pack = 0x46 # resource: resource_pack_push
		self.play_respawn = 0x47 # resource: respawn
		self.play_set_head_rotation = 0x48 # resource: rotate_head
		self.play_update_section_blocks = 0x49 # resource: section_blocks_update
		self.play_select_advancements_tab = 0x4A # resource: select_advancements_tab
		self.play_server_data = 0x4B # resource: server_data
		self.play_set_action_bar_text = 0x4C # resource: set_action_bar_text
		self.play_set_border_center = 0x4D # resource: set_border_center
		self.play_set_border_lerp_size = 0x4E # resource: set_border_lerp_size
		self.play_set_border_size = 0x4F # resource: set_border_size
		self.play_set_border_warning_delay = 0x50 # resource: set_border_warning_delay
		self.play_set_border_warning_distance = 0x51 # resource: set_border_warning_distance
		self.play_set_camera = 0x52 # resource: set_camera
		self.play_set_held_item_s2c = 0x53 # resource: set_carried_item
		self.play_set_center_chunk = 0x54 # resource: set_chunk_cache_center
		self.play_set_render_distance = 0x55 # resource: set_chunk_cache_radius
		self.play_set_default_spawn_position = 0x56 # resource: set_default_spawn_position
		self.play_display_objective = 0x57 # resource: set_display_objective
		self.play_set_entity_metadata = 0x58 # resource: set_entity_data
		self.play_link_entities = 0x59 # resource: set_entity_link
		self.play_set_entity_velocity = 0x5A # resource: set_entity_motion
		self.play_set_equipment = 0x5B # resource: set_equipment
		self.play_set_experience = 0x5C # resource: set_experience
		self.play_set_health = 0x5D # resource: set_health
		self.play_update_objectives = 0x5E # resource: set_objective
		self.play_set_passengers = 0x5F # resource: set_passengers
		self.play_update_teams = 0x60 # resource: set_player_team
		self.play_update_score = 0x61 # resource: set_score
		self.play_set_simulation_distance = 0x62 # resource: set_simulation_distance
		self.play_set_subtitle_text = 0x63 # resource: set_subtitle_text
		self.play_update_time = 0x64 # resource: set_time
		self.play_set_title_text = 0x65 # resource: set_title_text
		self.play_set_title_animation_times = 0x66 # resource: set_titles_animation
		self.play_entity_sound_effect = 0x67 # resource: sound_entity
		self.play_sound_effect = 0x68 # resource: sound
		self.play_start_configuration = 0x69 # resource: start_configuration
		self.play_stop_sound = 0x6A # resource: stop_sound
		self.play_store_cookie = 0x6B # resource: store_cookie
		self.play_system_chat_message = 0x6C # resource: system_chat
		self.play_set_tab_list_header_and_footer = 0x6D # resource: tab_list
		self.play_tag_query_response = 0x6E # resource: tag_query
		self.play_pickup_item = 0x6F # resource: take_item_entity
		self.play_teleport_entity = 0x70 # resource: teleport_entity
		self.play_set_ticking_state = 0x71 # resource: ticking_state
		self.play_step_tick = 0x72 # resource: ticking_step
		self.play_transfer = 0x73 # resource: transfer
		self.play_update_advancements = 0x74 # resource: update_advancements
		self.play_update_attributes = 0x75 # resource: update_attributes
		self.play_entity_effect = 0x76 # resource: update_mob_effect
		self.play_update_recipes = 0x77 # resource: update_recipes
		self.play_update_tags = 0x78 # resource: update_tags
		self.play_projectile_power = 0x79 # resource: projectile_power
		self.play_custom_report_details = 0x7A # resource: custom_report_details
		self.play_server_links = 0x7B # resource: server_links
		# Server bounds
		self.handshaking_handshake = 0x00 # resource: intention
		self.handshaking_legacy_server_list_ping = 0xFE
		self.status_request = 0x00 # resource: status_request
		self.status_ping = 0x01 # resource: ping_request
		self.login_start = 0x00 # resource: hello
		self.login_encryption_response = 0x01 # resource: key
		self.login_plugin_response = 0x02 # resource: custom_query_answer
		self.login_acknowledged = 0x03 # resource: login_acknowledged
		self.login_cookie_response = 0x04 # resource: cookie_response
		self.configuration_client_information = 0x00 # resource: client_information
		self.configuration_cookie_response = 0x01 # resource: cookie_response
		self.configuration_plugin_message = 0x02 # resource: custom_payload
		self.configuration_acknowledge_finish_configuration = 0x03 # resource: finish_configuration
		self.configuration_keep_alive = 0x04 # resource: keep_alive
		self.configuration_pong = 0x05 # resource: pong
		self.configuration_resource_pack_response = 0x06 # resource: resource_pack
		self.configuration_known_packs = 0x07 # resource: select_known_packs
		self.play_confirm_teleportation = 0x00 # resource: accept_teleportation
		self.play_query_block_entity_tag = 0x01
		self.play_change_difficulty = 0x02
		self.play_acknowledge_message = 0x03
		self.play_chat_command = 0x04
		self.play_signed_chat_command = 0x05
		self.play_chat_message = 0x06 # resource: chat
		self.play_player_session = 0x07
		self.play_chunk_batch_received = 0x08 # resource: chunk_batch_received
		self.play_client_status = 0x09 # resource: client_command
		self.play_client_information = 0x0A
		self.play_command_suggestions_request = 0x0B
		self.play_acknowledge_configuration = 0x0C
		self.play_click_container_button = 0x0D
		self.play_click_container = 0x0E
		self.play_close_container = 0x0F
		self.play_change_container_slot_state = 0x10
		self.play_cookie_response = 0x11
		self.play_plugin_message = 0x12
		self.play_debug_sample_subscription = 0x13
		self.play_edit_book = 0x14
		self.play_query_entity_tag = 0x15
		self.play_interact = 0x16
		self.play_generate_structure = 0x17
		self.play_keep_alive = 0x18 # resource: keep_alive
		self.play_lock_difficulty = 0x19
		self.play_set_player_position = 0x1A
		self.play_set_player_position_and_rotation = 0x1B
		self.play_set_player_rotation = 0x1C
		self.play_set_player_on_ground = 0x1D
		self.play_move_vehicle = 0x1E
		self.play_paddle_boat = 0x1F
		self.play_pick_item = 0x20
		self.play_ping_request = 0x21
		self.play_place_recipe = 0x22
		self.play_player_abilities_c2s = 0x23
		self.play_player_action = 0x24
		self.play_player_command = 0x25
		self.play_player_input = 0x26
		self.play_pong = 0x27
		self.play_change_recipe_book_settings = 0x28
		self.play_set_seen_recipe = 0x29
		self.play_rename_item = 0x2A
		self.play_resource_pack_response = 0x2B
		self.play_seen_advancements = 0x2C
		self.play_select_trade = 0x2D
		self.play_set_beacon_effect = 0x2E
		self.play_set_held_item_c2s = 0x2F
		self.play_program_command_block = 0x30
		self.play_program_command_block_minecart = 0x31
		self.play_set_creative_mode_slot = 0x32
		self.play_program_jigsaw_block = 0x33
		self.play_program_structure_block = 0x34
		self.play_update_sign = 0x35
		self.play_swing_arm = 0x36
		self.play_teleport_to_entity = 0x37
		self.play_use_item_on = 0x38
		self.play_use_item = 0x39
PacketV1_21_1.INSTANCE = PacketV1_21_1()

# Generate from <https://minecraft.wiki/w/Minecraft_Wiki:Projects/wiki.vg_merge/Protocol?oldid=2845901>
class PacketV1_21_4(PacketIdSet):
	INSTANCE: ClassVar[PacketIdSet]
	def __init__(self) -> None:
		super().__init__(Protocol.V1_21_4)
		# Client bounds
		self.status_response = 0x00 # resource: status_response
		self.status_pong = 0x01 # resource: pong_response
		self.login_disconnect = 0x00 # resource: login_disconnect
		self.login_encryption_request = 0x01 # resource: hello
		self.login_success = 0x02 # resource: login_finished
		self.login_set_compression = 0x03 # resource: login_compression
		self.login_plugin_request = 0x04 # resource: custom_query
		self.login_cookie_request = 0x05 # resource: cookie_request
		self.configuration_cookie_request = 0x00 # resource: cookie_request
		self.configuration_plugin_message = 0x01 # resource: custom_payload
		self.configuration_disconnect = 0x02 # resource: disconnect
		self.configuration_finish_configuration = 0x03 # resource: finish_configuration
		self.configuration_keep_alive = 0x04 # resource: keep_alive
		self.configuration_ping = 0x05 # resource: ping
		self.configuration_reset_chat = 0x06 # resource: reset_chat
		self.configuration_registry_data = 0x07 # resource: registry_data
		self.configuration_remove_resource_pack = 0x08 # resource: resource_pack_pop
		self.configuration_add_resource_pack = 0x09 # resource: resource_pack_push
		self.configuration_store_cookie = 0x0A # resource: store_cookie
		self.configuration_transfer = 0x0B # resource: transfer
		self.configuration_feature_flags = 0x0C # resource: update_enabled_features
		self.configuration_update_tags = 0x0D # resource: update_tags
		self.configuration_known_packs = 0x0E # resource: select_known_packs
		self.configuration_custom_report_details = 0x0F # resource: custom_report_details
		self.configuration_server_links = 0x10 # resource: server_links
		self.play_bundle_delimiter = 0x00 # resource: bundle_delimiter
		self.play_spawn_entity = 0x01 # resource: add_entity
		self.play_spawn_experience_orb = 0x02 # resource: add_experience_orb
		self.play_entity_animation = 0x03 # resource: animate
		self.play_award_statistics = 0x04 # resource: award_stats
		self.play_acknowledge_block_change = 0x05 # resource: block_changed_ack
		self.play_set_block_destroy_stage = 0x06 # resource: block_destruction
		self.play_block_entity_data = 0x07 # resource: block_entity_data
		self.play_block_action = 0x08 # resource: block_event
		self.play_block_update = 0x09 # resource: block_update
		self.play_boss_bar = 0x0A # resource: boss_event
		self.play_change_difficulty = 0x0B # resource: change_difficulty
		self.play_chunk_batch_finished = 0x0C # resource: chunk_batch_finished
		self.play_chunk_batch_start = 0x0D # resource: chunk_batch_start
		self.play_chunk_biomes = 0x0E # resource: chunks_biomes
		self.play_clear_titles = 0x0F # resource: clear_titles
		self.play_command_suggestions_response = 0x10 # resource: command_suggestions
		self.play_commands = 0x11 # resource: commands
		self.play_close_container = 0x12 # resource: container_close
		self.play_set_container_content = 0x13 # resource: container_set_content
		self.play_set_container_property = 0x14 # resource: container_set_data
		self.play_set_container_slot = 0x15 # resource: container_set_slot
		self.play_cookie_request = 0x16 # resource: cookie_request
		self.play_set_cooldown = 0x17 # resource: cooldown
		self.play_chat_suggestions = 0x18 # resource: custom_chat_completions
		self.play_plugin_message = 0x19 # resource: custom_payload
		self.play_damage_event = 0x1A # resource: damage_event
		self.play_debug_sample = 0x1B # resource: debug_sample
		self.play_delete_message = 0x1C # resource: delete_chat
		self.play_disconnect = 0x1D # resource: disconnect
		self.play_disguised_chat_message = 0x1E # resource: disguised_chat
		self.play_entity_event = 0x1F # resource: entity_event
		self.play_teleport_entity = 0x20 # resource: entity_position_sync
		self.play_explosion = 0x21 # resource: explode
		self.play_unload_chunk = 0x22 # resource: forget_level_chunk
		self.play_game_event = 0x23 # resource: game_event
		self.play_open_horse_screen = 0x24 # resource: horse_screen_open
		self.play_hurt_animation = 0x25 # resource: hurt_animation
		self.play_initialize_world_border = 0x26 # resource: initialize_border
		self.play_keep_alive = 0x27 # resource: keep_alive
		self.play_chunk_data_and_update_light = 0x28 # resource: level_chunk_with_light
		self.play_world_event = 0x29 # resource: level_event
		self.play_particle = 0x2A # resource: level_particles
		self.play_update_light = 0x2B # resource: light_update
		self.play_login = 0x2C # resource: login
		self.play_map_data = 0x2D # resource: map_item_data
		self.play_merchant_offers = 0x2E # resource: merchant_offers
		self.play_update_entity_position = 0x2F # resource: move_entity_pos
		self.play_update_entity_position_and_rotation = 0x30 # resource: move_entity_pos_rot
		self.play_move_minecart_along_track = 0x31 # resource: move_minecart_along_track
		self.play_update_entity_rotation = 0x32 # resource: move_entity_rot
		self.play_move_vehicle = 0x33 # resource: move_vehicle
		self.play_open_book = 0x34 # resource: open_book
		self.play_open_screen = 0x35 # resource: open_screen
		self.play_open_sign_editor = 0x36 # resource: open_sign_editor
		self.play_ping = 0x37 # resource: ping
		self.play_ping_response = 0x38 # resource: pong_response
		self.play_place_ghost_recipe = 0x39 # resource: place_ghost_recipe
		self.play_player_abilities_s2c = 0x3A # resource: player_abilities
		self.play_player_chat_message = 0x3B # resource: player_chat
		self.play_end_combat = 0x3C # resource: player_combat_end
		self.play_enter_combat = 0x3D # resource: player_combat_enter
		self.play_combat_death = 0x3E # resource: player_combat_kill
		self.play_player_info_remove = 0x3F # resource: player_info_remove
		self.play_player_info_update = 0x40 # resource: player_info_update
		self.play_look_at = 0x41 # resource: player_look_at
		self.play_synchronize_player_position = 0x42 # resource: player_position
		self.play_set_player_rotation = 0x43 # resource: player_rotation
		self.play_recipe_book_add = 0x44 # resource: recipe_book_add
		self.play_recipe_book_remove = 0x45 # resource: recipe_book_remove
		self.play_recipe_book_settings = 0x46 # resource: recipe_book_settings
		self.play_remove_entities = 0x47 # resource: remove_entities
		self.play_remove_entity_effect = 0x48 # resource: remove_mob_effect
		self.play_reset_score = 0x49 # resource: reset_score
		self.play_remove_resource_pack = 0x4A # resource: resource_pack_pop
		self.play_add_resource_pack = 0x4B # resource: resource_pack_push
		self.play_respawn = 0x47 # resource: respawn
		self.play_set_head_rotation = 0x4D # resource: rotate_head
		self.play_update_section_blocks = 0x4E # resource: section_blocks_update
		self.play_select_advancements_tab = 0x4F # resource: select_advancements_tab
		self.play_server_data = 0x50 # resource: server_data
		self.play_set_action_bar_text = 0x51 # resource: set_action_bar_text
		self.play_set_border_center = 0x52 # resource: set_border_center
		self.play_set_border_lerp_size = 0x53 # resource: set_border_lerp_size
		self.play_set_border_size = 0x54 # resource: set_border_size
		self.play_set_border_warning_delay = 0x55 # resource: set_border_warning_delay
		self.play_set_border_warning_distance = 0x56 # resource: set_border_warning_distance
		self.play_set_camera = 0x57 # resource: set_camera
		self.play_set_center_chunk = 0x58 # resource: set_chunk_cache_center
		self.play_set_render_distance = 0x59 # resource: set_chunk_cache_radius
		self.play_set_cursor_item = 0x5A # resource: set_cursor_item
		self.play_set_default_spawn_position = 0x5B # resource: set_default_spawn_position
		self.play_display_objective = 0x5C # resource: set_display_objective
		self.play_set_entity_metadata = 0x5D # resource: set_entity_data
		self.play_link_entities = 0x5E # resource: set_entity_link
		self.play_set_entity_velocity = 0x5F # resource: set_entity_motion
		self.play_set_equipment = 0x60 # resource: set_equipment
		self.play_set_experience = 0x61 # resource: set_experience
		self.play_set_health = 0x62 # resource: set_health
		self.play_set_held_item_s2c = 0x63 # resource: set_held_slot
		self.play_update_objectives = 0x64 # resource: set_objective
		self.play_set_passengers = 0x65 # resource: set_passengers
		self.play_set_player_inventory_slot = 0x66 # resource: set_player_inventory
		self.play_update_teams = 0x67 # resource: set_player_team
		self.play_update_score = 0x68 # resource: set_score
		self.play_set_simulation_distance = 0x69 # resource: set_simulation_distance
		self.play_set_subtitle_text = 0x6A # resource: set_subtitle_text
		self.play_update_time = 0x6B # resource: set_time
		self.play_set_title_text = 0x6C # resource: set_title_text
		self.play_set_title_animation_times = 0x6D # resource: set_titles_animation
		self.play_entity_sound_effect = 0x6E # resource: sound_entity
		self.play_sound_effect = 0x6F # resource: sound
		self.play_start_configuration = 0x70 # resource: start_configuration
		self.play_stop_sound = 0x71 # resource: stop_sound
		self.play_store_cookie = 0x72 # resource: store_cookie
		self.play_system_chat_message = 0x73 # resource: system_chat
		self.play_set_tab_list_header_and_footer = 0x74 # resource: tab_list
		self.play_tag_query_response = 0x75 # resource: tag_query
		self.play_pickup_item = 0x76 # resource: take_item_entity
		self.play_synchronize_vehicle_position = 0x77 # resource: teleport_entity
		self.play_set_ticking_state = 0x78 # resource: ticking_state
		self.play_step_tick = 0x79 # resource: ticking_step
		self.play_transfer = 0x7A # resource: transfer
		self.play_update_advancements = 0x7B # resource: update_advancements
		self.play_update_attributes = 0x7C # resource: update_attributes
		self.play_entity_effect = 0x7D # resource: update_mob_effect
		self.play_update_recipes = 0x7E # resource: update_recipes
		self.play_update_tags = 0x7F # resource: update_tags
		self.play_projectile_power = 0x80 # resource: projectile_power
		self.play_custom_report_details = 0x81 # resource: custom_report_details
		self.play_server_links = 0x82 # resource: server_links
		# Server bounds
		self.handshaking_handshake = 0x00 # resource: intention
		self.handshaking_legacy_server_list_ping = 0xFE
		self.status_request = 0x00 # resource: status_request
		self.status_ping = 0x01 # resource: ping_request
		self.login_start = 0x00 # resource: hello
		self.login_encryption_response = 0x01 # resource: key
		self.login_plugin_response = 0x02 # resource: custom_query_answer
		self.login_acknowledged = 0x03 # resource: login_acknowledged
		self.login_cookie_response = 0x04 # resource: cookie_response
		self.configuration_client_information = 0x00 # resource: client_information
		self.configuration_cookie_response = 0x01 # resource: cookie_response
		self.configuration_plugin_message = 0x02 # resource: custom_payload
		self.configuration_acknowledge_finish_configuration = 0x03 # resource: finish_configuration
		self.configuration_keep_alive = 0x04 # resource: keep_alive
		self.configuration_pong = 0x05 # resource: pong
		self.configuration_resource_pack_response = 0x06 # resource: resource_pack
		self.configuration_known_packs = 0x07 # resource: select_known_packs
		self.play_confirm_teleportation = 0x00 # resource: accept_teleportation
		self.play_query_block_entity_tag = 0x01 # resource: block_entity_tag_query
		self.play_bundle_item_selected = 0x02 # resource: bundle_item_selected
		self.play_change_difficulty = 0x03 # resource: change_difficulty
		self.play_acknowledge_message = 0x04 # resource: chat_ack
		self.play_chat_command = 0x05 # resource: chat_command
		self.play_signed_chat_command = 0x06 # resource: chat_command_signed
		self.play_chat_message = 0x07 # resource: chat
		self.play_player_session = 0x08 # resource: chat_session_update
		self.play_chunk_batch_received = 0x09 # resource: chunk_batch_received
		self.play_client_status = 0x0A # resource: client_command
		self.play_client_tick_end = 0x0B # resource: client_tick_end
		self.play_client_information = 0x0C # resource: client_information
		self.play_command_suggestions_request = 0x0D # resource: command_suggestion
		self.play_acknowledge_configuration = 0x0E # resource: configuration_acknowledged
		self.play_click_container_button = 0x0F # resource: container_button_click
		self.play_click_container = 0x10 # resource: container_click
		self.play_close_container = 0x11 # resource: container_close
		self.play_change_container_slot_state = 0x12 # resource: container_slot_state_changed
		self.play_cookie_response = 0x13 # resource: cookie_response
		self.play_plugin_message = 0x14 # resource: custom_payload
		self.play_debug_sample_subscription = 0x15 # resource: debug_sample_subscription
		self.play_edit_book = 0x16 # resource: edit_book
		self.play_query_entity_tag = 0x17 # resource: entity_tag_query
		self.play_interact = 0x18 # resource: interact
		self.play_generate_structure = 0x19 # resource: jigsaw_generate
		self.play_keep_alive = 0x1A # resource: keep_alive
		self.play_lock_difficulty = 0x1B # resource: lock_difficulty
		self.play_set_player_position = 0x1C # resource: move_player_pos
		self.play_set_player_position_and_rotation = 0x1D # resource: move_player_pos_rot
		self.play_set_player_rotation = 0x1E # resource: move_player_rot
		self.play_set_player_movement_flags = 0x1F # resource: move_player_status_only
		self.play_move_vehicle = 0x20 # resource: move_vehicle
		self.play_paddle_boat = 0x21 # resource: paddle_boat
		self.play_pick_item_from_block = 0x22 # resource: pick_item_from_block
		self.play_pick_item_from_entity = 0x23 # resource: pick_item_from_entity
		self.play_ping_request = 0x24 # resource: ping_request
		self.play_place_recipe = 0x25 # resource: place_recipe
		self.play_player_abilities_c2s = 0x26 # resource: player_abilities
		self.play_player_action = 0x27 # resource: player_action
		self.play_player_command = 0x28 # resource: player_command
		self.play_player_input = 0x29 # resource: player_input
		self.play_player_loaded = 0x2A # resource: player_loaded
		self.play_pong = 0x2B # resource: pong
		self.play_change_recipe_book_settings = 0x2C # resource: recipe_book_change_settings
		self.play_set_seen_recipe = 0x2D # resource: recipe_book_seen_recipe
		self.play_rename_item = 0x2E # resource: rename_item
		self.play_resource_pack_response = 0x2F # resource: resource_pack
		self.play_seen_advancements = 0x30 # resource: seen_advancements
		self.play_select_trade = 0x31 # resource: select_trade
		self.play_set_beacon_effect = 0x32 # resource: set_beacon
		self.play_set_held_item_c2s = 0x33 # resource: set_carried_item
		self.play_program_command_block = 0x34 # resource: set_command_block
		self.play_program_command_block_minecart = 0x35 # resource: set_command_minecart
		self.play_set_creative_mode_slot = 0x36 # resource: set_creative_mode_slot
		self.play_program_jigsaw_block = 0x37 # resource: set_jigsaw_block
		self.play_program_structure_block = 0x38 # resource: set_structure_block
		self.play_update_sign = 0x39 # resource: sign_update
		self.play_swing_arm = 0x3A # resource: swing
		self.play_teleport_to_entity = 0x3B # resource: teleport_to_entity
		self.play_use_item_on = 0x3C # resource: use_item_on
		self.play_use_item = 0x3D # resource: use_item
PacketV1_21_4.INSTANCE = PacketV1_21_4()
