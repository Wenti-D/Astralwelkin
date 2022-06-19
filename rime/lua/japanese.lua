local function japanese()
    local preedit = ''

    local function segmentor(segmentation, env)
        local engine = env.engine
        local context = engine.context

        if not context:get_option("ascii_mode") then
            preedit = segmentation.input

            preedit = preedit:gsub('qa_', 'xa')
            preedit = preedit:gsub('qi_', 'xi')
            preedit = preedit:gsub('qu_', 'xu')
            preedit = preedit:gsub('xu_', 'vu')
            preedit = preedit:gsub('qe_', 'xe')
            preedit = preedit:gsub('qo_', 'xo')
            preedit = preedit:gsub('xa_', 'qa')
            preedit = preedit:gsub('xi_', 'qi')
            preedit = preedit:gsub('vu_', 'qu')
            preedit = preedit:gsub('xe_', 'qe')
            preedit = preedit:gsub('xo_', 'qo')
            preedit = preedit:gsub('la_', 'ya')
            preedit = preedit:gsub('lu_', 'yu')
            preedit = preedit:gsub('lo_', 'yo')

            preedit = preedit:gsub('ka_', 'ga')
            preedit = preedit:gsub('ki_', 'gi')
            preedit = preedit:gsub('ku_', 'gu')
            preedit = preedit:gsub('ke_', 'ge')
            preedit = preedit:gsub('ko_', 'go')
            preedit = preedit:gsub('ga_', 'ka')
            preedit = preedit:gsub('gi_', 'ki')
            preedit = preedit:gsub('gu_', 'ku')
            preedit = preedit:gsub('ge_', 'ke')
            preedit = preedit:gsub('go_', 'ko')

            preedit = preedit:gsub('sa_', 'za')
            preedit = preedit:gsub('si_', 'zi')
            preedit = preedit:gsub('su_', 'zu')
            preedit = preedit:gsub('se_', 'ze')
            preedit = preedit:gsub('so_', 'zo')
            preedit = preedit:gsub('za_', 'sa')
            preedit = preedit:gsub('zi_', 'si')
            preedit = preedit:gsub('zu_', 'su')
            preedit = preedit:gsub('ze_', 'se')
            preedit = preedit:gsub('zo_', 'so')

            preedit = preedit:gsub('ta_', 'da')
            preedit = preedit:gsub('ti_', 'di')
            preedit = preedit:gsub('tu_', 'xx')
            preedit = preedit:gsub('xx_', 'du')
            preedit = preedit:gsub('te_', 'de')
            preedit = preedit:gsub('to_', 'do')
            preedit = preedit:gsub('da_', 'ta')
            preedit = preedit:gsub('di_', 'ti')
            preedit = preedit:gsub('du_', 'tu')
            preedit = preedit:gsub('de_', 'te')
            preedit = preedit:gsub('do_', 'to')

            preedit = preedit:gsub('na_', 'na')
            preedit = preedit:gsub('ni_', 'ni')
            preedit = preedit:gsub('nu_', 'nu')
            preedit = preedit:gsub('ne_', 'ne')
            preedit = preedit:gsub('no_', 'no')

            preedit = preedit:gsub('ha_', 'ba')
            preedit = preedit:gsub('hi_', 'bi')
            preedit = preedit:gsub('hu_', 'bu')
            preedit = preedit:gsub('he_', 'be')
            preedit = preedit:gsub('ho_', 'bo')
            preedit = preedit:gsub('ba_', 'pa')
            preedit = preedit:gsub('bi_', 'pi')
            preedit = preedit:gsub('bu_', 'pu')
            preedit = preedit:gsub('be_', 'pe')
            preedit = preedit:gsub('bo_', 'po')
            preedit = preedit:gsub('pa_', 'ha')
            preedit = preedit:gsub('pi_', 'hi')
            preedit = preedit:gsub('pu_', 'hu')
            preedit = preedit:gsub('pe_', 'he')
            preedit = preedit:gsub('po_', 'ho')

            preedit = preedit:gsub('ma_', 'ma')
            preedit = preedit:gsub('mi_', 'mi')
            preedit = preedit:gsub('mu_', 'mu')
            preedit = preedit:gsub('me_', 'me')
            preedit = preedit:gsub('mo_', 'mo')

            preedit = preedit:gsub('ya_', 'la')
            preedit = preedit:gsub('yu_', 'lu')
            preedit = preedit:gsub('yo_', 'lo')
            preedit = preedit:gsub('la_', 'ya')
            preedit = preedit:gsub('lu_', 'yu')
            preedit = preedit:gsub('lo_', 'yo')

            preedit = preedit:gsub('ra_', 'ra')
            preedit = preedit:gsub('ri_', 'ri')
            preedit = preedit:gsub('ru_', 'ru')
            preedit = preedit:gsub('re_', 're')
            preedit = preedit:gsub('ro_', 'ro')

            preedit = preedit:gsub('va_', 'wa')
            preedit = preedit:gsub('wa_', 'va')

            context.input = preedit
        end

        return true
    end

    return { segmentor = segmentor }
end

return japanese