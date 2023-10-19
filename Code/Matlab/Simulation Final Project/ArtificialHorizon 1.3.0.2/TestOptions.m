%% Test of artificial horizon options

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
dt = 0.75;

% Default artificial horizon in current axes
AH = ArtificialHorizon('Axes',Axes); pause(dt);

% Reticle type : '-o-'
set(AH,'ReticleType','-o-'); pause(dt);

% Reticle type : 'v'
set(AH,'ReticleType','v'); pause(dt);

% Reticle type : '+'
set(AH,'ReticleType','+'); pause(dt);

% Reticle type : 'w'
set(AH,'ReticleType','w'); pause(dt);

% Reticle color : green
set(AH,'ReticleColor','g'); pause(dt);

% Edge color : black
set(AH,'EdgeColor','k'); pause(dt);

% Font size and weight
set(AH,...
    'LineWidth',    2,...
    'Fontsize',     10,...
    'ReticleWidth', 4,...
    'FontWeight',   'Bold'); pause(dt);

% Font size and weight
set(AH,...
    'LineWidth',    1,...
    'Fontsize',     8,...
    'ReticleWidth', 2,...
    'FontWeight',   'Demi'); pause(dt);

% Horizon color type : 'Uniform'
set(AH,'ColorType','Uniform'); pause(dt);

% Horizon color type : 'Gradient'
set(AH,...
    'ColorType',   'Gradient',...   
    'GroundColor', [252 200 80]/255); pause(dt);

% Horizon color type : 'Uniform'
set(AH,'ColorType','Uniform'); pause(dt);
