`timescale 1ns / 1ps

module trend_detector #(
    parameter Heating = 2'b00,
    parameter normal  = 2'b01,
    parameter cooling = 2'b10
)(
    input  logic              clk,
    input  logic              rst,
    input  logic [7:0]        current_temp,

    output logic signed [8:0] temp_change,
    output logic [1:0]        change,
    output logic              trend_valid
);

    logic [7:0] previous_temp;

    always_ff @(posedge clk) begin

        if (rst) begin
            previous_temp <= 8'd0;
            trend_valid   <= 1'b0;
        end

        else begin
            previous_temp <= current_temp;

            if (!trend_valid)
                trend_valid <= 1'b1;
        end
    end


    always_comb begin

        if (!trend_valid) begin
            temp_change = 9'sd0;
            change      = normal;
        end

        else begin

            temp_change =
                $signed({1'b0, current_temp}) -
                $signed({1'b0, previous_temp});

            if (current_temp > previous_temp)
                change = Heating;

            else if (current_temp < previous_temp)
                change = cooling;

            else
                change = normal;
        end

    end

endmodule