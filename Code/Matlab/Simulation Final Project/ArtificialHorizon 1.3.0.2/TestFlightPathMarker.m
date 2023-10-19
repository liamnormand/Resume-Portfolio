%% Test of flight path marker
%  1) AoA
%  2) Lateral drift

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
   
% Sinusoid
n = 5;
t0 = 5e-2;
dt = 1e-3;
T = 0:dt:2*t0;
S = sin(2*pi*T/t0);

% Pitch and AoA
A0A0 = 7.5*pi/180;
Pitch = [zeros(1,10) 15*pi/180*S zeros(1,2*n)]+A0A0;
Pitch = smooth(Pitch,10)';
AoA   = -[A0A0*ones(1,n) Pitch(1:end-n)]+Pitch+A0A0;

% Heading and lateral drift
n = 10;
Heading = [zeros(1,10) 7*pi/180*sin(2*pi*T/t0) zeros(1,2*n)];
Heading = smooth(Heading,10)';
Drift = -[zeros(1,n) Heading(1:end-n)];

% Creation of artificial horizon
AH = ArtificialHorizon('Axes',Axes); 

% AoA
for n = 1:numel(Pitch)    
    update(AH, 0,Pitch(n),0,AoA(n),0); 
    pause(dt); drawnow();
end

% Lateral drift
for n = 1:numel(Heading)    
    update(AH, Heading(n),A0A0,0,A0A0,Drift(n)); 
    pause(dt); drawnow();    
end
