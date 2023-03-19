local function japanese()
    local preedit = ''

    local function processor_init(env)
        env.engine.context:set_option("ascii_mode", false)
        env.code_init = { 'q', 'k', 'g', 's', 'z', 't', 'd', 'n', 'h', 'b', 'p', 'm', 'y', 'r', 'w', 'x', 'l' }
        env.code_end = { 'a', 'i', 'u', 'e', 'o' }
        env.kana_table = {
            { 'あ', 'い', 'う', 'え', 'お' },
            { 'か', 'き', 'く', 'け', 'こ' },
            { 'が', 'ぎ', 'ぐ', 'げ', 'ご' },
            { 'さ', 'し', 'す', 'せ', 'そ' },
            { 'ざ', 'じ', 'ず', 'ぜ', 'ぞ' },
            { 'た', 'ち', 'つ', 'て', 'と' },
            { 'だ', 'ぢ', 'づ', 'で', 'ど' },
            { 'な', 'に', 'ぬ', 'ね', 'の' },
            { 'は', 'ひ', 'ふ', 'へ', 'ほ' },
            { 'ば', 'び', 'ぶ', 'べ', 'ぼ' },
            { 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ' },
            { 'ま', 'み', 'む', 'め', 'も' },
            { 'や', 'い', 'ゆ', 'え', 'よ' },
            { 'ら', 'り', 'る', 'れ', 'ろ' },
            { 'わ', 'い', 'う', 'え', 'を' },
            { 'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ' },
            { 'ゃ', 'ぃ', 'ゅ', 'ぇ', 'ょ' },
        }
        env.code_sp = { 'xx', 'vu', 'va', 'nn', '--' }
        env.kana_sp = { 'っ', 'ゔ', 'ゎ', 'ん', 'ー' }
        env.code_cycle_1 = {
            'k', 's', 't', 'q', 'y',
            'g', 'z', 'd', 'x', 'l'
        }
        env.code_cycle_2 = {
            'tu', 'qu',
            'xx', 'xu',
            'du', 'vu',
        }
        env.code_cycle_3 = { 'h', 'b', 'p' }

        env.Rejected, env.Accepted, env.Noop = 0, 1, 2
    end

    local function processor(key_e, env)
        local engine = env.engine
        local context = engine.context
        local input = context.input
        local composition = context.composition
        local segmentation = composition:toSegmentation()
        local current_keycode = key_e.keycode
        local current_keyrepr = key_e:repr()

        if (not context:get_option("ascii_mode")) then
            if current_keycode == 0x5f then
                local last_kana_code = string.sub(input, -2)
                local switched = false
                if last_kana_code == "wa" then
                    context:pop_input(2)
                    context:push_input("va")
                    switched = true
                end
                if last_kana_code == "va" then
                    context:pop_input(2)
                    context:push_input("wa")
                    switched = true
                end
                if not switched then
                    for index, value in ipairs(env.code_cycle_3) do
                        if value == string.sub(last_kana_code, 1, 1) then
                            context:pop_input(2)
                            context:push_input(env.code_cycle_3[index % 3 + 1] .. string.sub(last_kana_code, 2, 2))
                            switched = true
                            break
                        end
                    end
                end
                if not switched then
                    for index, value in ipairs(env.code_cycle_2) do
                        if value == last_kana_code then
                            context:pop_input(2)
                            context:push_input(env.code_cycle_2[(index + 1) % 6 + 1])
                            switched = true
                            break
                        end
                    end
                end
                if not switched then
                    for index, value in ipairs(env.code_cycle_1) do
                        if value == string.sub(last_kana_code, 1, 1) then
                            context:pop_input(2)
                            context:push_input(env.code_cycle_1[(index + 4) % 10 + 1] .. string.sub(last_kana_code, 2, 2))
                            break
                        end
                    end
                end
                return env.Accepted
            elseif current_keyrepr == 'BackSpace' and context:is_composing() then
                if segmentation:get_confirmed_position() == 0 then
                    context:pop_input(2)
                else
                    segmentation:pop_back()
                    context.caret_pos = string.len(input)
                end
                return env.Accepted
            elseif current_keyrepr == 'Return' and context:is_composing() then
                local kana_res = ''
                for i = 1, #input, 2 do
                    local kana_pos = { 0, 0 }
                    for index, value in ipairs(env.code_init) do
                        if value == string.sub(input, i, i) then
                            kana_pos[1] = index
                            break
                        end
                    end
                    for index, value in ipairs(env.code_end) do
                        if value == string.sub(input, i + 1, i + 1) then
                            kana_pos[2] = index
                            break
                        end
                    end
                    if kana_pos[1] ~= 0 and kana_pos[2] ~= 0 then
                        kana_res = kana_res .. env.kana_table[kana_pos[1]][kana_pos[2]]
                    else
                        for index, value in ipairs(env.code_sp) do
                            if value == string.sub(input, i, i + 1) then
                                kana_res = kana_res .. env.kana_sp[index]
                                break
                            end
                        end
                    end
                end
                engine:commit_text(kana_res)
                context:clear()
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
