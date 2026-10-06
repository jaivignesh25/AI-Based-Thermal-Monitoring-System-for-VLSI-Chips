`timescale 1ns / 1ps

module temp_sensor #(
    parameter int INITIAL_TEMP = 25
)(
    input  logic              clk,
    input  logic              rst,
    input  logic signed [8:0] temp_step,

    output logic [7:0]        temp_out
);

    logic signed [9:0] next_temp;

    always_comb begin

        next_temp = $signed({1'b0, temp_out}) + temp_step;

    end


    always_ff @(posedge clk) begin

        if (rst) begin

            temp_out <= INITIAL_TEMP;

        end

        else begin

            // Upper saturation
            if (next_temp > 10'sd255) begin

                temp_out <= 8'd255;

            end

            // Lower saturation
            else if (next_temp < 10'sd0) begin

                temp_out <= 8'd0;

            end

            else begin

                temp_out <= next_temp[7:0];

            end

        end

    end

endmodule