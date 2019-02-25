%Initial State. Starting Position, Heading Angle, TimeStep. 
startpos_x = 0;
startpos_y = 0;
heading_angle = 5; % degrees of the heading offset
heading_angle = heading_angle * pi / 180;
samples_per_second = 5; %per second
timestep = 1 / samples_per_second ;
speed = 10; %ms.

simulationtime = 30; %seconds
total_number_samples = simulationtime*samples_per_second;

X = zeros(total_number_samples, 1); % x the rows length of number of samples
Y = zeros(total_number_samples, 1); % y the rows length of number of samples

%%%% Update Loop
for i = 1:total_number_samples % from 1 to the length of the samples
    if i > 1 
        X(i) = X(i-1) + ... % index of x equals 1 minus the index
            cos(heading_angle) * speed * timestep;
        Y(i) = Y(i-1) + ...
            sin(heading_angle) * speed * timestep;
        plot(X,Y, 'ro')
        hold on
        axis equal
    end 
end
 

%End State plotting
% plot(X,Y,'ro') %position
% hold on

% axis equal
%axis([-1 100 -100 100]);