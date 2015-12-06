% initial value at t=0

function y = initial_func(xx)
	length_xx = length(xx);
	y = zeros(1, length_xx);
	for i=1:length_xx
		x = xx(i);

		if x <= -1 || x >= 1
			y(i) = 0;
		else
			y(i) = exp(- 1 / (1 - x**2));
		end
	end
end
