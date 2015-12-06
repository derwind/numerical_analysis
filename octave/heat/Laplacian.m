% Laplacian of uu

function y = Laplacian(uu)
	length_uu = length(uu);
	y = zeros(1, length_uu);

	for i = 1:length_uu
		u = uu(i);
		left_u  = 0;
		right_u = 0;
		if i - 1 >= 1
			left_u = uu(i - 1);
		end
		if i + 1 <= length_uu
			right_u = uu(i + 1);
		end

		y(i) = (left_u + right_u - 2*u) / 2;
	end
end
