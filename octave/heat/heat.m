function heat
	w  = 10; % half width of bar
	dx = 0.05;
	dt = dx**2;
	T  = 10; % total elapsed time [sec]

	n  = ceil(T/dt); % step num

	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	% sampling on x-axis
	xx = linspace(-w, w, ceil(2*w/dx));
	length_xx = length(xx);

	% solutions at each time
	u = zeros(n, length_xx);
	% initial value
	u(1,:) = initial_func(xx);

	% solve heat equation
	for step = 1:n-1
		t = dt * (step - 1); % current time
		u(step + 1,:) = u(step,:) + Laplacian(u(step,:));
	end

	show_result(u, xx, n);
	%show_result_animation(u, xx, n);
end

function show_result(u, xx, n)
	figure;
	hold on;
	plot(xx, u(1,:), "r");
	plot(xx, u(ceil(n/5),:), "b");
	plot(xx, u(ceil(2*n/5),:), "k");
	plot(xx, u(ceil(3*n/5),:), "g");
	plot(xx, u(ceil(4*n/5),:), "y");
	plot(xx, u(n,:), "m");
	axis([-10, 10, 0, 0.4]);
end

function show_result_animation(u, xx, n)
	figure;

	for i = 1:n
		plot(xx, u(i,:), "r");
		axis([-10, 10, 0, 0.4]);
		%sleep(0.01);
		refresh;
	end
end
