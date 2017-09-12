% Calculate d-prime, needs hit rate (HitRate) and false alarm rate
% (FARate), I think CRRate is used to calculate Beta (bias measure for
% d-prime, but I haven't used it (I've always just used A and b instead)

    % Can't calculate d' from 1 or 0 values
    if HitRate == 1
        HitRate = 0.9999;
    elseif HitRate == 0
        HitRate = 0.0001;
    end 
    
    % False alarm rate
    if FARate == 1
        FARate = 0.9999;
    elseif FARate == 0
        FARate = 0.0001;
    end 
    
    % Correct rejection rate
    if CRRate == 1
        CRRate = 0.9999;
    elseif CRRate == 0
        CRRate = 0.0001;
    end 
    
    
    % Calculate d'
    ZHR = norminv(HitRate);

    ZFA = norminv(FARate);

	DPrime = ZHR - ZFA;
    
    %% Calculate non-parametric detection measures needs hit rate (H) and
    %% false alar rate (F)

    % APrime (Pollock & Norman, 1964), I had to do it in three stages here
    % because it was being weird otherwise.
    Top    = (H-F)*(1+H-F);
    Bottom = 4*H*(1-F);

    APrime = .5 + Top/Bottom;


    % A (Zhang & Mueller, 2005), also calculates b (for bias).
    if F <= .5 && H >= .5
    
        A = .75 + ((H-F)/4) - (F*(1-H));
    
        b = (5 - (4*H))/ (1+(4*F));
    
    elseif F <= H && H <= .5
    
        A = .75 + ((H-F)/4) - (F/(4*H));
    
        b = (H^2 + H)/(H^2 + F);
    
    elseif H >= F && F >= .5
    
        A = .75 + ((H-F)/4) - ((1-H)/(4*(1-F)));
    
        b = (((1-F)^2) + (1-H))/ (((1-F)^2) + (1-F));
    
    else 
    
        A = NaN;
        b = NaN;
    
    end