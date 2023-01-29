local function japanese()
    local preedit = ''

    local function processor_init(env)
        env.code_init = { 'q', 'k', 's', 't', 'n', 'h', 'm', 'y', 'r', 'w', 'x', 'l' }
        env.code_end = { 'a', 'i', 'u', 'e', 'o' }
        env.kana_table = {
            { 'あ', 'い', 'う', 'え', 'お' },
            { 'か', 'き', 'く', 'け', 'こ' },
            { 'さ', 'し', 'す', 'せ', 'そ' },
            { 'た', 'ち', 'つ', 'て', 'と' },
            { 'な', 'に', 'ぬ', 'ね', 'の' },
            { 'は', 'ひ', 'ふ', 'へ', 'ほ' },
            { 'ま', 'み', 'む', 'め', 'も' },
            { 'や', 'い', 'ゆ', 'え', 'よ' },
            { 'ら', 'り', 'る', 'れ', 'ろ' },
            { 'わ', 'い', 'う', 'え', 'を' },
            { 'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ' },
            { 'ゃ', 'ぃ', 'ゅ', 'ぇ', 'ょ' },
        }
        env.code_sp = { 'xx', 'vu', 'nn', '--' }
        env.kana_sp = { 'っ', 'ゔ', 'ん', 'ー' }
        env.kana_cycle_1 = {
            'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'て', 'と', 'あ',
            'い', 'え', 'お', 'や', 'ゆ', 'よ',
            'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'そ', 'だ', 'ぢ', 'で', 'ど', 'ぁ',
            'ぃ', 'ぇ', 'ぉ', 'ゃ', 'ゅ', 'ょ'
        } -- 21x
        env.kana_cycle_2 = {
            'は', 'ひ', 'ふ', 'へ', 'ほ', 'つ', 'う',
            'ば', 'び', 'ぶ', 'べ', 'ぼ', 'っ', 'ぅ',
            'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'づ', 'ゔ'
        }

        env.tmp_code = ''
        env.Rejected, env.Accepted, env.Noop = 0, 1, 2
    end

    local function processor(key_e, env)
        local engine = env.engine
        local context = engine.context
        local input = context.input
        local composition = context.composition
        local segmentation = composition:toSegmentation()
        local current_keycode = key_e.keycode
        local current_keychar = string.format('%c', current_keycode)
        local current_keyrepr = key_e:repr()

        if (not context:get_option("ascii_mode")) then
            if (current_keycode >= 0x61 and current_keycode <= 0x7a) or current_keycode == 0x2d then
                env.tmp_code = env.tmp_code .. current_keychar
                if #env.tmp_code == 2 then
                    local kana_pos = { 0, 0 }
                    for index, value in ipairs(env.code_init) do
                        if value == string.sub(env.tmp_code, 1, 1) then
                            kana_pos[1] = index
                            break
                        end
                    end
                    for index, value in ipairs(env.code_end) do
                        if value == string.sub(env.tmp_code, 2) then
                            kana_pos[2] = index
                            break
                        end
                    end
                    if kana_pos[1] ~= 0 and kana_pos[2] ~= 0 then
                        context:push_input(env.kana_table[kana_pos[1]][kana_pos[2]])
                    else
                        for index, value in ipairs(env.code_sp) do
                            if value == env.tmp_code then
                                context:push_input(env.kana_sp[index])
                                break
                            end
                        end
                    end
                    env.tmp_code = ''
                end
                return env.Accepted
            elseif current_keycode == 0x5f then
                local last_kana = string.sub(context, -3)
                for index, value in ipairs(env.kana_cycle_1) do
                    if value == last_kana then
                        input = string.sub(input, 1, -4) .. env.kana_cycle_1[(index + 21) % 42]
                        break
                    end
                end
                for index, value in ipairs(env.kana_cycle_2) do
                    if value == last_kana then
                        input = string.sub(input, 1, -4) .. env.kana_cycle_2[(index + 7) % 21]
                        break
                    end
                end
                return env.Accepted
            elseif current_keyrepr == 'BackSpace' and context:is_composing() then
                if segmentation:get_confirmed_position() == 0 then
                    context:pop_input(3)
                else
                    segmentation:pop_back()
                end
                return env.Accepted
            end
        end
        return env.Noop
    end

    local function segmentor(segmentation, env)
        local engine = env.engine
        local context = engine.context

        if not context:get_option("ascii_mode") then
            preedit = segmentation.input

        end

        return true
    end

    return {
        processor = {
            init = processor_init,
            func = processor
        },
        segmentor = segmentor
    }
end

return japanese
