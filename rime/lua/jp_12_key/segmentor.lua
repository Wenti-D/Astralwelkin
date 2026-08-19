local s = {}

local preedit = ''

function s.func(segmentation, env)
    local engine = env.engine
    local context = engine.context

    if not context:get_option("ascii_mode") then
        preedit = segmentation.input
    end

    return true
end

return s
