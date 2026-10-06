`timescale 1ns / 1ps


module data_aggregator(
input logic clk,
input logic rst,
input logic [7:0]temp1,
input logic [7:0]temp2,
input logic [7:0]temp3,

output logic [7:0]zone1,
output logic [7:0]zone2,
output logic [7:0]zone3
    );
    always_ff @(posedge clk) begin

        if (rst) begin
            zone1 <= 8'd25;
            zone2 <= 8'd25;
            zone3 <= 8'd25;
        end
        else begin
            zone1 <= temp1;
            zone2 <= temp2;
            zone3 <= temp3;
        end

    end
endmodule
