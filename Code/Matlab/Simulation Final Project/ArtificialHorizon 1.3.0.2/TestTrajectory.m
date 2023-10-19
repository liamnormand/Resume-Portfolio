%% Test with a consistent trajectory attitude
%  Attitude from the file title 'Attitude.mat' (Heading|Pitch|Roll x925)

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

% Creation of an artificial horizon
AH = ArtificialHorizon('Axes',Axes,'ReticleType','-.-','Reticlecolor','y','EdgeColor','w'); 
AH.update(0,0,0);

% Loading of the the test trajectory
A = load('Attitude.mat');
A = A.Attitude;

% Artificial horizon update
for n = 1:size(A,1)
    AH.update(A(n,1),A(n,2),A(n,3));
    pause(0.01);
end
