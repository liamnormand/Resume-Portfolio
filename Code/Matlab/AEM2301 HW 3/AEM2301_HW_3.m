clear; clc; close all;

%The purpose of this function is to calculate the flight envelope for
%steady longitudinal glide at the minimum glide angle.

%Constant Values for Atmosphere and Gravity
stnd_density = 2.3769e-3;  %stnd refers to standard atmosphere at sea level
stnd_temp = 518.67;
lapse_rate = -3.567e-3;
g = 32.2;   %Gravity
R = 1716;

%Parameters for Aircraft
weight = 2900;
S = 175;
CD_0 = 0.026;
k = 0.054;

%Calculating airspeed at various altitudes, starting at input parameter
%down to sea level
alt_init = 4000;
h = linspace(alt_init,0,200);
%Anon. Function to calculate density at altitude based on stnd atmosphere
density = @() stnd_density * (1+(h.*lapse_rate)/stnd_temp).^(-(g/(lapse_rate*R) + 1));
%Calculating Airspeed at min glide angle condition
V = sqrt(((2*weight/S)*sqrt(k/CD_0))./density());

%Plotting and formatting
plt = plot(V,h);
set(plt,'MarkerSize',1);
set(plt,'LineWidth',1);
grid on
xlabel("Airspeed (ft/s)")
ylabel("Altitude (ft)")
title("Steady Glide Airspeed at Minimum Glide Angle Condition")
