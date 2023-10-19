classdef mechFlightTools
    methods(Static)
        function [T, p, rho] = StdAtpUS(h)
            %Standard atmosphere
            %input: h altitude(ft)
            %output: T temperature(F), p pressure (lbs/ft^2), rho density (slug/ft^3)
            h1 = 3.6089e4; h2 = 6.5616e4; h3=9.0e4; a0=-3.567e-3; a2 = 5.494e-4; g = 32.2;
            R = 1716;
            T0=518.67; p0=2116.2;rho0=2.3769e-3;T1=T0+a0*h1;
            p1=p0*(T1/T0)^(-g/a0/R); rho1=rho0*(T1/T0)^(-g/a0/R-1);
            T2=T1;
            p2=p1*exp(-g/R/T2*(h2-h1)); rho2=rho1*exp(-g/R/T2*(h2-h1));
            if h <= h1
                %disp('Troposphere');
                T = T0 + a0*h;
                p = p0*(T/T0)^(-g/a0/R);
                rho = rho0*(T/T0)^(-g/a0/R-1);
            elseif h <= h2
                %disp('Tropopause')
                T = T1;
                p = p1*exp(-g/R/T*(h-h1));
                rho = rho1*exp(-g/R/T*(h-h1));
            elseif h <= h3
                %disp('Stratosphere');
                T = T2 + a2*(h-h2);
                p=p2*(T/T2)^(-g/a2/R);
                rho=rho2*(T/T2)^(-g/a2/R-1);
            else
                disp('Error: the altitude should be less than 90000 ft');
            end
        end
        
        function error=eqnFCLP (h)
            w = 2900; s = 175; cd0 = 0.026; k = 0.054; psmax = 290*550; m = 0.6; eta = 0.8;
            [Ts ps rhos] = mechFlightTools.StdAtpUS (0);
            [Th ph rhoh] = mechFlightTools.StdAtpUS (h);
            error = 4/3*sqrt(2*w^3/rhoh/s*sqrt(3*k^3*cd0))-eta*psmax*(rhoh/rhos)^m;
        end

        function [Vmax, VminPC, Vstall] = SLFP(h)
            %Input: altitude h (ft)
            %Output: max air speed Vmax (ft/s), min air speed due to thrust
            %constraint VminPC (ft/s), stall speed Vstall (ft/s)
            w = 2900; s = 175; cd0 = 0.026; k = 0.054; psmax = 290*550; m = 0.6; eta = 0.8; CLmax = 2.4;
            [Ts ps rhos] = mechFlightTools.StdAtpUS (0);
            [T p rho] = mechFlightTools.StdAtpUS (h);
            tmp = sort(roots ([1/2*rho*s*cd0 0 0 -eta*psmax*(rho/rhos)^m 2*k*w^2/rho/s]));
            Vmax = tmp(2);
            VminPC=tmp(1);
            Vstall=sqrt(2*w/rho/s/CLmax);
        end

        function [] = plotSLFP()
            h = linspace(0,40160,1000);
            for k = 1:size(h,2)
                [Vmax(k) VminTC(k) Vstall(k)] = mechFlightTools.SLFP(h(k));
            end
            %Vmin = max(VminTC, Vstall);
            %area ([Vmin Vmax(end:-1:1)], [h h(end:-1:1)], 'FaceColor',[0.8 1 1], 'LineStyle','none');
            hold on;
            plot(Vmax, h,'k', VminTC, h,'k', Vstall, h,'k:');
            grid on;
            xlim ([0 400]);
            xlabel ('Velocity (ft/s)');
            ylabel('Altitude (ft)');
        end

    end
end