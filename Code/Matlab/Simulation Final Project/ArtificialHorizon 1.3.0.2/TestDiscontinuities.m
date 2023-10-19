%% Test of attitude discontinuities
%  1) Heading : 0° -> +180° -> -180° -> 0°
%  2) Pitch   : 0° ->  +90° ->  -90° -> 0°
%  3) Roll    : 0° -> +180° -> -180° -> 0°

% Figure
S = get(0,'ScreenSize');
d = 400;
P = [(S(3)-d)/2 (S(4)-d)/2 d d];
Figure = ...
    figure('Color',       'w',...
           'NumberTitle', 'Off',...
           'MenuBar',     'none',...
           'Position',    P);
Axes = ...
    axes('Parent',   Figure,...
         'Position', [0 0 1 1]);  
     
% Pause duration
dt = 0.001;

% Angle conversion function [0,2*pi[ -> ]-pi,+pi]
AngleWrapper = @(a) mod(a,2*pi)-pi*(1-(-1).^floor(a/pi));

% Pitch conversion function [0,2*pi[ -> ]-pi/2,+pi/2]
PitchWrapper = @(a) (mod(a,pi/2)-pi/4*(1-(-1).^floor(2*a/pi))).*(-1).^floor(1/2+a/pi);

% Creation of an artificial horizon  
AH = ...
    ArtificialHorizon('Axes',         Axes,...
                      'ReticleType',  '-.-',...
                      'Reticlecolor', 'y',...
                      'EdgeColor',    'w'); 
AH.update(0,0,0);
               
% 1) Heading test
r0 = 1.25*pi/4;
R = linspace(0,r0,10);
for r = R
    AH.update(0,0,r);
    pause(dt);
end
H = AngleWrapper(linspace(0,2*pi,100));
for h = H
    AH.update(h,0,r0);
    pause(dt);
end
R = linspace(r0,0,10);
for r = R
    AH.update(0,0,r);
    pause(dt);
end

% 2) Pitch test
P = PitchWrapper(linspace(0,2*pi,120));
I = lt([1 diff(P)],0);                      % Pitch   : 0° ->  +90° ->  -90° -> 0°
H = pi*I;                                   % Heading : 0° -> +180° -> +180° -> 0°
R = pi*I;                                   % Roll    : 0° -> +180° -> +180° -> 0°
for n = 1:numel(P)
    AH.update(R(n),P(n),R(n));
    pause(dt);
end

% 3) Roll test
R = AngleWrapper(linspace(0,2*pi,50));
for n = 1:numel(R)
    AH.update(0,0,R(n));
    pause(dt);
end
