clear; close all; clc;
w = 45;
rhos = 2.3769e-3;
s = 10.2;
clmax = 1.7;
g = deg2rad(-2.5); %This is gamma

%This is getting the atmospheric data for the flight ceiling
[atp1, atp2, atp3] = mechFlightTools.StdAtpUS(65462);
%Creating a list of densities between sea level and flight ceiling
rho = linspace(rhos,atp3,10000);
altitude = zeros(1);
%Calculating stall speed at each density
vstall = (2*w./(rho.*s.*clmax)).^.5;

vthrust = zeros(4);
%Anonymous function to define the coefficients for the velocity quartic at
%a given density, using our given fligth path angle gamma.
thrust_coeffs = @(ro) [0.0495*(.5*ro*s), 0.126*(ro/rhos)^0.6,...
    -(22*(ro/rhos)^.6 + (.07-g)*w), 0, 0.05*w^2/(.5*ro*s)];

%For each density, calculates the velocities that satisfy the quartic
%defined above, and calculates the altitude from the density using the
%function defined below.

for inc1 = 1:length(rho)
    vthrust(inc1,:) = roots(thrust_coeffs(rho(inc1)));
    altitude(inc1) = alt_from_rho(rho(:,inc1));
end

%This extracts the second and third columns from vthrust, as the first and
%fourth columns universally return negative values (which are impossible).
possible_vthrust = vthrust(:,2:3);

%Plotting the stall condition in blue and the thrust conditions in black
plot(vstall,altitude,'b')
hold on;
plot(possible_vthrust,altitude,'k');

%This is based on the standard atmosphere model, and it calculates the
%altitude given a density within the troposphere or tropopause.

function alt = alt_from_rho(rho)
    alt = 0;
    h1 = 3.6089e4; h2 = 6.5616e4; a0=-3.567e-3; g = 32.2;
    R = 1716;
    T0=518.67; rho0=2.3769e-3; T1=T0+a0*h1;
    rho1=rho0*(T1/T0)^(-g/a0/R-1);
    T2=T1; rho2=rho1*exp(-g/R/T2*(h2-h1));
    
    if rho>rho1
        alt = alt + T0/a0 * ((rho/rho0)^(-1/(g/(a0*R)+1))-1);
    elseif rho>rho2
        alt = h1 - log(rho/rho1)*(R*T1/g);
    else
        disp('Error, altitude too high')
    end
end


    

